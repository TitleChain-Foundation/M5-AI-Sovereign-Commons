# Commons public conformance fixtures

This module exercises public contracts with synthetic evidence. It does not
issue credentials, authenticate identity, verify external signatures, deploy
an inference model, execute payment, or implement private M5Canon policy.

Run from the repository root:

```sh
python -m pytest -q
```

Coverage includes migration, independently resolved namespace fixtures,
activation/revocation, contradiction rejection, metered free-public reference
receipts, replay/correction behavior and Tier I baseline controls. Production
evidence resolution and device/runtime conformance remain deployment work.
