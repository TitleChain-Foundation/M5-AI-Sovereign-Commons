# External Reference Review — 2026-09-22

This historical maintainer-supplied note records source claims from the Sept. 22
package. It is not a new independent verification or deployment approval. It does not
claim partnership, endorsement, implementation, or conformance.

## OpenMeter

Official docs describe event-driven usage ingestion using CloudEvents JSON and
metered entitlement/balance features. Use OpenMeter as a reference metering
implementation behind an M5 `UsageMeter` adapter rather than as an authority or
hard dependency.

- https://openmeter.io/docs/metering/events/overview
- https://openmeter.io/docs/metering/events/usage-events
- https://openmeter.io/docs/integrations/notifications/entitlements

## x402

x402 V2 documents modular paywall components and lifecycle hooks around payment
and settlement verification. Keep x402 behind an M5 settlement adapter and
separate payment from M5Canon authority.

- https://x402.org/x402-v2-launch/

## Laya

The ConvAI Innovations Laya model repository currently identifies the model as
Apache-2.0 and provides downloadable safetensors/checkpoints. Treat published
performance comparisons as provider-authored benchmark claims unless
independently reproduced.

- https://huggingface.co/convaiinnovations/laya
- https://laya.convaiinnovations.com/

## Jev

TypeSafe describes Jev as its hosted System One model. Provider pricing/model
facts are volatile and should be revalidated from official documentation at
runtime/release time rather than hard-coded into M5 routing logic.

- https://typesafe.ai/blog/introducing-system-one-models-and-jev
- https://api.typesafe.ai/docs

## W3C Verifiable Credentials

W3C Verifiable Credentials Data Model 2.0 became a Recommendation on 15 May
2025. A v2.1 Working Draft exists in September 2026. Use v2.0 as the stable
baseline for this release unless a later profile is explicitly adopted.

- https://www.w3.org/TR/vc-data-model-2.0/
- https://www.w3.org/TR/vc-data-model/all/

## GLEIF vLEI

GLEIF describes vLEI as a verifiable organizational identity credential and
supports Legal Entity, Official Organizational Role (OOR), and other role
credential frameworks through Qualified vLEI Issuers. Preserve vLEI's native
trust/credential framework rather than falsely relabeling it as W3C VC.

- https://www.gleif.org/en/organizational-identity/lei-vlei/the-verifiable-lei-vlei
- https://www.gleif.org/en/organizational-identity/get-an-lei-vlei/get-a-vlei

## OpenCorporates

OpenCorporates exposes company number, registered jurisdiction, company status
where available, filings, statements, and provenance through its API. Its own
documentation cautions that absence of an inactive flag does not prove a
company is active where the underlying register does not expose status. Use it
as a normalized entity/provenance source, not universal proof of good standing.

- https://api.opencorporates.com/documentation/API-Reference

## Sumsub

Sumsub documents identity verification and a reusable Sumsub ID. It also
publishes on-chain attestation integrations. Treat the exact artifact returned
by the chosen integration as its actual evidence format; do not claim W3C VC
issuance unless the specific official integration documents it.

- https://docs.sumsub.com/docs/identity-verification
- https://support.sumsub.com/sumsub-id/what-is-sumsub-ID

## ID.me

ID.me documents a Digital Wallet/Credential Broker and credential-check APIs for
valid active credentials under named policies. Treat the supported ID.me
assertion/API artifact as identity evidence; do not relabel it as W3C VC unless
the selected integration officially supports that representation.

- https://docs.id.me/guides/learn-more/digital-wallet/overview
- https://docs.id.me/apis/check-credentials-api/overview
