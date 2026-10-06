# Download the Norton Ranch Blueprint into Your Own M5POD

**Package:** `norton-ranch-blueprint-v1.4.0.zip`
**Status:** Draft for public review
**License state:** **Unregistered commons starter, not a licensed M5POD**

**[Download the package](https://github.com/TitleChain-Foundation/M5-AI-Sovereign-Commons/releases/download/norton-ranch-blueprint-v1.4.0/norton-ranch-blueprint-v1.4.0.zip)**
· [SHA-256](https://github.com/TitleChain-Foundation/M5-AI-Sovereign-Commons/releases/download/norton-ranch-blueprint-v1.4.0/norton-ranch-blueprint-v1.4.0.zip.sha256)
· [Package manifest](m5pod-package.manifest.json)

This is the whole Norton Ranch Blueprint in one download: the documents,
schemas, synthetic examples, data registries, local-only reference code,
portability profile, and licenses. You don't have to collect links. Unpack it
on a computer you control and it works there, with no network connection and
no vendor cloud.

> [!IMPORTANT]
> **This is not a licensed M5POD until you register and activate.**
> Downloading, unpacking, or running this package does not create an M5
> account, a licensed M5POD, a registered business entity, a credential, or
> any authority. You can read, plan, and test with it today. It becomes part
> of a licensed M5POD only after you complete the activation steps below.

## What is in the package

| Layer | What you get |
| --- | --- |
| **Blueprint** | The complete Norton Ranch Blueprint documents, business model, stewardship covenant, and founder dedication |
| **Sovereign Herd** | The first reference implementation: architecture, roadmap, OEM program, and Halter case study |
| **Schemas** | Farm, animal, device, and device-assignment schemas, plus the Biological Stewardship Record |
| **Synthetic examples** | Example farm, animal, and assignment records you can copy and adapt |
| **Reference code** | `provision_herd.py`, standard-library Python with no network calls, which turns your herd file into stable local animal, device, and assignment records |
| **Data registries** | Machine-readable free and public data sources, with access and rights cautions |
| **Portability** | The M5POD Data Portability Profile and M5HUM Refusal and Consent Profile |
| **Integrity** | `PACKAGE-CHECKSUMS.sha256` for every file, and a published SHA-256 for the ZIP |
| **Licenses** | Apache-2.0 for code, CC-BY-4.0 for content, notices and trademarks. Founder family photographs are excluded from the open grants. |

## Use it today, before activation

```bash
unzip norton-ranch-blueprint-v1.4.0.zip
cd norton-ranch-blueprint-v1.4.0
shasum -a 256 -c PACKAGE-CHECKSUMS.sha256          # verify every file

cd reference-implementation/sovereign-herd
python3 provision_herd.py \
  --entity m5ent:synthetic:red-river-ranch \
  --farm m5farm:synthetic:red-river:001 \
  --input sample-herd.json \
  --output herd-manifest.generated.json
```

Replace `sample-herd.json` with your own herd file to plan your real records.
The output stays on your machine. Before activation you can:

- read and adapt every document, schema, and example;
- plan your farm, herd, animal, and device records and test them against the schemas;
- run the provisioning utility locally on your own data;
- use the Farmer Toolkit registry to find free and public data starting points.

## Activate: from starter package to licensed M5POD

| Step | What happens | Where |
| --- | --- | --- |
| 1. Register yourself | Create an M5IAM account and establish TCID / M5HUM identity | [m5bank.app](https://m5bank.app/) |
| 2. Activate your M5POD | Reserve and activate the private M5POD that holds your identity, evidence, and farm data | [M5POD activation](https://m5podactivationdemo.netlify.app/) |
| 3. Record your authority | Establish your role and authority (M5-CV) for the farm or ranch | M5 account |
| 4. Register your entity | Record your existing LLC, cooperative, partnership, trust, or sole proprietorship with its namespace and jurisdiction | [Entity activation](sovereign-herd/ENTITY-ACTIVATION-AND-PRICING.md) |
| 5. Activate the farm tools | Turn on the farm, herd, animal, device, and assignment tools for the registered entity | M5 account |

Once those steps are complete, the records you planned with this package can be
loaded into your licensed business M5POD context. The proposed M5
implementation is **$840/year per farm or business entity and $0 per cow per
month** in required software rent. M5 registration does not replace government
formation, livestock identification, tax, veterinary, or other legal
requirements.

## Why we simulate it first

Every Foundation project, including 312 Spring Commons, People's Trust
Farmland, Global UN Commons, and this Blueprint, is run as a full public
simulation before anyone is asked to rely on it. Real schemas, real code, and
the same authority and evidence steps a live operator would follow, using
synthetic data. That way anyone can inspect, test, and challenge the process
before it touches a real farm, animal, or dollar.

## Why this matters: the Sovereign Compute Access Act

The Blueprint shows, at the scale of one ranch, what the
[Sovereign Compute Access Act](https://github.com/TitleChain-Foundation/icsn-standards/blob/main/legislation/sovereign-compute-access-act/OFFICIAL-TEXT.md)
would make possible for everyone. Under the model Act, individuals,
cooperatives, and small businesses could run their own entities with sovereign
AI, local compute, and privacy:

| The model Act proposes | What it means on the ranch |
| --- | --- |
| **Sec. 101:** free, unmetered access to open-weight AI inside your own Sovereign Pod, with no telemetry or hosted-API condition | Herd models run on the farm's own computer, not rented per animal from a vendor cloud |
| **Sec. 202(b):** data generated locally belongs to the account holder | Herd, pasture, and sensor data stay the farmer's property |
| **Sec. 203:** AI agents act only within authority delegated by a human principal, and that authority is revocable at any time | Farm agents and service providers answer to the farmer, who can cut them off |
| **Sec. 103:** no conditioning on a subscription or continuing vendor relationship | **The animal is not the subscription.** |

The Act is model legislation published for public review. It is **not enacted
law** and has not been introduced by a legislative office. Our focus is to get
it passed so that every person, family business, and cooperative can do what
this package demonstrates.
[Read the public-review hub](https://github.com/TitleChain-Foundation/icsn-standards/blob/main/legislation/sovereign-compute-access-act/PUBLIC-REVIEW.md)
· [Submit a public comment](https://github.com/orgs/TitleChain-Foundation/discussions/38)

## Non-claims

- Not a licensed M5POD until registration and activation are complete.
- No packaged M5 Desktop installer is claimed to be available yet.
- Not production-ready and not a veterinary system.
- No farmer, ranch, animal, or device is claimed to be live on the system.
- No collar vendor is claimed to be M5 certified.

## Maintainers: publishing a release

```bash
python tools/build_norton_package.py            # writes dist/ (git-ignored)
git tag norton-ranch-blueprint-v1.4.0 && git push origin norton-ranch-blueprint-v1.4.0
```

Pushing the tag runs `.github/workflows/norton-package.yml`, which rebuilds the
package and attaches the ZIP and its SHA-256 to the GitHub release.
