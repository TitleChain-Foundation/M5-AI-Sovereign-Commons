"""Front-door wiring must use maintained sources and resolvable page names."""
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit

ROOT=Path(__file__).resolve().parents[1]
def template():
    source=(ROOT/'site/index.html').read_text()
    return json.loads(re.search(r'<script[^>]*type="__bundler/template"[^>]*>(.*?)</script>',source,re.S).group(1))

class Connections(unittest.TestCase):
    def test_homepage_uses_single_maintained_catalog(self):
        source=(ROOT/'site/index.html').read_text();text=template()
        self.assertEqual(text.count('<script src="./commons-data.js"></script>'),1)
        manifest=json.loads(re.search(r'<script[^>]*type="__bundler/manifest"[^>]*>(.*?)</script>',source,re.S).group(1))
        self.assertNotIn('b00b16bb-ba18-44fe-b439-a5d65d517be8',manifest)
        self.assertNotIn('b00b16bb-ba18-44fe-b439-a5d65d517be8',text)
    def test_known_design_pages_and_fragments_exist(self):
        source=(ROOT/'site/commons-data.js').read_text()
        refs=re.findall(r"designRef: '([^']+)'",source)
        self.assertEqual(set(refs),{'labs.html','iwbe.html','iwbe.html#iswe'})
        for ref in refs:
            url=urlsplit(ref);p=ROOT/'site'/url.path
            self.assertTrue(p.is_file(),ref)
            if url.fragment:self.assertIn('id="'+url.fragment+'"',p.read_text())
    def test_dynamic_options_are_not_nested_inside_native_selects(self):
        text=template()
        selects=re.findall(r'<sc-raw-select\b[^>]*>(.*?)</sc-raw-select>',text,re.S)
        self.assertGreaterEqual(len(selects),7)
        for content in selects:
            self.assertNotIn('<sc-for',content)
            options=re.findall(r'<option\b[^>]*>(.*?)</option>',content,re.S)
            self.assertTrue(options)
            self.assertTrue(all(x.strip() and '{{' not in x for x in options))
    def test_search_frontends_and_current_m5labs_address(self):
        text=template()
        self.assertNotIn('https://titlechain-foundation.gitlab.io/m5labs/',text)
        self.assertIn('https://m5labs-8770fb.gitlab.io/',text)
        search=text.split('<div data-screen-label="Search">')[1].split('</section>')[0]
        for name in ('freedom-office.html','marketplace.html','iwbe.html','library/index.html'):
            self.assertIn('./'+name,search)
    def test_all_route_views_remain_inside_main(self):
        text=template();main=text.split('<main id="main"')[1].split('</main>')[0]
        for name in ('Search','Toolkit Library','Toolkit Detail'):
            self.assertIn('data-screen-label="'+name+'"',main)
        self.assertNotIn('f.likeAria',text) # obsolete duplicated family card, never wired

    def test_labs_discovery_links_and_navigation_contract(self):
        text=(ROOT/'site/labs.html').read_text()
        for route in ('observatory/', 'calculator-families/', 'research/', 'research/mathematical-knots.html'):
            self.assertIn('https://m5labs-8770fb.gitlab.io/'+route,text)
        contract=json.loads((ROOT/'shared-navigation/navigation.json').read_text())
        self.assertIn('observatory',[x['id'] for x in contract['menus']['labs']])
        self.assertIn('docs/M5LABS_RESEARCH_DISCOVERY.md',json.loads((ROOT/'site/content-map.json').read_text())['selected_sources'])

    def test_labs_does_not_import_missing_icon_component(self):
        text=(ROOT/'site/labs.html').read_text()
        self.assertNotIn('m5-ic.jsx',text)
        self.assertIn('aria-label="AI-assisted"',text)

if __name__=='__main__':unittest.main()
