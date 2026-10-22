// M5 Sovereign Commons — public catalog (preview). One record per project/tool; pathway views are derived.
// Every link points to a maintained source. Fields mirror registry/project.schema.json in the handoff.
(function () {
  const REPO = 'TitleChain-Foundation/M5-AI-Sovereign-Commons';
  const B = 'https://github.com/' + REPO + '/blob/main/';
  const T = 'https://github.com/' + REPO + '/tree/main/';
  const OBS = 'sec-observatory/';
  const VERIFIED = '2026-10-20';

  const STATUS = {
    concept:    { label: 'Concept',    tone: '#83713C', dash: true },
    simulation: { label: 'Simulation', tone: '#83713C', dash: true },
    proposed:   { label: 'Proposed',   tone: '#83713C', dash: true },
    draft:      { label: 'Draft for public review', tone: '#2C9BAA', dash: false },
    research:   { label: 'Public research release', tone: '#2C9BAA', dash: false },
    live:       { label: 'Live public service', tone: '#1F7A4D', dash: false },
    available:  { label: 'Public web tool · available', tone: '#1F7A4D', dash: false },
    candidate:  { label: 'Candidate', tone: '#3C7BFF', dash: false },
    released:   { label: 'Released', tone: '#1F7A4D', dash: false },
    archived:   { label: 'Archived', tone: '#6B7689', dash: true },
  };

  const pathways = [
    { slug: 'ai-science', num: '01', plate: 'Pl. I', title: 'Sovereign AI & Science', img: 'assets/plates2/sci.png', alt: 'É. L. Trouvelot, The Great Nebula in Orion, 1875', caption: 'Luminous I · after É. L. Trouvelot, The Great Nebula in Orion, 1875', tone: '#2C9BAA',
      short: 'Scientific Intelligence Commons connects mathematical inquiry, open research and sovereign compute with accountable human review.',
      intro: 'This pathway gathers the Commons work on AI governance, open models, sovereign compute and new mathematics. M5Labs is its research program, and the M5 Sovereign Intelligent Calculator is its first featured instrument project.',
      families: ['SI', 'SC', 'PL', 'LLM', 'SLM', 'SCI', 'FRN', 'AET'] },
    { slug: 'health-wellness', num: '02', plate: 'Pl. II', title: 'Health, Wellness & Sports', img: 'assets/plates2/health-d.png', alt: 'E. Muybridge, Animal Locomotion, 1887', caption: 'after E. Muybridge, Animal Locomotion, 1887', tone: '#A18B3C',
      short: 'A home for 23andMine cooperatives, genetic sovereignty, personal health records, sports and fitness, and responsible research that respects families, privacy and informed consent.',
      intro: 'Health records, genetic data and fitness information belong to the person they describe. Projects here are being indexed; calculators in the LIFE and PL families define how private health tools should work.',
      families: ['LIFE', 'PL', 'SLM'] },
    { slug: 'business-enterprise', num: '03', plate: 'Pl. III', title: 'Business & Enterprise', img: 'assets/plates2/biz.png', alt: 'G. Becanus, Triumphal ship before Ghent, 1636 · The Met', caption: 'after G. Becanus, Triumphal ship before Ghent, 1636 · The Met', tone: '#2C9BAA',
      short: 'A connected journey from a woman’s first sale and first company to professional services, manufacturing, procurement, capital formation and public markets.',
      intro: 'From a first sale to a registered company. iWBE and iSWE are the proposed activation programs, and two public web tools are available to use today.',
      families: ['FIN', 'LEX', 'TRU', 'BOM'] },
    { slug: 'creator-economy', num: '04', plate: 'Pl. IV', title: 'Creator Economy', img: 'assets/plates2/creator.png', alt: 'Diderot & d’Alembert, Encyclopédie, corsetry plate', caption: 'after Diderot & d’Alembert, Encyclopédie, corsetry plate', tone: '#B83CFF',
      short: 'For artists, makers, stylists and storytellers. Dagny Closet and fellow creators show how work, style and intellectual property stay credited to the person who made them.',
      intro: 'Work, style and intellectual property stay credited to the person who made them. The Dagny Bank of Me simulation shows a single storefront purchase across four kinds of value.',
      families: ['BOM', 'LEX', 'TRU'] },
    { slug: 'agriculture-land', num: '05', plate: 'Pl. V', title: 'Agriculture, Land & Real Estate', img: 'assets/plates2/agri.png', alt: 'Köhler’s Medizinal-Pflanzen, Triticum aestivum, 1887', caption: 'after Köhler’s Medizinal-Pflanzen, Triticum aestivum, 1887', tone: '#A18B3C',
      short: 'From farms, ranches and open space to homes, commercial property and public-purpose redevelopment, with verifiable title and responsible stewardship.',
      intro: 'Farms, ranches, land stewardship and public-purpose real estate. Each project tests the same eight controls: who holds the right, who may act, and what happens when something goes wrong.',
      subtopics: [{ id: 'agriculture', label: 'Agriculture' }, { id: 'real-estate', label: 'Real Estate' }, { id: 'land', label: 'Land' }],
      families: ['WV', 'SCI', 'LEX', 'FIN'] },
    { slug: 'energy-resources', num: '06', plate: 'Pl. VI', title: 'Energy & Natural Resources', img: 'assets/plates2/energy.png', alt: 'J. Sowerby, Cinnabar from Almadén, 1811', caption: 'after J. Sowerby, Cinnabar from Almadén, 1811', tone: '#A18B3C',
      short: 'From mineral deposits and forests to power generation and natural capital. Explore the M5 Global Index & Exchange families MINERA, NATURA and TERRAVERTE.',
      intro: 'Minerals, forests, water and power, recorded with provenance and stewardship. Projects here are being indexed.',
      families: ['SCI', 'WV', 'ECON'] },
    { slug: 'finance-markets', num: '07', plate: 'Pl. VII', title: 'Finance & Public Markets', img: 'assets/plates2/fin.png', alt: 'The Inside View of the Royal Exchange · Yale Center for British Art', caption: 'The Inside View of the Royal Exchange · Yale Center for British Art', tone: '#2C9BAA',
      short: 'From member finance and M5Pay to CEDECO, SWIFTBRIDGE, TradFi–DeFi interoperability, public markets, the SEC Observatory and M5 Global Index & Exchange.',
      intro: 'Public research on ownership, transfer and custody. The SEC Public Comment Observatory checks the official docket every hour, and SHADOW M5Index publishes public-data research on assets, debt and ownership.',
      families: ['FIN', 'ECON', 'BOM', 'TRU'] },
    { slug: 'government-institutions', num: '08', plate: 'Pl. VIII', title: 'Government & Institutions', img: 'assets/plates2/gov-b.png', alt: 'U.S. Capitol, East Front Elevation · Library of Congress', caption: 'U.S. Capitol, East Front Elevation · Library of Congress', tone: '#2C9BAA',
      short: 'Practical, open approaches to governance, institutional records, public stewardship and accountable digital systems.',
      intro: 'Institutional records, jurisdiction profiles and public stewardship. Global UN Commons is an independent concept and is not affiliated with or endorsed by the United Nations.',
      families: ['LEX', 'LLM', 'WV'] },
    { slug: 'spiritual-education-growth', num: '09', plate: 'Pl. IX', title: 'Spiritual Life, Education & Growth', img: 'assets/plates2/spirit.png', alt: 'Anna Atkins, Ferns, cyanotype, 1840s · National Gallery of Art', caption: 'Anna Atkins, Ferns, cyanotype, 1840s · National Gallery of Art', tone: '#2C9BAA',
      short: 'Learning pathways, mentorship, faith and community traditions, and lifelong personal growth, pursued on each person’s own terms.',
      intro: 'Learning, mentorship and personal growth on each person’s own terms. Projects here are being indexed.',
      families: ['BASE', 'LIFE', 'PL'] },
  ];

  const ART = {"ai-science":{"art":"radial-gradient(circle at 50% 34%, #FFFFFF 0 1.4%, rgba(62,231,247,.95) 3%, rgba(62,231,247,.45) 13.5%, rgba(62,231,247,0) 30%), radial-gradient(130% 55% at 50% 118%, #050A14 0 48%, rgba(5,10,20,0) 49%), repeating-radial-gradient(circle at 50% 34%, rgba(232,241,244,.09) 0 1px, rgba(232,241,244,0) 1.5px 26px), linear-gradient(180deg, #050A14 0%, #1B3C7A 100%)","study":"Luminous I · Study of a mind at dawn, after Agnes Pelton"},"health-wellness":{"art":"radial-gradient(circle at 50% 74%, #FFFFFF 0 1.4%, rgba(216,196,126,.95) 3%, rgba(216,196,126,.45) 15.3%, rgba(216,196,126,0) 34%), radial-gradient(130% 55% at 50% 118%, #0B1530 0 48%, rgba(5,10,20,0) 49%), linear-gradient(180deg, #16245A 0%, #C9A6B8 100%)","study":"Luminous II · Study of rising vitality, after Agnes Pelton"},"business-enterprise":{"art":"radial-gradient(circle at 32% 46%, #FFFFFF 0 1.4%, rgba(44,155,170,.95) 3%, rgba(44,155,170,.45) 12.6%, rgba(44,155,170,0) 28%), radial-gradient(130% 55% at 50% 118%, #07131C 0 48%, rgba(5,10,20,0) 49%), repeating-radial-gradient(circle at 32% 46%, rgba(232,241,244,.09) 0 1px, rgba(232,241,244,0) 1.5px 26px), linear-gradient(180deg, #050A14 0%, #1E5C66 100%)","study":"Luminous III · Study of first enterprise, after Agnes Pelton"},"creator-economy":{"art":"radial-gradient(circle at 64% 40%, #FFFFFF 0 1.4%, rgba(184,60,255,.95) 3%, rgba(184,60,255,.45) 13.5%, rgba(184,60,255,0) 30%), radial-gradient(130% 55% at 50% 118%, #0A0820 0 48%, rgba(5,10,20,0) 49%), linear-gradient(180deg, #0A0820 0%, #5B2A8C 100%)","study":"Luminous IV · Study of the maker’s flame, after Agnes Pelton"},"agriculture-land":{"art":"radial-gradient(circle at 50% 70%, #FFFFFF 0 1.4%, rgba(216,196,126,.95) 3%, rgba(216,196,126,.45) 13.5%, rgba(216,196,126,0) 30%), radial-gradient(130% 55% at 50% 118%, #0E2A33 0 48%, rgba(5,10,20,0) 49%), linear-gradient(180deg, #2C9BAA 0%, #E8F1F4 100%)","study":"Luminous V · Study of field and furrow, after Agnes Pelton"},"energy-resources":{"art":"radial-gradient(circle at 50% 52%, #FFFFFF 0 1.4%, rgba(255,214,140,.95) 3%, rgba(255,214,140,.45) 18%, rgba(255,214,140,0) 40%), radial-gradient(130% 55% at 50% 118%, #050A14 0 48%, rgba(5,10,20,0) 49%), repeating-radial-gradient(circle at 50% 52%, rgba(232,241,244,.09) 0 1px, rgba(232,241,244,0) 1.5px 26px), linear-gradient(180deg, #050A14 0%, #6B5A2C 100%)","study":"Luminous VI · Study of stored light, after Agnes Pelton"},"finance-markets":{"art":"radial-gradient(circle at 50% 46%, #FFFFFF 0 1.4%, rgba(62,231,247,.95) 3%, rgba(62,231,247,.45) 8.1%, rgba(62,231,247,0) 18%), radial-gradient(130% 55% at 50% 118%, #050A14 0 48%, rgba(5,10,20,0) 49%), repeating-radial-gradient(circle at 50% 46%, rgba(232,241,244,.09) 0 1px, rgba(232,241,244,0) 1.5px 26px), linear-gradient(180deg, #050A14 0%, #2A57B8 100%)","study":"Luminous VII · Study of exchange in balance, after Agnes Pelton"},"government-institutions":{"art":"radial-gradient(circle at 50% 26%, #FFFFFF 0 1.4%, rgba(232,241,244,.95) 3%, rgba(232,241,244,.45) 11.700000000000001%, rgba(232,241,244,0) 26%), linear-gradient(90deg, rgba(232,241,244,0) 49.4%, rgba(232,241,244,.55) 50%, rgba(232,241,244,0) 50.6%), radial-gradient(130% 55% at 50% 118%, #050A14 0 48%, rgba(5,10,20,0) 49%), linear-gradient(180deg, #0D1A3A 0%, #3C7BFF 100%)","study":"Luminous VIII · Study of the common house, after Agnes Pelton"},"spiritual-education-growth":{"art":"radial-gradient(circle at 50% 44%, #FFFFFF 0 1.4%, rgba(255,255,255,.95) 3%, rgba(255,255,255,.45) 19.8%, rgba(255,255,255,0) 44%), radial-gradient(130% 55% at 50% 118%, #050A14 0 48%, rgba(5,10,20,0) 49%), repeating-radial-gradient(circle at 50% 44%, rgba(232,241,244,.09) 0 1px, rgba(232,241,244,0) 1.5px 26px), linear-gradient(180deg, #2A1650 0%, #0B1130 100%)","study":"Luminous IX · Study of inner growth, after Agnes Pelton"}};
  const CAP = {"ai-science":"Luminous I · Study of a mind at dawn, after Agnes Pelton · from É. L. Trouvelot, The Great Nebula in Orion, 1875","health-wellness":"Luminous II · Study of rising vitality, after Agnes Pelton · from E. Muybridge, Animal Locomotion, 1887","business-enterprise":"Luminous III · Study of first enterprise, after Agnes Pelton · from G. Becanus, Triumphal ship before Ghent, 1636 · The Met","creator-economy":"Luminous IV · Study of the maker’s flame, after Agnes Pelton · from Diderot & d’Alembert, Encyclopédie, corsetry plate","agriculture-land":"Luminous V · Study of field and furrow, after Agnes Pelton · from Köhler’s Medizinal-Pflanzen, Triticum aestivum, 1887","energy-resources":"Luminous VI · Study of stored light, after Agnes Pelton · from J. Sowerby, Cinnabar from Almadén, 1811","finance-markets":"Luminous VII · Study of exchange in balance, after Agnes Pelton · from The Inside View of the Royal Exchange · Yale Center for British Art","government-institutions":"Luminous VIII · Study of the common house, after Agnes Pelton · from U.S. Capitol, East Front Elevation · Library of Congress","spiritual-education-growth":"Luminous IX · Study of inner growth, after Agnes Pelton · from Anna Atkins, Ferns, cyanotype, 1840s · National Gallery of Art"};
  pathways.forEach(p => { if (ART[p.slug]) p.art = ART[p.slug].art; if (CAP[p.slug]) p.caption = CAP[p.slug]; });

  const families = [
    ['SI', 'Sovereign Intelligence', '#C8264B', 'All the agents running your system, on your own compute, acting only within the authority you delegate.', 'Intelligence'],
    ['SC', 'Sovereign Compute', '#A18B3C', 'Computing power you own or authorize, operating within your permissions and/or federated environment.', 'Intelligence'],
    ['PL', 'Private Language', '#E0457B', 'A sovereign human’s own personal model: memory, health, conscious and subconscious. Private by default, shared only by choice.', 'Intelligence'],
    ['LLM', 'Large language', '#3C7BFF', 'Reasoning calculators for contracts, policy and law across large bodies of text.', 'Intelligence'],
    ['SLM', 'Small language', '#2C9BAA', 'Local models on the handset and M5POD. Private by default, usable offline.', 'Intelligence'],
    ['BOM', 'BankofMe', '#83713C', 'Personal finance calculator agents that work for one person, on their own records.', 'Money & markets'],
    ['FIN', 'Financial', '#A18B3C', 'Time value, credit, treasury and digital asset valuation for entities.', 'Money & markets'],
    ['ECON', 'M5Economics', '#83713C', 'Live economic measures computed from the M5 economy and published to the public index.', 'Money & markets'],
    ['LEX', 'Legal entity', '#3C7BFF', 'Formation, governance and the running cost of compliance.', 'Law & life'],
    ['TRU', 'Insurance & trust', '#2C9BAA', 'Cover, liability, trusts and estates, from a household to a business.', 'Law & life'],
    ['LIFE', 'Health, wellness & spirit', '#C8264B', 'Private calculators for body, mind and practice. Records stay with the person.', 'Law & life'],
    ['SCI', 'Scientific', '#2C9BAA', 'Engineering, actuarial and research math with published methods.', 'Science, space & frontier'],
    ['WV', 'WorldView', '#B83CFF', 'Graphing for place: jurisdictions, supply chains, land and climate on one map.', 'Science, space & frontier'],
    ['SPA', 'Spatial', '#3C7BFF', '3D and orbital calculators for digital twins, sensors and space.', 'Science, space & frontier'],
    ['FRN', 'Frontier', '#B83CFF', 'Calculators built from new published mathematics.', 'Science, space & frontier'],
    ['AET', 'Aether', '#1E348C', 'Compute in plasma and fields the eye cannot see. Held until a human understands it.', 'Beyond the frontier'],
    ['BASE', 'Foundations', '#0D1321', 'Four-function, unit and learning calculators for every citizen and classroom.', 'Foundations'],
  ].map(([code, name, tone, desc, group]) => ({ code, name, tone, desc, group }));

  const doc = (title, path, state, kind) => ({ title, url: path.startsWith('http') ? path : B + path, path, state: state || '', kind: kind || 'Document' });

  const projects = [
    { slug: 'spring-commons', title: '312 Spring Commons', place: 'California', kicker: 'GSA / CRE · PPT-EZ-CA-0001', primary_pathway: 'agriculture-land', subtopic: 'real-estate', pathways: ['agriculture-land', 'government-institutions', 'finance-markets'], publication_status: 'simulation',
      img: 'https://raw.githubusercontent.com/TitleChain-Foundation/M5-AI-Sovereign-Commons/main/pilots/312-spring-commons/documents/images/312-spring-commons-concept-plaza.jpg', imgAlt: '312 Spring Commons concept plaza', imgCredit: 'Concept image · 312 Spring Commons project library',
      description: 'Government-to-public civic real estate, historic surplus pathways, CRE rehabilitation, capital provenance and public-benefit operations.',
      notice: 'Conditional go / diligence. No transaction or operational launch. The Public Bank of California concept is not a chartered bank, state agency or approved financing source.',
      overview: ['The process tests jurisdiction, title, public-owner eligibility, preservation and use restrictions, source-of-funds provenance, escrow and draw controls, transfer-agent recordkeeping boundaries and fail-closed approval gates.', 'Physical conveyance and regulated securities recordkeeping remain distinct.'],
      source: 'pilots/312-spring-commons/README.md', controlIndex: 'pilots/312-spring-commons/PROJECT-CONTROL-INDEX.md',
      research: [doc('Initiative fit-gap review', 'pilots/312-spring-commons/INITIATIVE-FIT-GAP-REVIEW.md', 'Draft', 'Review'), doc('GSA pathway and application readiness', 'pilots/312-spring-commons/update-notes/GSA-PATHWAY-AND-APPLICATION-READINESS.md', 'Draft', 'Diligence'), doc('“The Bear Comes Home” · Public Bank of California concept', 'pilots/312-spring-commons/briefs/PPT-EZ-CA-0001-THE-BEAR-COMES-HOME-PUBLIC-BANK-OF-CALIFORNIA-CONCEPT-v0.1.md', 'Concept', 'Brief')],
      documents: [doc('Project Control Index', 'pilots/312-spring-commons/PROJECT-CONTROL-INDEX.md', 'Draft', 'Control index'), doc('DOC-17 Authority, Jurisdiction and Source-of-Truth Matrix', 'pilots/312-spring-commons/documents/public/DOC-17-M5Canon-Authority-Jurisdiction-and-Source-of-Truth-Matrix.pdf', 'Draft', 'PDF'), doc('DOC-18 CER, UCC Article 12 and Article 9 Rights Schedule', 'pilots/312-spring-commons/documents/public/DOC-18-TitleChain-CER-UCC12-and-Article9-Rights-Schedule.pdf', 'Draft', 'PDF'), doc('DOC-06 Capital Escrow and Draw Agreement', 'pilots/312-spring-commons/documents/public/DOC-06-Capital-Escrow-and-Draw-Agreement.pdf', 'Draft', 'PDF'), doc('DOC-15 Master Risk Factors and Disclosure Schedule', 'pilots/312-spring-commons/documents/public/DOC-15-Master-Risk-Factors-and-Disclosure-Schedule.pdf', 'Draft', 'PDF'), doc('DOC-23 Source of Funds, Entity Provenance and Jurisdiction Chain', 'pilots/312-spring-commons/documents/public/DOC-23-Source-of-Funds-Entity-Provenance-Jurisdiction-Chain-and-Public-Transaction-Graph-Standard.md', 'Draft', 'Standard')],
      funding: { status: 'proposed', label: 'Launch funding sought · review the brief', route: doc('SPRING — Initial Capital Tranche Brief', 'pilots/312-spring-commons/documents/summaries/SPRING-INITIAL-CAPITAL-TRANCHE-BRIEF.md', 'Proposed', 'Brief'), note: 'Donations and other support never create ownership, investment, voting or profit rights. No live offering exists.' },
      results: [doc('First-tranche simulation', 'pilots/312-spring-commons/simulations/first-tranche/README.md', 'Simulation', 'Simulation'), doc('Stakeholder checkpoint matrix', 'pilots/312-spring-commons/simulations/first-tranche/STAKEHOLDER-CHECKPOINT-MATRIX.md', 'Simulation', 'Matrix'), doc('Spring Commons document tests', 'tests/test_spring_commons_docs.py', 'Test', 'Test')],
      resultNote: 'All eight controls are answered in the public placeholder-template library and await counsel, regulatory and transaction review. No control is VERIFIED.',
      tools: [], participate: ['Public reviewer: free, grants no rights', 'Builder or professional: licence and credential verification', 'Donor, grant or PRI provider: support only', 'Lender or investor: instrument-specific eligibility; no live offering'] },

    { slug: 'norton-ranch', title: 'Norton Ranch Blueprint · Sovereign Herd for Ranchers', place: 'v1.4 · Founder Archive', kicker: 'FARMLAND / REDEVELOPMENT · M5 Sovereign Agriculture', primary_pathway: 'agriculture-land', subtopic: 'agriculture', pathways: ['agriculture-land', 'energy-resources', 'ai-science'], publication_status: 'draft',
      img: 'assets/repo-farmland.jpg', imgAlt: 'Crop rows, river bend and open farmland', imgCredit: 'Farmland · M5 Commons repository',
      description: 'Farmer-controlled agricultural data, a free and public data starting toolkit, biological stewardship records and the local-first Sovereign Herd reference implementation.',
      notice: 'Draft public-review blueprint with synthetic examples only. No live farm, veterinary diagnosis or provider certification. The download is an unregistered commons starter, not a licensed M5POD.',
      overview: ['Farmers, ranchers, growers and agricultural builders can download one verified package and run it on their own computer with no network connection: documents, schemas, examples, data registries and the local-only Sovereign Herd utility.', 'Core rule: the animal is not the subscription.'],
      source: 'pilots/norton-ranch-blueprint/README.md', controlIndex: null,
      research: [doc('Source research', 'pilots/norton-ranch-blueprint/SOURCE-RESEARCH.md', 'Draft', 'Research'), doc('Halter case study and the farmer-owned alternative', 'pilots/norton-ranch-blueprint/sovereign-herd/CASE-STUDY-HALTER-AND-THE-FARMER-OWNED-ALTERNATIVE.md', 'Draft', 'Case study'), doc('Why this Commons exists', 'pilots/norton-ranch-blueprint/WHY-THIS-COMMONS-EXISTS.md', '', 'Dedication')],
      documents: [doc('Norton Ranch Blueprint README', 'pilots/norton-ranch-blueprint/README.md', 'Draft', 'Overview'), doc('Business model', 'pilots/norton-ranch-blueprint/BUSINESS-MODEL.md', 'Draft', 'Model'), doc('Public purpose: American Producer Innovation Commons', 'pilots/norton-ranch-blueprint/PUBLIC-PURPOSE-AMERICAN-PRODUCER-INNOVATION-COMMONS.md', '', 'Purpose'), doc('M5 Stewardship Covenant', 'pilots/norton-ranch-blueprint/M5-STEWARDSHIP-COVENANT.md', 'Draft', 'Covenant'), doc('Biological stewardship record schema', 'schemas/m5-biological-stewardship-record.schema.json', 'Draft', 'Schema')],
      funding: { status: 'none', label: 'Contact the Foundation to join the funding team', note: 'The proposed M5 implementation price is $840/year per farm or ranch entity and $0 per cow per month in required software rent. This is a proposed price, not a funding award.' },
      results: [doc('Norton package build test', 'tests/test_norton_package.py', 'Test', 'Test'), doc('Package manifest', 'pilots/norton-ranch-blueprint/m5pod-package.manifest.json', 'Draft', 'Manifest')],
      resultNote: 'Passing tests demonstrate only the cases they exercise.',
      tools: ['farmer-toolkit', 'sovereign-herd', 'norton-m5pod-starter'], participate: ['Download and run the starter package locally', 'Correct or add a data source in the Grower/Caretaker Sustainable Planet Toolkit registry', 'Review the business model as a farmer, OEM, installer or service provider'] },

    { slug: 'peoples-trust', title: 'America’s People’s Trust Farmland', place: 'AG-PILOT-001 / ND-FARM-SIM-001', kicker: 'FARMLAND / REDEVELOPMENT', primary_pathway: 'agriculture-land', subtopic: 'agriculture', pathways: ['agriculture-land', 'government-institutions'], publication_status: 'simulation',
      img: 'https://raw.githubusercontent.com/TitleChain-Foundation/M5-AI-Sovereign-Commons/main/pilots/peoples-trust/visuals/00-project-wish-list.png', imgAlt: 'America’s People’s Trust Farmland project vision', imgCredit: 'Project vision · People’s Trust pilot library',
      description: 'Stewardship, local operations, food and land productivity, title separation, cooperative participation and repeatable national conformance tests.',
      notice: 'Pilot 001, sample-data simulation. It identifies no nonpublic property, owner, trustee, operator, county, parcel or transaction. The 275,000-acre figure is a research-pipeline target, not owned, controlled or offered acreage.',
      overview: ['The process tests entity and signer authority, local operator scope, stewardship evidence, title and economic-right separation, eligibility, correction, successor transfer and public review before any consequential action.'],
      source: 'pilots/peoples-trust/README.md', controlIndex: 'pilots/peoples-trust/PROJECT-CONTROL-INDEX.md',
      research: [doc('People’s Trust Public Conformance Pilot', 'docs/PEOPLES-TRUST-PUBLIC-PILOT.md', 'Draft', 'Pilot'), doc('Biological Stewardship Registry', 'pilots/peoples-trust/BIOLOGICAL-STEWARDSHIP-REGISTRY.md', 'Draft', 'Registry')],
      documents: [doc('Project Control Index', 'pilots/peoples-trust/PROJECT-CONTROL-INDEX.md', 'Draft', 'Control index'), doc('Activation Bridge', 'pilots/peoples-trust/ACTIVATION-BRIDGE.md', 'Draft', 'Bridge'), doc('Financial classification and escrow update', 'pilots/peoples-trust/FARMLAND-FINANCIAL-CLASSIFICATION-AND-ESCROW-UPDATE.md', 'Draft', 'Update'), doc('ND-FARM-SIM-001 simulation', 'pilots/peoples-trust/simulations/nd-farmland-reference/README.md', 'Simulation', 'Simulation')],
      funding: { status: 'proposed', label: 'Launch funding sought · review the brief', route: doc('Capital & Operating Partner Brief', 'pilots/peoples-trust/CAPITAL-AND-OPERATING-PARTNER-BRIEF.md', 'Proposed', 'Brief'), note: 'Support never creates ownership, investment, voting or profit rights.' },
      results: [doc('Farmland reference simulation test', 'tests/test_farmland_reference_simulation.py', 'Test', 'Test')], resultNote: 'No control is VERIFIED.',
      tools: ['farmer-toolkit'], participate: ['Public supporter or reviewer: free', 'Local farm operator: operator agreement and scoped authority', 'Donor or grantor: support only'] },

    { slug: 'global-un-commons', title: 'Global UN Commons', place: 'UN-NY-0001', kicker: 'GLOBAL DEVELOPMENT PROJECT', primary_pathway: 'government-institutions', subtopic: null, pathways: ['government-institutions', 'agriculture-land', 'spiritual-education-growth'], publication_status: 'concept',
      img: 'https://raw.githubusercontent.com/TitleChain-Foundation/M5-AI-Sovereign-Commons/main/pilots/global-un-commons/visuals/v1-un-commons-18-acre-masterplan.png', imgAlt: 'Global UN Commons V1 concept masterplan', imgCredit: 'Global UN Commons — concept and design by TitleChain Foundation (2026)',
      description: 'International interoperability, 193 Member-State jurisdiction profile slots, peaceful public-record coordination and human-authorized cross-border evidence.',
      notice: 'Independent public research and concept art only. Not affiliated with, endorsed by, commissioned by or authorized by the United Nations or any Member State. A profile slot is not an activated nation chain.',
      overview: ['The simulation explores how the approximately 18-acre UN Headquarters campus in New York could serve as a public demonstration of human-authorized digital records, open standards and interoperable jurisdiction profiles, while preserving its diplomatic function and special legal status.'],
      source: 'pilots/global-un-commons/README.md', controlIndex: 'pilots/global-un-commons/PROJECT-CONTROL-INDEX.md',
      research: [doc('Public review questions', 'pilots/global-un-commons/README.md#public-review-questions', '', 'Questions'), doc('Visual library and reuse notice', 'pilots/global-un-commons/visuals/README.md', '', 'Visuals')],
      documents: [doc('Project Control Index', 'pilots/global-un-commons/PROJECT-CONTROL-INDEX.md', 'Draft', 'Control index'), doc('Global UN Commons README', 'pilots/global-un-commons/README.md', 'Concept', 'Overview')],
      funding: { status: 'proposed', label: 'Launch funding sought · review the brief', route: doc('Founding Institutional Underwriter Brief', 'pilots/global-un-commons/FOUNDING-INSTITUTIONAL-UNDERWRITER-BRIEF.md', 'Proposed', 'Brief'), note: 'No UN or Member State endorsement is implied.' },
      results: [], resultNote: 'Authority effect of this simulation: NONE. Development authority, UN authorization and host-country approvals are not established.',
      tools: [], participate: ['Institutional reviewer: start with the underwriter brief', 'Public reviewer: answer the six public review questions'] },

    { slug: 'sec-observatory', title: 'SEC Public Input & Observatory', place: 'S7-2026-30 · S7-2026-35', kicker: 'PUBLIC RESEARCH · Cross-cutting review layer', primary_pathway: 'finance-markets', subtopic: null, pathways: ['finance-markets', 'government-institutions'], publication_status: 'live',
      img: 'https://raw.githubusercontent.com/TitleChain-Foundation/M5-AI-Sovereign-Commons/main/sec-public-input/visuals/public-input-cycle.svg', imgAlt: 'SEC public input review cycle', imgCredit: 'SEC public input review cycle · sec-public-input/visuals',
      description: 'Public-comment research on transfer agent and custody rules, with an automated observatory that checks the official SEC docket every hour.',
      notice: 'Public-comment research. Not an SEC publication, position, endorsement, rule status or legal advice. The official SEC docket controls.',
      overview: ['The observatory records exact docket metadata, the official source URL, retrieval time, media type and SHA-256 digest for each listed filing. Automated topic signals are labeled not human reviewed.'],
      source: 'sec-public-input/README.md', controlIndex: null, observatory: true,
      research: [doc('What the comments say: themes, gaps and Commons matrices', 'sec-public-input/COMMENT-THEMES-AND-COMMONS-MATRICES.md', 'Human reviewed', 'Analysis'), doc('Pilot and SEC RFI crosswalk', 'docs/PILOT-SEC-RFI-CROSSWALK.md', '', 'Crosswalk')],
      documents: [doc('Regulatory record and source verification', 'sec-public-input/REGULATORY-RECORD.md', '', 'Record'), doc('October 3 content and source handoff', 'sec-public-input/SEC_UPDATE_2026-10-03.md', '', 'Update'), doc('Supplemental Comment and Exhibits A–J', 'sec-public-input/foundation-submissions/2026-09-23-supplemental-comment/README.md', 'Pending SEC posting', 'Filing'), doc('Observatory README', 'sec-public-input/observatory/README.md', '', 'Method')],
      funding: { status: 'none', label: 'Contact the Foundation to join the funding team', note: '' },
      results: [doc('Live SEC Public Comment Observatory', OBS, 'Live', 'Dashboard'), doc('Observatory feed.json', OBS + 'feed.json', 'Live', 'Data')], resultNote: 'Filing frequency is not a vote or consensus signal.',
      tools: ['sec-observatory'], participate: ['Use the SEC’s official channel for a comment intended for the Commission', 'Discuss independent Foundation review on GitHub'] },

    { slug: 'shadow-m5index', title: 'SHADOW M5Index', place: 'Q3 2026 first edition', kicker: 'PUBLIC RESEARCH · Systemic Holdings, Assets, Debt & Ownership Watch', primary_pathway: 'finance-markets', subtopic: null, pathways: ['finance-markets', 'agriculture-land'], publication_status: 'research',
      img: 'https://raw.githubusercontent.com/TitleChain-Foundation/M5-AI-Sovereign-Commons/main/shadow-m5index/reports/shadow-camel-report-q3-2026-cover.png', imgAlt: 'SHADOW CAMEL Report Q3 2026 cover', imgCredit: 'TitleChain Foundation research concept and design (2026)',
      description: 'Public research connecting real-world asset state, title provenance, ownership, capital, debt, rights, obligations and public-benefit feasibility.',
      notice: 'First-edition research release with a preliminary, non-canonical score. Not a title report, official CAMELS rating, live ingestion service or authority grant. A nomination creates no right.',
      overview: ['The 23-page first edition publishes a preliminary 1.8 / 5 — Band 2 (Stable / Watch) public-data reading with confidence B and methodology v0.1.', 'The public does not directly edit the canonical record. The public contributes evidence to the record.'],
      source: 'shadow-m5index/README.md', controlIndex: null,
      research: [doc('SHADOW CAMEL Report Q3 2026', 'shadow-m5index/reports/SHADOW-CAMEL-REPORT-Q3-2026.md', 'Research release', 'Report'), doc('Public ingestion and QR architecture', 'docs/SHADOW-M5INDEX-PUBLIC-INGESTION-AND-QR.md', 'Proposed', 'Architecture'), doc('Engineering epic', 'docs/SHADOW-M5INDEX-ENGINEERING-EPIC.md', 'Proposed', 'Roadmap')],
      documents: [doc('Report PDF', 'shadow-m5index/reports/M5Index_SHADOW_CAMEL_Report_Q3_2026.pdf', 'Research release', 'PDF'), doc('Report, editable Word', 'shadow-m5index/reports/M5Index_SHADOW_CAMEL_Report_Q3_2026.docx', 'Research release', 'DOCX'), doc('Debt-state integrity', 'docs/SHADOW-M5INDEX-DEBT-STATE-INTEGRITY.md', 'Draft', 'Method')],
      funding: { status: 'none', label: 'Contact the Foundation to join the funding team', note: '' },
      results: [doc('SHADOW M5Index tests', 'tests/test_shadow_m5index.py', 'Test', 'Test')], resultNote: 'Submissions enter review as SUBMITTED and cannot overwrite canonical records.',
      tools: ['shadow-dataset'], participate: ['Nominate a public asset', 'Add registry or public-record evidence', 'Challenge or correct an index record'] },

    { slug: 'dagny-bank-of-me', title: 'Dagny Bank of Me · M5-VX simulation', place: 'Synthetic · write-disabled', kicker: 'CREATOR ECONOMY · Storefront use case', primary_pathway: 'creator-economy', subtopic: null, pathways: ['creator-economy', 'finance-markets', 'business-enterprise'], publication_status: 'simulation',
      img: null, description: 'How one storefront purchase can be represented across four settlement modalities: DIGITAL, CASH, ASSET and SERVICE.',
      notice: 'Synthetic and write-disabled. It does not move money, cash, property, services, credentials or authority, and calls no provider, wallet, M5POD or TitleChain service.',
      overview: ['The fixture models a synthetic USD 100 purchase: USD 40 DIGITAL, USD 20 CASH, USD 25 ASSET and USD 15 SERVICE. Every screen and receipt displays SIMULATION — NO VALUE MOVED.'],
      source: 'pilots/dagny-bank-of-me/README.md', controlIndex: null,
      research: [], documents: [doc('Dagny Bank of Me README', 'pilots/dagny-bank-of-me/README.md', 'Simulation', 'Overview')],
      funding: { status: 'none', label: 'Contact the Foundation to join the funding team', note: '' },
      results: [doc('Dagny M5-VX simulation test', 'tests/test_dagny_m5_vx_simulation.py', 'Test', 'Test')], resultNote: '',
      tools: ['dagny-m5-vx'], participate: ['Run the simulation locally and verify the receipt bundle'] },

    { slug: 'm5labs-calculators', title: 'M5 Sovereign Intelligent Calculator', place: 'M5Labs · first featured instrument project', kicker: 'M5LABS · Scientific instruments', primary_pathway: 'ai-science', subtopic: null, pathways: ['ai-science', 'business-enterprise', 'energy-resources', 'spiritual-education-growth'], publication_status: 'proposed', labs: true,
      img: 'assets/sovereign/calc-plate-k.png', imgAlt: 'Octagonal string drawing with a small reversed starfish at its center', imgCredit: 'M5 Intelligent Calculators plate · TitleChain Foundation',
      description: 'An open calculator standard with seventeen families, from Sovereign Intelligence to Foundations, developed through scientific review into M5 Toolkits.',
      notice: 'Featured M5Labs development project. Not a confirmed production calculator. M5-CALC-001, 002 and 003 are proposed and have not completed review or certification.',
      overview: ['Mathematical and scientific research enters M5Labs. Qualified referees review applicable methods. Engineers build instruments, and validated reference implementations are published with version-specific evidence. Individual calculators then become M5 Toolkits.'],
      source: null, controlIndex: null, designRef: 'labs.html', designRefLabel: 'Calculator families design',
      research: [doc('openai/math · identified external research source', 'https://github.com/openai/math', 'External', 'Repository')],
      documents: [], funding: { status: 'proposed', label: 'Proposed · no budget published', note: 'Igor Rivin’s participation as a referee is proposed and not confirmed.' },
      results: [], resultNote: 'No calculator has completed review.', tools: ['m5-calc-001', 'm5-calc-002', 'm5-calc-003'], participate: ['Propose a method for review', 'Build to the open calculator standard', 'Referee a family (proposed process)'] },

    { slug: 'iwbe', title: 'iWBE — Intelligent Women-Owned Business Activation', place: 'Proposed program', kicker: 'BUSINESS & ENTERPRISE', primary_pathway: 'business-enterprise', subtopic: null, pathways: ['business-enterprise', 'creator-economy'], publication_status: 'proposed',
      img: null, description: 'A proposed activation program for women-owned businesses, from a first sale to a registered company.',
      notice: 'Proposed program. No implementation or partnership is claimed. The detailed proposal is being indexed.',
      overview: [], source: null, pending: true, research: [], documents: [], funding: { status: 'proposed', label: 'Proposed', note: '' }, results: [], resultNote: '',
      tools: ['software-budget-toolkit', 'creative-studio'], participate: [] },

    { slug: 'iswe', title: 'iSWE — Engineering and Scientific Participation', place: 'Proposed program', kicker: 'BUSINESS & ENTERPRISE · SOVEREIGN AI & SCIENCE', primary_pathway: 'business-enterprise', subtopic: null, pathways: ['business-enterprise', 'ai-science'], publication_status: 'proposed',
      img: null, description: 'A proposed program for engineering and scientific participation in Commons projects and M5Labs instruments.',
      notice: 'Proposed program. No implementation or partnership is claimed. The detailed proposal is being indexed.',
      overview: [], source: null, pending: true, research: [], documents: [], funding: { status: 'proposed', label: 'Proposed', note: '' }, results: [], resultNote: '',
      tools: [], participate: [] },
  ];

  const FO_PENDING = 'Integration not yet confirmed';
  const tools = [
    { slug: 'software-budget-toolkit', id: 'urn:m5commons:tool:software-budget-toolkit', title: 'Software Budget Toolkit', purpose: 'Plan and compare software spending for a business.', project: 'iwbe', pathways: ['business-enterprise', 'finance-markets'], families: ['FIN'], status: 'available', version: 'Public web page', license: 'Not stated', openUrl: 'https://m5bank.app/m5-office-budget-toolkit.html', sourceUrl: null, offline: 'No · web page', evidence: 'Public availability confirmed by the owner on 20 October 2026. No testing, scientific or security review is published.', fo: FO_PENDING, audience: 'Business owners' },
    { slug: 'creative-studio', id: 'urn:m5commons:tool:creative-studio', title: 'Creative Studio & Product Marks', purpose: 'Create product marks and creative assets for a business or creator.', project: 'iwbe', pathways: ['creator-economy', 'business-enterprise'], families: ['LEX'], status: 'available', version: 'Public web page', license: 'Not stated', openUrl: 'https://m5bank.app/m5-creative-studio.html', sourceUrl: null, offline: 'No · web page', evidence: 'Public availability confirmed by the owner on 20 October 2026. No testing, scientific or security review is published. Creating a mark here does not register a trademark or issue a certificate.', fo: FO_PENDING, audience: 'Creators, makers' },
    { slug: 'farmer-toolkit', id: 'urn:m5commons:tool:farmer-toolkit', title: 'Grower/Caretaker Sustainable Planet Toolkit', purpose: 'Free and open starting points for weather, soil, imagery, water, markets, mapping and livestock research, each with a rights state.', project: 'norton-ranch', pathways: ['agriculture-land', 'energy-resources'], families: ['WV', 'SCI'], status: 'draft', version: 'Reviewed 4 October 2026', license: 'Per source; see rights states', openUrl: B + 'pilots/norton-ranch-blueprint/FARMER-TOOLKIT.md', sourceUrl: B + 'pilots/norton-ranch-blueprint/farmer-data-registry.json', offline: 'Documentation · yes', evidence: 'Each source carries VERIFIED_PERMISSIVE, VERIFIED_ATTRIBUTION_REQUIRED, REFERENCE_ONLY or LICENSE_UNCLEAR.', fo: FO_PENDING, audience: 'Farmers, ranchers, cooperatives' },
    { slug: 'sovereign-herd', id: 'urn:m5commons:tool:sovereign-herd', title: 'Sovereign Herd', purpose: 'Creates stable synthetic animal, device and assignment records locally, without a provider or network call.', project: 'norton-ranch', pathways: ['agriculture-land'], families: ['SCI', 'SLM'], status: 'draft', version: 'v1 · passive monitoring reference', license: 'See LICENSE.md', openUrl: B + 'reference-implementation/sovereign-herd/README.md', sourceUrl: T + 'reference-implementation/sovereign-herd', offline: 'Yes · local only', evidence: 'Reference code. Not veterinary-grade; no collar vendor is M5 certified.', fo: FO_PENDING, audience: 'Agricultural builders' },
    { slug: 'norton-m5pod-starter', id: 'urn:m5commons:tool:norton-m5pod-starter', title: 'Sovereign Herd for Ranchers · Norton Ranch M5POD starter', purpose: 'The blueprint for ranchers to manage their own data, herd and land. The whole Blueprint in one verified ZIP that runs on your own computer with no network connection.', project: 'norton-ranch', pathways: ['agriculture-land'], families: ['SLM', 'LEX'], status: 'draft', version: 'Blueprint v1.4', license: 'See package manifest', openUrl: B + 'pilots/norton-ranch-blueprint/M5POD-PACKAGE.md', sourceUrl: B + 'pilots/norton-ranch-blueprint/m5pod-package.manifest.json', offline: 'Yes', evidence: 'Unregistered commons starter. It is not a licensed M5POD until the principal and entity register and activate the M5 tools.', fo: FO_PENDING, audience: 'Farmers, ranchers' },
    { slug: 'm5-iam-free', id: 'urn:m5commons:tool:m5-iam-free', title: 'M5 IAM Free · local starting pod', purpose: 'Creates a free, self-attested IAM starting pod on your own computer with a hash-chained ledger and no network call.', project: null, pathways: ['business-enterprise', 'spiritual-education-growth'], families: ['SLM', 'BASE'], status: 'draft', version: 'Reference code', license: 'See LICENSE.md', openUrl: B + 'reference-implementation/m5-iam-free/README.md', sourceUrl: T + 'reference-implementation/m5-iam-free', offline: 'Yes · local only', evidence: 'Does not issue a TCID, verify identity, create an M5 Bank account or a licensed M5POD.', fo: FO_PENDING, audience: 'Anyone' },
    { slug: 'provider-neutral-governor', id: 'urn:m5commons:tool:provider-neutral-governor', title: 'Provider-neutral governor', purpose: 'Demonstrates cost, context, budget, policy preflight, evidence-ledger handling and replaceable provider adapters.', project: null, pathways: ['ai-science'], families: ['SI', 'SC'], status: 'draft', version: 'Reference code', license: 'See LICENSE.md', openUrl: B + 'reference-implementation/provider-neutral-governor/README.md', sourceUrl: T + 'reference-implementation/provider-neutral-governor', offline: 'Yes', evidence: 'Governor budget and malformed-ledger regression tests pass. Not production security.', fo: FO_PENDING, audience: 'Builders, engineers' },
    { slug: 'dagny-m5-vx', id: 'urn:m5commons:tool:dagny-m5-vx', title: 'Dagny M5-VX simulator', purpose: 'Validates a four-modality purchase fixture and emits deterministic synthetic M5 Value Receipts.', project: 'dagny-bank-of-me', pathways: ['creator-economy', 'finance-markets'], families: ['BOM', 'FIN'], status: 'simulation', version: 'Synthetic fixture', license: 'See LICENSE.md', openUrl: B + 'pilots/dagny-bank-of-me/README.md', sourceUrl: T + 'pilots/dagny-bank-of-me', offline: 'Yes', evidence: 'Write-disabled. SIMULATION — NO VALUE MOVED.', fo: FO_PENDING, audience: 'Builders, reviewers' },
    { slug: 'sec-observatory', id: 'urn:m5commons:tool:sec-observatory', title: 'SEC Public Comment Observatory', purpose: 'Checks the official SEC docket every hour and publishes exact filing metadata and source digests.', project: 'sec-observatory', pathways: ['finance-markets', 'government-institutions'], families: ['LLM', 'FIN'], status: 'live', version: 'Hourly', license: 'See LICENSE.md', openUrl: OBS, sourceUrl: T + 'sec-public-input/observatory', offline: 'No · web dashboard', evidence: 'Automated signals never become human-reviewed summaries automatically.', fo: 'Not applicable · public dashboard', audience: 'Reviewers, regulators, the public' },
    { slug: 'shadow-dataset', id: 'urn:m5commons:tool:shadow-dataset', title: 'SHADOW M5Index research seed', purpose: 'Machine-readable seed dataset, asset index, public views and ingestion schemas.', project: 'shadow-m5index', pathways: ['finance-markets', 'agriculture-land'], families: ['ECON', 'WV'], status: 'research', version: 'Q3 2026', license: 'See LICENSE.md', openUrl: B + 'shadow-m5index/README.md', sourceUrl: T + 'shadow-m5index', offline: 'Yes · data files', evidence: 'Preliminary, non-canonical score. Methodology v0.1.', fo: FO_PENDING, audience: 'Researchers' },
    { slug: 'm5-calc-001', id: 'M5-CALC-001', title: 'M5-CALC-001 · Business Cost & Margin', purpose: 'Proposed calculator for business cost and margin.', project: 'm5labs-calculators', pathways: ['business-enterprise', 'ai-science'], families: ['FIN'], status: 'proposed', version: 'Not released', license: 'To be set at release', openUrl: null, sourceUrl: null, offline: 'Not released', evidence: 'Proposed. No review has started.', fo: FO_PENDING, audience: 'Businesses' },
    { slug: 'm5-calc-002', id: 'M5-CALC-002', title: 'M5-CALC-002 · Engineering Units & Materials', purpose: 'Proposed calculator for engineering units and materials.', project: 'm5labs-calculators', pathways: ['ai-science', 'energy-resources'], families: ['SCI'], status: 'proposed', version: 'Not released', license: 'To be set at release', openUrl: null, sourceUrl: null, offline: 'Not released', evidence: 'Proposed. No review has started.', fo: FO_PENDING, audience: 'Engineers' },
    { slug: 'm5-calc-003', id: 'M5-CALC-003', title: 'M5-CALC-003 · Mathematical Research Laboratory', purpose: 'Proposed laboratory for working with new mathematical results.', project: 'm5labs-calculators', pathways: ['ai-science'], families: ['FRN'], status: 'proposed', version: 'Not released', license: 'To be set at release', openUrl: null, sourceUrl: null, offline: 'Not released', evidence: 'Proposed. openai/math is an identified external source; referee participation is proposed.', fo: FO_PENDING, audience: 'Researchers' },
  ];

  // 20 Oct 2026 · publication states and toolkit additions
  Object.assign(STATUS, {
    published: { label: 'Open reference toolkit · Published', tone: '#1F7F8C', dash: false },
    'in-development': { label: 'In development', tone: '#83713C', dash: true },
    gated: { label: 'Credential-gated · not yet confirmed', tone: '#3C7BFF', dash: true },
  });
  const TLS = s => tools.find(t => t.slug === s), PJS = s => projects.find(p => p.slug === s);
  Object.assign(TLS('software-budget-toolkit'), { purpose: 'A local planner that compares the software subscriptions you pay for with free-to-use office, creative and budgeting tools. Entries stay in your browser.', evidence: 'Public page confirmed 20 October 2026. It is not a payment service, account import, installer or cancellation tool, and no commission or auto-charge is active.' });
  Object.assign(TLS('creative-studio'), { purpose: 'Choose free local creative tools, then create a self-declared human/AI provenance mark for each version of your own work.', evidence: 'Public page confirmed 20 October 2026. Marks are self-declared: not independently verified, signed, C2PA-certified or TitleChain-registered. Source files are hashed in the browser and never uploaded.' });
  ['farmer-toolkit', 'm5-iam-free', 'norton-m5pod-starter'].forEach(s => TLS(s).status = 'published');
  Object.assign(TLS('farmer-toolkit'), { purpose: 'Source, instructions and datasets for farmland co-op trusts: land, animal and plant management starting points, each with a rights state.' });
  Object.assign(TLS('m5-iam-free'), { title: 'IAM Starter · local starting pod', project: 'peoples-trust', pathways: ['agriculture-land', 'business-enterprise', 'spiritual-education-growth'] });
  ['m5-calc-001', 'm5-calc-002', 'm5-calc-003'].forEach(s => Object.assign(TLS(s), { status: 'in-development', evidence: 'In development as the first M5Labs development and funding project. Not an available production instrument.' }));
  tools.unshift({ slug: 'commons-cooperative', id: 'urn:m5commons:tool:commons-cooperative', title: 'Commons Cooperative toolkit', purpose: 'Source, legal documents and workflows for turning distressed government real estate into community commons projects.', project: 'spring-commons', pathways: ['agriculture-land', 'government-institutions', 'finance-markets'], families: ['LEX', 'FIN', 'TRU'], status: 'published', version: 'main · ' + VERIFIED, license: 'See LICENSE.md', openUrl: B + 'pilots/312-spring-commons/README.md', sourceUrl: T + 'pilots/312-spring-commons', offline: 'Documentation · yes', evidence: 'Placeholder templates await counsel, regulatory and transaction review. No control is VERIFIED.', fo: FO_PENDING, audience: 'Communities, co-ops, public owners' });
  tools.push({ slug: 'm5pod-installer', id: 'urn:m5commons:tool:m5pod-installer', title: 'M5POD · managed M5-API installer', purpose: 'Managed installation and credential-gated marketplace actions inside a member’s own M5POD.', project: 'iwbe', pathways: ['business-enterprise', 'creator-economy', 'ai-science'], families: ['SLM', 'SC'], status: 'gated', version: 'Not released', license: 'To be set at release', openUrl: null, sourceUrl: null, offline: 'Not released', evidence: 'Requires credentials, explicit member approval, pinned releases and signature checks. Not yet confirmed; no installer is published.', fo: FO_PENDING, audience: 'Members' });
  PJS('spring-commons').tools = ['commons-cooperative'];
  PJS('peoples-trust').tools = ['farmer-toolkit', 'm5-iam-free'];
  PJS('iwbe').tools = ['software-budget-toolkit', 'creative-studio', 'm5pod-installer'];
  PJS('iswe').tools = ['m5pod-installer', 'm5-calc-003'];
  Object.assign(PJS('m5labs-calculators'), { publication_status: 'in-development', notice: 'In development. The first M5Labs development and funding project, not an available production instrument. M5-CALC-001, 002 and 003 have not completed review or certification.', funding: { status: 'proposed', label: 'First M5Labs development and funding project · seeking funding', note: 'Igor Rivin’s participation as a referee is proposed and not confirmed.' } });
  PJS('iwbe').funding = { status: 'proposed', label: 'Launch funding sought · review the brief', note: 'Funding launches each woman’s M5 Bank of Business and co-op. Proposed fees are designed to carry more of the operating cost each year.' };
  PJS('iswe').funding = { status: 'proposed', label: 'Launch funding sought · review the brief', note: 'Engineers can earn through provenance, review and licensing of the tools they create.' };

  // 21 Oct 2026 · Dagny Closet walkthrough, iWBE/iSWE Toolkit, iWBE as featured pilot
  tools.unshift({ slug: 'dagny-closet', id: 'urn:m5commons:tool:dagny-closet', title: 'Dagny Closet walkthrough', purpose: 'A founder use case anyone can follow: turn what is in your closet into a sustainable lovecycle, from a personal closet you sell from to a co-op.', project: 'dagny-bank-of-me', pathways: ['creator-economy', 'business-enterprise'], families: ['BOM', 'TRU'], status: 'available', version: 'Public web walkthrough', license: 'Not stated', openUrl: 'https://dagny.m5bank.app', sourceUrl: null, offline: 'No · web page', evidence: 'Public walkthrough stated by the owner. No testing, scientific or security review is published.', fo: FO_PENDING, audience: 'Creators, closet sellers, co-ops' });
  tools.push({ slug: 'iwbe-iswe-toolkit', id: 'urn:m5commons:tool:iwbe-iswe-toolkit', title: 'iWBE / iSWE Toolkit', purpose: 'Intelligent calculators and other tools for a woman’s business, and for engineers’ discoveries and research, developed with M5Labs.', project: 'iwbe', pathways: ['business-enterprise', 'ai-science'], families: ['FIN', 'SCI', 'FRN'], status: 'in-development', version: 'Not released', license: 'To be set at release', openUrl: null, sourceUrl: null, offline: 'Not released', evidence: 'In development alongside the M5 Sovereign Intelligent Calculator. Not an available tool.', fo: FO_PENDING, audience: 'iWBE members, iSWE engineers' });
  PJS('dagny-bank-of-me').tools = ['dagny-closet', 'dagny-m5-vx'];
  Object.assign(PJS('iwbe'), { pending: false, designRef: 'iwbe.html', designRefLabel: 'Read the full iWBE proposal', place: 'Featured pilot · proposed program',
    img: 'assets/women/w01.jpg', imgAlt: 'Woman business owner', imgCredit: 'iWBE · TitleChain Foundation',
    notice: 'Proposed program. Launch funding is sought; review the brief for details. No implementation or partnership is claimed.',
    overview: [
      'An open-source initiative of the TitleChain Foundation to activate 1,000 women-owned businesses. Funding establishes her iWBE certificate, activates her private and business M5PODs and keeps her training current as her work grows. Alongside iWBE, iSWE brings women engineers into the same Commons.',
      'Her path: 1. Walk through Dagny Closet, the founder’s own use case for launching a personal closet and growing it into a co-op. 2. Use the Software Budget Toolkit to see what she pays for software today and which free tools can replace it. 3. Create product marks in Creative Studio. 4. Join the waitlist.',
      'The iWBE / iSWE Toolkit is in development: intelligent calculators and other tools for her business, and for engineers’ discoveries and research.' ],
    participate: ['Walk through Dagny Closet', 'Compare your software costs with free tools', 'Join the iWBE waitlist'] });
  const CV = 'iwbe.html';
  Object.assign(PJS('iwbe'), { img: 'assets/iwbe-women-team.jpg', imgAlt: 'Three women business owners standing together, one holding a phone and one a binder', imgCredit: 'Photo · Yan Krukov / Pexels', ctaUrl: 'https://dagny.m5bank.app/claim', ctaLabel: 'Join the waitlist' });
  PJS('iwbe').participate = ['Walk through Dagny Closet', 'Compare your software costs with free tools', 'Join the waitlist at dagny.m5bank.app/claim', 'Contact the Foundation to join the team securing launch funding'];
  PJS('iwbe').funding.target = '$1.25M · first 12 months';
  PJS('iwbe').funding.routes = [{ kind: 'Underwriter brief', title: 'Underwrite the commons', url: CV + '#underwrite' }, { kind: 'Opportunity', title: 'Where $1.25M goes', url: CV + '#plan' }, { kind: 'Sustainability', title: 'Funding & Sustainability', url: CV + '#sustainability' }];
  PJS('iswe').funding.routes = [{ kind: 'Opportunity', title: 'iSWE in the iWBE proposal', url: CV + '#iswe' }, { kind: 'Underwriter brief', title: 'Underwrite the commons', url: CV + '#underwrite' }];
  PJS('iwbe').tools = ['dagny-closet', 'software-budget-toolkit', 'creative-studio', 'iwbe-iswe-toolkit', 'm5pod-installer'];
  Object.assign(PJS('iswe'), { pending: false, designRef: 'iwbe.html#iswe', designRefLabel: 'Read the iSWE proposal',
    notice: 'Proposed program. Launch funding is sought; review the brief for details. No implementation or partnership is claimed.',
    overview: ['iSWE brings women engineers into the same Commons as iWBE. Engineers build and review the intelligent calculators and tools that iWBE members use, and can earn through provenance, review and licensing of the tools they create.'],
    participate: ['Build to the open calculator standard', 'Review a toolkit'] });
  PJS('iswe').tools = ['iwbe-iswe-toolkit', 'm5pod-installer', 'm5-calc-003'];

  const standards = [
    ['M5-AIGOV-001', 'Provider, plugin, tool, budget, privacy, authorization and evidence governance', 'standards/M5-AIGOV-001.md'],
    ['M5-AIMOD-001', 'Resident and open-weight model artifacts, hardware profiles and portability', 'standards/M5-AIMOD-001.md'],
    ['M5-AISPACE-001', 'Spatial, embodied, experiential, sensor, simulation and actuator governance', 'standards/M5-AISPACE-001.md'],
    ['M5-AIPROV-001', 'Provider identity, credential status and verified endpoint binding', 'standards/M5-AIPROV-001.md'],
    ['M5-RICARDIAN-TRIPLE-LAYER-001', 'Human terms, machine policy and bounded executable settlement', 'standards/M5-RICARDIAN-TRIPLE-LAYER-001.md'],
    ['M5-AIMARKET-001', 'Sovereign intelligence baseline: a $0, unmetered local tier for M1-BOM', 'standards/M5-AIMARKET-001.md'],
    ['M5-EVENT-001', 'Event, metering, commerce and threat telemetry envelope', 'standards/M5-EVENT-001.md'],
  ].map(([code, scope, path]) => ({ code, scope, url: B + path }));

  const library = [
    doc('M5 Commons Project Control Pack Standard', 'docs/project-control-pack/M5-COMMONS-PROJECT-CONTROL-PACK-STANDARD.md', 'Informative', 'Standard'),
    doc('Participation Passport and Eligibility Matrix', 'docs/project-control-pack/M5-PROJECT-PARTICIPATION-PASSPORT-AND-ELIGIBILITY-MATRIX.md', 'Draft', 'Matrix'),
    doc('M5-CV Work, Opportunity and Support Matching', 'docs/project-control-pack/M5-CV-WORK-OPPORTUNITY-AND-SUPPORT-MATCHING.md', 'Draft', 'Model'),
    doc('Open Standards Evidence Registry', 'docs/OPEN-STANDARDS-EVIDENCE-REGISTRY.md', 'Draft', 'Registry'),
    doc('M5POD Data Portability Profile', 'docs/M5POD-DATA-PORTABILITY-PROFILE.md', 'Draft', 'Profile'),
    doc('Draft JSON Schemas', 'schemas/README.md', 'Draft', 'Schemas'),
    doc('Threat Model', 'THREAT-MODEL.md', 'Draft', 'Security'),
    doc('Glossary', 'GLOSSARY.md', '', 'Reference'),
    doc('Release Status · RC v0.7', 'RELEASE-STATUS.md', 'Release candidate', 'Status'),
  ];

  const published = [
    { date: '2026-10-08', title: 'SEC Observatory incident recovery: S7-2026-35 reconciliation added', url: B + 'sec-public-input/observatory/README.md', status: 'live' },
    { date: '2026-10-04', title: 'Grower/Caretaker Sustainable Planet Toolkit reviewed: weather, soil, imagery, water, markets and livestock sources', url: B + 'pilots/norton-ranch-blueprint/FARMER-TOOLKIT.md', status: 'draft' },
    { date: '2026-10-03', title: 'Norton Ranch Blueprint v1.4 · Founder Archive package', url: B + 'pilots/norton-ranch-blueprint/README.md', status: 'draft' },
    { date: '2026-10-03', title: 'SEC submissions extend the September 5 foundational filing', url: B + 'sec-public-input/SEC_UPDATE_2026-10-03.md', status: 'research' },
    { date: '2026-09-24', title: 'One Project Control Pack applied to all three development lanes', url: B + 'docs/project-control-pack/M5-COMMONS-PROJECT-CONTROL-PACK-STANDARD.md', status: 'draft' },
    { date: '2026-09-24', title: 'SHADOW CAMEL Report Q3 2026, first edition', url: B + 'shadow-m5index/reports/SHADOW-CAMEL-REPORT-Q3-2026.md', status: 'research' },
  ];

  const observatory = {
    dockets: [
      { id: 'S7-2026-30', title: 'Transfer Agent Rules', url: 'https://www.sec.gov/rules-regulations/public-comments/s7-2026-30' },
      { id: 'S7-2026-35', title: 'Adviser and Regulated Fund Custody Rules; Crypto Custody Rules', url: null },
    ],
    timeline: [
      { date: '2026-09-01', title: 'Earliest reviewed public comment (Zayn) on the official docket', url: 'https://www.sec.gov/comments/S7-2026-30/s7202630-1025059-3321906.html', state: 'Human reviewed' },
      { date: '2026-09-05', title: 'TitleChain Foundation public comment, now posted on the SEC docket', url: 'https://www.sec.gov/comments/S7-2026-30/s7202630-1029659-3393926.pdf', state: 'Posted by SEC' },
      { date: '2026-09-23', title: 'Supplemental Comment and Technical Exhibits A–J emailed to the SEC', url: B + 'sec-public-input/foundation-submissions/2026-09-23-supplemental-comment/README.md', state: 'Pending SEC posting' },
      { date: '2026-09-24', title: 'September 16–24 Open Commons Review (Foundation research, not an SEC submission)', url: B + 'sec-public-input/open-commons-review/2026-09-24.md', state: 'Foundation research' },
      { date: '2026-10-03', title: 'October 3 submissions extend the September 5 filing', url: B + 'sec-public-input/SEC_UPDATE_2026-10-03.md', state: 'Recorded' },
      { date: '2026-10-08', title: 'Incident recovery: withheld reviews with missing docket IDs; S7-2026-35 reconciliation', url: B + 'sec-public-input/observatory/README.md', state: 'Method change' },
    ],
  };

  const registry = [
    ...projects.map(p => ({ catalog_id: 'urn:m5commons:project:' + p.slug, kind: 'Project', title: p.title, slug: p.slug, maintainer: 'TitleChain Foundation', source: p.source ? B + p.source : null, sourcePath: p.source, version: 'main @ ' + VERIFIED, license: 'Apache-2.0 / CC-BY-4.0 per LICENSE.md', publication_status: p.publication_status, titlechain_registry_ref: null, certificate_ref: null, issuance_status: 'not-submitted' })),
    ...tools.map(t => ({ catalog_id: t.id.startsWith('urn') ? t.id : 'urn:m5commons:tool:' + t.slug, kind: 'Toolkit', title: t.title, slug: t.slug, maintainer: 'TitleChain Foundation', source: t.sourceUrl, sourcePath: t.sourceUrl, version: t.version, license: t.license, publication_status: t.status, titlechain_registry_ref: null, certificate_ref: null, issuance_status: 'not-submitted' })),
    { catalog_id: 'urn:m5commons:usecase:dagny-closet-certificate', kind: 'Reported use case', title: 'Dagny · free tools with a Certificate of Title for a private business', slug: 'dagny-closet-certificate', maintainer: 'Reported by the owner', source: 'https://dagny.m5bank.app/bank', sourcePath: 'dagny.m5bank.app/bank', version: '—', license: '—', publication_status: 'live', titlechain_registry_ref: null, certificate_ref: null, issuance_status: 'pending', reported: true,
      issuance: { entity: null, signer: null, type: 'Certificate of Title (reported)', date: null, verification: null } },
  ];

  const CONTACT = 'mailto:hello@titlechainfoundation.org';
  window.M5C = { CONTACT, REPO, B, T, OBS, VERIFIED, STATUS, pathways, families, projects, tools, standards, library, published, observatory, registry };
})();
