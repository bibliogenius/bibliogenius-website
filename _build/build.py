#!/usr/bin/env python3
"""Build script for BiblioGenius static site.

Generates one HTML file per language per page from templates + YAML translations.

Usage:
    python3 _build/build.py              # Build all pages
    python3 _build/build.py story        # Build only story page
    python3 _build/build.py index story  # Build index and story pages

Adding a new language to a page:
    1. Copy _i18n/{page}/fr.yml to _i18n/{page}/{code}.yml
    2. Translate all values (keep HTML tags as-is)
    3. Run: python3 _build/build.py

Adding a new page:
    1. Create template in _build/templates/{page}.html
    2. Create _i18n/{page}/ with at least fr.yml
    3. Run: python3 _build/build.py
"""

import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_DIR = os.path.dirname(SCRIPT_DIR)
TEMPLATE_DIR = os.path.join(SCRIPT_DIR, 'templates')
I18N_DIR = os.path.join(SITE_DIR, '_i18n')

BASE_URL = 'https://bibliogenius.org'
DEFAULT_LANG = 'fr'


def load_yaml(path):
    """Load a flat YAML file (key: value pairs, # comments, blank lines)."""
    data = {}
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n\r')
            stripped = line.strip()
            if not stripped or stripped.startswith('#'):
                continue
            idx = stripped.find(': ')
            if idx == -1:
                continue
            key = stripped[:idx]
            value = stripped[idx + 2:]
            if len(value) >= 2 and value[0] == '"' and value[-1] == '"':
                value = value[1:-1]
            data[key] = value
    return data


def page_url(page, lang):
    """URL path for a given page and language."""
    if page == 'index':
        return '/' if lang == DEFAULT_LANG else f'/{lang}/'
    if lang == DEFAULT_LANG:
        return f'/{page}.html'
    return f'/{lang}/{page}.html'


def output_path(page, lang):
    """Filesystem path for the generated page."""
    filename = f'{page}.html'
    if lang == DEFAULT_LANG:
        return os.path.join(SITE_DIR, filename)
    out_dir = os.path.join(SITE_DIR, lang)
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, filename)


def build_hreflang(page, langs):
    tags = []
    for lang in sorted(langs):
        tags.append(f'    <link rel="alternate" hreflang="{lang}" href="{BASE_URL}{page_url(page, lang)}">')
    tags.append(f'    <link rel="alternate" hreflang="x-default" href="{BASE_URL}{page_url(page, DEFAULT_LANG)}">')
    return '\n'.join(tags)


def build_switcher(page, all_langs, current):
    opts = []
    for lang in sorted(all_langs):
        name = all_langs[lang].get('lang_name', lang.upper())
        sel = ' selected' if lang == current else ''
        opts.append(f'            <option value="{page_url(page, lang)}"{sel}>{name}</option>')
    return '\n'.join(opts)


def discover_pages(filter_pages=None):
    """Discover all pages with templates and translations."""
    pages = {}
    if not os.path.isdir(TEMPLATE_DIR):
        return pages
    for fname in sorted(os.listdir(TEMPLATE_DIR)):
        if not fname.endswith('.html'):
            continue
        page_name = fname[:-5]
        if filter_pages and page_name not in filter_pages:
            continue
        i18n_dir = os.path.join(I18N_DIR, page_name)
        if not os.path.isdir(i18n_dir):
            continue
        langs = {}
        for yf in sorted(os.listdir(i18n_dir)):
            if yf.endswith('.yml'):
                langs[yf[:-4]] = load_yaml(os.path.join(i18n_dir, yf))
        if langs:
            tpl_path = os.path.join(TEMPLATE_DIR, fname)
            with open(tpl_path, encoding='utf-8') as f:
                template = f.read()
            pages[page_name] = {'template': template, 'langs': langs}
    return pages


def build():
    filter_pages = set(sys.argv[1:]) if len(sys.argv) > 1 else None
    pages = discover_pages(filter_pages)

    if not pages:
        print('No pages found. Check _build/templates/ and _i18n/ directories.')
        sys.exit(1)

    # Collect all page language sets for cross-page URL resolution
    all_page_langs = {name: set(info['langs'].keys()) for name, info in pages.items()}

    total = 0
    for page_name, info in sorted(pages.items()):
        template = info['template']
        langs = info['langs']
        print(f'\n{page_name}.html ({len(langs)} langs):')

        hreflang = build_hreflang(page_name, langs)

        for lang, t in sorted(langs.items()):
            html = template
            html = html.replace('{{hreflang}}', hreflang)
            html = html.replace('{{lang}}', lang)
            html = html.replace('{{canonical_url}}', BASE_URL + page_url(page_name, lang))
            html = html.replace('{{og_url}}', BASE_URL + page_url(page_name, lang))
            html = html.replace('{{lang_switcher}}', build_switcher(page_name, langs, lang))

            # Cross-page links: {{url:page_name}}
            def resolve_url(m, _lang=lang):
                target = m.group(1)
                if target in all_page_langs and _lang in all_page_langs[target]:
                    return page_url(target, _lang)
                return page_url(target, DEFAULT_LANG)

            html = re.sub(r'\{\{url:([\w-]+)\}\}', resolve_url, html)

            # Replace all remaining {{key}} placeholders
            missing = []

            def replace_key(m):
                key = m.group(1)
                if key in t:
                    return t[key]
                if DEFAULT_LANG in langs and key in langs[DEFAULT_LANG]:
                    missing.append(key)
                    return langs[DEFAULT_LANG][key]
                print(f'  [{lang}] ERROR: "{key}" not found')
                return m.group(0)

            html = re.sub(r'\{\{(\w+)\}\}', replace_key, html)

            if missing:
                print(f'  [{lang}] Fallback: {", ".join(missing)}')

            out = output_path(page_name, lang)
            with open(out, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f'  {os.path.relpath(out, SITE_DIR)}')
            total += 1

    print(f'\nDone! {total} pages generated across {len(pages)} templates.')


if __name__ == '__main__':
    build()
