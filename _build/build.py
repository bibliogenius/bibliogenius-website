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

import json
import os
import re
import shutil
import sys
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_DIR = os.path.dirname(SCRIPT_DIR)
TEMPLATE_DIR = os.path.join(SCRIPT_DIR, 'templates')
I18N_DIR = os.path.join(SITE_DIR, '_i18n')

BASE_URL = 'https://bibliogenius.org'
DEFAULT_LANG = 'fr'
DOCS_DIR = os.path.join(SITE_DIR, '_docs')
CHANGELOG_DIR = os.path.join(SITE_DIR, '_changelog')
VERSION_FILE = os.path.join(SCRIPT_DIR, 'version.txt')

# Sidebar group ordering
DOC_GROUPS = ['library', 'discovery', 'social', 'advanced', 'games', 'data']

# Map language code to OG locale
OG_LOCALES = {
    'fr': 'fr_FR',
    'en': 'en_US',
    'de': 'de_DE',
    'es': 'es_ES',
}

BLOG_CONTENT_DIR = os.path.join(SITE_DIR, '_blog', 'content')

# sitemap.xml is generated at deploy time (see build_sitemap).
SITEMAP_FILE = os.path.join(SITE_DIR, 'sitemap.xml')
# Per-page <priority>; pages absent here default to 0.5. Pages in
# SITEMAP_EXCLUDE are omitted entirely (e.g. the invite landing page).
SITEMAP_PRIORITY = {
    'index': '1.0',
    'story': '0.9',
    'contribute': '0.8',
    'changelog': '0.6',
    'free-your-library': '0.5',
    'support': '0.4',
    'privacy': '0.3',
    'data-deletion': '0.3',
}
SITEMAP_EXCLUDE = {'invite'}
DOC_PRIORITY = '0.6'
DOC_INDEX_PRIORITY = '0.7'
BLOG_PRIORITY = '0.6'

# Month names per language (for blog post date formatting)
MONTH_NAMES = {
    'fr': ['janvier', 'février', 'mars', 'avril', 'mai', 'juin',
           'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'],
    'en': ['January', 'February', 'March', 'April', 'May', 'June',
           'July', 'August', 'September', 'October', 'November', 'December'],
    'es': ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
           'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'],
    'de': ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni',
           'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember'],
}

# Robots directive, injected in every page.
# max-image-preview:large lets Google use a full-size thumbnail in mobile
# search results and makes the page eligible for Discover cards.
ROBOTS_META = '    <meta name="robots" content="max-image-preview:large">'

# Language suggestion banner (injected only in default-lang pages).
# It replaces an earlier automatic location.replace() to /en/. Googlebot
# renders JavaScript with an en-US locale, so that redirect fired on every
# crawl of the French pages and contradicted their own canonical and
# hreflang="fr". Google advises suggesting a translation instead of forcing
# it. The banner is fixed to the bottom of the viewport so it costs no
# layout shift, and the choice is remembered via sessionStorage.
LANG_SUGGEST_SCRIPT = '''<script>
(function(){
  if(sessionStorage.getItem('lang_chosen'))return;
  var l=navigator.language||navigator.userLanguage||'';
  if(l.substring(0,2)==='fr')return;
  var target=location.pathname.replace(/^\\/(?!en\\/|de\\/|es\\/)/,'/en/');
  if(target===location.pathname)return;
  function remember(){try{sessionStorage.setItem('lang_chosen','1');}catch(e){}}
  function show(){
    var bar=document.createElement('div');
    bar.setAttribute('role','complementary');
    bar.setAttribute('aria-label','Language');
    bar.style.cssText='position:fixed;left:0;right:0;bottom:0;z-index:1000;display:flex;flex-wrap:wrap;gap:0.5rem 1rem;align-items:center;justify-content:center;background:#1e40af;color:#fff;padding:0.7rem 1rem;font-size:0.95rem;line-height:1.4;';
    var msg=document.createElement('span');
    msg.textContent='This page is also available in English.';
    var link=document.createElement('a');
    link.href=target+location.search+location.hash;
    link.textContent='Read in English';
    link.style.cssText='color:#fff;font-weight:600;text-decoration:underline;';
    link.addEventListener('click',remember);
    var close=document.createElement('button');
    close.type='button';
    close.textContent='Dismiss';
    close.style.cssText='background:none;border:1px solid rgba(255,255,255,0.5);color:#fff;border-radius:4px;padding:0.2rem 0.6rem;font-size:0.85rem;cursor:pointer;';
    close.addEventListener('click',function(){remember();bar.parentNode.removeChild(bar);});
    bar.appendChild(msg);bar.appendChild(link);bar.appendChild(close);
    document.body.appendChild(bar);
  }
  if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',show);}else{show();}
})();
</script>'''


def finalize_html(html, lang, has_english, schema=''):
    """Apply the injections every generated page shares.

    Injects the robots directive and any JSON-LD right after <head>, the
    language suggestion banner right before </body>, and the sessionStorage
    flag on the language switcher. The banner goes at the end of the body so
    <meta charset> stays within the first bytes of the document.
    """
    head_extras = ROBOTS_META
    if schema:
        head_extras += '\n' + schema
    # Anchor on the charset meta so it stays the first element of the head.
    charset = '<meta charset="UTF-8">'
    if charset in html:
        html = html.replace(charset, charset + '\n' + head_extras, 1)
    else:
        html = html.replace('<head>', '<head>\n' + head_extras, 1)
    if lang == DEFAULT_LANG and has_english:
        html = html.replace('</body>', LANG_SUGGEST_SCRIPT + '\n</body>', 1)
    return inject_lang_chosen(html)


def inject_lang_chosen(html):
    """Add sessionStorage flag to language switcher so manual choice is remembered."""
    return html.replace(
        'onchange="location.href=this.value"',
        "onchange=\"sessionStorage.setItem('lang_chosen','1');location.href=this.value\""
    )


# Publisher / author node reused by every JSON-LD block below.
ORGANIZATION = {
    '@type': 'Organization',
    'name': 'BiblioGenius',
    'url': BASE_URL + '/',
    'logo': BASE_URL + '/favicon-192x192.png',
    # sameAs consolidates the entity: the same profiles are declared on the
    # homepage, so every page points answer engines at one identity.
    'sameAs': [
        'https://codeberg.org/bibliogenius',
        'https://apps.apple.com/app/bibliogenius/id6757465461',
        'https://play.google.com/store/apps/details?id=com.bibliogenius.app',
    ],
}

WEBSITE = {
    '@type': 'WebSite',
    'name': 'BiblioGenius',
    'url': BASE_URL + '/',
}

# Schema.org type per vitrine page. Pages absent here get no page-level
# JSON-LD; index.html carries its own SoftwareApplication in the template.
PAGE_SCHEMA_TYPES = {
    'story': 'AboutPage',
    'contribute': 'WebPage',
    'free-your-library': 'WebPage',
    'support': 'WebPage',
}


def _plain(value):
    """Strip tags and collapse whitespace: JSON-LD values carry no markup."""
    text = re.sub(r'<[^>]+>', '', value or '')
    text = text.replace('&nbsp;', ' ').replace('&amp;', '&')
    return ' '.join(text.split())


def _short_title(t):
    """Page title without the site-name suffix, for breadcrumbs and names."""
    title = _plain(t.get('og_title') or t.get('title') or 'BiblioGenius')
    for sep in (' - BiblioGenius', ' — BiblioGenius', ' | BiblioGenius'):
        if title.endswith(sep):
            return title[: -len(sep)]
    return title


def _schema_block(payload):
    """Render one JSON-LD payload as an indented <script> block."""
    body = json.dumps(payload, ensure_ascii=False, indent=4)
    body = '\n'.join('    ' + line for line in body.split('\n'))
    return '    <script type="application/ld+json">\n' + body + '\n    </script>'


def build_faq_schema(t):
    """FAQPage built from the faq_q{n}/faq_a{n} pairs of a translation file.

    Answer engines quote question/answer pairs far more readily than prose,
    and the support page already holds the four questions users actually ask.
    """
    entries = []
    n = 1
    while f'faq_q{n}' in t and f'faq_a{n}' in t:
        entries.append({
            '@type': 'Question',
            'name': _plain(t[f'faq_q{n}']),
            'acceptedAnswer': {
                '@type': 'Answer',
                'text': _plain(t[f'faq_a{n}']),
            },
        })
        n += 1
    if not entries:
        return ''
    return _schema_block({
        '@context': 'https://schema.org',
        '@type': 'FAQPage',
        'mainEntity': entries,
    })


def build_page_schema(page, lang, t):
    """JSON-LD for a vitrine page: the page node, its breadcrumb, and any FAQ."""
    schema_type = PAGE_SCHEMA_TYPES.get(page)
    if not schema_type:
        return ''
    url = BASE_URL + page_url(page, lang)
    home = BASE_URL + page_url('index', lang)
    name = _short_title(t)
    payload = {
        '@context': 'https://schema.org',
        '@type': schema_type,
        'name': name,
        'description': _plain(t.get('meta_description', '')),
        'url': url,
        'inLanguage': lang,
        'isPartOf': WEBSITE,
        'publisher': ORGANIZATION,
        'breadcrumb': {
            '@type': 'BreadcrumbList',
            'itemListElement': [
                {'@type': 'ListItem', 'position': 1,
                 'name': 'BiblioGenius', 'item': home},
                {'@type': 'ListItem', 'position': 2,
                 'name': name, 'item': url},
            ],
        },
    }
    blocks = [_schema_block(payload)]
    faq = build_faq_schema(t)
    if faq:
        blocks.append(faq)
    return '\n'.join(blocks)


def build_doc_schema(slug, lang, meta):
    """TechArticle for a documentation guide.

    Google retired the HowTo rich result in 2023, so the guides are typed as
    TechArticle: still accurate, and still read by answer engines. The
    template already carries the BreadcrumbList, so it is not repeated here.
    """
    url = BASE_URL + doc_url(slug, lang)
    return _schema_block({
        '@context': 'https://schema.org',
        '@type': 'TechArticle',
        'headline': _plain(meta.get('title', slug)),
        'description': _plain(meta.get('description', '')),
        'url': url,
        'mainEntityOfPage': {'@type': 'WebPage', '@id': url},
        'inLanguage': lang,
        'isPartOf': WEBSITE,
        'about': {
            '@type': 'SoftwareApplication',
            'name': 'BiblioGenius',
            'url': BASE_URL + '/',
        },
        'author': ORGANIZATION,
        'publisher': ORGANIZATION,
    })


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
                # Double-quoted scalar: strip the wrapping quotes and unescape
                # the YAML sequences used in these files (\\ and \"). The NUL
                # placeholder keeps the two passes from interfering.
                value = value[1:-1]
                value = value.replace('\\\\', '\x00').replace('\\"', '"').replace('\x00', '\\')
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


def sibling_page_url(page, lang, root_path, exists):
    """Relative URL to a top-level page from inside a /docs/ directory.

    `changelog` and `support` are not translated into every language the docs
    are. When the page is missing for `lang`, fall back to the default-language
    one at the site root instead of linking to a 404.
    """
    if lang == DEFAULT_LANG or lang in exists:
        return f'../{page}.html'
    return f'{root_path}{page}.html'


def doc_langs(slug, langs):
    """Languages that actually carry a translation of `slug`.

    A guide is published in a language only when `_docs/{slug}/{lang}.md`
    exists. No fallback to the default language: serving French text under a
    Spanish URL is worse than not serving the page at all, and it would tell
    search engines the translation exists. This is what lets a language be
    translated guide by guide instead of all at once.
    """
    return [
        lang for lang in sorted(langs)
        if os.path.isfile(os.path.join(DOCS_DIR, slug, f'{lang}.md'))
    ]


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

    # Languages that actually have a changelog / support page, so the doc
    # nav can fall back instead of pointing at a page that was never built.
    changelog_langs = {
        f[:-3] for f in os.listdir(CHANGELOG_DIR) if f.endswith('.md')
    } if os.path.isdir(CHANGELOG_DIR) else set()
    support_dir = os.path.join(I18N_DIR, 'support')
    support_langs = {
        f[:-4] for f in os.listdir(support_dir) if f.endswith('.yml')
    } if os.path.isdir(support_dir) else set()

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
                # Not translated in this language yet: skip it entirely
                # (see doc_langs), never publish the default-language body.
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
            translated = doc_langs(slug, all_langs)
            hreflang = build_doc_hreflang(slug, translated)
            switcher = build_doc_switcher(
                slug, {l: all_ui[l] for l in translated}, lang, root_path
            )

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
            html = html.replace('{{nav_blog}}', ui.get('nav_blog', 'Blog'))
            html = html.replace('{{nav_changelog}}', ui.get('nav_changelog', 'Changelog'))
            html = html.replace('{{lang_label}}', ui.get('lang_label', 'Language'))
            html = html.replace('{{help_title}}', ui.get('help_title', ''))
            html = html.replace('{{help_desc}}', ui.get('help_desc', ''))
            html = html.replace('{{help_cta}}', ui.get('help_cta', ''))
            html = html.replace(
                '{{changelog_url}}',
                sibling_page_url('changelog', lang, root_path, changelog_langs),
            )
            html = html.replace(
                '{{support_url}}',
                sibling_page_url('support', lang, root_path, support_langs),
            )

            doc_schema = build_doc_schema(slug, lang, meta)
            html = finalize_html(html, lang, 'en' in all_ui, doc_schema)

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
        html = html.replace('{{nav_blog}}', ui.get('nav_blog', 'Blog'))
        html = html.replace('{{nav_changelog}}', ui.get('nav_changelog', 'Changelog'))
        html = html.replace('{{lang_label}}', ui.get('lang_label', 'Language'))
        html = html.replace('{{help_title}}', ui.get('help_title', ''))
        html = html.replace('{{help_desc}}', ui.get('help_desc', ''))
        html = html.replace('{{help_cta}}', ui.get('help_cta', ''))
        html = html.replace(
            '{{changelog_url}}',
            sibling_page_url('changelog', lang, root_path, changelog_langs),
        )
        html = html.replace(
            '{{support_url}}',
            sibling_page_url('support', lang, root_path, support_langs),
        )

        html = finalize_html(html, lang, 'en' in all_ui)

        index_file = os.path.join(out_dir, 'index.html')
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'  {os.path.relpath(index_file, SITE_DIR)}')
        total += 1

    return total


def changelog_url(lang):
    """URL path for the changelog page."""
    if lang == DEFAULT_LANG:
        return '/changelog.html'
    return f'/{lang}/changelog.html'


def changelog_output_path(lang):
    """Filesystem path for the generated changelog page."""
    if lang == DEFAULT_LANG:
        return os.path.join(SITE_DIR, 'changelog.html')
    out_dir = os.path.join(SITE_DIR, lang)
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, 'changelog.html')


def build_changelog_hreflang(langs):
    """Build hreflang tags for the changelog page."""
    tags = []
    for lang in sorted(langs):
        tags.append(f'    <link rel="alternate" hreflang="{lang}" href="{BASE_URL}{changelog_url(lang)}">')
    tags.append(f'    <link rel="alternate" hreflang="x-default" href="{BASE_URL}{changelog_url(DEFAULT_LANG)}">')
    return '\n'.join(tags)


def build_changelog_switcher(all_meta, current_lang):
    """Language switcher for the changelog page."""
    opts = []
    for lang in sorted(all_meta):
        name = all_meta[lang].get('lang_name', lang.upper())
        sel = ' selected' if lang == current_lang else ''
        if current_lang == DEFAULT_LANG:
            url = f'{lang}/changelog.html' if lang != DEFAULT_LANG else 'changelog.html'
        elif lang == DEFAULT_LANG:
            url = '../changelog.html'
        elif lang == current_lang:
            url = 'changelog.html'
        else:
            url = f'../{lang}/changelog.html'
        opts.append(f'            <option value="{url}"{sel}>{name}</option>')
    return '\n'.join(opts)


def build_version_nav(html_content):
    """Extract h2 headings from changelog HTML and build a sidebar nav."""
    headings = re.findall(r'<h2 id="([^"]+)">([^<]+)', html_content)
    lines = []
    for anchor, label in headings:
        # Strip the <small> part — label is just the version number
        lines.append(f'                <a href="#{anchor}">{label.strip()}</a>')
    return '\n'.join(lines)


def build_changelog():
    """Build changelog page from _changelog/ Markdown files."""
    import markdown

    if not os.path.isdir(CHANGELOG_DIR):
        return 0

    tpl_path = os.path.join(TEMPLATE_DIR, '_changelog.html')
    if not os.path.isfile(tpl_path):
        print('WARNING: _changelog.html template not found, skipping changelog.')
        return 0

    with open(tpl_path, encoding='utf-8') as f:
        template = f.read()

    # Discover languages from Markdown files in _changelog/
    all_meta = {}
    all_body = {}
    for fname in sorted(os.listdir(CHANGELOG_DIR)):
        if not fname.endswith('.md'):
            continue
        lang = fname[:-3]
        md_path = os.path.join(CHANGELOG_DIR, fname)
        with open(md_path, encoding='utf-8') as f:
            raw = f.read()
        meta, body = parse_frontmatter(raw)
        all_meta[lang] = meta
        all_body[lang] = body

    if not all_meta:
        return 0

    all_langs = sorted(all_meta.keys())
    hreflang = build_changelog_hreflang(all_langs)

    md = markdown.Markdown(extensions=['fenced_code', 'tables', 'toc'])

    total = 0
    print(f'\n--- Changelog ---')

    for lang in all_langs:
        meta = all_meta[lang]
        body = all_body[lang]
        root = '' if lang == DEFAULT_LANG else '../'

        md.reset()
        content_html = md.convert(body)

        # Replace toc-generated ids with clean version-only anchors
        def clean_h2_id(m):
            old_id = m.group(1)
            text = m.group(2)
            # Extract version number (before <small>)
            version = re.sub(r'\s*<small>.*', '', text).strip()
            anchor = re.sub(r'[^a-z0-9]+', '-', version.lower()).strip('-')
            return f'<h2 id="{anchor}">{text}</h2>'

        content_html = re.sub(r'<h2 id="([^"]*)">(.*?)</h2>', clean_h2_id, content_html)

        version_nav = build_version_nav(content_html)
        switcher = build_changelog_switcher(all_meta, lang)

        html = template
        html = html.replace('{{root}}', root)
        html = html.replace('{{lang}}', lang)
        html = html.replace('{{canonical_url}}', BASE_URL + changelog_url(lang))
        html = html.replace('{{hreflang}}', hreflang)
        html = html.replace('{{og_locale}}', OG_LOCALES.get(lang, lang))
        html = html.replace('{{lang_switcher}}', switcher)
        html = html.replace('{{version_nav}}', version_nav)
        html = html.replace('{{content}}', content_html)
        html = html.replace('{{breadcrumb_home}}', BASE_URL + page_url('index', lang))
        html = html.replace('{{nav_site_label}}', meta.get('nav_site_label', 'Main navigation'))

        # Replace all remaining {{key}} placeholders from frontmatter
        for key, value in meta.items():
            html = html.replace(f'{{{{{key}}}}}', value)

        html = finalize_html(html, lang, 'en' in all_meta)

        out_file = changelog_output_path(lang)
        with open(out_file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'  {os.path.relpath(out_file, SITE_DIR)}')
        total += 1

    return total


def parse_toml_frontmatter(text):
    """Parse Zola-style TOML frontmatter (between +++ markers)."""
    if not text.startswith('+++'):
        return {}, text
    end = text.find('+++', 3)
    if end == -1:
        return {}, text
    fm_text = text[3:end].strip()
    body = text[end + 3:].strip()
    meta = {}
    for line in fm_text.split('\n'):
        line = line.strip()
        if not line or line.startswith('#') or line.startswith('['):
            continue
        idx = line.find(' = ')
        if idx == -1:
            continue
        key = line[:idx].strip()
        value = line[idx + 3:].strip()
        if len(value) >= 2 and value[0] == '"' and value[-1] == '"':
            value = value[1:-1]
        meta[key] = value
    return meta, body


def format_blog_date(date_str, lang):
    """Format a YYYY-MM-DD date string for the given language."""
    dt = datetime.strptime(date_str, '%Y-%m-%d')
    months = MONTH_NAMES.get(lang, MONTH_NAMES['fr'])
    month = months[dt.month - 1]
    if lang == 'en':
        return f'{month} {dt.day}, {dt.year}'
    if lang == 'de':
        return f'{dt.day}. {month} {dt.year}'
    return f'{dt.day} {month} {dt.year}'


def get_latest_blog_post(lang):
    """Get the latest blog post metadata for a given language.

    Falls back to the default language if no post exists for the requested lang.
    Returns a dict with title, description, date, slug, blog_lang or None.
    """
    if not os.path.isdir(BLOG_CONTENT_DIR):
        return None

    def _scan_posts(target_lang):
        posts = []
        for fname in os.listdir(BLOG_CONTENT_DIR):
            if fname.startswith('_'):
                continue
            if target_lang == DEFAULT_LANG:
                # Default-lang files have no language suffix: slug.md
                if not fname.endswith('.md'):
                    continue
                base = fname[:-3]
                if '.' in base:
                    continue  # Skip language-specific files like slug.en.md
            else:
                suffix = f'.{target_lang}.md'
                if not fname.endswith(suffix):
                    continue
                base = fname[:-len(suffix)]

            filepath = os.path.join(BLOG_CONTENT_DIR, fname)
            with open(filepath, encoding='utf-8') as f:
                raw = f.read()
            meta, _ = parse_toml_frontmatter(raw)
            if 'date' not in meta or 'title' not in meta:
                continue
            slug = meta.get('slug', base)
            posts.append({
                'title': meta['title'],
                'description': meta.get('description', ''),
                'date': meta['date'],
                'slug': slug,
                'blog_lang': target_lang,
            })
        posts.sort(key=lambda p: p['date'], reverse=True)
        return posts[0] if posts else None

    post = _scan_posts(lang)
    if post is None and lang != DEFAULT_LANG:
        post = _scan_posts(DEFAULT_LANG)
    return post


def blog_post_relative_url(post, current_lang):
    """Compute relative blog post URL from the homepage of current_lang."""
    blog_lang = post['blog_lang']
    slug = post['slug']
    if blog_lang == DEFAULT_LANG:
        blog_path = f'blog/{slug}/'
    else:
        blog_path = f'blog/{blog_lang}/{slug}/'
    if current_lang == DEFAULT_LANG:
        return blog_path
    return f'../{blog_path}'


def load_app_version():
    """Load app version from version.txt."""
    if os.path.isfile(VERSION_FILE):
        with open(VERSION_FILE, encoding='utf-8') as f:
            return f.read().strip()
    return ''


def _mtime_date(*paths):
    """Most recent mtime among existing paths as YYYY-MM-DD; today if none exist."""
    stamps = []
    for p in paths:
        try:
            stamps.append(os.path.getmtime(p))
        except OSError:
            continue
    if not stamps:
        return datetime.now().strftime('%Y-%m-%d')
    return datetime.fromtimestamp(max(stamps)).strftime('%Y-%m-%d')


def _sitemap_main_entries():
    """(loc, lastmod, priority) for every translated top-level page."""
    entries = []
    pages = discover_pages()
    for page in sorted(pages):
        if page in SITEMAP_EXCLUDE:
            continue
        priority = SITEMAP_PRIORITY.get(page, '0.5')
        for lang in sorted(pages[page]['langs']):
            src = os.path.join(I18N_DIR, page, f'{lang}.yml')
            entries.append((BASE_URL + page_url(page, lang), _mtime_date(src), priority))
    return entries


def _sitemap_doc_entries():
    """(loc, lastmod, priority) for doc pages and per-language doc indexes."""
    entries = []
    ui_dir = os.path.join(DOCS_DIR, '_ui')
    if not os.path.isdir(DOCS_DIR) or not os.path.isdir(ui_dir):
        return entries
    langs = sorted(f[:-4] for f in os.listdir(ui_dir) if f.endswith('.yml'))
    sections = sorted(
        e for e in os.listdir(DOCS_DIR)
        if not e.startswith(('_', '.')) and os.path.isdir(os.path.join(DOCS_DIR, e))
    )
    for lang in langs:
        index_sources = []
        for slug in sections:
            src = os.path.join(DOCS_DIR, slug, f'{lang}.md')
            if not os.path.isfile(src):
                continue
            entries.append((BASE_URL + doc_url(slug, lang), _mtime_date(src), DOC_PRIORITY))
            index_sources.append(src)
        if index_sources:
            entries.append((BASE_URL + doc_index_url(lang), _mtime_date(*index_sources), DOC_INDEX_PRIORITY))
    return entries


def _sitemap_changelog_entries():
    """(loc, lastmod, priority) for each translated changelog page."""
    entries = []
    if not os.path.isdir(CHANGELOG_DIR):
        return entries
    for fname in sorted(os.listdir(CHANGELOG_DIR)):
        if not fname.endswith('.md'):
            continue
        lang = fname[:-3]
        src = os.path.join(CHANGELOG_DIR, fname)
        entries.append((BASE_URL + changelog_url(lang), _mtime_date(src), SITEMAP_PRIORITY.get('changelog', '0.6')))
    return entries


def _sitemap_blog_entries():
    """(loc, lastmod, priority) for each published blog post, using frontmatter dates."""
    entries = []
    if not os.path.isdir(BLOG_CONTENT_DIR):
        return entries
    for fname in sorted(os.listdir(BLOG_CONTENT_DIR)):
        if fname.startswith('_') or not fname.endswith('.md'):
            continue
        base = fname[:-3]
        if '.' in base:
            slug_part, lang = base.rsplit('.', 1)
        else:
            slug_part, lang = base, DEFAULT_LANG
        with open(os.path.join(BLOG_CONTENT_DIR, fname), encoding='utf-8') as f:
            meta, _ = parse_toml_frontmatter(f.read())
        if meta.get('draft') == 'true' or 'date' not in meta:
            continue
        slug = meta.get('slug', slug_part)
        if lang == DEFAULT_LANG:
            loc = f'{BASE_URL}/blog/{slug}/'
        else:
            loc = f'{BASE_URL}/blog/{lang}/{slug}/'
        entries.append((loc, meta.get('updated', meta['date']), BLOG_PRIORITY))
    return entries


def build_sitemap():
    """Generate sitemap.xml covering pages, docs, changelog and blog posts."""
    entries = (
        _sitemap_main_entries()
        + _sitemap_doc_entries()
        + _sitemap_changelog_entries()
        + _sitemap_blog_entries()
    )

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for loc, lastmod, priority in entries:
        lines.append('  <url>')
        lines.append(f'    <loc>{loc}</loc>')
        lines.append(f'    <lastmod>{lastmod}</lastmod>')
        lines.append(f'    <priority>{priority}</priority>')
        lines.append('  </url>')
    lines.append('</urlset>')
    lines.append('')

    with open(SITEMAP_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f'\n--- Sitemap ---\n  sitemap.xml ({len(entries)} URLs)')
    return len(entries)


def build():
    filter_pages = set(sys.argv[1:]) if len(sys.argv) > 1 else None
    pages = discover_pages(filter_pages)

    if not pages:
        print('No pages found. Check _build/templates/ and _i18n/ directories.')
        sys.exit(1)

    app_version = load_app_version()
    if app_version:
        print(f'App version: {app_version}')

    # Collect all page language sets for cross-page URL resolution
    all_page_langs = {name: set(info['langs'].keys()) for name, info in pages.items()}

    # Register changelog languages so {{url:changelog}} resolves in templates
    changelog_langs = set()
    if os.path.isdir(CHANGELOG_DIR):
        for f in os.listdir(CHANGELOG_DIR):
            if f.endswith('.md'):
                changelog_langs.add(f[:-3])
    if changelog_langs:
        all_page_langs['changelog'] = changelog_langs

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
            html = html.replace('{{app_version}}', app_version)
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

            # Inject latest blog post data for the index page
            if page_name == 'index':
                post = get_latest_blog_post(lang)
                if post:
                    html = html.replace('{{blog_post_title}}', post['title'])
                    html = html.replace('{{blog_post_description}}', post['description'])
                    html = html.replace('{{blog_post_date}}', format_blog_date(post['date'], lang))
                    html = html.replace('{{blog_post_url}}', blog_post_relative_url(post, lang))

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

            page_schema = build_page_schema(page_name, lang, t)
            html = finalize_html(html, lang, 'en' in langs, page_schema)

            out = output_path(page_name, lang)
            with open(out, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f'  {os.path.relpath(out, SITE_DIR)}')
            total += 1

    # Build documentation pages
    doc_count = build_docs()
    total += doc_count

    # Build changelog
    changelog_count = build_changelog()
    total += changelog_count

    # Regenerate sitemap.xml (always scans the full source tree, even on a
    # filtered build, so it never drifts out of sync with published pages).
    build_sitemap()

    print(f'\nDone! {total} pages generated.')


if __name__ == '__main__':
    build()
