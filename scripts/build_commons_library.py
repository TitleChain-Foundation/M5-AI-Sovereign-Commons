"""Build selected Commons Markdown into the existing Pages artifact, offline."""
import argparse
from collections import Counter
import hashlib
from html import escape
from html.parser import HTMLParser
import json
import posixpath
from pathlib import Path
import re
import subprocess
from urllib.parse import quote, unquote, urlsplit

from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]
REPO = 'https://github.com/TitleChain-Foundation/M5-AI-Sovereign-Commons'


def slug(text):
    return re.sub(r'[^\w\- ]', '', text.lower()).replace(' ', '-')


def tracked(root):
    return set(subprocess.check_output(['git', 'ls-files', '-z'], cwd=root).decode().strip('\0').split('\0'))


def safe_source(root, path, files):
    p = Path(path)
    if p.is_absolute() or any(x in ('', '.', '..') or x.startswith('.') for x in p.parts):
        raise ValueError('Unsafe source path: ' + path)
    target = (root / p).resolve()
    if not target.is_relative_to(root.resolve()) or path not in files or not target.is_file():
        raise ValueError('Not an existing tracked source: ' + path)
    return target


class SmallHTML(HTMLParser):
    """Only inert GitHub disclosure markup; no source attributes survive."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
    def handle_starttag(self, tag, attrs):
        self.parts.append('<' + tag + '>' if tag in ('details', 'summary', 'br') else escape(self.get_starttag_text()))
    def handle_endtag(self, tag):
        self.parts.append('</' + tag + '>' if tag in ('details', 'summary') else escape('</' + tag + '>'))
    def handle_data(self, data):
        self.parts.append(escape(data))
    def handle_comment(self, data):
        self.parts.append(escape('<!--' + data + '-->'))
    def handle_decl(self, data):
        self.parts.append(escape('<!' + data + '>'))


def safe_html(text):
    parser = SmallHTML()
    parser.feed(text)
    parser.close()
    return ''.join(parser.parts)


def markdown():
    md = MarkdownIt('js-default', {'html': True, 'typographer': False}).enable('table')
    def html_rule(tokens, idx, options, env):
        return safe_html(tokens[idx].content)
    md.renderer.rules['html_block'] = html_rule
    md.renderer.rules['html_inline'] = html_rule
    return md


def parsed(md, text):
    tokens = md.parse(text)
    headings = set()
    counts = Counter()
    title = None
    for i, token in enumerate(tokens):
        if token.type == 'heading_open':
            content = tokens[i+1]
            plain = ''.join(c.content for c in content.children or [] if c.type in ('text', 'code_inline', 'image'))
            base = slug(plain)
            n = counts[base]
            counts[base] += 1
            ident = base + ('-' + str(n) if n else '')
            token.attrSet('id', 'doc-' + ident)
            headings.add(ident)
            title = title or plain
    return tokens, headings, title or 'Source document'


# Editorial discovery metadata only; classifications do not grant canonical status.
LIBRARY_TOPICS = [
    ('orientation', 'Start here', 'The overview, language and participation essentials.'),
    ('identity', 'Identity & workspaces', 'Free M5-IAM, consent, portability and member environments.'),
    ('standards', 'Standards & building', 'Proposed standards, schemas, providers and reference code.'),
    ('projects', 'Projects & pilots', 'Public project briefs, control packs and disclosed simulations.'),
    ('research', 'Research & indices', 'SHADOW research, methodologies, public data and reports.'),
    ('regulatory', 'SEC & public input', 'Submissions, exhibits, regulatory crosswalks and monitoring.'),
    ('governance', 'Governance & evidence', 'Rights, licensing, security, authority and review records.'),
]


def discovery_metadata(source, title, text):
    path = source.lower()
    if source in ('README.md', 'GLOSSARY.md', 'CONTRIBUTING.md', 'CODE_OF_CONDUCT.md', 'docs/README.md'):
        topic = 'orientation'
    elif path.startswith('sec-public-input/') or 'pilot-sec-rfi' in path:
        topic = 'regulatory'
    elif path.startswith('shadow-m5index/') or '/shadow-m5index-' in path:
        topic = 'research'
    elif path.startswith('pilots/') or 'project-control' in path or 'peoples-trust-public-pilot' in path:
        topic = 'projects'
    elif any(x in path for x in ('m5-iam', 'm5iam', 'm5-pod/', 'm5-eve/', 'activation/', 'consent', 'refusal', 'portability', 'workspace', 'm5pod', 'm5bom-activation', 'm5-eve-')):
        topic = 'identity'
    elif any(x in path for x in ('governance', 'legal', 'license', 'patent', 'trademark', 'security', 'threat', 'authority', 'validation', 'evidence', 'canonical', 'conformance', 'namespace', 'crosswalk', 'release-status')):
        topic = 'governance'
    else:
        topic = 'standards'
    if '/simulations/' in path:
        kind = 'Simulation'
    elif path.startswith('standards/') and source != 'standards/README.md':
        kind = 'Proposed standard'
    elif '/update-notes/' in path or '/reports/' in path or re.search(r'20\d\d-\d\d-\d\d', path):
        kind = 'Dated review / record'
    elif path.startswith('reference-implementation/') or '/reference/' in path:
        kind = 'Reference implementation'
    elif path.startswith('pilots/'):
        kind = 'Project document'
    else:
        kind = 'Guide / source'
    # Remove front matter for discovery excerpts, without changing reader/source text.
    prose = re.sub(r'\A---\s*\n.*?\n---\s*\n', '', text, count=1, flags=re.S)
    paragraphs = re.split(r'\n\s*\n', prose)
    summary = ''
    for paragraph in paragraphs:
        if paragraph.lstrip().startswith(('#', '```', '|', '<', '![', '---', '- ', '* ')):
            continue
        plain = re.sub(r'!?\[([^\]]*)\]\([^)]*\)', r'\1', paragraph)
        plain = re.sub(r'<[^>]*>', '', plain)
        plain = re.sub(r'[*`_]', '', plain)
        plain = ' '.join(plain.split())
        if len(plain) >= 45 and not plain.startswith(('Status:', 'Version:', 'Date:', '©')):
            summary = plain[:177].rsplit(' ', 1)[0] + '…' if len(plain) > 180 else plain
            break
    if not summary:
        summary = dict((k, description) for k, _, description in LIBRARY_TOPICS)[topic]
    display_title = title
    if 'PPT-EZ-CA-0001-THE-BEAR-COMES-HOME' in source:
        display_title = 'The Bear Comes Home — Public Bank of California concept'
    elif len(title) > 160:
        display_title = Path(source).stem.replace('-', ' ').replace('_', ' ')
    return {'topic': topic, 'document_kind': kind, 'display_title': display_title, 'summary': summary}


def library_index(entries, rendered_count):
    counts = Counter(e['topic'] for e in entries)
    links = {e['source_path']: posixpath.relpath(e['route'], 'library') if e['route'] else e['source_url'] for e in entries}
    def entry_link(path, label):
        return '<a href="'+escape(links[path], quote=True)+'">'+escape(label)+' <span aria-hidden="true">↗</span></a>' if path in links else ''
    journeys = [
        ('01', 'Understand the Commons', 'Begin with the overview and shared vocabulary.', [('README.md', 'Commons overview'), ('GLOSSARY.md', 'Glossary')]),
        ('02', 'Build with the standards', 'Follow the specifications into reference implementations.', [('standards/README.md', 'Proposed standards'), ('reference-implementation/README.md', 'Reference code')]),
        ('03', 'Explore public projects', 'Read project scopes, evidence and disclosed simulations.', [('pilots/README.md', 'Public pilots'), ('shadow-m5index/README.md', 'SHADOW research')]),
        ('04', 'Review the evidence', 'Check release status, rights and security boundaries.', [('RELEASE-STATUS.md', 'Release status'), ('THREAT-MODEL.md', 'Threat model')]),
    ]
    journey_html = ''.join('<section class="library-journey"><span class="journey-number">'+n+'</span><h3>'+title+'</h3><p>'+description+'</p><div>'+''.join(entry_link(p, label) for p, label in paths)+'</div></section>' for n, title, description, paths in journeys)
    topics = '<a class="topic-link is-active" href="#documents" data-library-topic="all" aria-current="true"><span>All topics</span><span>'+str(len(entries))+'</span></a>'
    topics += ''.join('<a class="topic-link" href="#documents" data-library-topic="'+key+'"><span>'+label+'</span><span>'+str(counts[key])+'</span></a>' for key, label, _ in LIBRARY_TOPICS)
    cards = []
    for e in entries:
        href = links[e['source_path']]
        label = 'Read on Commons' if e['route'] else 'Open GitHub source'
        source_class = 'reader' if e['route'] else 'source'
        searchable = ' '.join([e['display_title'], e['source_path'], e['summary'], e['document_kind'], dict((k, n) for k, n, _ in LIBRARY_TOPICS)[e['topic']]])
        cards.append('<li class="library-card" data-topic="'+e['topic']+'" data-format="'+source_class+'" data-search="'+escape(searchable, quote=True)+'"><div class="card-meta"><span>'+escape(e['document_kind'])+'</span><span class="format-label '+source_class+'">'+('Read here' if e['route'] else 'GitHub')+'</span></div><h3><a href="'+escape(href, quote=True)+'">'+escape(e['display_title'])+'</a></h3><p>'+escape(e['summary'])+'</p><details class="card-source"><summary>Source details</summary><code>'+escape(e['source_path'])+'</code></details><a class="card-action" href="'+escape(href, quote=True)+'">'+label+' <span aria-hidden="true">↗</span></a></li>')
    return '''<section class="library-hero"><div><p class="library-kicker">Explore · understand · build</p><h1>Commons knowledge library</h1><p class="hero-description">Find the right starting point. Follow a topic, explore a project or go straight to the source.</p><a class="hero-action" href="#documents">Explore the library <span aria-hidden="true">↓</span></a></div><div class="library-stat"><strong>'''+str(rendered_count)+'''</strong><span>documents to read here</span><div>'''+str(len(entries)-rendered_count)+''' more source documents on GitHub</div></div></section>
<section class="journeys" aria-labelledby="journey-heading"><div class="section-label"><h2 id="journey-heading">What brings you here?</h2><span>Four ways into the collection</span></div><div class="journey-grid">'''+journey_html+'''</div></section>
<section class="library-explorer" id="documents" aria-labelledby="explorer-heading"><aside><h2 id="explorer-heading">Browse by topic</h2><nav class="topic-list" aria-label="Library topics">'''+topics+'''</nav><div class="library-note"><strong>A guide to the sources</strong><p>Topic and document-type labels help you navigate. They do not establish approval, deployment or canonical authority. Check each source’s own status and version.</p></div></aside><div class="library-results"><div class="library-toolbar" data-library-controls hidden><label for="library-query">Search the collection</label><input id="library-query" type="search" placeholder="Try consent, free IAM, Spring Commons…" autocomplete="off"><div class="filter-row"><label>Open in<select id="library-format"><option value="all">All locations</option><option value="reader">Read on Commons</option><option value="source">GitHub source</option></select></label><label>Sort by<select id="library-sort"><option value="recommended">Starting points first</option><option value="az">Title A–Z</option></select></label><button id="library-clear" type="button">Clear filters</button></div></div><div class="results-heading"><h2 id="library-topic-heading">All documents</h2><p id="library-count" role="status" aria-live="polite">'''+str(len(entries))+''' documents</p></div><p class="search-hint" data-library-controls hidden>Search titles, descriptions and source paths. Results come from this repository’s public collection.</p><ul class="library-grid" id="library-results">'''+''.join(cards)+'''</ul><div id="library-empty" class="library-empty" hidden><h3>No documents match yet.</h3><p>Try a shorter phrase or clear the topic and location filters.</p><button type="button" data-library-reset>Show all documents</button></div><button id="library-more" type="button" hidden>Show more documents</button><noscript><p>The complete directory is shown below the starting points. Use your browser’s Find command to search it.</p></noscript></div></section>'''


def page(title, body, prefix, provenance='', directory=False):
    navigation_version=json.loads((ROOT/'site/assets/navigation/manifest.json').read_text())['bundle_sha256'][:12]
    directory_assets = f'<link rel="stylesheet" href="{prefix}assets/library-index.css"><script src="{prefix}assets/library-index.js" defer></script>' if directory else ''
    body_class = ' class="library-directory"' if directory else ''
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'self'; img-src 'self' https:; script-src 'self'; connect-src 'self'; base-uri 'none'; form-action 'none'">
<title>{escape(title)} · Commons documentation</title>{directory_assets}<link rel="stylesheet" href="{prefix}assets/library.css"><link rel="stylesheet" href="{prefix}assets/navigation/navigation.css?v={navigation_version}"><script src="{prefix}assets/navigation/navigation.js?v={navigation_version}" data-m5-site="commons" defer></script></head>
<body{body_class}><header><nav aria-label="Documentation"><a href="{prefix}index.html">TitleChain Foundation · Commons</a><a href="{prefix}library/index.html">Documentation</a><a href="{REPO}">GitHub source</a></nav></header>
<main><p class="eyebrow">Commons documentation · source edition</p>{provenance}<article>{body}</article></main>
<script src="{prefix}assets/library-reader.js" defer></script></body></html>'''


def build(root, output, manifest_path=None):
    root, output = Path(root).resolve(), Path(output).resolve()
    if output == root or root.is_relative_to(output):
        raise ValueError('Output must be a separate artifact directory')
    config = json.loads((manifest_path or root/'site/content-map.json').read_text())
    if config.get('schema_version') != 1:
        raise ValueError('Unsupported manifest schema')
    files = tracked(root)
    commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip()
    selected = config['selected_sources']
    if len(selected) != len(set(selected)):
        raise ValueError('Duplicate selected source')
    for source in selected:
        if not source.endswith('.md'):
            raise ValueError('Only Markdown sources may be rendered')
        safe_source(root, source, files)
    aliases = config.get('aliases', {})
    for alias, target in aliases.items():
        if not alias.endswith('.md') or target not in selected or alias.startswith('/') or '..' in Path(alias).parts:
            raise ValueError('Unsafe or unresolved alias')
    all_md = sorted(p for p in files if p.endswith('.md'))
    md = markdown()
    documents = {}
    for source in selected:
        text = safe_source(root, source, files).read_text()
        tokens, anchors, title = parsed(md, text)
        documents[source] = {'tokens': tokens, 'anchors': anchors, 'title': title, 'sha256': hashlib.sha256((root/source).read_bytes()).hexdigest(), 'route': 'library/'+source[:-3]+'.html'}
    missing = set()
    assets = {}
    def source_link(path, fragment='', directory=False):
        return REPO + ('/tree/' if directory else '/blob/') + commit + '/' + quote(path, safe='/') + ('#'+quote(fragment, safe='-') if fragment else '')
    def resolve(value, current, image=False):
        url = urlsplit(value)
        if url.scheme or url.netloc:
            if url.scheme not in ('https', 'http', 'mailto') or (image and url.scheme not in ('https', 'http')):
                return None
            return value
        if url.query:
            return source_link(posixpath.normpath(posixpath.join(posixpath.dirname(current), unquote(url.path))))
        fragment = unquote(url.fragment)
        if not url.path:
            if fragment and fragment not in documents[current]['anchors']:
                missing.add(current+'#'+fragment)
                return source_link(current, fragment)
            return '#doc-'+quote(fragment, safe='-') if fragment else '#'
        path = posixpath.normpath(posixpath.join(posixpath.dirname(current), unquote(url.path)))
        if path.startswith(('../', '/')) or path in ('..', '.'):
            return REPO if path=='.' else None
        path = aliases.get(path, path)
        if path not in files:
            if any(f.startswith(path.rstrip('/')+'/') for f in files):
                return source_link(path, fragment, True)
            missing.add(current+' -> '+path)
            return source_link(path, fragment)
        if image:
            safe_source(root, path, files)
            if Path(path).suffix.lower() not in ('.svg', '.png', '.jpg', '.jpeg', '.webp', '.gif'):
                return None
            data = (root/path).read_bytes()
            if len(data)>10_000_000:
                raise ValueError('Image too large: '+path)
            assets[path] = data
            return posixpath.relpath('library/media/'+path, posixpath.dirname(documents[current]['route']))
        if path in documents:
            if fragment and fragment not in documents[path]['anchors']:
                missing.add(current+' -> '+path+'#'+fragment)
                return source_link(path, fragment)
            return posixpath.relpath(documents[path]['route'], posixpath.dirname(documents[current]['route'])) + ('#doc-'+quote(fragment, safe='-') if fragment else '')
        return source_link(path, fragment)
    for source, doc in documents.items():
        def visit(tokens):
            for token in tokens:
                attr = 'src' if token.type=='image' else 'href' if token.type=='link_open' else None
                if attr:
                    value = resolve(token.attrGet(attr) or '', source, token.type=='image')
                    token.attrSet(attr, value or '#')
                    if token.type=='link_open':
                        token.attrSet('rel', 'noopener noreferrer')
                if token.children:
                    visit(token.children)
        visit(doc['tokens'])
        body = md.renderer.render(doc['tokens'], md.options, {})
        prefix = '../' * len(Path(doc['route']).parent.parts)
        source_url = source_link(source)
        provenance = '<details class="provenance"><summary>Source and version</summary><p>Source: <a href="'+escape(source_url, quote=True)+'">'+escape(source)+'</a></p><p>Build commit <code>'+commit+'</code> · SHA-256 <code>'+doc['sha256']+'</code></p><p>Document status and limitations remain as written below. Website rendering grants no approval, credential or certification.</p></details>'
        dest=output/doc['route'];dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(page(doc['title'], body, prefix, provenance))
    entries=[]
    for source in all_md:
        doc=documents.get(source)
        text=(root/source).read_text()
        title=doc['title'] if doc else next((line.lstrip('# ').strip() for line in text.splitlines() if line.startswith('# ')),source)
        entries.append({'source_path':source,'title':title,'disposition':'on_domain_reader' if doc else 'github_source','route':doc['route'] if doc else None,'anchors':sorted(doc['anchors']) if doc else [],'source_url':source_link(source),'sha256':hashlib.sha256((root/source).read_bytes()).hexdigest(), **discovery_metadata(source, title, text)})
    catalog={'schema_version':1,'source_commit':commit,'rendered_count':len(documents),'entries':entries,'aliases':aliases,'source_reference_warnings':sorted(missing)}
    dest=output/'library';dest.mkdir(parents=True,exist_ok=True)
    (dest/'source-map.json').write_text(json.dumps(catalog,indent=2)+'\n')
    (dest/'index.html').write_text(page('Knowledge library', library_index(entries, len(documents)), '../', directory=True))
    for source,data in assets.items():
        dest=output/'library/media'/source;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
    return catalog


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    result=build(ROOT,args.output)
    print(json.dumps({k:result[k] for k in ('source_commit','rendered_count','source_reference_warnings')},indent=2))
    if result['source_reference_warnings']:
        raise SystemExit('Source references need correction before publication')
