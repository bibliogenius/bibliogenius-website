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
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_DIR = os.path.dirname(SCRIPT_DIR)
TEMPLATE_DIR = os.path.join(SCRIPT_DIR, 'templates')
I18N_DIR = os.path.join(SITE_DIR, '_i18n')

BASE_URL = 'https://bibliogenius.org'
DEFAULT_LANG = 'fr'
DOCS_DIR = os.path.join(SITE_DIR, '_docs')

# Sidebar group ordering
DOC_GROUPS = ['library', 'discovery', 'social', 'advanced', 'data']

# Map language code to OG locale
OG_LOCALES = {
    'fr': 'fr_FR',
    'en': 'en_US',
    'de': 'de_DE',
    'es': 'es_ES',
}


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
    """Language switcher for main pages (relative URLs)."""
    opts = []
    for lang in sorted(all_langs):
        name = all_langs[lang].get('lang_name', lang.upper())
        sel = ' selected' if lang == current else ''
        # Compute relative URL from current page to target page
        url = _relative_page_url(page, lang, current)
        opts.append(f'            <option value="{url}"{sel}>{name}</option>')
    return '\n'.join(opts)


def _relative_page_url(page, target_lang, current_lang):
    """Relative URL from current page to the same page in target_lang."""
    if target_lang == current_lang:
        # Same directory
        return f'{page}.html' if page != 'index' else 'index.html'
    if current_lang == DEFAULT_LANG:
        # From root to /{lang}/ subfolder
        if page == 'index':
            return f'{target_lang}/index.html'
        return f'{target_lang}/{page}.html'
    if target_lang == DEFAULT_LANG:
        # From /{lang}/ subfolder to root
        return f'../{page}.html' if page != 'index' else '../index.html'
    # From one subfolder to another (e.g. /en/ -> /de/)
    if page == 'index':
        return f'../{target_lang}/index.html'
    return f'../{target_lang}/{page}.html'


def discover_pages(filter_pages=None):
    """Discover all pages with templates and translations."""
    pages = {}
    if not os.path.isdir(TEMPLATE_DIR):
        return pages
    for fname in sorted(os.listdir(TEMPLATE_DIR)):
        if not fname.endswith('.html') or fname.startswith('_'):
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


def parse_frontmatter(text):
    """Split a Markdown file into frontmatter dict and body string."""
    if not text.startswith('---'):
        return {}, text
    end = text.find('---', 3)
    if end == -1:
        return {}, text
    fm_text = text[3:end].strip()
    body = text[end + 3:].strip()
    meta = {}
    for line in fm_text.split('\n'):
        line = line.strip()
        if not line:
            continue
        idx = line.find(': ')
        if idx == -1:
            continue
        key = line[:idx].strip()
        value = line[idx + 2:].strip()
        if len(value) >= 2 and value[0] == '"' and value[-1] == '"':
            value = value[1:-1]
        meta[key] = value
    # Convert order to int
    if 'order' in meta:
        try:
            meta['order'] = int(meta['order'])
        except ValueError:
            meta['order'] = 99
    return meta, body


def doc_url(slug, lang):
    """URL path for a doc page."""
    if lang == DEFAULT_LANG:
        return f'/docs/{slug}.html'
    return f'/{lang}/docs/{slug}.html'


def doc_index_url(lang):
    """URL path for the docs index."""
    if lang == DEFAULT_LANG:
        return '/docs/'
    return f'/{lang}/docs/'


def build_doc_sidebar(docs, current_slug, lang, ui):
    """Generate sidebar HTML grouped by category. Uses relative links (same dir)."""
    lines = []
    for group in DOC_GROUPS:
        group_docs = [d for d in docs if d['meta'].get('group') == group]
        if not group_docs:
            continue
        group_docs.sort(key=lambda d: d['meta'].get('order', 99))
        label = ui.get(f'group_{group}', group.capitalize())
        lines.append(f'                <div class="sidebar-group">')
        lines.append(f'                    <div class="sidebar-group-label">{label}</div>')
        for d in group_docs:
            is_current = d['slug'] == current_slug
            active = ' active' if is_current else ''
            aria = ' aria-current="page"' if is_current else ''
            title = d['meta'].get('title', d['slug'])
            lines.append(f'                    <a href="{d["slug"]}.html" class="sidebar-link{active}"{aria}>{title}</a>')
        lines.append(f'                </div>')
    return '\n'.join(lines)


def build_doc_index_groups(docs, lang, ui):
    """Generate grouped cards HTML for the docs index page. Uses relative links (same dir)."""
    lines = []
    for group in DOC_GROUPS:
        group_docs = [d for d in docs if d['meta'].get('group') == group]
        if not group_docs:
            continue
        group_docs.sort(key=lambda d: d['meta'].get('order', 99))
        label = ui.get(f'group_{group}', group.capitalize())
        lines.append(f'        <div class="doc-group">')
        lines.append(f'            <h3 class="doc-group-title">{label}</h3>')
        lines.append(f'            <div class="doc-cards">')
        for d in group_docs:
            title = d['meta'].get('title', d['slug'])
            desc = d['meta'].get('description', '')
            lines.append(f'                <a href="{d["slug"]}.html" class="doc-card">')
            lines.append(f'                    <h4>{title}</h4>')
            lines.append(f'                    <p>{desc}</p>')
            lines.append(f'                </a>')
        lines.append(f'            </div>')
        lines.append(f'        </div>')
    return '\n'.join(lines)


def build_doc_hreflang(slug, langs):
    """Build hreflang tags for a doc page."""
    tags = []
    for lang in sorted(langs):
        tags.append(f'    <link rel="alternate" hreflang="{lang}" href="{BASE_URL}{doc_url(slug, lang)}">')
    tags.append(f'    <link rel="alternate" hreflang="x-default" href="{BASE_URL}{doc_url(slug, DEFAULT_LANG)}">')
    return '\n'.join(tags)


def build_doc_index_hreflang(langs):
    """Build hreflang tags for the doc index page."""
    tags = []
    for lang in sorted(langs):
        tags.append(f'    <link rel="alternate" hreflang="{lang}" href="{BASE_URL}{doc_index_url(lang)}">')
    tags.append(f'    <link rel="alternate" hreflang="x-default" href="{BASE_URL}{doc_index_url(DEFAULT_LANG)}">')
    return '\n'.join(tags)


def _relative_doc_url(slug, target_lang, current_lang, root_path):
    """Relative URL from current doc page to a doc page in target_lang."""
    if target_lang == current_lang:
        return f'{slug}.html'
    # Go up to site root, then into target lang docs dir
    if target_lang == DEFAULT_LANG:
        return f'{root_path}docs/{slug}.html'
    return f'{root_path}{target_lang}/docs/{slug}.html'


def _relative_doc_index_url(target_lang, current_lang, root_path):
    """Relative URL from current doc dir to the doc index in target_lang."""
    if target_lang == current_lang:
        return 'index.html'
    if target_lang == DEFAULT_LANG:
        return f'{root_path}docs/index.html'
    return f'{root_path}{target_lang}/docs/index.html'


def build_doc_switcher(slug, all_ui, current_lang, root_path):
    """Language switcher for a doc page (relative URLs)."""
    opts = []
    for lang in sorted(all_ui):
        name = all_ui[lang].get('lang_name', lang.upper())
        sel = ' selected' if lang == current_lang else ''
        url = _relative_doc_url(slug, lang, current_lang, root_path)
        opts.append(f'            <option value="{url}"{sel}>{name}</option>')
    return '\n'.join(opts)


def build_doc_index_switcher(all_ui, current_lang, root_path):
    """Language switcher for the doc index page (relative URLs)."""
    opts = []
    for lang in sorted(all_ui):
        name = all_ui[lang].get('lang_name', lang.upper())
        sel = ' selected' if lang == current_lang else ''
        url = _relative_doc_index_url(lang, current_lang, root_path)
        opts.append(f'            <option value="{url}"{sel}>{name}</option>')
    return '\n'.join(opts)


def build_docs():
    """Build documentation pages from _docs/ Markdown files."""
    import markdown

    if not os.path.isdir(DOCS_DIR):
        return 0

    # Load UI translations
    ui_dir = os.path.join(DOCS_DIR, '_ui')
    all_ui = {}
    if os.path.isdir(ui_dir):
        for f in os.listdir(ui_dir):
            if f.endswith('.yml'):
                lang = f[:-4]
                all_ui[lang] = load_yaml(os.path.join(ui_dir, f))

    if not all_ui:
        return 0

    # Load templates
    doc_tpl_path = os.path.join(TEMPLATE_DIR, '_doc.html')
    index_tpl_path = os.path.join(TEMPLATE_DIR, '_doc-index.html')
    if not os.path.isfile(doc_tpl_path) or not os.path.isfile(index_tpl_path):
        print('WARNING: _doc.html or _doc-index.html template not found, skipping docs.')
        return 0

    with open(doc_tpl_path, encoding='utf-8') as f:
        doc_template = f.read()
    with open(index_tpl_path, encoding='utf-8') as f:
        index_template = f.read()

    # Discover doc sections (directories in _docs/ that are not _ui)
    sections = []
    for entry in sorted(os.listdir(DOCS_DIR)):
        if entry.startswith('_') or entry.startswith('.'):
            continue
        section_dir = os.path.join(DOCS_DIR, entry)
        if not os.path.isdir(section_dir):
            continue
        sections.append(entry)

    if not sections:
        return 0

    md = markdown.Markdown(extensions=['fenced_code', 'tables', 'toc'])

    total = 0
    all_langs = sorted(all_ui.keys())

    print(f'\n--- Documentation ---')

    for lang in all_langs:
        ui = all_ui[lang]

        # Parse all sections for this language (for sidebar)
        docs = []
        for slug in sections:
            md_path = os.path.join(DOCS_DIR, slug, f'{lang}.md')
            if not os.path.isfile(md_path):
                # Fall back to default lang
                md_path = os.path.join(DOCS_DIR, slug, f'{DEFAULT_LANG}.md')
                if not os.path.isfile(md_path):
                    continue
            with open(md_path, encoding='utf-8') as f:
                raw = f.read()
            meta, body = parse_frontmatter(raw)
            docs.append({'slug': slug, 'meta': meta, 'body': body})

        if not docs:
            continue

        # Build output directory and compute relative root path
        if lang == DEFAULT_LANG:
            out_dir = os.path.join(SITE_DIR, 'docs')
            root_path = '../'
        else:
            out_dir = os.path.join(SITE_DIR, lang, 'docs')
            root_path = '../../'
        os.makedirs(out_dir, exist_ok=True)

        # Generate each doc page
        for doc in docs:
            slug = doc['slug']
            meta = doc['meta']
            body = doc['body']

            # Rewrite image paths: images/x.png -> images/{slug}/x.png
            body = re.sub(
                r'!\[([^\]]*)\]\(images/([^)]+)\)',
                rf'![\1](images/{slug}/\2)',
                body
            )

            md.reset()
            content_html = md.convert(body)

            # Add loading="lazy" to images for performance
            content_html = content_html.replace('<img ', '<img loading="lazy" ')

            sidebar = build_doc_sidebar(docs, slug, lang, ui)
            hreflang = build_doc_hreflang(slug, all_langs)
            switcher = build_doc_switcher(slug, all_ui, lang, root_path)

            html = doc_template
            html = html.replace('{{root}}', root_path)
            html = html.replace('{{page_title}}', meta.get('title', slug))
            html = html.replace('{{page_description}}', meta.get('description', ''))
            html = html.replace('{{site_title}}', ui.get('title', 'Documentation'))
            html = html.replace('{{canonical_url}}', BASE_URL + doc_url(slug, lang))
            html = html.replace('{{hreflang}}', hreflang)
            html = html.replace('{{lang}}', lang)
            html = html.replace('{{lang_switcher}}', switcher)
            html = html.replace('{{hero_title}}', ui.get('hero_title', 'Documentation'))
            html = html.replace('{{hero_subtitle}}', ui.get('hero_subtitle', ''))
            html = html.replace('{{sidebar_title}}', ui.get('sidebar_title', 'Guide'))
            html = html.replace('{{sidebar}}', sidebar)
            html = html.replace('{{doc_index_url}}', 'index.html')
            html = html.replace('{{index_title}}', ui.get('index_title', 'All guides'))
            html = html.replace('{{breadcrumb_home}}', BASE_URL + page_url('index', lang))
            html = html.replace('{{breadcrumb_docs_label}}', ui.get('hero_title', 'Documentation'))
            html = html.replace('{{breadcrumb_docs_url}}', BASE_URL + doc_index_url(lang))
            html = html.replace('{{content}}', f'                <h1>{meta.get("title", slug)}</h1>\n{content_html}')
            html = html.replace('{{og_locale}}', OG_LOCALES.get(lang, lang))
            html = html.replace('{{footer_text}}', ui.get('footer_text', ''))
            # Navigation keys
            html = html.replace('{{nav_site_label}}', ui.get('nav_site_label', 'Main navigation'))
            html = html.replace('{{nav_home}}', ui.get('nav_home', 'Home'))
            html = html.replace('{{nav_story}}', ui.get('nav_story', 'Our Story'))
            html = html.replace('{{nav_docs}}', ui.get('nav_docs', 'Documentation'))
            html = html.replace('{{nav_contribute}}', ui.get('nav_contribute', 'Contribute'))
            html = html.replace('{{lang_label}}', ui.get('lang_label', 'Language'))

            out_file = os.path.join(out_dir, f'{slug}.html')
            with open(out_file, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f'  {os.path.relpath(out_file, SITE_DIR)}')
            total += 1

            # Copy images
            img_src = os.path.join(DOCS_DIR, slug, 'images')
            if os.path.isdir(img_src) and os.listdir(img_src):
                img_dst = os.path.join(out_dir, 'images', slug)
                os.makedirs(img_dst, exist_ok=True)
                for img_file in os.listdir(img_src):
                    src = os.path.join(img_src, img_file)
                    if os.path.isfile(src):
                        shutil.copy2(src, os.path.join(img_dst, img_file))

        # Generate index page
        hreflang = build_doc_index_hreflang(all_langs)
        switcher = build_doc_index_switcher(all_ui, lang, root_path)
        groups_html = build_doc_index_groups(docs, lang, ui)

        html = index_template
        html = html.replace('{{root}}', root_path)
        html = html.replace('{{title}}', ui.get('title', 'Documentation'))
        html = html.replace('{{meta_description}}', ui.get('meta_description', ''))
        html = html.replace('{{canonical_url}}', BASE_URL + doc_index_url(lang))
        html = html.replace('{{hreflang}}', hreflang)
        html = html.replace('{{lang}}', lang)
        html = html.replace('{{lang_switcher}}', switcher)
        html = html.replace('{{hero_title}}', ui.get('hero_title', 'Documentation'))
        html = html.replace('{{hero_subtitle}}', ui.get('hero_subtitle', ''))
        html = html.replace('{{url_home}}', root_path + 'index.html')
        html = html.replace('{{btn_back}}', ui.get('btn_back', 'Back'))
        html = html.replace('{{index_title}}', ui.get('index_title', 'All guides'))
        html = html.replace('{{index_subtitle}}', ui.get('index_subtitle', ''))
        html = html.replace('{{breadcrumb_home}}', BASE_URL + page_url('index', lang))
        html = html.replace('{{breadcrumb_docs_label}}', ui.get('hero_title', 'Documentation'))
        html = html.replace('{{groups}}', groups_html)
        html = html.replace('{{og_locale}}', OG_LOCALES.get(lang, lang))
        html = html.replace('{{footer_text}}', ui.get('footer_text', ''))
        # Navigation keys
        html = html.replace('{{nav_site_label}}', ui.get('nav_site_label', 'Main navigation'))
        html = html.replace('{{nav_home}}', ui.get('nav_home', 'Home'))
        html = html.replace('{{nav_story}}', ui.get('nav_story', 'Our Story'))
        html = html.replace('{{nav_docs}}', ui.get('nav_docs', 'Documentation'))
        html = html.replace('{{nav_contribute}}', ui.get('nav_contribute', 'Contribute'))
        html = html.replace('{{lang_label}}', ui.get('lang_label', 'Language'))

        index_file = os.path.join(out_dir, 'index.html')
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'  {os.path.relpath(index_file, SITE_DIR)}')
        total += 1

    return total


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
            # Relative root path: FR pages are at site root, others in /{lang}/
            root = '' if lang == DEFAULT_LANG else '../'

            html = template
            html = html.replace('{{root}}', root)
            html = html.replace('{{hreflang}}', hreflang)
            html = html.replace('{{lang}}', lang)
            html = html.replace('{{canonical_url}}', BASE_URL + page_url(page_name, lang))
            html = html.replace('{{og_url}}', BASE_URL + page_url(page_name, lang))
            html = html.replace('{{lang_switcher}}', build_switcher(page_name, langs, lang))

            # Cross-page links: {{url:page_name}} (relative paths)
            def resolve_url(m, _lang=lang):
                target = m.group(1)
                # Same-language pages are always in the same directory
                if target in all_page_langs and _lang in all_page_langs[target]:
                    return f'{target}.html' if target != 'index' else 'index.html'
                # Fallback to default language (may be in a different directory)
                if _lang == DEFAULT_LANG:
                    return f'{target}.html' if target != 'index' else 'index.html'
                return f'../{target}.html' if target != 'index' else '../index.html'

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

    # Build documentation pages
    doc_count = build_docs()
    total += doc_count

    print(f'\nDone! {total} pages generated ({total - doc_count} pages + {doc_count} docs).')


if __name__ == '__main__':
    build()
