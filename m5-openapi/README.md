# M5 OpenAPI — Public Reference Surface

**Status: Draft reference surface. No production paid API is deployed by this repository.**

Initial resource model:

```text
GET /v1/assets
GET /v1/assets/{asset_id}
GET /v1/assets/{asset_id}/evidence
GET /v1/assets/{asset_id}/events
GET /v1/assets/{asset_id}/debt
GET /v1/entities/{entity_id}
GET /v1/products
```

Future authorized commercial capabilities may include:

```text
POST /v1/intelligence/evaluate
POST /v1/authority/evaluate
POST /v1/webhooks
```

Core separations:

```text
M3 asset != M4 instrument
metering != pricing
payment != authority
model output != M5Canon
local Laya usage != compulsory paid inference
provider cost != customer price
```

See:

- `docs/M5-TRANSACTION-FOOTPRINT-AND-ECONOMIC-CLASSIFICATION.md`
- `docs/M5-INTELLIGENCE-ROUTER-AND-M5POD-RUNTIME.md`
- `docs/LAYA-LOCAL-SYSTEM-ONE-PROFILE.md`
- `docs/JEV-HOSTED-SYSTEM-ONE-PROFILE.md`
- `docs/M5-OPENAPI-METERING-X402-COMMERCE.md`
- `docs/M5-OPENAPI-EARLY-ACCESS-AND-DEMAND-PILOT.md`
