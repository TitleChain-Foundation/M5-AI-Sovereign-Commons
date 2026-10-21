"""Create and check a free, local M5 IAM starting pod.

Runs on a computer the person controls. Uses only the Python standard library
and performs no network calls. It records a self-attested human origin and a
local folder layout; it does not issue a TCID, a credential, an M5 account, a
licensed M5POD, or any authority.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import html
import json
import os
from pathlib import Path
import sys
import uuid
import zipfile

SCHEMA = 'm5.iam.local/0.1'
ACCOUNT_SKU = 'M5IAM-000'
LEGACY_ALIAS = '000-IAM'
STATUS = 'IAM ONLY'
IDENTITY_STATUS = 'SELF_ATTESTED_NOT_VERIFIED'
LICENSE_STATE = 'UNREGISTERED_LOCAL_STARTER'
LAYER = 'M0-M5IAM-000'
GENESIS = '0' * 64
CONTRACT_VERSION = '0.2.0'
HUMAN_TERMS = """# IAM Human Attestation

I, {name}, state that I am a living human being, acting for myself.

I am creating this IAM account on a device I control.

My state chain is {chain}. This is my own choice and has not been verified.

I understand that this is my own attestation. No one has verified it. It does
not issue a TCID or a credential, open a Bank of Me account, or authorize any
payment, signature, transfer or agent action.

I accept the CYRUS Protocol, which protects me: no slavery, servitude or
forced labour; freedom of thought, conscience and faith, any faith or none;
and my rights to identity, data, privacy, self-determination and portability.

Under it I hold the right to refuse consent. I may select it now. It
activates only when my credentials are verified.

I may delete this account and its records from my device at any time.

Attested: {now}
"""
ATTESTATION_TEXT = (
    'I am a human being. I am creating this local IAM starting pod for myself, '
    'on a computer I control. I understand this statement is self-attested and '
    'has not been verified by any credential, issuer or registry.'
)
SIGNATURE_SLOTS = {
    'holder': 'RESERVED_NOT_SIGNED',
    'approving_agency': 'RESERVED_NOT_SIGNED',
    'note': 'Signed when the holder has a signing key and when an approved agency verifies this IAM through M5-x401.',
}
# Accepting the CYRUS Protocol is required: it is what protects the holder.
# Wording is a draft for counsel review.
CYRUS_PROTOCOL = {
    'name': 'CYRUS Protocol',
    'held_by': 'TitleChain Sovereign Purpose Trust',
    'basic_rights': ['No slavery, servitude or forced labour',
                     'Freedom of thought, conscience and faith: any faith or none'],
    'sovereign_rights': ['Identity', 'Data', 'Privacy', 'Self-determination', 'Portability'],
    'grants': 'The right to refuse consent',
}
REFUSAL_ACTIVATES = ('When your credentials are verified, by registering Bank of Me or by an approved agency '
                     'verifying this IAM through M5-x401.')
NON_CLAIMS = [
    'Not a TCID. No TitleChain ID has been issued.',
    'Not a verified identity. No credential or issuer has checked this statement.',
    'Not an M5 Bank account and not a licensed M5POD.',
    'Cannot authorize a transaction, title transfer, payment, signature or delegated agent action.',
]
VAULT_NOTE = {
    'consent': 'Your acceptance of the CYRUS Protocol, and your right to refuse consent: selected by you, activated when your credentials are verified.',
    'attestation': 'The human attestation in three matching parts: the words, the data and the check.',
    'identifiers': 'The local identifier. TCID, PayName, ENS and WSW URI stay empty until issued by registration.',
    'receive': 'Reserved for a receiving address. Empty until one is issued by registration.',
    'registry': 'Your TitleChain Registry entry. A sample until launch: only a hash would ever be anchored, never your personal data.',
    'ledger': 'Append-only, hash-chained record of what this tool has written.',
    'm5agent': 'Rules and tooling for any agent the holder chooses. Nothing here is specific to one vendor.',
}


class PodError(Exception):
    pass


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def utc_now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def write_json(path, data):
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def read_events(layer):
    path = layer / 'ledger' / 'events.jsonl'
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]


def event_hash(event):
    body = {key: event[key] for key in ('seq', 'at', 'type', 'path', 'sha256', 'prev')}
    return sha256_bytes(json.dumps(body, sort_keys=True, separators=(',', ':')).encode('utf-8'))


def append_event(layer, event_type, at, path=None):
    events = read_events(layer)
    event = {
        'seq': len(events) + 1,
        'at': at,
        'type': event_type,
        'path': path,
        'sha256': sha256_bytes((layer / path).read_bytes()) if path else None,
        'prev': events[-1]['hash'] if events else GENESIS,
    }
    event['hash'] = event_hash(event)
    with (layer / 'ledger' / 'events.jsonl').open('a', encoding='utf-8') as handle:
        handle.write(json.dumps(event, sort_keys=True) + '\n')
    return event


def status_page(record):
    name = html.escape(record['display_name'] or 'Not given')
    claims = ''.join(f'<li>{html.escape(item)}</li>' for item in record['non_claims'])
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>M5 IAM</title>
<style>
body{{font-family:system-ui,sans-serif;max-width:40rem;margin:2rem auto;padding:0 1rem;line-height:1.5;color:#1a1a1a;background:#fafafa}}
@media (prefers-color-scheme: dark){{body{{color:#eee;background:#161616}}}}
.card{{border:1px solid #8884;border-radius:10px;padding:1rem 1.25rem;margin:1rem 0}}
dt{{font-size:.8rem;opacity:.7;margin-top:.6rem}}dd{{margin:0;word-break:break-word}}
.tag{{display:inline-block;border:1px solid currentColor;border-radius:999px;padding:.1rem .7rem;font-size:.85rem}}
</style></head><body>
<h1>M5 IAM</h1>
<p><span class="tag">{html.escape(record['status'])}</span>
<span class="tag">Human attested, not verified</span></p>
<div class="card"><dl>
<dt>Name</dt><dd>{name}</dd>
<dt>Account</dt><dd>{html.escape(record['account_sku'])} · free</dd>
<dt>Local identifier</dt><dd>{html.escape(record['local_id'])}</dd>
<dt>TCID</dt><dd>Not issued</dd>
<dt>Created</dt><dd>{html.escape(record['created_at'])}</dd>
</dl></div>
<h2>What this is not</h2><ul>{claims}</ul>
<p>This page was written by <code>m5_iam.py</code> on this computer. It loads nothing from the network.</p>
</body></html>
"""


def registry_receipt(layer, contract_id, now):
    """A simulated TitleChain Registry entry for the IAM origin.

    The commitment is a real SHA-256 over the attestation's parts, so it would
    match the record if it were anchored. Nothing is sent and nothing is
    anchored: the block and reference are derived samples, marked as such.
    """
    parts = [contract_id] + [sha256_bytes((layer / 'attestation' / name).read_bytes())
                             for name in ('human-terms.md', 'human-attestation.json', 'executable-check.json')]
    commitment = sha256_bytes('|'.join(parts).encode('utf-8'))
    return {'schema': SCHEMA, 'registry': 'TitleChain Registry', 'entry_type': 'IAM_ORIGIN',
            'ref_id': 'TCR-IAM-' + commitment[:12].upper(), 'commitment_sha256': commitment,
            'network': 'titlechain (simulated)', 'sample_block': int(commitment[:7], 16),
            'recorded_at': now, 'status': 'SIMULATED_NOT_ANCHORED', 'anchored': False,
            'personal_data_on_chain': 'none', 'synthetic': True, 'authority_effect': 'NONE',
            'network_write': False, 'financial_movement': False,
            'note': 'Sample entry. At launch, only this commitment hash would be anchored to the TitleChain '
                    'Registry. Your name, contact and statement stay on your own device.'}


COMMONS = {
    'publisher': 'TitleChain Foundation',
    'repository': 'https://github.com/TitleChain-Foundation/M5-AI-Sovereign-Commons',
    'software_license': 'Apache-2.0',
    'standard_license': 'CC-BY-4.0',
    'your_records': 'Yours. The licences cover the software and the standard, never your records.',
}
USAGE = {
    'price': 'Free for life',
    'scope': 'Personal. One human, acting for themselves.',
    'transfer': 'Not transferable. A new holder makes their own attestation.',
    'can_authorize': [],
}


def iam_certificate(record, receipt, consent):
    """A sample Certificate of Title for the IAM origin, issued against the simulated registry entry."""
    body = {'schema': SCHEMA, 'certificate': 'Certificate of Title', 'subject': 'IAM origin',
            'title_no': receipt['ref_id'], 'holder': record['display_name'] or 'Holder of this IAM',
            'account': ACCOUNT_SKU, 'state_chain': record.get('chain'), 'attested_at': record['created_at'],
            'identity_status': 'Human attested, not verified',
            'rights': ['Use the free IAM for life', 'Use free and open tools on your own devices',
                       'Export or delete your own records at any time', 'Apply for a registered account when they open'],
            'cyrus_protocol': {'status': consent['cyrus_protocol']['status'],
                               'accepted_at': consent['cyrus_protocol']['accepted_at']},
            'right_to_refuse': {'selected': consent['right_to_refuse']['selected'],
                                'status': consent['right_to_refuse']['status'],
                                'current_choice': 'consent/consent.json'},
            'commons': COMMONS, 'usage': USAGE,
            'shape': 'ISO/IEC 19770-3 entitlement (sample); licences as SPDX identifiers',
            'limits': 'Not a TCID or a verified identity. Cannot authorize a payment, signature, title transfer or agent action.',
            'registry_commitment_sha256': receipt['commitment_sha256'], 'status': 'SAMPLE_NOT_ISSUED',
            'sample': True, 'issued_by': None,
            'note': 'Sample certificate. A Certificate of Title is issued by the TitleChain Registry only after launch.'}
    body['certificate_sha256'] = sha256_bytes(json.dumps(body, sort_keys=True).encode('utf-8'))
    return body


KIT_TERMS = """# Software kit acceptance

I, {name}, holder of IAM account {account}, choose these free tools for my own use:

{lines}

I download each tool from its official source, listed above.

I accept each tool's licence as published by the people who make it. The
licence is granted by them, not by M5 or TitleChain Foundation. The sample
certificates in my pod record each licence; they do not grant it.

M5 tool names are TitleChain Foundation's names for these kits. Each tool
keeps its own name, licence and trademarks, and its makers are not affiliated
with M5.

My records stay mine, in this pod.

Accepted: {now}
"""
KIT_RIGHTS = ['Use it for any purpose', 'Study how it works', 'Change it', 'Share copies']
COPYLEFT = ('GPL', 'AGPL', 'MPL', 'LGPL')


def load_starter_kit():
    """The starter kit listed in iam-catalog.json beside this file."""
    catalog = Path(__file__).resolve().parent / 'iam-catalog.json'
    return json.loads(catalog.read_text(encoding='utf-8'))['starter_kit']


def kit_certificate(record, tool, accepted_at, terms_sha256):
    """A sample Software Licence Certificate of Title for one tool in the holder's kit."""
    components = [{key: part[key] for key in ('name', 'version', 'license', 'source', 'download')}
                  for part in tool['components']]
    seed = json.dumps({'local_id': record['local_id'], 'tool': tool['id'], 'components': components,
                       'accepted_at': accepted_at}, sort_keys=True)
    copyleft = any(part['license'].startswith(COPYLEFT) for part in components)
    body = {'schema': SCHEMA, 'certificate': 'Certificate of Title', 'subject': 'Software licence',
            'title_no': 'SAMPLE-SW-' + sha256_bytes(seed.encode('utf-8'))[:8].upper(),
            'holder': record['display_name'] or 'Holder of this IAM', 'account': ACCOUNT_SKU,
            'm5_tool': tool['m5_name'], 'job': tool['job'], 'powered_by': components,
            'licences': sorted({part['license'] for part in components}), 'kind': 'Open source', 'cost': 'FREE',
            'accepted_at': accepted_at, 'kit_terms_sha256': terms_sha256, 'rights': KIT_RIGHTS,
            'share_alike': copyleft,
            'licence_note': 'The licence is granted by the people who make this software, under its public terms. '
                            'This certificate records it; it does not grant it.',
            'shape': 'ISO/IEC 19770-3 entitlement (sample); licences as SPDX identifiers',
            'registry': 'SIMULATED_NOT_ANCHORED', 'status': 'SAMPLE_NOT_ISSUED', 'sample': True, 'issued_by': None,
            'authority_effect': 'NONE', 'network_write': False, 'financial_movement': False,
            'note': 'Sample certificate. A Certificate of Title is issued by the TitleChain Registry only after launch.'}
    body['certificate_sha256'] = sha256_bytes(json.dumps(body, sort_keys=True).encode('utf-8'))
    return body


def accept_kit(pod, tool_ids, signer, now=None, kit=None):
    """Record the holder's acceptance of their software kit, with a sample certificate for each tool.

    Writes the acceptance words, one sample certificate per tool and a kit record into the pod, each
    entered in the ledger. Downloads nothing and sends nothing: the holder downloads each tool themselves.
    """
    record = load_record(pod)
    if load_consent(pod) is None:
        raise PodError('This pod has no CYRUS Protocol acceptance on record, so it cannot accept a kit.')
    kit = kit or load_starter_kit()
    tools = {tool['id']: tool for tool in kit['tools']}
    wanted = set(tool_ids or [])
    if not wanted:
        raise PodError('Choose at least one tool for your kit.')
    unknown = sorted(wanted - set(tools))
    if unknown:
        raise PodError('Not in the starter kit: ' + ', '.join(unknown))
    signer = ' '.join(str(signer or '').split())[:80]
    if not signer:
        raise PodError('Type your name to sign.')
    now = now or utc_now()
    chosen = [tool for tool in kit['tools'] if tool['id'] in wanted]
    layer = Path(pod).expanduser() / LAYER
    (layer / 'software').mkdir(exist_ok=True)

    lines = '\n'.join(f'- {tool["m5_name"]}: ' + ', '.join(
        f'{part["name"]} {part["version"]} ({part["license"]}), from {part["download"]}' for part in tool['components'])
        for tool in chosen)
    terms = KIT_TERMS.format(name=signer, account=ACCOUNT_SKU, lines=lines, now=now)
    (layer / 'software' / 'kit-terms.md').write_text(terms, encoding='utf-8')
    append_event(layer, 'KIT_TERMS_WRITTEN', now, 'software/kit-terms.md')
    terms_sha256 = sha256_bytes(terms.encode('utf-8'))

    certificates = []
    for tool in chosen:
        certificate = kit_certificate(record, tool, now, terms_sha256)
        name = f'registry/certificate-software-{tool["id"]}.json'
        write_json(layer / name, certificate)
        append_event(layer, 'SOFTWARE_CERTIFICATE_SAMPLE_WRITTEN', now, name)
        certificates.append({'m5_tool': tool['m5_name'], 'title_no': certificate['title_no'], 'file': name,
                             'certificate_sha256': certificate['certificate_sha256']})

    kit_record = {'schema': SCHEMA, 'type': 'software-kit', 'account': ACCOUNT_SKU, 'local_id': record['local_id'],
                  'accepted_at': now, 'versions_checked': kit.get('versions_checked'),
                  'signed_by': signer, 'signature': {'method': 'TYPED_NAME', 'cryptographic': False},
                  'signature_slots': SIGNATURE_SLOTS, 'kit_terms': 'software/kit-terms.md',
                  'kit_terms_sha256': terms_sha256,
                  'tools': [{'id': tool['id'], 'm5_tool': tool['m5_name'], 'job': tool['job'],
                             'components': tool['components'], 'installer_sha256': None}
                            for tool in chosen],
                  'installer_note': 'Record each installer\'s SHA-256 after you download it from its official source.',
                  'certificates': certificates, 'registry': 'SIMULATED_NOT_ANCHORED',
                  'authority_effect': 'NONE', 'network_write': False, 'financial_movement': False}
    write_json(layer / 'software' / 'kit-record.json', kit_record)
    append_event(layer, 'KIT_ACCEPTED', now, 'software/kit-record.json')
    if os.name == 'posix':
        for path in [layer / 'software', *(layer / 'software').iterdir(), *(layer / 'registry').iterdir()]:
            path.chmod(0o700 if path.is_dir() else 0o600)
    return kit_record


def load_kit(pod):
    """The holder's kit record and its certificates, or None if no kit has been accepted."""
    layer = Path(pod).expanduser() / LAYER
    path = layer / 'software' / 'kit-record.json'
    if not path.exists():
        return None
    kit_record = json.loads(path.read_text(encoding='utf-8'))
    certificates = [json.loads((layer / item['file']).read_text(encoding='utf-8'))
                    for item in kit_record['certificates']]
    return {'record': kit_record, 'certificates': certificates}


def refusal_status(selected):
    return 'SELECTED_NOT_ACTIVATED' if selected else 'NOT_SELECTED'


def consent_record(contract_id, accepted_at, selected, now, history):
    return {'schema': SCHEMA, 'type': 'iam-consent', 'contract_id': contract_id,
            'cyrus_protocol': {**CYRUS_PROTOCOL, 'status': 'ACCEPTED', 'accepted_at': accepted_at,
                               'required': True},
            'right_to_refuse': {'selected': selected, 'status': refusal_status(selected), 'activated': False,
                                'activates': REFUSAL_ACTIVATES,
                                'why_not_active': 'An IAM is self-attested. Its credentials are not verified yet.'},
            'decided_at': now, 'history': history,
            'authority_effect': 'NONE', 'network_write': False, 'financial_movement': False}


def init_pod(pod, display_name='', attested=False, now=None, local_id=None, chain='', contact='',
             accept_cyrus=False, select_refusal=False):
    pod = Path(pod).expanduser()
    if not attested:
        raise PodError('The human attestation is required to create an IAM pod. On the command line, add --i-am-human.')
    if accept_cyrus is not True:
        raise PodError('Accepting the CYRUS Protocol is required: it is what protects you. On the command line, add --accept-cyrus.')
    if pod.exists() and any(pod.iterdir()):
        raise PodError(f'{pod} already exists and is not empty. Nothing was changed.')
    now = now or utc_now()
    local_id = local_id or f'local-iam:{uuid.uuid4()}'
    layer = pod / LAYER
    for name in VAULT_NOTE:
        (layer / name).mkdir(parents=True, exist_ok=True)
    (pod / 'm5agent').mkdir(exist_ok=True)

    # Three matching parts, per M5-RICARDIAN-TRIPLE-LAYER-001: human terms, machine record, executable check.
    contract_id = f'iam-human-attestation:{local_id}'
    terms = HUMAN_TERMS.format(name=display_name or 'the holder of this account',
                               chain=chain or 'not chosen', now=now)
    (layer / 'attestation' / 'human-terms.md').write_text(terms, encoding='utf-8')
    check = {'schema': SCHEMA, 'contract_id': contract_id, 'layer': 'executable', 'version': CONTRACT_VERSION,
             'language': 'python', 'entry': 'm5_iam.py verify',
             'code_sha256': sha256_bytes(Path(__file__).read_bytes()),
             'does': 'Recomputes the ledger chain and the digest of every recorded file. Fails closed on any difference.',
             'authority_effect': 'NONE', 'network_write': False, 'financial_movement': False}
    write_json(layer / 'attestation' / 'executable-check.json', check)
    attestation = {'schema': SCHEMA, 'type': 'human-attestation', 'contract_id': contract_id,
                   'layer': 'machine', 'version': CONTRACT_VERSION, 'statement': ATTESTATION_TEXT,
                   'attested_at': now, 'method': 'SELF_ATTESTED_LOCAL', 'verified': False,
                   'chain': {'selected': chain or None, 'status': 'SELF_SELECTED_NOT_VERIFIED'},
                   'human_terms_sha256': sha256_bytes(terms.encode('utf-8')),
                   'executable_check_sha256': sha256_bytes((layer / 'attestation' / 'executable-check.json').read_bytes()),
                   'authority_effect': 'NONE', 'network_write': False, 'financial_movement': False,
                   # Reserved: the holder's signature, and an approving agency's signature over its own claim (via M5-x401).
                   'signatures': [], 'signature_slots': SIGNATURE_SLOTS}
    identifiers = {'schema': SCHEMA, 'local_id': local_id, 'tcid': None, 'payname': None,
                   'ens': None, 'wsw_uri': None,
                   'chain': {'selected': chain or None, 'status': 'SELF_SELECTED_NOT_VERIFIED'},
                   'note': 'Only local_id exists. The other identifiers are issued by registration, not by this tool.'}
    record = {'schema': SCHEMA, 'account_sku': ACCOUNT_SKU, 'legacy_alias': LEGACY_ALIAS,
              'status': STATUS, 'identity_status': IDENTITY_STATUS, 'license_state': LICENSE_STATE,
              'display_name': display_name, 'local_id': local_id, 'tcid': None, 'created_at': now,
              'chain': chain or None, 'chain_status': 'SELF_SELECTED_NOT_VERIFIED',
              'contact': contact or None, 'contract_id': contract_id,
              'price': 'FREE', 'network_required': False, 'can_authorize': [], 'non_claims': NON_CLAIMS,
              'signature_status': 'RESERVED_NOT_SIGNED', 'consent_file': 'consent/consent.json',
              'cyrus_protocol': 'ACCEPTED'}
    write_json(layer / 'attestation' / 'human-attestation.json', attestation)
    write_json(layer / 'identifiers' / 'identifiers.json', identifiers)
    write_json(layer / 'iam.json', record)

    (pod / 'm5readme.md').write_text(
        '# M5 IAM starting pod\n\n'
        f'Status: **{STATUS}** · human attested, not verified · free\n\n'
        f'- `{LAYER}/` holds the IAM record, the attestation and the ledger.\n'
        '- `m5agent/` is for rules and tooling for any agent you choose.\n'
        '- `m5-iam.html` shows the status of this pod. Open it in any browser.\n\n'
        'This folder stays on your computer. Nothing in it is sent anywhere.\n', encoding='utf-8')
    (pod / 'm5agent' / 'm5readme.md').write_text(
        '# m5agent\n\nRules, prompts and configuration for any agent, local or hosted, that you allow '
        'to read this pod.\nEvery agent works under the CYRUS Protocol the holder accepted '
        f'({LAYER}/consent/consent.json). No agent may act for you on the strength of an IAM-only pod.\n', encoding='utf-8')
    (layer / 'm5readme.md').write_text(
        f'# {ACCOUNT_SKU} · IAM · free\n\nStatus: **{STATUS}** · {IDENTITY_STATUS}\n\n'
        + ''.join(f'- `{name}/` — {note}\n' for name, note in VAULT_NOTE.items())
        + '\n## What this is not\n\n' + ''.join(f'- {item}\n' for item in NON_CLAIMS), encoding='utf-8')
    (pod / 'm5-iam.html').write_text(status_page(record), encoding='utf-8')

    append_event(layer, 'POD_CREATED', now)
    append_event(layer, 'HUMAN_TERMS_WRITTEN', now, 'attestation/human-terms.md')
    append_event(layer, 'EXECUTABLE_CHECK_WRITTEN', now, 'attestation/executable-check.json')
    append_event(layer, 'HUMAN_ATTESTED', now, 'attestation/human-attestation.json')
    append_event(layer, 'IDENTIFIERS_WRITTEN', now, 'identifiers/identifiers.json')
    append_event(layer, 'IAM_RECORD_WRITTEN', now, 'iam.json')
    selected = bool(select_refusal)
    consent = consent_record(contract_id, now, selected, now,
                             [{'at': now, 'cyrus_protocol': 'ACCEPTED', 'right_to_refuse': refusal_status(selected)}])
    write_json(layer / 'consent' / 'consent.json', consent)
    append_event(layer, 'CONSENT_RECORDED', now, 'consent/consent.json')
    receipt = registry_receipt(layer, contract_id, now)
    write_json(layer / 'registry' / 'registry-receipt.json', receipt)
    append_event(layer, 'REGISTRY_ENTRY_SIMULATED', now, 'registry/registry-receipt.json')
    write_json(layer / 'registry' / 'certificate-iam-origin.json', iam_certificate(record, receipt, consent))
    append_event(layer, 'CERTIFICATE_SAMPLE_WRITTEN', now, 'registry/certificate-iam-origin.json')
    if os.name == 'posix':
        for path in [pod, *pod.rglob('*')]:
            path.chmod(0o700 if path.is_dir() else 0o600)
    return record


def load_consent(pod):
    path = Path(pod).expanduser() / LAYER / 'consent' / 'consent.json'
    consent = json.loads(path.read_text(encoding='utf-8')) if path.exists() else None
    # Pods made before the CYRUS Protocol step have no acceptance on record.
    return consent if consent and 'cyrus_protocol' in consent else None


def set_refusal(pod, selected, now=None):
    """Select or unselect the right to refuse consent. It stays not activated until credentials are verified."""
    record = load_record(pod)
    current = load_consent(pod)
    if current is None:
        raise PodError('This pod has no consent record. It was created before the CYRUS Protocol step existed.')
    now = now or utc_now()
    selected = bool(selected)
    layer = Path(pod).expanduser() / LAYER
    path = layer / 'consent' / 'consent.json'
    history = current['history'] + [{'at': now, 'cyrus_protocol': 'ACCEPTED', 'right_to_refuse': refusal_status(selected)}]
    write_json(path, consent_record(record['contract_id'], current['cyrus_protocol']['accepted_at'], selected, now, history))
    append_event(layer, 'REFUSAL_SELECTED' if selected else 'REFUSAL_UNSELECTED', now, 'consent/consent.json')
    if os.name == 'posix':
        path.chmod(0o600)
    return load_consent(pod)


def load_record(pod):
    path = Path(pod).expanduser() / LAYER / 'iam.json'
    if not path.exists():
        raise PodError(f'No IAM pod found at {Path(pod).expanduser()}. Create one with: m5_iam.py init')
    return json.loads(path.read_text(encoding='utf-8'))


def verify_pod(pod):
    layer = Path(pod).expanduser() / LAYER
    load_record(pod)
    problems, prev, latest = [], GENESIS, {}
    events = read_events(layer)
    if not events:
        problems.append('ledger is empty')
    for index, event in enumerate(events, start=1):
        if event.get('seq') != index:
            problems.append(f'event {index}: sequence broken')
        if event.get('prev') != prev:
            problems.append(f'event {index}: chain broken')
        if event_hash(event) != event.get('hash'):
            problems.append(f'event {index}: record altered')
        prev = event.get('hash')
        if event.get('path'):
            latest[event['path']] = event['sha256']
    for name, digest in sorted(latest.items()):
        target = layer / name
        if not target.exists():
            problems.append(f'{name}: missing')
        elif sha256_bytes(target.read_bytes()) != digest:
            problems.append(f'{name}: changed since it was recorded')
    return {'status': 'FAIL' if problems else 'PASS', 'events': len(events),
            'files_checked': len(latest), 'problems': problems}


def export_pod(pod, output):
    pod = Path(pod).expanduser()
    load_record(pod)
    output = Path(output).expanduser()
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(pod.rglob('*')):
            if path.is_file():
                archive.write(path, f'{pod.name}/{path.relative_to(pod).as_posix()}')
    return output


def main(argv=None):
    parser = argparse.ArgumentParser(description='Free, local M5 IAM starting pod. No network calls.')
    commands = parser.add_subparsers(dest='command', required=True)
    for name, text in [('init', 'create a new local IAM pod'), ('status', 'show the IAM record'),
                       ('verify', 'check the ledger and recorded files'), ('export', 'copy the pod into one ZIP you keep'),
                       ('consent', 'select or unselect your right to refuse consent'),
                       ('kit', 'sign and accept your free starter kit')]:
        command = commands.add_parser(name, help=text)
        command.add_argument('--pod', default='~/M5POD-IAM', help='pod folder (default: ~/M5POD-IAM)')
        if name == 'init':
            command.add_argument('--name', default='', help='a display name of your choosing (optional)')
            command.add_argument('--i-am-human', action='store_true', help='make the human attestation')
            command.add_argument('--chain', default='', help='your state chain, your own choice (optional)')
        if name == 'init':
            command.add_argument('--accept-cyrus', action='store_true',
                                 help='accept the CYRUS Protocol, which protects you (required)')
            command.add_argument('--select-refusal', action='store_true',
                                 help='select your right to refuse consent (activates when your credentials are verified)')
        if name == 'consent':
            command.add_argument('--right-to-refuse', choices=['select', 'unselect'], required=True)
        if name == 'export':
            command.add_argument('--output', required=True, help='ZIP file to write')
        if name == 'kit':
            command.add_argument('--tools', required=True,
                                 help='comma-separated tool ids from the starter kit, e.g. ai-agent,office')
            command.add_argument('--name', required=True, help='your name, as your signature')
    args = parser.parse_args(argv)
    try:
        if args.command == 'init':
            record = init_pod(args.pod, args.name, args.i_am_human, chain=args.chain,
                              accept_cyrus=args.accept_cyrus, select_refusal=args.select_refusal)
            print(json.dumps({'created': str(Path(args.pod).expanduser()), 'status': record['status'],
                              'identity_status': record['identity_status'], 'local_id': record['local_id'],
                              'open': str(Path(args.pod).expanduser() / 'm5-iam.html')}, indent=2))
        elif args.command == 'status':
            print(json.dumps(load_record(args.pod), indent=2, ensure_ascii=False))
        elif args.command == 'consent':
            consent = set_refusal(args.pod, args.right_to_refuse == 'select')
            print(json.dumps({'cyrus_protocol': consent['cyrus_protocol']['status'],
                              'right_to_refuse': consent['right_to_refuse']['status']}, indent=2))
        elif args.command == 'kit':
            kit_record = accept_kit(args.pod, [t.strip() for t in args.tools.split(',') if t.strip()], args.name)
            print(json.dumps({'accepted': [c['m5_tool'] for c in kit_record['certificates']],
                              'certificates': [c['title_no'] for c in kit_record['certificates']],
                              'registry': kit_record['registry']}, indent=2))
        elif args.command == 'verify':
            result = verify_pod(args.pod)
            print(json.dumps(result, indent=2))
            return 0 if result['status'] == 'PASS' else 1
        else:
            print(json.dumps({'exported': str(export_pod(args.pod, args.output))}, indent=2))
    except PodError as error:
        print(str(error), file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
