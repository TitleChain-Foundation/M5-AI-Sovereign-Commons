"""Foundation record rendered alongside, but separate from, official feed data."""
from datetime import date
from html import escape
import json
from pathlib import Path
import shutil
from urllib.parse import urlparse

BASE = Path(__file__).resolve().parent
SEC = BASE.parent
TITLE = 'SEC Modernization | Transfer Agents, Crypto Custody & Digital Authority | TitleChain Foundation'
DESCRIPTION = "TitleChain Foundation's public record and analysis of SEC Files S7-2026-30 and S7-2026-35 covering transfer agents, digital securities, crypto custody, cryptographic control and legal authority."


def date_label(value):
    day = date.fromisoformat(value)
    return f"{ {9: 'Sept.', 10: 'Oct.'}.get(day.month, day.strftime('%b.'))} {day.day}, {day.year}"


def load_record():
    record = json.loads((BASE / 'foundation-record.json').read_text())
    for filing in record['filings']:
        if filing['secPosted'] and not filing['secUrl']:
            raise ValueError('Posted filing requires an official SEC comment URL')
        if not filing['secPosted'] and filing['secUrl']:
            raise ValueError('Pending filing must not have a SEC comment URL')
        if filing['secUrl'] and (urlparse(filing['secUrl']).hostname != 'www.sec.gov' or not urlparse(filing['secUrl']).path.startswith('/comments/')):
            raise ValueError('Filing URL must point directly to an official SEC comment')
        for key in ('localPdf', 'additionalPdf'):
            if filing.get(key):
                path = (SEC / filing[key]).resolve()
                if not path.is_relative_to(SEC) or path.suffix != '.pdf' or not path.is_file():
                    raise ValueError('Foundation PDF must exist within sec-public-input')
    return record


def filing_status(filing):
    return 'Posted on SEC.gov' if filing['secPosted'] else f"Submitted {date_label(filing['submitted'])} — SEC posting pending"


def link(url, label):
    return f'<a href="{escape(url, quote=True)}">{escape(label)}</a>'


def render_record(record=None):
    record = record or load_record()
    cards = []
    events = []
    for proceeding in record['proceedings']:
        sources = ' · '.join(link(proceeding[key], label) for key, label in [('ruleUrl', 'SEC rulemaking source'), ('commentsUrl', 'SEC received comments'), ('pressUrl', 'SEC press release')])
        submissions = []
        events.append((proceeding['date'], f"SEC proposes {proceeding['title']} — {proceeding['id']}", proceeding['summary'], 'Proposed rule'))
        for filing in record['filings']:
            if filing['docket'] != proceeding['id']:
                continue
            links = []
            if filing['localPdf']:
                links.append(link(filing['localPdf'], 'Read Foundation copy' if filing['secPosted'] else 'Read submitted comment'))
            if filing.get('additionalPdf'):
                links.append(link(filing['additionalPdf'], 'Read Technical Exhibits A–J'))
            if filing['secPosted']:
                links.append(link(filing['secUrl'], 'View on SEC.gov'))
            submissions.append(f"<article><h4>{escape(filing['title'])}</h4><p>Submitted {date_label(filing['submitted'])}</p><p class='filing-status'><strong>{escape(filing_status(filing))}</strong></p><p>{escape(filing['focus'])}</p><p>{' · '.join(links)}</p></article>")
            events.append((filing['submitted'], f"TitleChain Foundation {'files' if filing['secPosted'] else 'submits'} {filing['title']} — {filing['docket']}", filing['focus'], filing_status(filing)))
        cards.append(f"<section><p class='eyebrow'>SEC proposal</p><h3>{escape(proceeding['title'])}</h3><dl><dt>SEC file</dt><dd>{proceeding['id']}</dd><dt>Release</dt><dd>{escape('; '.join(proceeding['releases']))}</dd><dt>Proposal date</dt><dd>{date_label(proceeding['date'])}</dd><dt>Status</dt><dd>{proceeding['status']}</dd><dt>Comment deadline</dt><dd>{escape(proceeding['deadline'])}</dd></dl><p>{escape(proceeding['summary'])}</p><p>{sources}</p><h3>TitleChain Foundation submissions</h3>{''.join(submissions)}</section>")
    timeline = ''.join(f'<li><time datetime="{day}">{date_label(day)}</time><h3>{escape(title)}</h3><p>{escape(focus)}</p><p><strong>{escape(status)}</strong></p></li>' for day, title, focus, status in sorted(events, key=lambda event: event[0]))
    distinctions = [('Control', 'Who can technically move the asset.'), ('Custody', 'Who safeguards the asset or relevant key material.'), ('Authority', 'Who has the legal right to direct an action.'), ('Ownership', 'Who holds the legally recognized interest.'), ('Registration', 'Who is reflected in the official securityholder record.'), ('Execution', 'What person, system or machine carries out the instruction.'), ('Evidence', 'What proves the authority, transaction and resulting ownership state.')]
    return f"""
<header id="foundation-record">
<p class="eyebrow">TitleChain Foundation · Public regulatory record</p>
<h1>SEC Modernization: Ownership, Transfer, Custody and Digital Authority</h1>
<p>The SEC is now considering two related pieces of market infrastructure at the same time: how securities ownership and transfers are recorded, and how crypto assets are held.</p>
<p>TitleChain Foundation has submitted comments in both proceedings because the same question now runs through each:</p>
<p><strong>Who has custody, who has control, who has authority, and which record establishes legally recognized ownership?</strong></p>
<p>A wallet can identify an address. A private key can make a transaction technically possible. Neither, standing alone, establishes that the person or machine using it has the legal right to transfer the asset.</p>
<p>The Foundation's work focuses on the evidence connecting those layers while preserving the responsibilities of issuers, transfer agents, custodians, advisers and other regulated entities.</p>
<p>Last verified: {date_label(record['lastVerified'])}. Publication of a comment does not imply SEC endorsement, acceptance, review or approval.</p>
<nav aria-label="SEC section"><a href="#proceedings">Proceedings and filings</a> · <a href="#timeline">Timeline</a> · <a href="#assessment">Foundation assessment</a> · <a href="#official-observatory">Live transfer-agent observatory</a></nav>
</header>
<div id="proceedings" class="proceeding-grid">{''.join(cards)}</div>
<section id="timeline"><h2>Regulatory timeline</h2><p>The Oct. 3 filings extend the original record; they do not supersede the Sept. 5 comment. The existing Sept. 23 submission is also retained.</p><ol class="timeline">{timeline}</ol></section>
<section id="assessment"><p class="eyebrow">Foundation assessment</p><h2>What changed after our first filing?</h2>
<p>When TitleChain Foundation filed its original transfer-agent comment on Sept. 5, the Commission was considering how a decades-old transfer-agent framework should operate in an electronic and blockchain-enabled market. On Oct. 1, the SEC opened a second proceeding addressing custody of crypto assets.</p>
<p>That matters because custody introduces another layer of control into the transaction. The custodian may hold the key. The adviser may have authority to act for the client. The transfer agent may maintain the securityholder record. The blockchain may record the transaction. A software agent may execute it. Those facts can all be true at the same time.</p>
<p>The regulatory system therefore needs a way to establish not merely that a transaction occurred, but <strong>who had authority to cause it and what legally recognized ownership state resulted.</strong></p>
<blockquote><strong>A private key establishes an ability to act; it does not, standing alone, establish the legal right to act.</strong></blockquote>
<blockquote><strong>Custody should protect the asset. It should not become the source of legal authority over the asset.</strong></blockquote>
<p>The Foundation supports open, interoperable, implementation-neutral infrastructure. A transfer agent's authoritative securityholder record remains relevant to digital securities. Custody and transaction systems should exchange verifiable evidence while preserving each regulated entity's responsibility for its legally authoritative records.</p>
<h2>The distinctions that matter</h2><dl>{''.join(f'<dt>{term}</dt><dd>{definition}</dd>' for term, definition in distinctions)}</dl>
<p><strong>Digitizing a security should make these relationships more verifiable, not erase them.</strong></p>
<h2>What does “adviser self-custody” mean here?</h2>
<p>In the SEC proposal, adviser self-custody refers to a limited circumstance in which the <strong>investment adviser itself safeguards client crypto assets or associated key material</strong> rather than relying on an outside permitted custodian. It is proposed as a regulated fallback subject to conditions and controls.</p>
<p>It does not mean that possession of a private key creates ownership. It also does not mean that ordinary investor self-custody is being defined as investment-adviser custody.</p>
<h2>Uncertificated security</h2><p>A security that is not represented by a physical paper certificate. Ownership is instead reflected in the issuer's or transfer agent's official records. The custody proceeding raises questions involving transfer agents and uncertificated digital securities.</p>
<h2>Software and AI agents</h2><p>As software becomes capable of initiating and executing financial transactions, technical access should not become a substitute for legal authority. A machine may execute an authorized instruction. It should not create the authority on which that instruction depends.</p>
<p>Authority should originate with an accountable human or legal entity and be capable of being:</p><ul><li>scoped;</li><li>audited;</li><li>expired;</li><li>revoked; and</li><li>tied to a defined role or capacity.</li></ul>
<p>This is consistent with the Foundation's existing human-principal architecture.</p>
<p><strong>The SEC is now modernizing both sides of the digital securities equation: who owns and transfers the asset, and who is permitted to hold the keys. The unresolved bridge is authority.</strong></p></section>
"""


def copy_public_pdfs(output):
    for filing in load_record()['filings']:
        for key in ('localPdf', 'additionalPdf'):
            if filing.get(key):
                destination = output / filing[key]
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(SEC / filing[key], destination)
