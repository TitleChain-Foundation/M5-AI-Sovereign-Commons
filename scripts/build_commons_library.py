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


def page(title, body, prefix, provenance=''):
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'self'; img-src 'self' https:; script-src 'self'; connect-src 'self'; base-uri 'none'; form-action 'none'">
<title>{escape(title)} · Commons documentation</title><link rel="stylesheet" href="{prefix}assets/library.css"></head>
<body><header><nav aria-label="Documentation"><a href="{prefix}index.html">TitleChain Foundation · Commons</a><a href="{prefix}library/index.html">Documentation</a><a href="{REPO}">GitHub source</a></nav></header>
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
        entries.append({'source_path':source,'title':title,'disposition':'on_domain_reader' if doc else 'github_source','route':doc['route'] if doc else None,'anchors':sorted(doc['anchors']) if doc else [],'source_url':source_link(source),'sha256':hashlib.sha256((root/source).read_bytes()).hexdigest()})
    catalog={'schema_version':1,'source_commit':commit,'rendered_count':len(documents),'entries':entries,'aliases':aliases,'source_reference_warnings':sorted(missing)}
    dest=output/'library';dest.mkdir(parents=True,exist_ok=True)
    (dest/'source-map.json').write_text(json.dumps(catalog,indent=2)+'\n')
    groups=[]
    for kind,label in [('on_domain_reader','Read on the Commons'),('github_source','Additional GitHub source documents')]:
        links=[]
        for item in entries:
            if item['disposition']==kind:
                href=posixpath.relpath(item['route'],'library') if item['route'] else item['source_url']
                links.append('<li><a href="'+escape(href,quote=True)+'">'+escape(item['title'])+'</a><small>'+escape(item['source_path'])+'</small></li>')
        groups.append('<section><h2>'+label+'</h2><ul class="catalog">'+''.join(links)+'</ul></section>')
    intro=f'<h1>Commons documentation</h1><p>Read the standards, project guides and public research linked from the Commons. {len(documents)} selected documents open here; other source documents remain available on GitHub. Status labels and limitations remain part of each source.</p>'
    (dest/'index.html').write_text(page('Commons documentation',intro+''.join(groups),'../'))
    for source,data in assets.items():
        dest=output/'library/media'/source;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
    return catalog


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    result=build(ROOT,args.output)
    print(json.dumps({k:result[k] for k in ('source_commit','rendered_count','source_reference_warnings')},indent=2))
    if result['source_reference_warnings']:
        raise SystemExit('Source references need correction before publication')
