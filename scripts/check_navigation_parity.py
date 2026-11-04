"""Read-only comparison of deployed public navigation contracts and asset bytes."""
import argparse, hashlib, json
from urllib.request import urlopen

def inspect(root):
    root=root.rstrip('/')+'/assets/navigation/'
    with urlopen(root+'manifest.json',timeout=20) as response:
        manifest=json.load(response)
    if set(manifest['assets'])!={'navigation.js','navigation.css','mark.png'}:
        raise ValueError('Unexpected navigation asset set')
    for name,digest in manifest['assets'].items():
        with urlopen(root+name+'?v='+manifest['bundle_sha256'][:12],timeout=20) as response:
            actual=hashlib.sha256(response.read(2_000_001)).hexdigest()
        if actual!=digest:raise ValueError('Deployed navigation asset mismatch: '+name)
    return manifest

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('urls',nargs=2);a=p.parse_args()
    manifests=[inspect(url) for url in a.urls]
    if manifests[0]!=manifests[1]:raise SystemExit('FAIL: public navigation manifests differ')
    print(json.dumps({'status':'PASS','urls':a.urls,'manifest':manifests[0]},indent=2))
