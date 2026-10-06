# Farmer Toolkit — Free and Open Starting Points

**Reviewed:** October 4, 2026  
**Scope:** United States unless a source states otherwise

This toolkit gives farmers, ranchers, cooperatives and local implementers a
practical starting point for weather, soil, imagery, water, markets, mapping,
farm records and livestock research without requiring a proprietary data
subscription.

The companion
[`farmer-data-registry.json`](farmer-data-registry.json) records the same
sources in machine-readable form.

## Before using a source

- **Free access is not the same as permission to redistribute.**
- Preserve the source URL, observation date, retrieval date, units, spatial
  resolution, transformations and quality flags with every imported record.
- Recheck the provider's current terms before redistribution, commercial
  packaging, model training or automated high-volume access.
- Treat forecasts, satellite estimates, classifications and model outputs as
  decision support, not as veterinary, agronomic, legal or safety
  determinations.
- Keep farm-generated operational data in the farmer-controlled environment
  unless the lawful principal authorizes a purpose-limited transfer.

## Evidence states

| State | Meaning |
| --- | --- |
| `VERIFIED_PERMISSIVE` | Official terms or a repository license permit broad reuse. Preserve provenance and any required notices. |
| `VERIFIED_ATTRIBUTION_REQUIRED` | Reuse is permitted when the provider's attribution or license conditions are followed. |
| `REFERENCE_ONLY` | Useful free-access source, but reuse, redistribution or commercial terms must be checked for the intended use. |
| `LICENSE_UNCLEAR` | A public record exists, but this review did not establish sufficient rights for redistribution. |

## Quick start for a farm or ranch

1. Draw the farm boundary in [QGIS](https://qgis.org/) and keep the project
   file locally.
2. Export the relevant soil map and report from
   [Web Soil Survey](https://websoilsurvey.nrcs.usda.gov/).
3. Add current forecasts and alerts from the
   [National Weather Service API](https://www.weather.gov/documentation/services-web-api).
4. Add field context from [NAIP imagery](https://naip-usdaonline.hub.arcgis.com/)
   and crop history from
   [USDA CroplandCROS](https://www.nass.usda.gov/Research_and_Science/Cropland/).
5. Add nearby water observations from
   [USGS Water Data for the Nation](https://api.waterdata.usgs.gov/docs/).
6. Use [farmOS](https://farmos.org/) when a self-hosted farm record system is
   appropriate.
7. Record every source and transformation; do not publish private boundaries,
   animal locations, credentials or farm economics by default.

## Weather and climate

| Source | Access and cost | Best use | Rights state and cautions |
| --- | --- | --- | --- |
| [National Weather Service API](https://www.weather.gov/documentation/services-web-api) | Free REST API; no key; identifying `User-Agent` required | Forecasts, alerts and observations | `VERIFIED_PERMISSIVE`. NWS states the API is open data free for any purpose. Cache responsibly; undisclosed reasonable rate limits apply. |
| [NOAA Climate Data Online](https://www.ncei.noaa.gov/cdo-web/webservices/v2) | Free REST API; free token required | Historical station and climate observations | `VERIFIED_PERMISSIVE`. Five requests per second and 10,000 per day per token. Certified records may use a separate paid process. |
| [NASA POWER](https://power.larc.nasa.gov/docs/services/api/) | Free REST APIs; no key documented for standard access | Solar, meteorological and agroclimatology time series | `REFERENCE_ONLY`. U.S. Government source; cite NASA and verify product-specific terms and quality. HTTP 429 limits apply. |

## Soil and land capability

| Source | Access and cost | Best use | Rights state and cautions |
| --- | --- | --- | --- |
| [NRCS Web Soil Survey](https://websoilsurvey.nrcs.usda.gov/) | Free browser map, reports and downloads | Area-of-interest soil interpretation and planning | `VERIFIED_PERMISSIVE`. Preserve survey date and map-unit metadata; field conditions can differ from mapped interpretations. |
| [NRCS Soil Data Access](https://sdmdataaccess.sc.egov.usda.gov/) | Free query and web-service access; no key | Automated access to SSURGO soil attributes | `VERIFIED_PERMISSIVE`. Technical schema and query knowledge required; avoid unbounded national queries. |

## Satellite, aerial and crop-cover data

| Source | Access and cost | Best use | Rights state and cautions |
| --- | --- | --- | --- |
| [USGS Landsat](https://www.usgs.gov/landsat-missions/landsat-data-access) | Free EarthExplorer, cloud and machine-to-machine access; some services require an account | Long-term vegetation, surface reflectance, water and land-change analysis | `VERIFIED_PERMISSIVE`. Use product-level quality masks, acquisition dates and citations. Cloud, smoke and resolution affect field-scale interpretation. |
| [Copernicus Sentinel Data Space](https://dataspace.copernicus.eu/) | Free registration; browser, download and APIs | Higher-frequency optical and radar observation | `VERIFIED_ATTRIBUTION_REQUIRED`. Sentinel data are free, full and open under the Sentinel legal notice. Non-Sentinel portal content has different, more restrictive terms. |
| [USDA NAIP](https://naip-usdaonline.hub.arcgis.com/) | Free imagery viewer and downloads | High-resolution aerial context, boundaries and visible change | `REFERENCE_ONLY`. Confirm the specific service's metadata and terms before redistribution; vintages and coverage differ by state. |
| [USDA Cropland Data Layer / CroplandCROS](https://www.nass.usda.gov/Research_and_Science/Cropland/) | Free browser, downloads and developer services | Annual crop classification and crop-sequence context | `REFERENCE_ONLY`. Classification is modeled and can be wrong at parcel edges; preserve year, confidence and source terms. |

## Water, drought and evapotranspiration

| Source | Access and cost | Best use | Rights state and cautions |
| --- | --- | --- | --- |
| [USGS Water Data APIs](https://api.waterdata.usgs.gov/docs/) | Free OGC, STAC and water-quality APIs; optional key increases limits | Streamflow, groundwater, water quality and monitoring-site context | `VERIFIED_PERMISSIVE`. Values may be provisional or revised. Prefer current APIs and retain parameter, unit and qualification codes. |
| [U.S. Drought Monitor](https://droughtmonitor.unl.edu/DmData/DataDownload.aspx) | Free weekly maps and data downloads | Regional drought-status context | `REFERENCE_ONLY`. This is a weekly expert synthesis, not a forecast or parcel measurement. Preserve map date, authorship and current attribution policy. |
| [OpenET](https://openetdata.org/) | Free public explorer; account or API conditions may apply | Field-scale evapotranspiration estimates | `REFERENCE_ONLY`. Model estimates have known regional and crop-specific uncertainty. Verify current access, attribution and commercial-use terms before integration. |

## Agricultural statistics and markets

| Source | Access and cost | Best use | Rights state and cautions |
| --- | --- | --- | --- |
| [USDA NASS Quick Stats](https://quickstats.nass.usda.gov/) | Free web queries; API access follows NASS registration and terms | Production, acreage, yield, inventory, prices and Census of Agriculture estimates | `VERIFIED_ATTRIBUTION_REQUIRED`. Applications using the API must display the NASS non-endorsement notice. Do not modify data and still represent it as NASS content. |
| [USDA AMS MyMarketNews](https://mymarketnews.ams.usda.gov/) | Free website, reports and API access | Commodity, livestock and specialty-crop market reports | `REFERENCE_ONLY`. Preserve report identity, market, unit, grade and publication time; verify current API registration and terms. |
| [USDA ERS Data Products and APIs](https://www.ers.usda.gov/developer/data-apis) | Free downloads; supported APIs require a free key | Farm economics, trade, food, rural and ARMS-derived analysis | `REFERENCE_ONLY`. Only selected datasets have APIs. Follow dataset confidentiality, suppression and API terms; aggregates are not individual-farm records. |

## Base maps and elevation

| Source | Access and cost | Best use | Rights state and cautions |
| --- | --- | --- | --- |
| [USGS 3D Elevation Program](https://www.usgs.gov/3d-elevation-program) | Free downloads through The National Map and related services | Terrain, slope, drainage and watershed context | `VERIFIED_PERMISSIVE`. Coverage, collection date and point density vary; elevation does not establish a surveyed legal boundary. |
| [Census TIGER/Line](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html) | Free direct downloads | Roads, administrative areas and geographic reference layers | `VERIFIED_PERMISSIVE`. General mapping data, not cadastral or surveyed property boundaries. |

## Open-source farm and mapping software

| Software | License | Best use | Deployment cautions |
| --- | --- | --- | --- |
| [QGIS](https://qgis.org/) | GPL-2.0 | Desktop mapping, analysis and offline farm projects | `VERIFIED_ATTRIBUTION_REQUIRED`. Vet plugins, back up projects and use supported releases. |
| [farmOS](https://farmos.org/) | GPL-2.0 | Self-hosted farm planning, assets and records | `VERIFIED_ATTRIBUTION_REQUIRED`. Internet-facing deployment requires normal server security, updates and backups. |
| [AgOpenGPS](https://github.com/AgOpenGPS-Official/AgOpenGPS) | Apache-2.0 in the official core repository | DIY guidance, mapping and precision-agriculture experimentation | `VERIFIED_PERMISSIVE`. Steering and electrical integration are safety-critical; inspect component licenses and use qualified installation practices. |
| [OpenDroneMap](https://github.com/OpenDroneMap/ODM) | AGPL-3.0 | Local processing of lawful drone imagery into maps and models | `VERIFIED_ATTRIBUTION_REQUIRED`. Network-service modifications can trigger source-sharing duties. Follow aviation, privacy and property rules. |

## Livestock research and software

The detailed cattle registry remains in
[`SOURCE-RESEARCH.md`](SOURCE-RESEARCH.md) and
[`sovereign-herd/open-data-registry.json`](sovereign-herd/open-data-registry.json).

| Source | Material | Rights state |
| --- | --- | --- |
| [Precision Beef — Animal Behaviour Classification](https://zenodo.org/records/4064802) | Accelerometer data and behavior labels | `LICENSE_UNCLEAR`; do not redistribute until the exact dataset license is verified. |
| [Strathclyde classified bolus dataset](https://pureportal.strath.ac.uk/en/datasets/bolus-sensor-acceleration-data-with-timestamp-and-behavioural-cla/) | Labeled three-axis acceleration | `VERIFIED_ATTRIBUTION_REQUIRED`; source record states CC BY 4.0. |
| [Strathclyde raw bolus 3x dataset](https://pureportal.strath.ac.uk/en/datasets/bolus-acceleration-data-3x/) | Raw bovine bolus acceleration | `VERIFIED_ATTRIBUTION_REQUIRED`; source record states CC BY 4.0. |
| [BovHEAT](https://github.com/bovheat/bovheat) | Estrus and activity-analysis software | `VERIFIED_PERMISSIVE`; MIT software license does not grant rights in input data. |
| [MmCows](https://github.com/neis-lab/mmcows) | Multimodal cattle research, sensors, imagery and weights | `REFERENCE_ONLY`; audit terms separately for code, data, annotations, imagery and weights. |

## Minimum provenance record

For each imported dataset or observation, retain:

```text
source_id
official_url
retrieved_at
observation_or_publication_time
geographic_coverage
units_and_resolution
license_or_terms_snapshot
transformation_history
quality_or_confidence_flags
local_record_owner
```

Do not put API keys, credentials, precise private animal locations, veterinary
notes, private financial records or unpublished farm boundaries into a public
provenance record.
