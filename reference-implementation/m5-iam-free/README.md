# M5 IAM Free — local starting pod

**Status:** Draft for public review · reference code, not a production service

`m5_iam.py` creates a free IAM starting pod on a computer you control. It uses
only the Python standard library and makes no network calls. There is no
account to open, nothing to pay, and nothing is sent anywhere.

## Run it

Double-click **Start M5 IAM.command** (macOS) or **Start M5 IAM.bat**
(Windows), or run:

```bash
python3 m5_iam_app.py        # opens the IAM app in your browser
```

The app shows one short form: your name, your state chain, and "I am
attesting to my humanity." When you submit it, your IAM pod is created in
`~/M5POD-IAM` and the app shows what you have, the free tools you can use,
and the accounts you can open later.

The same steps from the command line:

```bash
python3 m5_iam.py init --name "Your name" --chain wyomingchain.eth --i-am-human --accept-cyrus
python3 m5_iam.py status
python3 m5_iam.py verify
python3 m5_iam.py consent --right-to-refuse select
python3 m5_iam.py export --output my-iam-pod.zip
```

The app listens on 127.0.0.1 only, accepts the form only from its own page,
and can do one thing to your files: create the pod. Neither file makes an
outbound network call.

## What it creates

```text
M5POD-IAM/
  m5readme.md
  m5-iam.html              status page, loads nothing from the network
  m5agent/                 rules and tooling for any agent you choose
  M0-M5IAM-000/
    iam.json               the IAM record: IAM ONLY, self-attested, not verified
    attestation/           your statement in three parts: words, data, check
    consent/consent.json   CYRUS Protocol accepted; right to refuse selected or not
    identifiers/           a local identifier; TCID and the others stay empty
    receive/               reserved, empty
    ledger/events.jsonl    hash-chained record of what the tool wrote
```

The first file in every folder is `m5readme.md` and tooling lives in
`m5agent/`, so the pod is not tied to any one agent or vendor.

## The CYRUS Protocol and your right to refuse

Activation requires you to **accept the CYRUS Protocol**, because it is what
protects you: no slavery, servitude or forced labour; freedom of thought,
conscience and faith, any faith or none; and your rights to identity, data,
privacy, self-determination and portability. It is held by the TitleChain
Sovereign Purpose Trust.

Under it you hold the **right to refuse consent**. You can select it when you
activate, or later with `m5_iam.py consent --right-to-refuse select`. On an IAM
it is recorded as **selected, not activated**: an IAM is self-attested, so it
activates only when your credentials are verified, by registering Bank of Me
or by an approved agency verifying your IAM through M5-x401. Every change is
recorded in the ledger.

## What it does not do

- It does not issue a TCID, PayName, ENS name or WSW URI.
- It does not verify identity. The attestation is your own statement.
- It does not create an M5 Bank account or a licensed M5POD.
- It cannot authorize a transaction, title transfer, payment, signature or
  delegated agent action.

The ledger shows whether recorded files were changed after they were written.
It is an integrity check, not a signature, and it does not prove who you are.

When you are ready to register, start at <https://m5bank.app/>.
