# Canonical context v1 → v2 migration

**Draft for Public Comment.** Preserve original records and hashes. This is a
breaking migration, not a relabeling of unknown or asserted authority.

| v1 field | v2 field | Required review |
| --- | --- | --- |
| title_container | title_state | Identify actual asset/title state and evidence |
| wrapper | instrument_state | Identify instrument and underlying M3 rights; no opaque basket inference |
| jurisdictional_security_state | jurisdiction_binding + authority_state | Resolve each namespace independently and separately evaluate authority |

V2 contains 13 dimensions, plus schema_version and context_id. Migration MUST
produce a new record with a digest of the preserved original and attributable
mapping evidence. Do not overwrite historical receipts or invent authority.

- KNOWN MAPPING with evidence → MIGRATE.
- AMBIGUOUS MAPPING or missing evidence → HOLD; no authorized v2 record emitted.
- INVALID LEGACY → REJECT or quarantine for review.

The [reference migration](../reference-implementation/commons-contracts/contracts.py)
requires explicit mappings for all changed dimensions. Its conservative public
fixture only migrates known mappings; not-applicable or more complex mappings
need an explicit reviewed deployment profile. It validates structure, not the
truth of evidence. The old schema remains a test fixture solely for migration.

Consumers MUST dispatch by schema version and reject unsupported versions.
Rollback selects the retained v1 record and its original consumer; it must not
silently convert v2 namespace/authority state back into the old combined field.
Jurisdiction binding itself is v2 for multi-namespace records; old v1 bindings
remain unresolved until independently mapped and validated. The event contract
is pre-release v1 with the corrected m5eventversion attribute; no production
compatibility is claimed for earlier draft ZIPs.
