# Download the Free M5 IAM Starting Pod

**Package:** `m5-iam-free-v0.2.0.zip`
**Status:** Draft for public review
**License state:** **Unregistered commons starter, not a registered M5 account**

**[Download the package](https://github.com/TitleChain-Foundation/M5-AI-Sovereign-Commons/releases/download/m5-iam-free-v0.2.0/m5-iam-free-v0.2.0.zip)**
· [SHA-256](https://github.com/TitleChain-Foundation/M5-AI-Sovereign-Commons/releases/download/m5-iam-free-v0.2.0/m5-iam-free-v0.2.0.zip.sha256)
· [Package manifest](m5iam-package.manifest.json)

IAM is the free starting point for every person. This package lets you create
an IAM starting pod on a computer you control, with open tools only: Python's
standard library and any web browser. No account, no payment, no network
connection and no vendor cloud.

> [!IMPORTANT]
> **This is a self-attested starting pod, not a verified identity.**
> Running this package does not issue a TCID, verify who you are, create an M5
> Bank account or a licensed M5POD, or give any authority to sign, pay,
> transfer title or delegate to an agent.

## Use it today

```bash
unzip m5-iam-free-v0.2.0.zip
cd m5-iam-free-v0.2.0
shasum -a 256 -c PACKAGE-CHECKSUMS.sha256          # verify every file
```

Then open `reference-implementation/m5-iam-free/` and double-click
**Start M5 IAM** (`.command` on macOS, `.bat` on Windows). The IAM app opens
in your browser. It runs on your own computer only.

1. **Attest.** Enter your name, choose your state chain, and tick
   "I am attesting to my humanity." That is the whole form.
2. **See what you have.** Your IAM is shown as active: human attested, not
   verified, free for life, with your attestation kept in three matching
   parts.
3. **See what you can use.** Free and open tools you can run today, and the
   registered accounts you can open later, shown as not activated.

On macOS, the first time you open a downloaded launcher you may need to
right-click it and choose **Open**. Prefer the command line? Run
`python3 m5_iam_app.py`, or `python3 m5_iam.py init --name "Your name" --chain wyomingchain.eth --i-am-human`.

## What you get

| Part | What it is |
| --- | --- |
| **IAM record** | `iam.json`: account `M5IAM-000`, status `IAM ONLY`, free |
| **Human attestation** | Your own statement that you are a human, in three matching parts: the words you read, the data software reads, and the check that confirms nothing changed. Marked self-attested and not verified |
| **Identifiers** | One local identifier. TCID, PayName, ENS and WSW URI stay empty |
| **Ledger** | A hash-chained record of what the tool wrote, so later changes are detectable |
| **IAM app** | A one-page app in your browser, served from your own computer only, with the form, your results, free tools and accounts you can open later |
| **Agent folder** | `m5agent/`, for rules and tooling for any agent you choose. Not tied to one vendor |
| **Export** | `m5_iam.py export` copies the whole pod into one ZIP you keep |

Every folder starts with `m5readme.md`. The pod is plain files: you can read,
copy, back up or delete it with ordinary tools.

## What needs registration

| You want | What it takes | Where |
| --- | --- | --- |
| A TCID and the three identifiers | Register your IAM account | [m5bank.app](https://m5bank.app/) |
| A verified identity or credential | Separate verification by an issuer | M5 account |
| A registered Bank of Me account and M5POD | Separate, optional activation | [M5POD activation](https://m5podactivationdemo.netlify.app/) |

The free IAM starting pod keeps working whether or not you ever register.

## Limits

- The attestation is your statement only. Nobody has checked it.
- The ledger detects changes to recorded files. It is not a signature and does
  not prove identity.
- This is reference code for inspection and testing, not a production service.
