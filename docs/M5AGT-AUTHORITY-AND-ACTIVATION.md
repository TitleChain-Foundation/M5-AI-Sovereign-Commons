# M5AGT Authority and Activation

**Status:** Draft for Public Comment

## 1. Governing relationship

An M5AGT is a bounded software capability. It is not an independent legal,
human, governmental, monetary, or regulatory principal.

Every consequential action must resolve through:

```text
accountable human or lawful entity
        |
        v
current identity, role, credential, standing, and jurisdiction
        |
        v
explicit and revocable delegation
        |
        v
bounded capability results
        |
        v
deterministic M5Canon evaluation
        |
        v
required accountable approval
        |
        v
authorized activation or action
        |
        v
append-only evidence receipt
```

## 2. Canonical activation sequence

The public architecture uses one activation sequence:

1. **Principal submission**  
   An accountable human or lawful entity signs the activation request and
   identifies its authority source.

2. **Identity and standing verification**  
   M5Canon verifies the principal, operator, current credentials, registrations,
   affiliations, good standing, scope, expiry, and revocation status.

3. **Origin and artifact verification**  
   M5Canon verifies the proposed implementation identity, source or artifact
   digest, declared operator, software bill of materials where required,
   deployment boundary, and provenance.

4. **Human-refusal evaluation**
   Before any covered persistent recording, retention, identification,
   tracking, unrelated inference, training, sharing, or actuation, M5Canon
   evaluates applicable human refusal profiles and signals. Minimal transient
   sensor processing may be used only to detect and enforce a refusal and must
   not be retained or repurposed. Active or unresolved refusal denies the
   covered operation. Absence, withdrawal, or expiry of refusal does not
   establish consent.

5. **Rights-constraint evaluation**
   A conforming `M5CAP.RIGHTS.CONSTRAINT.EVALUATE.v1` implementation may produce
   a signed result. Cyrus is the M5 reference named role for this capability.
   The result cannot create, waive, or remove rights.

6. **Provenance and continuity validation**
   A conforming `M5CAP.PROVENANCE.CONTINUITY.VALIDATE.v1` implementation may
   validate origin, custody, transformation, attribution, and continuity and
   produce a signed attestation. Savant is the M5 reference named role. The
   attestation is not an approval.

7. **Deterministic policy decision**
   M5Canon evaluates the verified evidence against a versioned policy and
   produces an allow or deny result. Supporting capabilities cannot replace
   this step.

8. **Accountable approval**
   Where policy, law, contract, governance, or risk classification requires an
   approval, M5Canon verifies the current signed approval of the accountable
   human, entity, board, officer, regulator, court, or other competent body.
   An M5AGT cannot approve itself or another M5AGT.

9. **Registry write and receipt**
   M5Canon records the status, scope, policy version, evidence references,
   approvals, restrictions, effective period, suspension and revocation
   controls, and an append-only receipt.

10. **Bounded runtime activation**
   The implementation may operate only within the authorized scope and must be
   re-evaluated when its identity, operator, model, endpoint, artifact,
   credential, delegation, jurisdiction, policy, or risk state changes.

Any failed, missing, malformed, expired, revoked, altered, disputed, or
out-of-scope requirement produces denial or an unresolved state. It must not be
silently converted into approval.

## 3. Named-role boundaries

Named roles make the architecture easier to understand, but their names are not
authority claims.

- Cyrus evaluates rights constraints; Cyrus is not the source of rights.
- Savant validates provenance and continuity of origin; Savant is not the
  approval authority.
- Milner protects the account's identity, knowledge, cognitive, policy, and
  operational boundary across BOM, BOU, BOB, BOI, and BOG; Milner is not
  M5Canon.
- Vionneta records and anchors provenance evidence and attribution; Vionneta
  does not create title or authorship.
- Lina orchestrates approved work; Lina cannot authorize it.
- Justitia supports dispute analysis and routing; Justitia is not automatically
  a court or binding adjudicator.
- Paine explains records; Paine's explanation is not the authoritative record.
- Green analyzes economic conditions; Green cannot independently move value.

## 4. Classification tracks

Native, marketplace, service, provider, certification, and tool classifications
must remain separate.

Connection, usefulness, API compatibility, marketplace acceptance, provider
registration, certification-node status, or an external relationship does not
automatically create M5NativeAgent status.

Public documentation must not claim that an external company, agency, regulator,
standards body, university, hospital, or government participates in M5 unless
that organization has supplied current authoritative evidence for the precise
claim.

Such organizations may instead be identified as external authoritative sources,
potential interfaces, or informative examples with an express
non-participation and non-endorsement statement.

## 5. Private implementation histories

The public Commons specifies interoperable functions, controls, and conformance
requirements. It does not need to publish private founding sequences, personal
identity records, private repository provenance, private M5POD evidence, or
internal operational history.

Named implementation histories may be documented separately after privacy,
authority, provenance, and publication review.

## 6. Activation does not confer external status

M5 activation does not itself confer:

- governmental, diplomatic, treaty, or sovereign recognition;
- legal-person status;
- professional or regulated status;
- issuer, transfer-agent, broker, dealer, adviser, bank, custodian, or fiduciary
  authority;
- authority to issue money, securities, stablecoins, deposits, or CBDCs;
- authority to adjudicate disputes;
- provider endorsement or certification.

M5Canon verifies evidence supplied from applicable authoritative sources. It
does not manufacture the underlying authority.
