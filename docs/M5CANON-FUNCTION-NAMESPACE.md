# M5Canon Function Namespace

**Status:** Draft for Public Comment

## 1. Purpose

This document separates deterministic M5Canon controls from bounded supporting
capabilities and human-readable role names.

Function identifiers define interoperable contracts. Names help people
understand those contracts. A name, identifier, registration, or implementation
does not grant legal authority, jurisdiction, recognition, or permission.

## 2. Namespace classes

### 2.1 M5Canon controls

`M5CANON.*` identifies a deterministic control function whose decision is owned
by M5Canon.

Initial control functions are:

| Compact identifier | Purpose |
| --- | --- |
| `M5CANON.PRINCIPAL.RESOLVE.v1` | Resolve the accountable human or lawful entity |
| `M5CANON.CREDENTIAL.VERIFY.v1` | Verify current role, credential, standing, and scope |
| `M5CANON.DELEGATION.VERIFY.v1` | Verify explicit, bounded, current delegation |
| `M5CANON.JURISDICTION.RESOLVE.v1` | Resolve the applicable-authority graph and sources |
| `M5CANON.POLICY.EVALUATE.v1` | Apply deterministic, versioned policy |
| `M5CANON.APPROVAL.VERIFY.v1` | Verify required accountable approvals |
| `M5CANON.ACTION.AUTHORIZE.v1` | Produce the final deterministic allow or deny result |
| `M5CANON.RECEIPT.COMMIT.v1` | Commit the attributable, append-only decision receipt |

### 2.2 Bounded capabilities

`M5CAP.*` identifies a supporting capability. An M5AGT, deterministic service,
external provider, or other approved implementation may perform that capability.
Its result is evidence supplied to a control; it is not the final source of
authority.

Initial capability functions are:

| Compact identifier | Reference named role | Authoritative limit |
| --- | --- | --- |
| `M5CAP.RIGHTS.CONSTRAINT.EVALUATE.v1` | Cyrus | Cannot create, remove, or waive rights |
| `M5CAP.PROVENANCE.CONTINUITY.VALIDATE.v1` | Savant | Validates origin and continuity but cannot grant permission or independently declare legal truth |
| `M5CAP.ACCOUNT.COGNITIVE_BOUNDARY.PROTECT.v1` | Milner | Protects account identity, knowledge, cognitive, policy, and operational boundaries but cannot become the source of authority |
| `M5CAP.PROVENANCE.EVIDENCE.ATTEST.v1` | Vionneta | Records and anchors provenance evidence but cannot independently establish title, authorship, or legal standing |
| `M5CAP.RUNTIME.ORCHESTRATE.v1` | Lina | Cannot approve issuance, transfer, classification, or jurisdiction |
| `M5CAP.DISPUTE.ANALYZE_AND_ROUTE.v1` | Justitia | Is not a court, tribunal, or binding adjudicator |
| `M5CAP.RECORD.PLAIN_LANGUAGE.EXPLAIN.v1` | Paine | Does not replace the authoritative record or qualified legal interpretation |
| `M5CAP.ECONOMIC.ANALYZE.v1` | Green | Cannot independently issue, allocate, transfer, or move value |

The named roles are reference implementations or interfaces. Another
implementation may conform to the same capability contract without using or
claiming the reference name.

## 3. Canonical URI

The canonical URI form is:

```text
urn:m5:function:<owner>:<domain>:<function>:v<major>
```

Examples:

```text
urn:m5:function:m5canon:action:authorize:v1
urn:m5:function:m5cap:provenance:continuity-validate:v1
```

The compact identifier and canonical URI must resolve to the same versioned
contract.

## 4. Versioning

- The final segment is a positive major version such as `v1`.
- A breaking change to required inputs, output meaning, authority boundary, or
  failure behavior requires a new major version.
- Compatible clarifications may update the document revision without changing
  the function major version.
- Receipts must record the exact function identifier and policy version used.
- An implementation version must be recorded separately from the function
  version.

## 5. Required registry fields

Every registered function or implementation must identify:

- canonical function identifier and URI;
- formal name and plain-language purpose;
- function class: `M5CANON_CONTROL` or `BOUNDED_CAPABILITY`;
- version;
- input and output contracts;
- deterministic versus AI-assisted behavior;
- implementation identity and version;
- accountable operator;
- permitted and prohibited effects;
- required credentials and delegation;
- applicable jurisdiction and policy references;
- evidence and receipt requirements;
- activation, suspension, revocation, and expiry state;
- conformance status and supporting evidence.

## 6. Naming boundary

Named roles improve comprehension. They do not:

- become principals;
- inherit the authority of a person represented in a name;
- create legal or governmental status;
- create an M5NativeAgent classification;
- authorize their own activation;
- expand their own scope;
- replace external authoritative records.

Machine policy must evaluate canonical identifiers and verified evidence, never
the persuasive force or familiarity of a display name.

## 7. Provider implementations

A provider may propose an implementation of an `M5CAP.*` contract. Function
compatibility does not imply endorsement, enrollment, certification, or
activation.

An external provider must not implement or claim ownership of an
`M5CANON.*` decision function. It may supply evidence or technical services that
M5Canon evaluates within a separately verified trust boundary.
