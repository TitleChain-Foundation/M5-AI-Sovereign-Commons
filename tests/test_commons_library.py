"""Source fidelity, routing and hostile-markup boundaries for the generated reader."""
import importlib.util
from html.parser import HTMLParser
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch
from urllib.parse import unquote, urlsplit

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('commons_library',ROOT/'scripts/build_commons_library.py')
lib=importlib.util.module_from_spec(spec);spec.loader.exec_module(lib)

class Tags(HTMLParser):
    def __init__(self):super().__init__();self.tags=[];self.attrs=[]
    def handle_starttag(self,tag,attrs):self.tags.append(tag);self.attrs.append(dict(attrs))

class LibraryTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)/'repo';self.root.mkdir();self.output=Path(self.temp.name)/'output'
        (self.root/'site').mkdir();self.manifest=self.root/'site/content-map.json'
    def write(self,path,text):
        dest=self.root/path;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(text)
    def build(self,selected,aliases=None):
        self.manifest.write_text(json.dumps({'schema_version':1,'selected_sources':selected,'aliases':aliases or {}}))
        files={p.relative_to(self.root).as_posix() for p in self.root.rglob('*') if p.is_file()}
        with patch.object(lib,'tracked',return_value=files),patch.object(lib.subprocess,'check_output',return_value='a'*40+'\n'):
            return lib.build(self.root,self.output)
    def text(self,path='library/README.html'):return (self.output/path).read_text()
    def test_real_selected_sources_links_and_images_resolve(self):
        shutil.copytree(ROOT/'site',self.output)
        catalog=lib.build(ROOT,self.output)
        self.assertEqual(catalog['rendered_count'],68)
        self.assertEqual(catalog['source_reference_warnings'],[])
        self.assertEqual(len(catalog['entries']),len([x for x in lib.tracked(ROOT) if x.endswith('.md')]))
        self.assertIn('Draft for Public Comment',self.text())
        for page in (self.output/'library').rglob('*.html'):
            parsed=Tags();parsed.feed(page.read_text())
            for attrs in parsed.attrs:
                for key in ('href','src'):
                    if key not in attrs:continue
                    url=urlsplit(attrs[key])
                    if url.scheme or url.netloc or not url.path:continue
                    dest=(page.parent/unquote(url.path)).resolve()
                    self.assertTrue(dest.is_relative_to(self.output.resolve()),attrs[key])
                    self.assertTrue(dest.is_file(),str(page)+': '+attrs[key])
                    if url.fragment and dest.suffix=='.html':
                        self.assertIn('id="'+unquote(url.fragment)+'"',dest.read_text())
    def test_discovery_preserves_every_source_destination_and_escapes_metadata(self):
        self.write('README.md', '# Overview\n\nWelcome to this public collection of documents and source records.')
        self.write('docs/guide.md', '# <img src=x onerror=alert(1)>\n\nA source description that must remain inert rather than execute markup.')
        catalog=self.build(['README.md'])
        index=self.text('library/index.html');parsed=Tags();parsed.feed(index)
        links={a['href'] for a in parsed.attrs if 'href' in a}
        self.assertIn('README.html',links)
        self.assertIn('https://github.com/TitleChain-Foundation/M5-AI-Sovereign-Commons/blob/'+'a'*40+'/docs/guide.md',links)
        self.assertEqual(sum(a.get('class')=='library-card' for a in parsed.attrs),2)
        self.assertNotIn('img',parsed.tags)
        self.assertIn('library-index.js',index)
        self.assertEqual({e['source_path'] for e in catalog['entries']},{'README.md','docs/guide.md'})
        self.assertTrue(all(e['topic'] in {x[0] for x in lib.LIBRARY_TOPICS} for e in catalog['entries']))

    def test_discovery_front_matter_title_does_not_change_source_reader(self):
        path='pilots/312-spring-commons/briefs/PPT-EZ-CA-0001-THE-BEAR-COMES-HOME.md'
        text='---\ntitle: A source title\nstatus: concept_only\n---\n\n# Source title\n\nThis is a proposed research concept and is not an approved institution.'
        self.write(path,text)
        catalog=self.build([path]);entry=catalog['entries'][0]
        self.assertEqual(entry['display_title'],'The Bear Comes Home — Public Bank of California concept')
        self.assertEqual(entry['document_kind'],'Project document')
        self.assertIn('proposed research concept',entry['summary'])
        self.assertEqual((self.root/path).read_text(),text)

    def test_traversal_absolute_and_hidden_sources_are_rejected(self):
        for source in ('../private.md','/private.md','.git/secret.md'):
            with self.subTest(source=source),self.assertRaises(ValueError):self.build([source])
    def test_duplicates_and_missing_sources_are_rejected(self):
        self.write('README.md','# Test')
        for selected in (['README.md','README.md'],['missing.md']):
            with self.assertRaises(ValueError):self.build(selected)
    def test_symlink_outside_repository_is_rejected(self):
        secret=Path(self.temp.name)/'outside.md';secret.write_text('Private')
        (self.root/'README.md').symlink_to(secret)
        with self.assertRaises(ValueError):self.build(['README.md'])
    def test_raw_scripts_handlers_frames_and_dom_ids_are_not_executable(self):
        self.write('README.md','''# Security
<script>alert(1)</script>

<img src=x onerror=alert(1)><iframe src="https://example.org"></iframe>

<details onclick="alert(1)" id="location"><summary>Safe disclosure</summary>Text</details>
''')
        self.build(['README.md']);p=Tags();p.feed(self.text())
        self.assertNotIn('iframe',p.tags);self.assertNotIn('img',p.tags)
        self.assertEqual(p.tags.count('script'),2) # trusted external reader and shared navigation only
        self.assertEqual({urlsplit(a['src']).path for a in p.attrs if 'src' in a and urlsplit(a['src']).path.endswith('.js')},{'../assets/library-reader.js','../assets/navigation/navigation.js'})
        self.assertIn('details',p.tags)
        for attrs in p.attrs:
            self.assertFalse(any(k.startswith('on') for k in attrs))
            self.assertNotEqual(attrs.get('id'),'location')
        self.assertIn('&lt;script&gt;',self.text())
    def test_unsafe_url_schemes_are_not_links_or_image_sources(self):
        self.write('README.md','# URLs\n[x](javascript:alert%281%29)\n\n[x](file:///tmp/test)\n\n![x](data:image/png;base64,AAAA)\n\n[x](//outside.example/file)')
        self.build(['README.md']);p=Tags();p.feed(self.text())
        for attrs in p.attrs:
            self.assertFalse(any(str(v).startswith(('javascript:','file:','data:','//')) for k,v in attrs.items() if k in ('href','src')))
    def test_selected_links_and_prefixed_duplicate_anchors(self):
        self.write('README.md','# Home\n[Read](docs/guide.md#same-1)\n[Legacy](docs/old.md#same)')
        self.write('docs/guide.md','# Same\n## Same\n')
        self.build(['README.md','docs/guide.md'],{'docs/old.md':'docs/guide.md'})
        self.assertIn('href="docs/guide.html#doc-same-1"',self.text())
        self.assertIn('href="docs/guide.html#doc-same"',self.text())
        self.assertIn('id="doc-same-1"',self.text('library/docs/guide.html'))
    def test_unselected_sources_and_code_keep_pinned_github_destinations(self):
        self.write('README.md','# Home\n[Other](draft.md)\n[Code](code.py)')
        self.write('draft.md','# Draft');self.write('code.py','pass')
        catalog=self.build(['README.md'])
        self.assertIn('/blob/'+'a'*40+'/draft.md',self.text())
        self.assertEqual(next(e for e in catalog['entries'] if e['source_path']=='draft.md')['disposition'],'github_source')
        self.assertIn('/blob/'+'a'*40+'/code.py',self.text())
    def test_source_change_updates_fingerprint(self):
        self.write('README.md','# First');a=self.build(['README.md'])['entries'][0]['sha256']
        self.write('README.md','# Second');b=self.build(['README.md'])['entries'][0]['sha256']
        self.assertNotEqual(a,b)
    def test_tables_currency_code_and_escaped_brackets_remain_literal(self):
        self.write('README.md','# Values\n\n| Item | Value |\n|---|---|\n| Budget | $25 |\n\nSG\\[provider\\] → US-CA\\[destination\\]\n\n```text\n<script>not executable</script>\n```')
        self.build(['README.md']);text=self.text()
        self.assertIn('<table>',text);self.assertIn('$25',text);self.assertIn('SG[provider]',text)
        self.assertIn('&lt;script&gt;not executable&lt;/script&gt;',text)
    def test_bad_local_reference_is_reported_without_fabricated_local_page(self):
        self.write('README.md','# Home\n[Missing](missing.md)')
        result=self.build(['README.md'])
        self.assertEqual(result['source_reference_warnings'],['README.md -> missing.md'])
        self.assertIn('/blob/'+'a'*40+'/missing.md',self.text())
    def test_output_cannot_overwrite_repository(self):
        self.write('README.md','# Home');self.output=self.root
        with self.assertRaises(ValueError):self.build(['README.md'])

if __name__=='__main__':unittest.main()
