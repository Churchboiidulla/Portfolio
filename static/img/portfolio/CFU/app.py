from flask import Flask, render_template, send_from_directory, abort
import os

BASE_DIR = os.path.dirname(__file__)
TEMPLATE_DIR = os.path.join(BASE_DIR, 'CFU', 'CFU-templates')
STATIC_DIR = os.path.join(TEMPLATE_DIR, 'assets')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<path:page>')
def show_page(page):
    # Normalize and prevent directory traversal
    safe = os.path.normpath(page).lstrip(os.sep)
    if safe.startswith('..'):
        abort(404)
    # Ensure .html extension
    if not safe.endswith('.html'):
        safe = safe + '.html'
    # Check file exists inside templates dir
    full = os.path.join(TEMPLATE_DIR, safe)
    if not os.path.isfile(full):
        abort(404)
    # Convert to forward-slash path for Jinja
    rel = safe.replace(os.sep, '/')
    return render_template(rel)


@app.route('/assets/<path:filename>')
def assets(filename):
    # Serve assets directly from the template assets folder (fallback)
    return send_from_directory(STATIC_DIR, filename)


@app.route('/_templates')
def list_templates():
    pages = []
    for root, _, files in os.walk(TEMPLATE_DIR):
        for f in files:
            if f.endswith('.html'):
                rel = os.path.relpath(os.path.join(root, f), TEMPLATE_DIR).replace(os.sep, '/')
                pages.append(rel)
    links = ['<a href="/{0}">{0}</a>'.format(p) for p in sorted(pages)]
    return '<br>'.join(links)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Run CFU Flask preview server')
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', type=int, default=5000)
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()
    app.run(host=args.host, port=args.port, debug=args.debug)
