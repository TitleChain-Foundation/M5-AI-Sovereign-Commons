#!/usr/bin/env python3
"""Offline, non-authoritative evaluator for the Spring Commons tranche fixture."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

from canonical import canonical_digest, draft_asset_policy_blockers, file_digest, jurisdiction_graph_errors

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent.parent
DEFAULT_FIXTURE = (
    PROJECT / "examples" / "PPT-EZ-CA-0001-first-tranche-simulation.json"
)
FIXTURE_SCHEMA_PATH = PROJECT / "schemas" / "m5-first-tranche-simulation.schema.json"
RECEIPT_SCHEMA_PATH = PROJECT / "schemas" / "m5-first-tranche-receipt.schema.json"
DECISION_CONTEXT_SCHEMA_PATH = PROJECT / "schemas" / "m5canon-decision-context.schema.json"
HUMAN_TERMS_MANIFEST_PATH = (
    HERE / "manifests" / "SPRING-COMMONS-DOC-SET-01-23.v0.6-draft.json"
)
EXECUTABLE_PATH = HERE / "numscript" / "reserve-tranche.num"
EXTERNAL_GATES = {
    "EXTERNAL_AUTHORITY",
    "REGULATED_PROVIDER",
    "PROFESSIONAL_JUDGMENT",
    "HUMAN_FIDUCIARY",
}
ACCEPTED_EXTERNAL_STATUS = "EVIDENCED_AUTHORITY"
ACCEPTED_INTERNAL_STATUSES = {"SIMULATED_PASS", "EVIDENCED_AUTHORITY"}
POLICY_VERSION = "M5-RICARDIAN-TRIPLE-LAYER-001:draft-2026-09-20"
IMPLEMENTATION_VERSION = "1.1.0-draft"
FUNCTION_URIS = (
    ("M5CANON.PRINCIPAL.RESOLVE.v1", "urn:m5:function:m5canon:principal:resolve:v1"),
    ("M5CANON.CREDENTIAL.VERIFY.v1", "urn:m5:function:m5canon:credential:verify:v1"),
    ("M5CANON.DELEGATION.VERIFY.v1", "urn:m5:function:m5canon:delegation:verify:v1"),
    ("M5CANON.JURISDICTION.RESOLVE.v1", "urn:m5:function:m5canon:jurisdiction:resolve:v1"),
    ("M5CANON.POLICY.EVALUATE.v1", "urn:m5:function:m5canon:policy:evaluate:v1"),
    ("M5CANON.APPROVAL.VERIFY.v1", "urn:m5:function:m5canon:approval:verify:v1"),
    ("M5CANON.ACTION.AUTHORIZE.v1", "urn:m5:function:m5canon:action:authorize:v1"),
    ("M5CANON.RECEIPT.COMMIT.v1", "urn:m5:function:m5canon:receipt:commit:v1"),
)


def _timestamp(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _schema_errors(record: Any) -> list[str]:
    schema = json.loads(FIXTURE_SCHEMA_PATH.read_text())
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [
        f"{'.'.join(str(part) for part in error.absolute_path) or '$'}: {error.message}"
        for error in sorted(validator.iter_errors(record), key=lambda item: list(item.absolute_path))
    ]


def _duplicate_ids(items: list[dict[str, Any]], field: str) -> set[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for item in items:
        if not isinstance(item, dict) or not isinstance(item.get(field), str):
            continue
        value = item[field]
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    return duplicates


def _relational_errors(record: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return ["$: input must be an object"]
    collections = (
        ("documents", "document_id"),
        ("participants", "participant_id"),
        ("evidence_catalog", "evidence_id"),
        ("checkpoints", "checkpoint_id"),
        ("impact_metrics", "metric_id"),
    )
    for collection, field in collections:
        items = record.get(collection, [])
        if not isinstance(items, list):
            continue
        for duplicate in sorted(_duplicate_ids(items, field)):
            errors.append(f"duplicate {field}: {duplicate}")

    document_ids = {
        item["document_id"]
        for item in record.get("documents", [])
        if isinstance(item, dict) and isinstance(item.get("document_id"), str)
    }
    evidence_ids = {
        item["evidence_id"]
        for item in record.get("evidence_catalog", [])
        if isinstance(item, dict) and isinstance(item.get("evidence_id"), str)
    }
    checkpoints = record.get("checkpoints", [])
    if not isinstance(checkpoints, list):
        checkpoints = []
    for checkpoint in checkpoints:
        if not isinstance(checkpoint, dict):
            continue
        checkpoint_id = checkpoint.get("checkpoint_id", "UNRESOLVED-CHECKPOINT")
        source_documents = checkpoint.get("source_documents", [])
        if not isinstance(source_documents, list):
            source_documents = []
        for reference in source_documents:
            if reference not in document_ids:
                errors.append(f"{checkpoint_id} unresolved source_document: {reference}")
        evidence_refs = checkpoint.get("evidence_refs", [])
        if not isinstance(evidence_refs, list):
            evidence_refs = []
        for reference in evidence_refs:
            if reference not in evidence_ids:
                errors.append(f"{checkpoint_id} unresolved evidence_ref: {reference}")
        if checkpoint.get("status") in ACCEPTED_INTERNAL_STATUSES and not evidence_refs:
            errors.append(f"{checkpoint_id} passing status requires evidence")

    metrics = record.get("impact_metrics", [])
    if not isinstance(metrics, list):
        metrics = []
    for metric in metrics:
        if not isinstance(metric, dict):
            continue
        source_documents = metric.get("source_documents", [])
        if not isinstance(source_documents, list):
            source_documents = []
        for reference in source_documents:
            if reference not in document_ids:
                errors.append(f"{metric.get('metric_id', 'UNRESOLVED-METRIC')} unresolved source_document: {reference}")
    return errors


def _load_decision_context(record: Any) -> tuple[dict[str, Any] | None, list[str]]:
    if not isinstance(record, dict) or not isinstance(record.get("decision_context"), dict):
        return None, ["decision_context: missing or malformed binding"]
    binding = record["decision_context"]
    uri = binding.get("uri")
    schema_uri = binding.get("schema_uri")
    if not isinstance(uri, str) or not isinstance(schema_uri, str):
        return None, ["decision_context: URI and schema URI must be strings"]
    context_path = (DEFAULT_FIXTURE.parent / uri).resolve()
    schema_path = (DEFAULT_FIXTURE.parent / schema_uri).resolve()
    errors: list[str] = []
    for label, path in (("record", context_path), ("schema", schema_path)):
        if not path.is_relative_to(PROJECT) or not path.is_file():
            errors.append(f"decision_context: {label} URI is outside the project or missing")
    if errors:
        return None, errors
    if file_digest(context_path) != binding.get("digest"):
        return None, ["decision_context: URI and digest do not identify the same artifact"]
    context = json.loads(context_path.read_text())
    schema = json.loads(schema_path.read_text())
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors.extend(
        f"decision_context.{'.'.join(str(part) for part in error.absolute_path) or '$'}: {error.message}"
        for error in sorted(validator.iter_errors(context), key=lambda item: list(item.absolute_path))
    )
    if (
        context.get("context_id") != binding.get("id")
        or context.get("version") != binding.get("version")
        or context.get("supersession_history") != binding.get("supersession_history")
    ):
        errors.append("decision_context: binding identity or supersession history mismatch")
    taxonomy = context.get("taxonomy", {})
    taxonomy_uri = taxonomy.get("uri") if isinstance(taxonomy, dict) else None
    if not isinstance(taxonomy_uri, str):
        errors.append("decision_context.taxonomy: missing URI")
    else:
        taxonomy_path = (context_path.parent / taxonomy_uri).resolve()
        if not taxonomy_path.is_relative_to(PROJECT) or not taxonomy_path.is_file():
            errors.append("decision_context.taxonomy: URI is outside the project or missing")
        elif file_digest(taxonomy_path) != taxonomy.get("digest"):
            errors.append("decision_context.taxonomy: URI and digest do not identify the same artifact")
    return context, errors


def _decision_context_errors(
    context: dict[str, Any], evidence: dict[str, dict[str, Any]] | None = None
) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    unresolved: list[str] = []
    evidence = evidence or {}

    def evidence_is_current(reference: Any) -> bool:
        item = evidence.get(reference) if isinstance(reference, str) else None
        return bool(
            item
            and item.get("status") == "CURRENT"
            and item.get("authoritative") is True
            and item.get("synthetic") is False
        )

    graph = context.get("jurisdiction_graph", {})
    nodes = graph.get("nodes", []) if isinstance(graph, dict) else []
    relationships = graph.get("relationships", []) if isinstance(graph, dict) else []
    node_ids = {item.get("jurisdiction_id") for item in nodes if isinstance(item, dict)}
    errors.extend(
        f"decision_context.jurisdiction_graph: {detail}"
        for detail in jurisdiction_graph_errors(graph)
    )
    for relationship in relationships:
        if not isinstance(relationship, dict):
            continue
        for field in ("from_ref", "to_ref"):
            if relationship.get(field) not in node_ids:
                errors.append(f"decision_context.jurisdiction_graph: unresolved {field}")

    asset = context.get("asset_classification", {})
    authority = context.get("account_authority", {})
    route = context.get("institutional_route", {})
    legal = context.get("external_legal_classification", {})
    access = context.get("receipt_access_policy", {})
    if isinstance(asset, dict) and isinstance(authority, dict):
        errors.extend(
            f"decision_context.asset_classification: {detail}"
            for detail in draft_asset_policy_blockers(asset, str(authority.get("account_type")))
            if detail not in {"ASSET_CLASSIFICATION_NOT_CURRENT"}
        )
        if authority.get("account_type") not in asset.get("permitted_account_types", []):
            errors.append("decision_context: account type is not permitted for the asset")
        if asset.get("jurisdiction_graph_ref") != graph.get("graph_id"):
            errors.append("decision_context: asset jurisdiction graph reference is unresolved")
        if asset.get("receipt_policy_ref") != access.get("policy_id"):
            errors.append("decision_context: asset receipt policy reference is unresolved")
        if legal.get("classification_id") not in asset.get("external_legal_classification_refs", []):
            errors.append("decision_context: external legal classification reference is unresolved")
        if route.get("route_id") not in asset.get("institutional_routing_refs", []):
            errors.append("decision_context: institutional route reference is unresolved")
        if not set(asset.get("required_credential_refs", [])).issubset(
            set(authority.get("credential_refs", []))
        ):
            errors.append("decision_context: required asset credentials are absent from account authority")
    if isinstance(authority, dict):
        for field, refs_field in (
            ("credential_state", "credential_refs"),
            ("delegation_state", "delegation_refs"),
        ):
            if authority.get(field) == "CURRENT" and not authority.get(refs_field):
                errors.append(f"decision_context: CURRENT {field} requires {refs_field}")
        if authority.get("mandate_state") == "CURRENT" and not authority.get("mandate_ref"):
            errors.append("decision_context: CURRENT mandate requires mandate_ref")
        if authority.get("credential_state") == "CURRENT" or authority.get("delegation_state") == "CURRENT" or authority.get("mandate_state") == "CURRENT":
            authority_evidence = authority.get("evidence_refs", [])
            if not authority_evidence or not all(evidence_is_current(ref) for ref in authority_evidence):
                errors.append("decision_context: current account authority requires resolved authoritative evidence")
    if isinstance(legal, dict) and legal.get("status") == "CURRENT":
        legal_evidence = legal.get("evidence_refs", [])
        if not legal_evidence or not all(evidence_is_current(ref) for ref in legal_evidence):
            errors.append("decision_context: current legal classification requires resolved authoritative evidence")
    if isinstance(graph, dict) and graph.get("status") == "CURRENT":
        graph_evidence = graph.get("evidence_refs", [])
        if not graph_evidence or not all(evidence_is_current(ref) for ref in graph_evidence):
            errors.append("decision_context: current jurisdiction graph requires resolved authoritative evidence")
    if isinstance(route, dict):
        if route.get("subject_asset_ref") != asset.get("asset_id"):
            errors.append("decision_context: institutional route subject asset is unresolved")
        if route.get("jurisdiction_graph_ref") != graph.get("graph_id"):
            errors.append("decision_context: institutional route jurisdiction graph is unresolved")
        requirement_ids = set()
        required_route_semantics = {
            "ROUTE-REQ-LEGAL-CLASSIFICATION": {
                "organization_type": "QUALIFIED_PROFESSIONAL",
                "institution_identifier": "OTHER",
                "function": "EXTERNAL_LEGAL_CLASSIFICATION",
                "required_action": "QUALIFIED_PROFESSIONAL_REVIEW",
            },
            "ROUTE-REQ-ESCROW": {
                "organization_type": "BANK_FSP_ESCROW",
                "institution_identifier": "OTHER",
                "function": "ESCROW_ACCOUNT_AND_SETTLEMENT",
                "required_action": "LICENSE_OR_CREDENTIAL_VERIFICATION",
            },
            "ROUTE-REQ-DTTC": {
                "participant_ref": "M5-DTTC",
                "organization_type": "INTERNAL_MEMBER_POOL",
                "institution_identifier": "M5_DTTC",
                "function": "INTERNAL_DISTRIBUTED_TRUST_AND_TITLE_MEMBER_POOL",
                "required_action": "MEMBERSHIP_STATUS_VERIFICATION",
            },
        }
        for requirement in route.get("requirements", []):
            if not isinstance(requirement, dict):
                continue
            requirement_id = requirement.get("requirement_id")
            if requirement_id in requirement_ids:
                errors.append(f"decision_context: duplicate route requirement {requirement_id}")
            requirement_ids.add(requirement_id)
            if requirement.get("jurisdiction_ref") not in node_ids:
                errors.append(f"decision_context: {requirement_id} jurisdiction is unresolved")
            if requirement.get("receipt_access_policy_ref") != access.get("policy_id"):
                errors.append(f"decision_context: {requirement_id} receipt policy is unresolved")
            expected = required_route_semantics.get(requirement_id)
            if expected and any(requirement.get(field) != value for field, value in expected.items()):
                errors.append(f"decision_context: {requirement_id} institution or function semantics mismatch")
            route_evidence = requirement.get("evidence_refs", [])
            if requirement.get("status") != "CURRENT" or not route_evidence:
                unresolved.append(str(requirement_id))
            elif not all(evidence_is_current(ref) for ref in route_evidence):
                errors.append(f"decision_context: {requirement_id} evidence is unresolved or non-authoritative")
        required_route_ids = {
            "ROUTE-REQ-LEGAL-CLASSIFICATION",
            "ROUTE-REQ-ESCROW",
            "ROUTE-REQ-DTTC",
        }
        for missing in sorted(required_route_ids - requirement_ids):
            errors.append(f"decision_context: missing required institutional route {missing}")

    status_fields = (
        ("ASSET_CLASSIFICATION", asset.get("classification_state")),
        ("EXTERNAL_LEGAL_CLASSIFICATION", legal.get("status")),
        ("JURISDICTION_GRAPH", graph.get("status")),
        ("CREDENTIAL", authority.get("credential_state")),
        ("DELEGATION", authority.get("delegation_state")),
        ("MANDATE", authority.get("mandate_state")),
        ("INSTITUTIONAL_ROUTE", route.get("status")),
    )
    unresolved.extend(label for label, state in status_fields if state != "CURRENT")
    if authority.get("revocation_state") != "NOT_REVOKED":
        unresolved.append("AUTHORITY_REVOCATION_STATE")
    return errors, sorted(set(unresolved))


def _checkpoint_satisfied(checkpoint: dict[str, Any], evidence: dict[str, Any]) -> bool:
    status = checkpoint["status"]
    gate_type = checkpoint["gate_type"]
    references = checkpoint["evidence_refs"]
    if status not in ACCEPTED_INTERNAL_STATUSES or not references:
        return False
    if not all(ref in evidence and evidence[ref]["status"] == "CURRENT" for ref in references):
        return False
    if gate_type in EXTERNAL_GATES:
        if status != ACCEPTED_EXTERNAL_STATUS:
            return False
        return all(
            evidence[ref]["authoritative"]
            and not evidence[ref]["synthetic"]
            for ref in references
        )
    return True


def _receipt(
    record: Any,
    validation_errors: list[str],
    unresolved: list[str],
    decision_context: dict[str, Any] | None = None,
    fixture_digest: str | None = None,
) -> dict[str, Any]:
    if not isinstance(record, dict):
        record = {}
    simulation_id = record.get("simulation_id")
    if not isinstance(simulation_id, str) or not simulation_id:
        simulation_id = "UNRESOLVED-SIMULATION"
    state_machine = record.get("state_machine", {}) if isinstance(record.get("state_machine"), dict) else {}
    context = record.get("receipt_context", {}) if isinstance(record.get("receipt_context"), dict) else {}
    checkpoints = record.get("checkpoints", [])
    if not isinstance(checkpoints, list):
        checkpoints = []
    required_count = sum(
        item.get("required") is True for item in checkpoints if isinstance(item, dict)
    )
    timestamp = context.get("timestamp")
    if not isinstance(timestamp, str) or not FormatChecker().conforms(timestamp, "date-time"):
        timestamp = "1970-01-01T00:00:00Z"
    sequence = context.get("sequence")
    if not isinstance(sequence, int) or isinstance(sequence, bool) or sequence < 0:
        sequence = 0
    anchor = context.get("ordering_anchor")
    previous_digest = context.get("previous_receipt_digest")
    if anchor != "PREVIOUS_RECEIPT" or not isinstance(previous_digest, str):
        anchor = "GENESIS"
        previous_digest = None
    decision = "HOLD" if validation_errors or unresolved else "READY_FOR_AUTHORIZED_HUMAN_REVIEW"
    exceptions = [
        {"code": "INPUT_VALIDATION_FAILED", "status": "UNRESOLVED", "detail": detail}
        for detail in validation_errors
    ] + [
        {"code": checkpoint_id, "status": "UNRESOLVED", "detail": "Required checkpoint is not satisfied"}
        for checkpoint_id in unresolved
    ]
    policy_outcome = "UNRESOLVED" if validation_errors or unresolved else "READY_FOR_AUTHORIZED_HUMAN_REVIEW"
    function_base = {
        "policy_version": POLICY_VERSION,
        "implementation_id": "SPRING-COMMONS-FIRST-TRANCHE-EVALUATOR",
        "implementation_version": IMPLEMENTATION_VERSION,
    }
    context = decision_context or {}
    context_binding = record.get("decision_context", {}) if isinstance(record.get("decision_context"), dict) else {}
    taxonomy = context.get("taxonomy", {}) if isinstance(context.get("taxonomy"), dict) else {}
    asset = context.get("asset_classification", {}) if isinstance(context.get("asset_classification"), dict) else {}
    legal = context.get("external_legal_classification", {}) if isinstance(context.get("external_legal_classification"), dict) else {}
    graph = context.get("jurisdiction_graph", {}) if isinstance(context.get("jurisdiction_graph"), dict) else {}
    authority = context.get("account_authority", {}) if isinstance(context.get("account_authority"), dict) else {}
    route = context.get("institutional_route", {}) if isinstance(context.get("institutional_route"), dict) else {}
    access = context.get("receipt_access_policy", {}) if isinstance(context.get("receipt_access_policy"), dict) else {}
    requirements = route.get("requirements", []) if isinstance(route.get("requirements"), list) else []
    grants = access.get("grants", []) if isinstance(access.get("grants"), list) else []
    receipt_id = f"{simulation_id}-RECEIPT"
    unresolved_requirements = sorted(set((["INPUT_VALIDATION_FAILED"] if validation_errors else []) + unresolved))
    authority_evidence = authority.get("evidence_refs", [])
    function_outcomes = {
        "M5CANON.PRINCIPAL.RESOLVE.v1": "SATISFIED" if authority.get("human_principal_refs") and not validation_errors else "UNRESOLVED",
        "M5CANON.CREDENTIAL.VERIFY.v1": "SATISFIED" if not validation_errors and authority.get("credential_state") == "CURRENT" and authority_evidence else "UNRESOLVED",
        "M5CANON.DELEGATION.VERIFY.v1": "SATISFIED" if not validation_errors and authority.get("delegation_state") == "CURRENT" and authority_evidence else "UNRESOLVED",
        "M5CANON.JURISDICTION.RESOLVE.v1": "SATISFIED" if not validation_errors and graph.get("status") == "CURRENT" and graph.get("evidence_refs") else "UNRESOLVED",
        "M5CANON.POLICY.EVALUATE.v1": policy_outcome,
        "M5CANON.APPROVAL.VERIFY.v1": "SATISFIED" if not validation_errors and requirements and all(item.get("status") == "CURRENT" and item.get("evidence_refs") for item in requirements if isinstance(item, dict)) else "UNRESOLVED",
        "M5CANON.ACTION.AUTHORIZE.v1": "HOLD",
        "M5CANON.RECEIPT.COMMIT.v1": "COMMITTED_SIMULATION_RECEIPT",
    }
    receipt = {
        "schema_version": "1.0-draft",
        "receipt_id": f"{simulation_id}-RECEIPT",
        "receipt_version": "1.2",
        "receipt_class": "PUBLIC_SYNTHETIC_NON_AUTHORITATIVE",
        "simulation_id": simulation_id,
        "project_id": record.get("project_id") if isinstance(record.get("project_id"), str) and record.get("project_id") else "UNRESOLVED-PROJECT",
        "tranche_id": record.get("tranche", {}).get("tranche_id") if isinstance(record.get("tranche"), dict) and isinstance(record.get("tranche", {}).get("tranche_id"), str) and record.get("tranche", {}).get("tranche_id") else "UNRESOLVED-TRANCHE",
        "m5canon": {
            "policy_version": POLICY_VERSION,
            "functions": [
                {
                    **function_base,
                    "function_id": function_id,
                    "function_uri": function_uri,
                    "outcome": function_outcomes[function_id],
                }
                for function_id, function_uri in FUNCTION_URIS
            ],
        },
        "artifacts": {
            "fixture": {
                "id": simulation_id,
                "version": record.get("schema_version", "UNRESOLVED"),
                "digest": fixture_digest or canonical_digest(record),
                "uri": f"urn:sha256:{(fixture_digest or canonical_digest(record)).removeprefix('sha256:')}",
            },
            "human_terms_manifest": {
                "id": "SPRING-COMMONS-DOC-SET-01-23",
                "version": "v0.6-draft-package",
                "digest": file_digest(HUMAN_TERMS_MANIFEST_PATH),
                "uri": "pilots/312-spring-commons/simulations/first-tranche/manifests/SPRING-COMMONS-DOC-SET-01-23.v0.6-draft.json",
            },
            "machine_policy": {
                "id": "SPRING-COMMONS-FIRST-TRANCHE-GATES",
                "version": "1.0-draft",
                "digest": file_digest(FIXTURE_SCHEMA_PATH),
                "uri": "pilots/312-spring-commons/schemas/m5-first-tranche-simulation.schema.json",
            },
            "executable_instruction": {
                "id": "SPRING-COMMONS-RESERVE-TRANCHE",
                "version": "1.0-draft",
                "digest": file_digest(EXECUTABLE_PATH),
                "uri": "pilots/312-spring-commons/simulations/first-tranche/numscript/reserve-tranche.num",
            },
            "decision_context": {
                "id": context_binding.get("id", "UNRESOLVED-DECISION-CONTEXT"),
                "version": context_binding.get("version", "UNRESOLVED"),
                "digest": context_binding.get("digest", canonical_digest({})),
                "uri": context_binding.get("uri", "urn:m5:unresolved:decision-context"),
            },
            "taxonomy_profile": {
                "id": taxonomy.get("profile_id", "UNRESOLVED-TAXONOMY"),
                "version": taxonomy.get("version", "UNRESOLVED"),
                "digest": taxonomy.get("digest", canonical_digest({})),
                "uri": taxonomy.get("uri", "urn:m5:unresolved:taxonomy"),
            },
        },
        "decision_record": {
            "decision_id": f"DECISION-{simulation_id}",
            "result": decision,
            "unresolved_requirements": unresolved_requirements,
            "receipt_ref": receipt_id,
        },
        "decision_context": {
            "context_ref": context.get("context_id", "UNRESOLVED-DECISION-CONTEXT"),
            "taxonomy_profile_ref": taxonomy.get("profile_id", "UNRESOLVED-TAXONOMY"),
            "asset_ref": asset.get("asset_id", "UNRESOLVED-ASSET"),
            "m5_class": asset.get("m5_class", "UNRESOLVED"),
            "external_legal_classification_ref": legal.get("classification_id", "UNRESOLVED-LEGAL-CLASSIFICATION"),
            "jurisdiction_graph_ref": graph.get("graph_id", "UNRESOLVED-JURISDICTION-GRAPH"),
            "account_ref": authority.get("account_ref", "UNRESOLVED-ACCOUNT"),
            "account_type": authority.get("account_type", "UNRESOLVED"),
            "human_principal_refs": authority.get("human_principal_refs", []),
            "credential_state": authority.get("credential_state", "UNRESOLVED"),
            "delegation_state": authority.get("delegation_state", "UNRESOLVED"),
            "mandate_ref": authority.get("mandate_ref", "UNRESOLVED-MANDATE"),
            "mandate_state": authority.get("mandate_state", "UNRESOLVED"),
            "revocation_state": authority.get("revocation_state", "UNRESOLVED"),
            "institutional_route_ref": route.get("route_id", "UNRESOLVED-INSTITUTIONAL-ROUTE"),
            "institutional_route_status": route.get("status", "UNRESOLVED"),
            "receipt_access_policy_ref": access.get("policy_id", "UNRESOLVED-RECEIPT-POLICY"),
        },
        "actor_authority": {
            "actor_ref": "OFFLINE-DETERMINISTIC-SIMULATOR",
            "principal_ref": (authority.get("human_principal_refs") or ["UNRESOLVED-PRINCIPAL"])[0],
            "legal_entity_ref": authority.get("legal_entity_ref", "UNRESOLVED-ENTITY"),
            "account_ref": authority.get("account_ref", "UNRESOLVED-ACCOUNT"),
            "account_type": authority.get("account_type", "UNRESOLVED"),
            "role_ref": "CAPITAL_PROVIDER",
            "credential_refs": authority.get("credential_refs", []),
            "credential_state": authority.get("credential_state", "UNRESOLVED"),
            "delegation_refs": authority.get("delegation_refs", []),
            "delegation_state": authority.get("delegation_state", "UNRESOLVED"),
            "mandate_ref": authority.get("mandate_ref", "UNRESOLVED-MANDATE"),
            "mandate_state": authority.get("mandate_state", "UNRESOLVED"),
            "jurisdiction_refs": authority.get("jurisdiction_refs", []),
            "revocation_state": authority.get("revocation_state", "UNRESOLVED"),
            "authority_evidence_refs": authority.get("evidence_refs", []),
        },
        "approvals": [],
        "adapter_provider_refs": [
            {
                "participant_ref": item.get("participant_ref", "UNRESOLVED-PARTICIPANT"),
                "institution_identifier": item.get("institution_identifier", "OTHER"),
                "function": item.get("function", "UNRESOLVED-FUNCTION"),
                "required_action": item.get("required_action", "UNRESOLVED-ACTION"),
                "status": item.get("status", "UNRESOLVED"),
                "evidence_refs": item.get("evidence_refs", []),
            }
            for item in requirements if isinstance(item, dict)
        ],
        "receipt_access": {
            "policy_ref": access.get("policy_id", "UNRESOLVED-RECEIPT-POLICY"),
            "policy_digest": canonical_digest(access),
            "default_access": access.get("default_access", "DENY"),
            "public_field_scope": sorted({field for grant in grants if isinstance(grant, dict) and grant.get("grantee_type") == "PUBLIC" and grant.get("access_state") == "AUTHORIZED" for field in grant.get("field_scope", [])}),
            "protected_field_classes": access.get("protected_field_classes", []),
            "authorized_grant_refs": [grant.get("grant_id") for grant in grants if isinstance(grant, dict) and grant.get("access_state") == "AUTHORIZED"],
            "pending_grant_refs": [grant.get("grant_id") for grant in grants if isinstance(grant, dict) and grant.get("access_state") == "PENDING"],
            "access_log_required": access.get("access_log_required", True),
            "access_log_refs": [],
        },
        "ordering": {
            "timestamp": timestamp,
            "sequence": sequence,
            "anchor": anchor,
            "previous_receipt_digest": previous_digest,
        },
        "decision": decision,
        "execution_authorized": False,
        "authority_effect": "NONE",
        "network_write_performed": False,
        "financial_movement_performed": False,
        "checkpoint_summary": {
            "required": required_count,
            "satisfied": max(0, required_count - len(unresolved)) if not validation_errors else 0,
            "unresolved_ids": ["INPUT_VALIDATION_FAILED"] if validation_errors else unresolved,
        },
        "state_transition": {
            "prior_state": state_machine.get("current_state", "UNRESOLVED"),
            "requested_state": state_machine.get("requested_state", "UNRESOLVED"),
            "resulting_state": state_machine.get("fail_closed_state", "HOLD") if decision == "HOLD" else state_machine.get("current_state", "UNRESOLVED"),
        },
        "exceptions": exceptions,
        "reconciliation": {
            "status": "NOT_APPLICABLE_SIMULATION",
            "provider_receipt_refs": [],
        },
        "observations": {
            "fixture_digest": fixture_digest or canonical_digest(record),
            "validation_status": "INVALID_UNRESOLVED" if validation_errors else "VALID",
        },
        "notices": [
            "Synthetic developer demonstration only.",
            "A ready result routes evidence to authorized humans; it never approves closing, source-chain activation, escrow release, draw authorization, settlement, or legal state.",
            "Authoritative external records and executed instruments control their respective domains.",
            "Targets and modeled values are not achieved impact or investment performance.",
        ],
    }
    receipt_schema = json.loads(RECEIPT_SCHEMA_PATH.read_text())
    Draft202012Validator(
        receipt_schema, format_checker=FormatChecker()
    ).validate(receipt)
    return receipt


def evaluate(record: Any) -> dict[str, Any]:
    """Evaluate fixture gates without authorizing or executing any transaction."""
    schema_errors = _schema_errors(record)
    validation_errors = schema_errors + _relational_errors(record)
    if schema_errors:
        return _receipt({}, validation_errors, [], fixture_digest=canonical_digest(record))
    decision_context, context_binding_errors = _load_decision_context(record)
    validation_errors.extend(context_binding_errors)
    context_unresolved: list[str] = []
    if decision_context is not None:
        evidence = {
            item["evidence_id"]: item
            for item in record.get("evidence_catalog", [])
            if isinstance(item, dict) and isinstance(item.get("evidence_id"), str)
        }
        context_errors, context_unresolved = _decision_context_errors(decision_context, evidence)
        validation_errors.extend(context_errors)
    if validation_errors:
        return _receipt(record, validation_errors, [], decision_context if not context_binding_errors else None)

    evidence = {item["evidence_id"]: item for item in record["evidence_catalog"]}
    required = [item for item in record["checkpoints"] if item["required"]]
    unresolved = [
        item["checkpoint_id"]
        for item in required
        if not _checkpoint_satisfied(item, evidence)
    ]
    return _receipt(record, [], sorted(set(unresolved + context_unresolved)), decision_context)


def render_receipt_view(
    receipt: dict[str, Any],
    decision_context: dict[str, Any],
    *,
    grantee_ref: str,
    credential_refs: set[str],
    jurisdiction_refs: set[str],
    access_purpose: str,
    access_log_ref: str,
    observed_at: str,
) -> dict[str, Any]:
    """Return a policy-bounded synthetic receipt view or deny access."""
    policy = decision_context["receipt_access_policy"]
    grant = next(
        (
            item
            for item in policy["grants"]
            if item["grantee_ref"] == grantee_ref
            and item["access_purpose"] == access_purpose
            and item["access_state"] == "AUTHORIZED"
        ),
        None,
    )
    if grant is None:
        raise PermissionError("receipt access denied by default")
    if not set(grant["credential_requirement_refs"]).issubset(credential_refs):
        raise PermissionError("receipt access credential requirement not satisfied")
    if grant["jurisdiction_ref"] is not None and grant["jurisdiction_ref"] not in jurisdiction_refs:
        raise PermissionError("receipt access jurisdiction requirement not satisfied")
    observed = _timestamp(observed_at)
    if grant["effective_from"] is not None and observed < _timestamp(grant["effective_from"]):
        raise PermissionError("receipt access grant is not yet effective")
    if grant["expires_at"] is not None and observed > _timestamp(grant["expires_at"]):
        raise PermissionError("receipt access grant has expired")
    if grant["revocation_ref"] is not None:
        raise PermissionError("receipt access grant is revoked")
    if policy["access_log_required"] and not access_log_ref:
        raise PermissionError("receipt access requires an attributable access log")

    if grant["grantee_type"] == "PUBLIC":
        allowed = {
            "decision": receipt["decision"],
            "safety": {
                "execution_authorized": receipt["execution_authorized"],
                "authority_effect": receipt["authority_effect"],
                "network_write_performed": receipt["network_write_performed"],
                "financial_movement_performed": receipt["financial_movement_performed"],
            },
            "public_exceptions": receipt["exceptions"],
        }
    else:
        field_views = {
            "classification": receipt["decision_context"],
            "authority": receipt["actor_authority"],
            "approvals": receipt["approvals"],
            "transfers": receipt["state_transition"],
            "settlement": {
                "execution_authorized": receipt["execution_authorized"],
                "network_write_performed": receipt["network_write_performed"],
                "financial_movement_performed": receipt["financial_movement_performed"],
                "adapter_provider_refs": receipt["adapter_provider_refs"],
            },
            "reconciliation": receipt["reconciliation"],
        }
        allowed = {field: field_views[field] for field in grant["field_scope"] if field in field_views}
    return {
        "grant_ref": grant["grant_id"],
        "grantee_ref": grantee_ref,
        "access_purpose": access_purpose,
        "field_scope": grant["field_scope"],
        "access_log_ref": access_log_ref,
        "view": allowed,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", nargs="?", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    record = json.loads(args.fixture.read_text())
    receipt = evaluate(record)
    rendered = json.dumps(receipt, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
