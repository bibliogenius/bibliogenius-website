# BiblioGenius Website

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](https://www.gnu.org/licenses/agpl-3.0.html)
[![Status](https://img.shields.io/badge/status-live-success)](https://bibliogenius.org)

Public website for [bibliogenius.org](https://bibliogenius.org) - app showcase, documentation, and project story.

## Prerequisites

- Python 3
- `pip install markdown` (used for doc generation)

## Project structure

```
_build/
  build.py              # Build script: templates + YAML/Markdown -> HTML
  templates/
    index.html          # Homepage template
    story.html          # "Our Story" page template
    contribute.html     # Contribute page template
    free-your-library.html
    tutorials.html
    _doc.html           # Doc article template (prefix _ = not a page)
    _doc-index.html     # Doc index template

_i18n/
  {page}/{lang}.yml     # Translations per page (fr, en, es, de)

_docs/
  {slug}/{lang}.md      # Documentation guides (Markdown + frontmatter)
  {slug}/images/        # Screenshots for that guide
  _ui/{lang}.yml        # Shared UI strings for doc pages (sidebar, nav, footer)

assets/                 # CSS, images, fonts
docs/                   # Generated doc HTML (do not edit)
{lang}/                 # Generated translated pages (do not edit)
```

French (`fr`) is the default language. French pages are generated at the site root; other languages go into `/{lang}/` subdirectories.

## Quick start

```bash
make build    # Generate all HTML from templates + translations
make serve    # Local dev server at http://localhost:8000
```

You can also build a single page: `python3 _build/build.py story`

## Common workflows

### Edit an existing page

1. Modify the YAML values in `_i18n/{page}/{lang}.yml` (keep HTML tags as-is)
2. Run `make build`

To change the page layout or structure, edit `_build/templates/{page}.html`. Placeholders use `{{key}}` syntax, resolved from the YAML translations.

### Add a new language

```bash
make new LANG=pt        # Creates _i18n/story/pt.yml from the French reference
```

For full coverage, also copy the YAML files for each page directory under `_i18n/` and translate them. Then `make build`.

### Add or edit a documentation guide

Docs live in `_docs/{slug}/{lang}.md` with YAML frontmatter:

```yaml
---
title: How to add a book
description: Guide for adding books by scan, search, or manual entry
order: 1
group: library
---

Markdown content here...
```

Available groups: `library`, `discovery`, `social`, `advanced`, `data`.

To add a new guide: create `_docs/{slug}/fr.md` (and other languages), add images in `_docs/{slug}/images/`, then `make build`.

### Add a new page (not a doc)

1. Create `_build/templates/{page}.html` with `{{key}}` placeholders
2. Create `_i18n/{page}/` with at least `fr.yml`
3. Run `make build`

Cross-page links use `{{url:page_name}}` - the build script resolves them to correct relative paths per language.

## Deployment

Push to `main`. GitHub Pages serves the site automatically.

Generated files (`docs/`, `{lang}/`, root HTML) are committed to the repo since GitHub Pages serves static files directly.

## Cleanup

```bash
make clean    # Remove generated language subdirectories (keeps French root files)
```

## Related repositories

- [bibliogenius](https://github.com/bibliogenius/bibliogenius) - Rust backend
- [bibliogenius-app](https://github.com/bibliogenius/bibliogenius-app) - Flutter frontend

## License

This project is licensed under the [GNU AGPL-3.0](https://www.gnu.org/licenses/agpl-3.0.html).
