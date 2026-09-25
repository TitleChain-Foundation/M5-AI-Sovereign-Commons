# Exhibit E - Capital, Debt, Securities and Settlement Architecture

> **© 2026 TitleChain Foundation.** Part of the Foundation's written submission
> to the SEC on File No. S7-2026-30 (emailed September 23, 2026; pending SEC
> posting). Licensed under CC-BY-4.0 with required attribution. TitleChain
> Foundation, M5 and related marks are not licensed, and no patent rights are
> granted. See [NOTICE](../NOTICE.md). *This notice is added by the repository and
> is not part of the submitted text.*

## Separation principle

A project may contain multiple economic and legal layers. They must not be collapsed into one token or one ledger entry.

```text
PHYSICAL / PUBLIC TITLE
        |
STEWARDSHIP / OPERATING RIGHTS
        |
PROJECT ENTITY / CONTRACTUAL RIGHTS
        |
DEBT / EQUITY / OTHER CAPITAL INSTRUMENTS
        |
SECURITY INSTRUMENT + TRANSFER AGENT (WHEN APPLICABLE)
        |
BANK / ESCROW / PAYMENT / PERMITTED DIGITAL RAILS
        |
RECONCILIATION + EVIDENCE
```

## Required fields for a material capital event

- source entity and accountable human;
- authority and account purpose;
- instrument/legal terms;
- asset/economic classification;
- external legal/regulatory classification where required;
- jurisdiction path;
- source-of-funds evidence appropriate to the regulated context;
- destination account and owner;
- rail/provider;
- approval thresholds;
- settlement confirmation;
- reconciliation result;
- exceptions/corrections;
- evidence receipt.

## On/off-chain rule

Onchain evidence may attest to an event, instruction, state reference, or reconciliation. It does not silently replace the authoritative bank, escrow, transfer-agent, recorder, issuer, or other legally controlling record.
