"""Public conformance examples, not production M5Canon or an evidence verifier.

Evidence resolvers are injected. JSON declarations cannot authenticate sources.
No network, keys, private policy, payment execution, or local inference gate.
"""
from copy import deepcopy
from datetime import datetime
from decimal import Decimal, InvalidOperation
import hashlib
import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker, ValidationError

ROOT = Path(__file__).resolve().parents[2]


def load(path):
    return json.loads((ROOT / path).read_text())


def validate(name, record):
    Draft202012Validator(load(f"schemas/{name}.schema.json"),
                         format_checker=FormatChecker()).validate(record)


def current(record, now):
    try:
        start = datetime.fromisoformat(record["effective_at"].replace("Z", "+00:00"))
        end = datetime.fromisoformat(record["expires_at"].replace("Z", "+00:00"))
        return start <= now < end
    except (KeyError, ValueError, TypeError):
        return False


def resolve_namespace(binding, resolver, now):
    """Require independently resolved, matching authority and registration facts.

    resolver returns an authenticated observation under deployment trust policy.
    The synthetic tests provide a test double; a caller-supplied verified flag is
    not a replacement for a production resolver's signature/source validation.
    """
    if (binding["status"] != "ESTABLISHED" or binding["revoked"] or binding["disputed"]
            or binding["superseded_by"] or binding["standing"] != "GOOD_STANDING"
            or binding["authority_basis"] != "INDEPENDENT_AUTHORITY_EVIDENCE"
            or not current(binding, now)):
        return False
    for refs, kind in ((binding["authority_evidence_refs"], "AUTHORITY"),
                       (binding["registration_provenance_refs"], "REGISTRATION"),
                       ([binding["validation_record_ref"]], "VALIDATION")):
        if not refs or not all(refs):
            return False
        for ref in refs:
            record = resolver(ref)
            if not record or record.get("kind") != kind or record.get("status") != "VALID":
                return False
            if not current(record, now):
                return False
            if any(record.get(k) != binding[k] for k in
                   ("namespace", "controller_ref", "canonical_entity_ref", "binding_role")):
                return False
            if not set(binding["scope"]) <= set(record.get("scope", [])):
                return False
            if record.get("digest") not in binding["evidence_hashes"]:
                return False
    return True


def authorize(action, activation, namespaces, resolver, now, runtime):
    """Evaluate a synthetic protected action against current resolver state.

    This is separate from Tier I inference. A False result limits the requested
    protected function, never possession or ordinary use of a local model.
    """
    try:
        validate("m5-action-authorization", action)
        validate("m5-eve-activation", activation)
        validate("m5-jurisdiction-binding", namespaces)
    except (ValueError, TypeError, ValidationError):
        return False
    if not action["authorized"] or action["policy_result"] != "ALLOW":
        return False
    if activation["lifecycle_state"] != "ACTIVE" or not current(activation, now):
        return False
    if (action["principal_ref"] != activation["principal_ref"]
            or action["agent_ref"] != activation["agent_id"]
            or action["activation_ref"] != activation["activation_id"]
            or action["policy_version"] != activation["policy_version"]
            or action["capability_ref"] not in activation["capability_refs"]
            or action["purpose"] not in activation["data_domains"]
            or runtime not in activation["provider_classes"]):
        return False
    if runtime in {"JEV_HOSTED", "HOSTED_GENERATIVE", "HOSTED_SYSTEM_ONE_OTHER"} and (
            activation["local_required"] or not activation["external_allowed"]):
        return False
    # Resolve the activation itself each time: revocation cannot rely on a stale snapshot.
    live = resolver(activation["activation_id"])
    if not live or live.get("status") != "VALID" or not current(live, now):
        return False
    if any(live.get(k) != activation[k] for k in
           ("principal_ref", "agent_id", "account_ref", "activation_version", "policy_version")):
        return False
    policy = resolver(action["decision_ref"])
    if (not policy or policy.get("policy_result") != "ALLOW" or not current(policy, now)
            or any(policy.get(k) != action[k] for k in
                   ("principal_ref", "agent_ref", "activation_ref", "capability_ref",
                    "purpose", "resource_ref", "policy_version", "namespace_binding_refs", "provider_ref"))):
        return False
    for source, keys in ((action, ("credential", "delegation", "jurisdiction", "approval",
                                  "provider_standing", "provider_capability", "endpoint")),
                         (activation, ("credential", "delegation", "approval"))):
        for key in keys:
            gate = source[key]
            if gate["status"] != "VALID" or not current(gate, now):
                return False
            evidence = resolver(gate["evidence_ref"])
            if not evidence or evidence.get("status") != "VALID" or not current(evidence, now):
                return False
            if key not in evidence.get("verified_gate_types", []):
                return False
            if key == "approval" and (not evidence.get("approver_ref")
                                      or evidence["approver_ref"] == action["agent_ref"]):
                return False
            if (evidence.get("principal_ref") != action["principal_ref"]
                    or evidence.get("provider_ref") != action["provider_ref"]
                    or action["capability_ref"] not in evidence.get("capability_refs", [])
                    or action["resource_ref"] not in evidence.get("resource_refs", [])
                    or action["purpose"] not in evidence.get("purposes", [])):
                return False
    if namespaces["status"] != "ACTIVE" or not current(namespaces, now):
        return False
    if not set(action["namespace_binding_refs"]) <= set(activation["namespace_binding_refs"]):
        return False
    by_id = {b["binding_id"]: b for b in namespaces["namespace_bindings"]}
    if len(by_id) != len(namespaces["namespace_bindings"]):
        return False
    return all(ref in by_id and action["purpose"] in by_id[ref]["scope"]
               and resolve_namespace(by_id[ref], resolver, now)
               for ref in action["namespace_binding_refs"])


def validate_correction(event, previous):
    validate("m5-event-envelope", event)
    d = event["data"]
    target = d.get("corrects_event_id") or d.get("supersedes_event_id")
    old = previous.get(target)
    return bool(old and event["id"] != target and old["source"] == event["source"]
                and old["data"]["principal_ref"] == d["principal_ref"])


def migrate_context(legacy, mappings):
    """Never infer new authority from the old combined jurisdiction field.

    Explicit mappings are reviewed inputs, not automatic evidence verification.
    Return a new record only when all changed dimensions are unambiguous.
    """
    validator = Draft202012Validator(load("tests/fixtures/canonical-context-v1.schema.json"))
    if not validator.is_valid(legacy):
        return {"status": "REJECT", "record": None, "reason": "INVALID_LEGACY"}
    needed = ("title_state", "instrument_state", "jurisdiction_binding", "authority_state")
    for key in needed:
        mapping = mappings.get(key)
        if (not mapping or mapping.get("status") != "known" or not mapping.get("source_refs")
                or mapping.get("value") is None):
            return {"status": "HOLD", "record": None, "reason": "AMBIGUOUS_OR_MISSING_EVIDENCE"}
    result = deepcopy(legacy)
    for old in ("title_container", "wrapper", "jurisdictional_security_state"):
        del result[old]
    result.update({k: deepcopy(mappings[k]) for k in needed})
    result["schema_version"] = "2.0.0"
    digest = hashlib.sha256(json.dumps(legacy, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    result["provenance"]["source_refs"].append("sha256:" + digest)
    try:
        validate("m5-canonical-context-envelope", result)
    except ValidationError:
        return {"status": "REJECT", "record": None, "reason": "INVALID_MAPPING"}
    return {"status": "MIGRATE", "record": result, "reason": "EXPLICIT_EVIDENCED_MAPPING"}


class SyntheticMeter:
    """In-memory conformance fixture. Production requires durable deduplication.

    Duplicate IDs with identical payloads return the same receipt; conflicting
    replay is rejected. Corrections are tested separately and never rebilled here.
    """
    def __init__(self):
        self.seen = {}
        self.keys = {}

    def consume(self, event):
        validate("m5-event-envelope", event)
        d = event["data"]
        if d.get("compute_class") == "SOVEREIGN_LOCAL":
            return None
        if d["event_phase"] in {"CORRECTED", "SUPERSEDED"}:
            raise ValueError("Correction reconciliation requires the prior event; never count as fresh usage")
        payload = json.dumps(event, sort_keys=True)
        identity = (event["source"], event["id"])
        key = (event["source"], d["idempotency_key"])
        if identity in self.seen:
            prior, receipt = self.seen[identity]
            if prior != payload:
                raise ValueError("Conflicting event replay")
            return deepcopy(receipt)
        if key in self.keys:
            raise ValueError("Idempotency key reused by a different event")
        m = d["metering"]
        registry = load("m5-openapi/metering/meters.example.yaml")
        catalog = load("m5-openapi/pricing/reference-catalog-v1.example.json")
        meter = next(x for x in registry["meters"] if x["slug"] == m["meter_id"])
        product = next(x for x in catalog["products"] if x["product_id"] == m["product_id"])
        if (meter["event_type"] != event["type"] or product["meter"] != meter["slug"]
                or m["meter_version"] != meter["version"] or m["price_version"] != catalog["catalog_id"]
                or m["billing_policy"] != product["default_billing_policy"]):
            raise ValueError("Event, meter, product, policy, or version mismatch")
        quantity = event
        for part in meter["value_property"].removeprefix("$.").split("."):
            quantity = quantity[part]
        if Decimal(str(quantity)) != Decimal(str(m["quantity"])):
            raise ValueError("Meter quantity mismatch")
        reference = Decimal(str(quantity)) * Decimal(product["reference_unit_price_usd"])
        if (Decimal(m["reference_unit_price_usd"]) != Decimal(product["reference_unit_price_usd"])
                or Decimal(m["notional_service_value_usd"]) != reference):
            raise ValueError("Reference valuation mismatch")
        if m["billing_policy"] != "FREE_PUBLIC":
            raise ValueError("Synthetic consumer supports free-public fixtures only; no settlement")
        receipt = load("examples/m5-commerce-receipt-laya-local.example.json")
        receipt.update(commerce_receipt_id="SYN-RECEIPT-"+event["id"], request_id=d["correlation_id"],
                       principal_ref=d["principal_ref"], product_id=product["product_id"],
                       agent_ref=d.get("agent_ref"), asset_ref=next(iter(d.get("asset_refs", [])), None),
                       m5_tags=d["related_m5_classes"], provider_cost=m["actual_cost_usd"],
                       provider_ref=d["provider"]["provider_id"],runtime="API_DATA",entitlement_type="FREE",
                       meter=meter["slug"],quantity=quantity,billing_policy="FREE_PUBLIC",
                       reference_value_usd=str(reference),usage_event_ref=event["id"],
                       authority_decision_ref="SYN-NO-AUTHORITY-GRANTED",created_at=event["time"],
                       execution_result="DENIED" if d["event_phase"]=="DENIED" else "HUMAN_REVIEW_REQUIRED")
        receipt["price_quote"].update(price_version=catalog["catalog_id"],quoted_at=event["time"])
        receipt["versions"].update(model_family="NOT_APPLICABLE",model_revision="NOT_APPLICABLE",
                                  model_artifact_hash=None,meter_version=meter["version"],
                                  reference_catalog_version=catalog["catalog_id"])
        validate("m5-commerce-receipt", receipt)
        self.seen[identity] = payload, deepcopy(receipt)
        self.keys[key] = identity
        return receipt


def paid_compute_allowed(consent, request, now):
    """Independent opt-in and budget; authorization to act is evaluated separately."""
    if not consent or consent.get("status") != "APPROVED" or not current(consent, now):
        return False
    try:
        price, budget = Decimal(request["quoted_usd"]), Decimal(consent["budget_usd"])
        return (price.is_finite() and budget.is_finite() and 0 <= price <= budget
                and all(request[k] and consent.get(k) == request[k]
                        for k in ("principal_ref", "provider_ref", "purpose", "data_scope"))
                and now < datetime.fromisoformat(request["quote_expires_at"].replace("Z", "+00:00")))
    except (KeyError, ValueError, TypeError, InvalidOperation):
        return False
