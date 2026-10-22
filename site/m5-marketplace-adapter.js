/* M5-OpenAPI Marketplace adapter.
 * Every function the marketplace UI calls lives here. All are SIMULATED today.
 * To go live: replace each function body with the real call, keep the return shape,
 * and set SIMULATED to false. The UI reads only the fields returned here.
 * Package facts come from m5-pod/iam-free/M5IAM-FREE-PACKAGE.md (release m5-iam-free-v0.2.0).
 */
(function () {
  const wait = ms => new Promise(r => setTimeout(r, ms));
  const sha256 = async s => { const b = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s)); return [...new Uint8Array(b)].map(x => x.toString(16).padStart(2, '0')).join(''); };
  const now = () => new Date().toISOString();
  const REPO = 'TitleChain-Foundation/M5-AI-Sovereign-Commons';
  const TAG = 'm5-iam-free-v0.2.0';
  const REL = 'https://github.com/' + REPO + '/releases/download/' + TAG + '/';

  // Freedom Office starter kit. Source: freeToolsCatalog.js (dagny.m5bank.app), checked 21 Oct 2026.
  const TOOLS = [
    { id: 'agent', cat: 'Personal AI agent', t: 'M5 AI Agent', by: 'Dagny founder program · Hermes Agent + Ollama', d: 'Your own AI agent on your computer, and the first step in getting everything in one place. Your M5-IAM account gives you a folder structure for your life that you can add to and change as you go. The AI model runs on your machine through Ollama, so nothing leaves it. The agent can use your files and terminal, so you decide what it may do.',
      points: [['Start', 'Laya, the starter agent in your kit, sets up your account with guardrails and gives you how-to prompts.'], ['Gather', 'Bring in your files from wherever they are.'], ['Organize', 'Sort your ideas, thoughts, writing and designs into your M5-IAM folders.'], ['Activate', 'Shape them into a new business, or prepare an invention for a patent or to keep as a trade secret.'], ['Build', 'Take a new algorithm into the M5 Sovereign Calculator.'], ['Grow', 'Add agents as you expand. You remain the first and most important person in your pod.']],
      founder: 'Built on Dagny, the founder program. Our founder has trained Dagny on her own world for the past ten years and is now releasing the code to you for free.',
      replaces: 'ChatGPT Plus', save: 20, help: true, other: 'LM Studio (easier to start, but closed source)', early: '', about: 'https://github.com/NousResearch/hermes-agent', aboutLabel: 'Hermes Agent',
      sw: [{ n: 'Hermes Agent', role: 'Personal AI agent', v: 'v0.22.4', lic: 'MIT', src: 'github.com/NousResearch/hermes-agent' }, { n: 'Ollama', role: 'AI model runtime', v: 'v0.40.7', lic: 'MIT', src: 'github.com/ollama/ollama' }] },
    { id: 'office', cat: 'Office', t: 'M5 Office', by: 'LibreOffice', d: 'Documents, spreadsheets and slides. Opens and saves Word, Excel and PowerPoint files.', replaces: 'Microsoft 365', save: 9.99, other: '', early: 'WordCraft, GridCraft and DeckCraft from ArtCraft', about: 'https://www.libreoffice.org', aboutLabel: 'LibreOffice',
      sw: [{ n: 'LibreOffice', role: 'Office', v: '26.2.7', lic: 'MPL-2.0', src: 'libreoffice.org' }] },
    { id: 'notes', cat: 'Notes & files', t: 'M5 Notes', by: 'Joplin', d: 'Notes, to-do lists and project pages, kept on your own computer.', replaces: 'Notion', save: 10, other: 'Syncthing, to keep files in step across your devices', early: '', about: 'https://github.com/laurent22/joplin', aboutLabel: 'Joplin',
      sw: [{ n: 'Joplin', role: 'Notes & files', v: 'v3.7.21', lic: 'AGPL-3.0-or-later', src: 'github.com/laurent22/joplin' }] },
    { id: 'design', cat: 'Photos & design', t: 'M5 Design', by: 'GIMP', d: 'Edit photos and make graphics.', replaces: 'Adobe Photoshop', save: 22.99, other: 'Penpot for social posts and layouts', early: 'PhotoCraft and VectorCraft from ArtCraft', about: 'https://gitlab.gnome.org/GNOME/gimp', aboutLabel: 'GIMP',
      sw: [{ n: 'GIMP', role: 'Photos & design', v: '3.2.6', lic: 'GPL-3.0-or-later', src: 'gitlab.gnome.org/GNOME/gimp' }] },
    { id: 'video', cat: 'Video', t: 'M5 Video', by: 'Shotcut', d: 'Cut, trim and caption videos for posts and reels.', replaces: 'CapCut Pro', save: 9.99, other: 'OBS Studio for screen recording', early: 'FilmCraft from ArtCraft', about: 'https://github.com/mltframework/shotcut', aboutLabel: 'Shotcut',
      sw: [{ n: 'Shotcut', role: 'Video', v: '26.9.27', lic: 'GPL-3.0', src: 'github.com/mltframework/shotcut' }] },
    { id: 'publish', cat: 'Newsletter', t: 'M5 Publish', by: 'Ghost', d: 'Publish a newsletter on your own site and keep all of your subscription income.', replaces: 'Substack fees', save: 50, help: true, other: 'Listmonk', early: '', about: 'https://github.com/TryGhost/Ghost', aboutLabel: 'Ghost',
      sw: [{ n: 'Ghost', role: 'Newsletter', v: 'v6.72.0', lic: 'MIT', src: 'github.com/TryGhost/Ghost' }] },
    { id: 'wallet', cat: 'Wallet', t: 'M5 Self-Custody Wallet', by: 'Rabby Wallet', d: 'Hold your own digital money and keys, with no account fees. Write your recovery phrase on paper and keep it offline.', replaces: 'custodial wallet fees', save: 5, other: 'Frame', early: '', about: 'https://github.com/RabbyHub/Rabby', aboutLabel: 'Rabby Wallet',
      sw: [{ n: 'Rabby Wallet', role: 'Wallet', v: 'v0.94.12', lic: 'MIT (name and logo reserved)', src: 'github.com/RabbyHub/Rabby' }] }
  ];
  // Bundled by M5 in every kit. Versions and licenses to be confirmed before launch.
  const BASE = [
    { t: 'M5 Shell · Laya', role: 'Desktop app · Tauri v2', n: 'Laya (Tauri v2 shell)', v: 'latest release', lic: 'Apache-2.0', src: 'github.com/aayushch/laya', d: 'Laya is an open-source, local-first desktop app built on Tauri v2. It keeps your data on your computer, stores keys in your computer’s keychain, reads your documents in place and runs AI locally through Ollama or with your own keys. M5 sets up your M5-IAM folders inside it.' },
    { t: 'Laya starter agent', role: 'Guardrails & prompts', n: 'M5 prompt pack for Laya', v: 'to be pinned', lic: 'Apache-2.0', src: 'TitleChain Foundation', d: 'M5 guardrail rules and how-to prompts loaded as Laya custom prompts, so it helps you set up your account and pull together everything you want to do.' },
    { t: 'Guides & worksheets', role: 'Documentation', n: 'How-to prompts and worksheets', v: 'to be pinned', lic: 'CC BY 4.0', src: 'TitleChain Foundation', d: 'Step-by-step documentation and worksheets for organizing your files, ideas and plans.' }
  ];
  const PODS = [
    { t: 'IAM Pod', s: 'Active with this kit', on: true },
    { t: 'Bank of Me pod', s: 'Opens with M1 · Bank of Me' },
    { t: 'Bank of Us pod', s: 'Opens with M2' },
    { t: 'Business pod', s: 'Opens with M3 · Bank of Business' }
  ];
  const PARTS = TOOLS;

  const CHAINS = ['Alabama:alabamachain.eth','Alaska:alaskachain.eth','Arizona:arizonachain.eth','Arkansas:arkansaschain.eth','California:californiachain.eth','Colorado:coloradochain.eth','Connecticut:connecticutchain.eth','Delaware:delawarechain.eth','Florida:floridachain.eth','Georgia:georgiastatechain.eth','Hawaii:hawaiichain.eth','Idaho:idahochain.eth','Illinois:illinoischain.eth','Indiana:indianachain.eth','Iowa:iowachain.eth','Kansas:kansaschain.eth','Kentucky:kentuckychain.eth','Louisiana:louisianachain.eth','Maine:mainechain.eth','Maryland:marylandchain.eth','Massachusetts:massachusettschain.eth','Michigan:michiganstatechain.eth','Minnesota:minnesotachain.eth','Mississippi:mississippichain.eth','Missouri:missourichain.eth','Montana:montanachain.eth','Nebraska:nebraskachain.eth','Nevada:nevadachain.eth','New Hampshire:newhampshirechain.eth','New Jersey:newjerseychain.eth','New Mexico:newmexicochain.eth','New York:newyorkchain.eth','North Carolina:northcarolinachain.eth','North Dakota:northdakotachain.eth','Ohio:ohiochain.eth','Oklahoma:oklahomachain.eth','Oregon:oregonchain.eth','Pennsylvania:pennsylvaniachain.eth','Rhode Island:rhodeislandchain.eth','South Carolina:southcarolinachain.eth','South Dakota:southdakotachain.eth','Tennessee:tennesseechain.eth','Texas:texaschain.eth','Utah:utahchain.eth','Vermont:vermontchain.eth','Virginia:virginiachain.eth','Washington:washingtonchain.eth','West Virginia:westvirginiachain.eth','Wisconsin:wisconsinchain.eth','Wyoming:wyomingchain.eth'].map(s => { const [name, chain] = s.split(':'); return { name, chain }; });

  // From iam-catalog.json. Registered accounts are not open yet.
  const ACCOUNTS = [
    { tier: 'M1', name: 'Bank of Me', for: 'You, as a person', price: '$49 per year' },
    { tier: 'M2', name: 'Bank of Us', for: 'Each family, co-op, nonprofit or trust', price: '$79 per year · pending launch' },
    { tier: 'M3', name: 'Bank of Business', for: 'Each business', price: '$99 per year · pending launch' },
    { tier: 'M4', name: 'Bank of Institutions', for: 'Each institution · Master Entity ID', price: 'Request a quote' },
    { tier: 'M5', name: 'Bank of Government', for: 'Each government entity · Master Entity ID', price: 'Request a quote' }
  ];

  const interest = {};

  window.M5Adapter = {
    SIMULATED: true, TOOLS, BASE, PODS, PARTS, CHAINS, ACCOUNTS,

    // LIVE: GET https://api.github.com/repos/{REPO}/releases/tags/{TAG}
    async fetchRelease(pkg) {
      await wait(500);
      return { pkg, repo: REPO, tag: TAG, asset: TAG + '.zip', url: REL + TAG + '.zip', shaUrl: REL + TAG + '.zip.sha256', manifest: 'm5-pod/iam-free/m5iam-package.manifest.json', license: 'Apache-2.0', state: 'Unregistered commons starter' };
    },

    // LIVE: one button. The M5 installer runs on the member's computer, fetches each tool from its official source
    // (M5 never hosts or mirrors), adds the M5 Runtime License, and seals one container into the IAM Pod with a TitleChain Certificate.
    async download(release, toolIds, onProgress) {
      for (let p = 0; p <= 100; p += 10) { onProgress && onProgress(p); await wait(80); }
      const files = [];
      for (const b of BASE) files.push({ id: 'base', t: b.t, file: b.n, src: b.src, sha256: await sha256(b.n) });
      for (const t of TOOLS.filter(x => toolIds.includes(x.id))) for (const s of t.sw) files.push({ id: t.id, t: t.t, file: s.n + ' ' + s.v, src: s.src, sha256: await sha256(s.src + s.v) });
      const seal = await sha256(files.map(f => f.sha256).join(':') + ':m5-runtime-license');
      return { asset: 'Freedom Office kit', container: 'm5-freedom-office-kit.m5pod', runtimeLicense: 'M5 Runtime License · bundled', certificate: 'urn:titlechain:cert:' + seal.slice(0, 24), sealedTo: 'IAM Pod · M5IAM-000', files };
    },

    // LIVE: compare each installer's SHA-256 with the checksum published on its official release page
    async verifyPackage(release, dl) {
      await wait(600);
      const rows = await Promise.all(dl.files.map(async f => ({ ...f, expected: f.sha256, match: true })));
      return { certificate: 'urn:m5commons:kit:freedom-office:' + TAG, checksums: 'official release checksums', rows, allMatch: rows.every(r => r.match) };
    },

    // LIVE: TitleChain Registry issues one Certificate of Title per accepted tool into the IAM-Free pod
    async kitCertificates({ name, tools }) {
      const out = [];
      for (const t of TOOLS.filter(x => tools.includes(x.id))) {
        const s = t.sw[0];
        const body = { registry: 'TitleChain Registry', kind: 'M5 Freedom Office · Software License', titleNo: 'SAMPLE-SW-' + Math.floor(10000000 + Math.random() * 89999999), holder: name + ' · M5IAM-000', tool: t.t, poweredBy: t.sw.map(x => x.n + ' ' + x.v).join(' + '), license: s.lic, type: 'Open source', cost: '$0', source: s.src.replace(/^github\.com\/|^gitlab\.gnome\.org\//, ''), accepted: new Date().toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' }), status: 'Sample · not issued', registryEntry: 'Simulated · not anchored' };
        out.push({ id: t.id, ...body, sha256: await sha256(JSON.stringify(body)) });
      }
      return out;
    },

    // LIVE: python3 m5_iam.py init --name "…" --chain … --i-am-human   (runs on the member's computer, no network)
    async createIam({ name, chain, human, parts }) {
      await wait(800);
      const genesis = await sha256('genesis:' + name + ':' + chain + ':' + now());
      const att = await sha256(genesis + ':attestation');
      return { account: 'M5IAM-000', status: 'IAM ONLY', name, chain, humanAttested: !!human, verified: false, price: 'Free for life', localId: 'm5iam:local:' + genesis.slice(0, 12), parts, ledgerHead: att, ledger: [{ n: 0, event: 'pod.created', hash: genesis }, { n: 1, event: 'attestation.recorded', prev: genesis.slice(0, 16), hash: att }], path: '~/M5POD-IAM', created: now() };
    },

    // LIVE: the kit writes iam.json + attestation; this is the portable self-attested summary.
    iamCertificate(iam, verify) {
      return { type: 'M5 IAM Starting Pod Certificate', selfAttested: true, verified: false, account: iam.account, status: iam.status, holder: iam.name, stateChain: iam.chain, localIdentifier: iam.localId, ledgerHead: iam.ledgerHead, package: verify.certificate, parts: iam.parts, created: iam.created,
        notice: 'Self-attested starting pod. Not a TCID, not a verified identity, not an M5 Bank account or licensed M5POD.' };
    },

    // LIVE: POST https://m5bank.app/api/iam/register  { email, tiers, iamCertificate }
    async registerIam({ email, tiers, iam }) {
      await wait(900);
      return { tcid: 'TCID-' + (await sha256(email)).slice(0, 10).toUpperCase(), iamId: 'did:m5:iam:' + (await sha256(email)).slice(0, 16), tiers, carriedLedgerHead: iam.ledgerHead.slice(0, 16), status: 'registered', at: now() };
    },

    // LIVE: POST https://m5bank.app/api/openapi/activate  { iamId }
    async activateOpenApi({ iamId }) { await wait(700); return { iamId, marketplace: 'M5-OpenAPI', scopes: ['catalog:read', 'package:install', 'credential:receive'], status: 'active', at: now() }; },

    // LIVE: POST https://m5bank.app/api/credentials/issue → W3C VC stored in the M5POD
    async issueCredential({ iamId, certificate, tag, parts }) {
      await wait(900);
      return { '@context': ['https://www.w3.org/ns/credentials/v2'], type: ['VerifiableCredential', 'M5InstallationCredential'], id: 'urn:m5:vc:' + (await sha256(iamId + certificate)).slice(0, 20), issuer: 'did:m5:titlechain-foundation (to be confirmed)', validFrom: now(),
        credentialSubject: { id: iamId, package: 'm5-iam-free', release: tag, packageCertificate: certificate, parts, installedTo: 'M5POD (registered)' }, status: 'issued-pending-activation', visibility: 'private' };
    },

    // LIVE: POST https://m5bank.app/api/credentials/activate  { vcId }
    async activateCredential(vc) { await wait(700); return { ...vc, status: 'active', activatedAt: now() }; },

    // LIVE: GET/POST https://m5bank.app/api/interest  { family } — aggregate interest per calculator family
    async getInterest() { await wait(200); return { ...interest }; },
    async setInterest(code, on) { await wait(150); interest[code] = Math.max(0, (interest[code] || 0) + (on ? 1 : -1)); return { code, count: interest[code] }; }
  };
})();
