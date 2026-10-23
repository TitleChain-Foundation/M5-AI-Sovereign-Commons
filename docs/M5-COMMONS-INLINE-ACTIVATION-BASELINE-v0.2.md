# M5 Commons, InLine and Namespace Registry Activation — Baseline v0.2

**Status:** Review draft. No DNS, ENS, TLS, registrar or production website changes authorized. `commons.titlechainfoundation.org` is DNS/Pages pending.

## Reuse existing canonical infrastructure
- **Private M5Ecosystem:** `packages/jurisdiction/M5titlechain-domains.json` (326 registry records declared), `M5jurisdiction-registry.json`, `m5-api/standards/{registry-standard,namespace-authority-map,naming-standard,account-class-mapping,legacy-credential-terminology}.md`, `packages/m5agents/m5agents.registry.yaml`.
- **Public Foundation:** existing Commons `site/index.html`, docs and CI plus `TitleChain-Foundation/icsn-standards`.
- **Brand:** user-approved M5 Sovereign Commons RC v0.7 HTML; preserve visual foundation and reconcile route links before replacement.

## Eight workstreams
1. Branded website with reusable accessible components, preserving original Commons pathways.
2. Recover missing links and pages from canonical repos before creating placeholders. Placeholder labels must be explicit.
3. Public/private documentation mapping including repo/path/commit, classification, steward, approval and review receipts.
4. Native M5AGT document assignments, actual canonical agent identifiers, M5HUM/M5-CV authority, M5Canon fail-closed gates.
5. M5 InLine: reviewed static snapshots, content hashes, independent HTTPS hosts plus IPFS pin/mirror, ENS contenthash after authorized signing.
6. Monitoring: broken links, source/site drift, DNS or ENS pointer drift, TLS, missing backups, credential and policy drift, safe disclosure.
7. GitHub Pages custom domain and HTTPS verification for `commons.titlechainfoundation.org`; deployment requires human approval.
8. Deploy existing ICSN/M5Canon registry standards: hierarchy of nations, states/provinces, tribal nations, territories, counties/cities, institutions, entities and BKOM/BKOU/BKOB/BKOI/BKOG contexts, products/services, brands, standards and distinct adjudication pools. Reconcile schema versions before implementation.

## Critical addition: conventional DNS domain inventory and mapping
The 326-domain registry is predominantly sovereign ENS and other blockchain names and **is not a complete inventory of legacy DNS domains**. In particular, `m5bank.app` and `m5bank.cloud` do not appear in its current raw registry file. Do not mark them absent from the organization's Namecheap portfolio; the registered inventory is incomplete for DNS.

Maintain a separate **legacy_dns_domains** collection feeding the existing Legacy Namespace Credential / imported alias model, with one row per actual FQDN and a relation to its canonical entity/namespace record. Begin reconciliation with:
- `m5bank.app` — user-named existing domain; registrar/name-server/owner and exact ENS mapping require verification.
- `m5bank.cloud` — user-named existing domain; registrar/name-server/owner and exact ENS mapping require verification.
- `titlechainfoundation.org` — Foundation website; its `commons.titlechainfoundation.org` subdomain is pending verification and Pages binding.
- `icsnglobal.org`, `m5capital.com`, `m5bank.com`, `m5api.org`, `m5scan.io` — documented legacy mappings/references; verify current ownership individually.

Record fields: `fqdn`, `apex_domain`, `record_type`, `registrar`, `nameserver_provider`, `dns_zone_version`, `dns_records_evidence_ref`, `legal_entity_ref`, `canonical_icsn_name_ref`, `ens_name_ref`, `ens_controller_verified_at`, `legacy_domain_control_verified_at`, `intended_host`, `current_host`, `publication_manifest_sha256`, `mirror_cid`, `mirror_pin_status`, `certificate_ref`, `credential_status`, `last_checked_at`, `next_review_at`, `control_exception_status`.
Treat subdomains as route/host entries beneath their registered apex, not automatically as independently owned domains.
Imported DNS and ENS mappings must be **claims with verification evidence**, not inferred solely from matching names.
Government and tribunal naming examples are design references, not asserted governmental authority or real-world treaty recognition.

## Release controls
- No public export of private M5POD records, account evidence or registrar API keys.
- Signed human approval before TitleChain CAC issuance, ENS resolver changes, DNS failover or production deployments.
- Check registrar access, authoritative NS, DNSSEC, zone backups, DNS TXT proof, actual resolver/controller, pinning, HTTPS, and independent recovery procedures.
- Record policy and content hashes; test restore and alternate access periodically.
- Preserve current accounting rules: CCF-5 versus adjudication/due process versus `protocolpool.eth`; do not merge namespace and fund roles.
- Preserve historic naming patterns as aliases until canonical version reconciliation, including current BK-series naming.

## Acceptance
An audited source inventory, complete checked DNS portfolio, individual DNS→ICSN→ENS mapping proofs, published pages or labeled placeholders, passing link/content/privacy checks, tested mirror restore and M5HUM approval. No automated change is currently active.
