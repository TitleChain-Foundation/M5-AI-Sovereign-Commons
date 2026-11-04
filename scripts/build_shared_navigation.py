"""Build/check identical, local navigation assets without a cross-site runtime service."""
import argparse, hashlib, json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def payloads(root=ROOT):
    source=root/'shared-navigation'
    contract=json.loads((source/'navigation.json').read_text())
    if contract.get('schema')!='m5-public-navigation/v1' or set(contract['sites'])!={'commons','labs'}:
        raise ValueError('Invalid public navigation contract')
    for site,config in contract['sites'].items():
        if not config['url'].startswith('https://') or not config['url'].endswith('/'):
            raise ValueError('Canonical HTTPS root required')
        ids=[x['id'] for x in contract['menus'][site]]
        if len(ids)!=len(set(ids)):raise ValueError('Duplicate navigation ID')
    for item in contract['sharedTools']+sum(contract['menus'].values(),[]):
        if item['site'] not in contract['sites'] or '..' in item['path'] or ':' in item['path'] or item['path'].startswith('/'):
            raise ValueError('Unsafe navigation target')
    canonical=json.dumps(contract,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
    template=(source/'navigation.js').read_text()
    if template.count('__M5_NAVIGATION_CONTRACT__')!=1:raise ValueError('Missing contract placeholder')
    result={'navigation.js':template.replace('__M5_NAVIGATION_CONTRACT__',canonical.decode()).encode(),'navigation.css':(source/'navigation.css').read_bytes(),'mark.png':(source/'mark.png').read_bytes()}
    manifest={'schema':1,'version':contract['version'],'contract_sha256':hashlib.sha256(canonical).hexdigest(),'assets':{k:hashlib.sha256(v).hexdigest() for k,v in result.items()}}
    manifest['bundle_sha256']=hashlib.sha256(json.dumps(manifest['assets'],sort_keys=True).encode()).hexdigest()
    result['manifest.json']=(json.dumps(manifest,indent=2)+'\n').encode()
    return result

def main():
    p=argparse.ArgumentParser();p.add_argument('--web-root',choices=['site','public'],required=True);p.add_argument('--check',action='store_true');a=p.parse_args()
    dest=ROOT/a.web_root/'assets/navigation'
    generated=payloads()
    version=json.loads(generated['manifest.json'])['bundle_sha256'][:12]
    for name,data in generated.items():
        path=dest/name
        if a.check:
            if not path.is_file() or path.read_bytes()!=data:raise SystemExit('Navigation asset out of sync: '+str(path.relative_to(ROOT)))
        else:
            dest.mkdir(parents=True,exist_ok=True);path.write_bytes(data)
    for page in (ROOT/a.web_root).rglob('*.html'):
        if 'assets' in page.relative_to(ROOT/a.web_root).parts:continue
        text=page.read_text()
        for suffix in ('js','css'):
            pattern=r'navigation\.'+suffix+r'(?:\?v=[a-f0-9]+)?'
            expected='navigation.'+suffix+'?v='+version
            matches=re.findall(pattern,text)
            if matches!=[expected]:
                if a.check:raise SystemExit('Navigation HTML reference out of sync: '+str(page.relative_to(ROOT)))
                if not matches:raise SystemExit('Missing navigation reference: '+str(page))
                text=re.sub(pattern,lambda m:expected,text)
        if not a.check:page.write_text(text)
    snapshot=ROOT/'docs/review/inversion-template.html'
    packed=ROOT/a.web_root/'inversion/index.html'
    if snapshot.exists() and packed.exists():
        match=re.search(r'<script[^>]*type="__bundler/template"[^>]*>([\s\S]*?)</script>',packed.read_text())
        if not match:raise SystemExit('Missing Inversion template')
        template=json.loads(match[1])
        if a.check:
            if snapshot.read_text()!=template:raise SystemExit('Inversion review snapshot out of sync')
        else:snapshot.write_text(template)
    print('Navigation assets match contract' if a.check else 'Navigation assets built')
if __name__=='__main__':main()
