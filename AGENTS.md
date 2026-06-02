# BiblioGenius Website - Agent Instructions

Anyone (human or AI) editing this repo: **read this before changing any HTML.**
For project structure and build commands, see [README.md](README.md).

## ⚠️ Source of truth vs. generated files

This site uses a Python build script (`_build/build.py`) that **renders the
final HTML from YAML translations and HTML templates**. Most `.html` files at
the repo root, under `{lang}/`, and under `docs/` are **build outputs, not
source**. Editing them directly is a trap: the next `make build` (or
contributor's local rebuild) silently reverts your change.

### Editing existing page copy (text, slogans, descriptions, alt-text)

| You want to change... | Edit this | NOT this |
|---|---|---|
| Homepage hero, features, CTAs | `_i18n/index/{lang}.yml` | `index.html`, `{lang}/index.html` |
| "Our story" page copy | `_i18n/story/{lang}.yml` | `story.html`, `{lang}/story.html` |
| "Contribute" page copy | `_i18n/contribute/{lang}.yml` | `contribute.html`, `{lang}/contribute.html` |
| Any other top-level page | `_i18n/{page}/{lang}.yml` | `{page}.html`, `{lang}/{page}.html` |
| Documentation guide content | `_docs/{slug}/{lang}.md` (Markdown + frontmatter) | `docs/{slug}.html`, `{lang}/docs/{slug}.html` |
| Shared doc UI strings (sidebar, nav) | `_docs/_ui/{lang}.yml` | (none, applied at build time) |
| Page layout / new placeholder slot | `_build/templates/{page}.html` | the generated `{page}.html` files |

After editing, run `make build` to regenerate. Commit both the source change
and the regenerated HTML in the same commit (or in a follow-up `chore: regen`
commit, see existing history for the convention).

### Editing the blog

The blog is in a different system: **Zola** (Rust static site generator) in
`_blog/`.

| You want to change... | Edit this | NOT this |
|---|---|---|
| Blog post content | `_blog/content/{slug}.{lang}.md` | `_blog/public/...`, `blog/...` |
| Blog template / layout | `_blog/templates/*.html` | the generated output |

After editing, run `make blog` (or `make build` which also runs Zola), which
regenerates `_blog/public/` and mirrors it to `blog/`. Both are committed.

### Quick check before editing any HTML

If you're about to open an `.html` file and edit text, **first grep for the
text in `_i18n/`, `_docs/`, and `_blog/content/`**:

```bash
grep -rn "the exact phrase you want to change" _i18n/ _docs/ _blog/content/
```

If the phrase is found in one of those, that's the source. Edit there.
If it's not found, you may be editing a hand-written page (rare) — in that
case the HTML is the source. Confirm with the user before proceeding.

### Why this matters (recorded lesson)

In June 2026, an agent edited the "Sans cloud, sans compte. Open Source."
tagline directly in `index.html`, `en/index.html`, `es/index.html` and
`de/index.html`. The change looked applied, was committed, but the YAML
source (`_i18n/index/{lang}.yml`) still held the old wording. The user
noticed because the source code still showed the old text. Any subsequent
`make build` would have silently reverted the published HTML.

The rule: **never edit a generated file. Always trace the text back to its
YAML/Markdown source first.**

## Other guidance

- French (`fr`) is the default language; FR pages live at the site root, other
  languages at `{lang}/`.
- Keep HTML tags inside YAML values intact (`<br>`, `<span class="...">`, etc.)
  - they get inlined verbatim into the template.
- For deployment workflow, see the `deploy` target in [Makefile](Makefile).
- The deploy uses an SSH alias `hub-vps` defined in the user's local SSH config
  - not hardcoded in this repo.
