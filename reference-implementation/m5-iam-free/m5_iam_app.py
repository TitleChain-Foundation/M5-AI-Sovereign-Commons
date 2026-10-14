"""Open the free M5 IAM app in your browser.

Runs on your own computer only. Standard library only. It listens on the
loopback address, shows one page, and can do one thing to your files: create
your IAM starting pod when you make the human attestation. It makes no
outbound network calls.
"""
import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import sys
import threading
import webbrowser

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))  # find m5_iam.py beside this file, however the app is started

import m5_iam  # noqa: E402
HOST = '127.0.0.1'
MAX_BODY = 4096


def clean(value, limit):
    return ' '.join(str(value or '').split())[:limit]


class Handler(BaseHTTPRequestHandler):
    pod = Path('~/M5POD-IAM').expanduser()
    port = 8756

    def log_message(self, *args):
        pass

    def origin(self):
        return f'http://{HOST}:{self.port}'

    def send(self, status, content_type, body):
        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Content-Security-Policy',
                         "default-src 'none'; style-src 'unsafe-inline'; script-src 'unsafe-inline'; connect-src 'self'")
        self.end_headers()
        self.wfile.write(body)

    def send_json(self, status, data):
        self.send(status, 'application/json', json.dumps(data).encode('utf-8'))

    def local_request(self):
        return self.headers.get('Host') in (f'{HOST}:{self.port}', f'localhost:{self.port}')

    def state(self):
        catalog = json.loads((HERE / 'iam-catalog.json').read_text(encoding='utf-8'))
        try:
            record, check = m5_iam.load_record(self.pod), m5_iam.verify_pod(self.pod)
        except m5_iam.PodError:
            record, check = None, None
        receipt_file = self.pod / m5_iam.LAYER / 'registry' / 'registry-receipt.json'
        receipt = json.loads(receipt_file.read_text(encoding='utf-8')) if record and receipt_file.exists() else None
        home = str(Path.home())
        shown = str(self.pod)
        shown = '~' + shown[len(home):] if shown.startswith(home) else shown
        return {'pod_path': shown, 'record': record, 'check': check, 'catalog': catalog,
                'registry': receipt, 'terms_template': m5_iam.HUMAN_TERMS}

    def do_GET(self):
        if not self.local_request():
            self.send(403, 'text/plain; charset=utf-8', b'Forbidden')
        elif self.path == '/':
            self.send(200, 'text/html; charset=utf-8', (HERE / 'app.html').read_bytes())
        elif self.path == '/api/state':
            self.send_json(200, self.state())
        else:
            self.send(404, 'text/plain; charset=utf-8', b'Not found')

    def do_POST(self):
        # Only this page, on this computer, may ask for the pod to be created.
        if (not self.local_request() or self.path != '/api/attest'
                or self.headers.get('Origin') not in (self.origin(), f'http://localhost:{self.port}')
                or self.headers.get('Content-Type') != 'application/json'):
            self.send(403, 'text/plain; charset=utf-8', b'Forbidden')
            return
        length = int(self.headers.get('Content-Length') or 0)
        if length <= 0 or length > MAX_BODY:
            self.send_json(400, {'error': 'Request too large or empty.'})
            return
        try:
            data = json.loads(self.rfile.read(length))
            chains = {c['chain'] for c in json.loads((HERE / 'iam-catalog.json').read_text(encoding='utf-8'))['chains']}
            chain = clean(data.get('chain'), 80)
            if chain and chain not in chains:
                raise m5_iam.PodError('Choose a state chain from the list.')
            m5_iam.init_pod(self.pod, clean(data.get('name'), 80), data.get('attest') is True,
                            chain=chain, contact=clean(data.get('contact'), 120))
        except (ValueError, AttributeError):
            self.send_json(400, {'error': 'The form could not be read.'})
        except m5_iam.PodError as error:
            self.send_json(409, {'error': str(error)})
        else:
            self.send_json(200, self.state())


def main():
    parser = argparse.ArgumentParser(description='Free M5 IAM app. Runs on this computer only.')
    parser.add_argument('--pod', type=Path, default=Handler.pod)
    parser.add_argument('--port', type=int, default=Handler.port)
    parser.add_argument('--no-browser', action='store_true')
    args = parser.parse_args()
    Handler.pod, Handler.port = args.pod.expanduser(), args.port
    server = ThreadingHTTPServer((HOST, args.port), Handler)
    url = f'http://{HOST}:{args.port}/'
    print(f'M5 IAM is open at {url}\nYour IAM pod: {Handler.pod}\nClose this window to stop.')
    if not args.no_browser:
        threading.Timer(0.6, webbrowser.open, [url]).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
