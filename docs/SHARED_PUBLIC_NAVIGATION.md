# Shared public navigation — proposed UI framework

This changes public website navigation only. It does not change M5Canon, account names/codes, authorization, certificates, research claims, paper authorship or private data boundaries.

## Framework

Both properties use the same Foundation mark, masthead, Commons / M5Labs switcher, Freedom Office and M5-OpenAPI Marketplace links, keyboard behavior and mobile Menu. A second row belongs to the current site; optional “On this page” links sit below the shared header so they cannot change its height. The Labs menu uses the short label Papers; the homepage research introduction retains its own editorial heading.

Commons retains Pathways, Toolkits, Research & Standards, Funding, Search and Documentation. M5Labs uses Calculators, Projects, Observatory, Simulations, The Inversion, Marketplace, Papers and About, in that order on every page. Papers and About have dedicated index pages; old homepage fragments remain available. The shared Marketplace entry opens the existing Commons marketplace; the Labs reference copy remains available. This is routing consolidation, not a new credential or vendor approval claim.

Research status/source bars remain document context. H1 hero introductions remain content. The masthead is excluded from print; existing paper body, Word/PDF downloads and legal notices remain intact. Generated Commons readers and the generated SEC dashboard also use the shared assets. The standalone SEC monitor remains usable without website assets; the repository publication includes them.

## Sources and checks

- `shared-navigation/navigation.json`: labels, canonical sites, local menus and page-specific links.
- `shared-navigation/navigation.js` / `.css` / `mark.png`: identical mirrored sources in both repositories.
- `scripts/build_shared_navigation.py`: deterministic local bundle and SHA-256 manifest; updates cache fingerprints in existing HTML. No cross-site runtime fetch is required.
- `scripts/check_shared_navigation.cjs`: desktop/mobile header, menus, destinations, keyboard close and print checks across all published HTML.
- `scripts/check_navigation_parity.py`: verifies both deployed manifests and actual asset hashes. A missing manifest or mismatched deployment fails the audit.

Update both mirrored sources together, build and check both repositories, then compare `assets/navigation/manifest.json` byte-for-byte. Existing CI checks the generated files and browser behavior. Do not claim deployed parity until both approved deployments pass:

```
python3 scripts/check_navigation_parity.py https://commons.titlechainfoundation.org/ https://m5labs-8770fb.gitlab.io/
```

The command is intended AFTER the paired rollout; the current sites do not yet publish these manifests. It is a read-only command, not an activated recurring schedule. Commons also includes a manual, read-only `Public navigation parity` workflow for this post-rollout check.

## Rollout and rollback

This paired update starts from Commons main `489cb3f045d5040644bb32c31a09c10761374114` and Labs main `1d532b654dda66000301a10bd7657f3dc466dd45`. It preserves the merged Observatory and monitor work. Prepare one navigation review per repository; preserve existing deployment approval requirements. MR !10 separately contains the privacy corrections and must remain independently reviewable. Deploy both approved navigation updates, then run the parity audit. An interval of mixed navigation versions is not deployed parity.

After approved deployments run the parity command and spot-check search, readers, scientific papers, mobile menus and cross-site links. For rollback, revert only each navigation commit on a review branch and use the established deployment pipeline. Never reset main or remove older branches. GitHub/GitLab repository chrome is platform-controlled and is outside this website framework.

## Published DOI links

The research introduction and four HTML paper pages link to the approved November 2, 2026 version1 Zenodo records:23900983,23901314,23901345 and23901361. The links retain the existing All rights reserved statement. These are citation metadata additions, not new editions of the deposited papers. All15 source/download files remain unchanged from the reviewed base.
