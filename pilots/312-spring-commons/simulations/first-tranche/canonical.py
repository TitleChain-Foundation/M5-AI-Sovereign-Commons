"""Shared canonical JSON and SHA-256 helpers for the first-tranche simulation."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


def canonical_json(value: Any) -> bytes:
    """Serialize JSON deterministically for digest and fingerprint bindings."""
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def sha256_bytes(value: bytes) -> str:
    """Return a tagged SHA-256 digest."""
    return f"sha256:{hashlib.sha256(value).hexdigest()}"


def canonical_digest(value: Any) -> str:
    """Return the SHA-256 digest of canonical JSON."""
    return sha256_bytes(canonical_json(value))


def file_digest(path: Path) -> str:
    """Return the SHA-256 digest of the exact bytes at *path*."""
    return sha256_bytes(path.read_bytes())


def verify_bound_artifact(
    base_dir: Path,
    uri: Any,
    expected_digest: Any,
    project_root: Path,
    label: str,
) -> Path:
    """Resolve and verify one project-contained, digest-bound artifact."""
    if not isinstance(uri, str) or not isinstance(expected_digest, str):
        raise ValueError(f"{label} URI and digest must be strings")
    path = (base_dir / uri).resolve()
    root = project_root.resolve()
    if not path.is_relative_to(root):
        raise ValueError(f"{label} URI escapes the Spring Commons project")
    if not path.is_file() or file_digest(path) != expected_digest:
        raise ValueError(f"{label} URI and digest do not identify the same artifact")
    return path


def draft_asset_policy_blockers(asset: dict[str, Any], account_type: str) -> list[str]:
    """Evaluate pilot-only M1–M5 invariants without creating legal authority."""
    blockers: list[str] = []
    m5_class = asset.get("m5_class")
    if m5_class not in {"M1", "M2", "M3", "M4", "M5"}:
        return ["ASSET_CLASSIFICATION_UNKNOWN"]
    if asset.get("classification_state") != "CURRENT":
        blockers.append("ASSET_CLASSIFICATION_NOT_CURRENT")
    if m5_class == "M1":
        if asset.get("investment_rights") is True:
            blockers.append("M4_CLASSIFICATION_REVIEW_REQUIRED")
        if any(asset.get(field) is True for field in ("creates_title", "transfers_source_asset")):
            blockers.append("M1_UTILITY_CANNOT_TRANSFER_M3_TITLE")
    elif m5_class == "M2":
        activity = asset.get("activity")
        if activity == "DERIVATIVE" and "DERIVATIVES_REGULATORY_REVIEW" not in asset.get("required_route_actions", []):
            blockers.append("M2_DERIVATIVE_ROUTE_REQUIRED")
        if activity == "SPOT" and "COMMODITY_PROVENANCE_VERIFY" not in asset.get("required_route_actions", []):
            blockers.append("M2_SPOT_PROVENANCE_ROUTE_REQUIRED")
    elif m5_class == "M3" and not asset.get("title_evidence_refs"):
        blockers.append("M3_TITLE_PROVENANCE_REQUIRED")
    elif m5_class == "M4" and account_type not in {"BOI", "BOG"}:
        blockers.append("M4_ACCOUNT_NOT_PERMITTED")
    elif m5_class == "M5":
        if account_type != "BOG":
            blockers.append("M5_ACCOUNT_NOT_PERMITTED")
        if asset.get("destination_account_domain") in {"M1", "M2", "M3"}:
            blockers.append("M5_DIRECT_LOWER_CLASS_POSTING_PROHIBITED")
        if asset.get("retail_access") is True:
            blockers.append("M5_RETAIL_ACCESS_PROHIBITED")
    return blockers


def jurisdiction_graph_errors(graph: dict[str, Any]) -> list[str]:
    """Check graph references and prevent Tribal Nations becoming state children."""
    errors: list[str] = []
    nodes = graph.get("nodes", []) if isinstance(graph.get("nodes"), list) else []
    relationships = graph.get("relationships", []) if isinstance(graph.get("relationships"), list) else []
    node_by_id = {
        item.get("jurisdiction_id"): item
        for item in nodes
        if isinstance(item, dict) and isinstance(item.get("jurisdiction_id"), str)
    }
    if len(node_by_id) != len(nodes):
        errors.append("duplicate or malformed jurisdiction IDs")
    for relationship in relationships:
        if not isinstance(relationship, dict):
            errors.append("malformed jurisdiction relationship")
            continue
        from_ref = relationship.get("from_ref")
        to_ref = relationship.get("to_ref")
        if from_ref not in node_by_id or to_ref not in node_by_id:
            errors.append("unresolved jurisdiction relationship reference")
            continue
        if (
            node_by_id[from_ref].get("normalized_level") == "TRIBAL_INDIGENOUS"
            and node_by_id[to_ref].get("normalized_level") == "STATE_PROVINCE"
            and relationship.get("relationship_type") == "SUBDIVISION_OF"
        ):
            errors.append("Tribal Nation cannot be reduced to a state subdivision")
    return errors
