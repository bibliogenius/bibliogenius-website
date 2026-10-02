#!/usr/bin/env python3
"""Scaffold and check the website changelog (_changelog/{lang}.md).

The changelog text is editorial and stays hand-written. What this script
automates is the mechanical part: the section header (version, date, diff and
release links computed from the app repo's tags) and the raw commit list to
rewrite, dropped in as an HTML comment that must be removed once the section
is written.

Usage (from the workspace root, via the Makefile):
  changelog.py                 scaffold every tagged version newer than the
                               newest documented one (gap fill)
  changelog.py 1.1.12          scaffold that version (tag may not exist yet:
                               dated today, commits since the previous tag)
  changelog.py --check 1.1.12  fail unless the section exists in every
                               language file, is written, and no draft
                               comment is left
  changelog.py --latest        print the newest tagged version
"""
import datetime as dt
import os
import re
import subprocess
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_DIR = os.path.dirname(SCRIPT_DIR)
CHANGELOG_DIR = os.path.join(SITE_DIR, '_changelog')
DEFAULT_LANG = 'fr'

# Sibling checkouts of the workspace. The compare/release links point at the
# app repo, which is also where the tags that define a version live.
WORKSPACE_DIR = os.path.dirname(SITE_DIR)
APP_REPO = os.path.join(WORKSPACE_DIR, 'bibliogenius-app')
COMMIT_REPOS = ['bibliogenius-app', 'bibliogenius']

REPO_URL = 'https://codeberg.org/bibliogenius/bibliogenius-app'
DRAFT_MARKER = 'changelog-draft'

TAG_RE = re.compile(r'^v(\d+)\.(\d+)\.(\d+)(?:-([A-Za-z]+)\.?(\d+)?)?$')
H2_RE = re.compile(r'^## (\d+)\.(\d+)\.(\d+)\b', re.MULTILINE)

# Sort key for the prerelease part: a stable tag ranks above any prerelease
# of the same version, so "v1.1.9" beats "v1.1.9-beta.0".
STABLE = (1,)

MONTHS = {
    'fr': ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet',
           'août', 'septembre', 'octobre', 'novembre', 'décembre'],
    'en': ['January', 'February', 'March', 'April', 'May', 'June', 'July',
           'August', 'September', 'October', 'November', 'December'],
}


# --- Pure helpers (unit-tested in test_changelog.py) -------------------------

def parse_tag(tag):
    """Split 'v1.1.8-beta.3' into ((1, 1, 8), (0, 'beta', 3)); None if foreign."""
    m = TAG_RE.match(tag)
    if not m:
        return None
    base = (int(m.group(1)), int(m.group(2)), int(m.group(3)))
    if m.group(4) is None:
        return base, STABLE
    return base, (0, m.group(4), int(m.group(5) or 0))


def release_tags(tags):
    """Map each version to the tag that released it.

    Historically a version could ship from a prerelease tag ("1.1.8" shipped
    as v1.1.8-beta.0); the newest tag of a version is the one the changelog
    links to.
    """
    best = {}
    for tag in tags:
        parsed = parse_tag(tag)
        if parsed is None:
            continue
        base, pre = parsed
        if base not in best or pre > best[base][0]:
            best[base] = (pre, tag)
    return {base: tag for base, (_, tag) in best.items()}


def previous_tag(releases, version):
    """Release tag of the newest version strictly below `version`, if any."""
    older = [v for v in releases if v < version]
    return releases[max(older)] if older else None


def format_date(date, lang):
    months = MONTHS.get(lang)
    if months is None:
        return date.isoformat()
    month = months[date.month - 1]
    if lang == 'fr':
        day = '1er' if date.day == 1 else str(date.day)
        return f'{day} {month} {date.year}'
    return f'{month} {date.day}, {date.year}'


def version_str(version):
    return '.'.join(str(n) for n in version)


def documented_versions(text):
    return {tuple(int(n) for n in m.groups()) for m in H2_RE.finditer(text)}


def render_section(version, tag, prev_tag, date, lang, commits):
    links = []
    if prev_tag:
        links.append(f'<a href="{REPO_URL}/compare/{prev_tag}...{tag}" '
                     'class="changelog-link">diff</a>')
    links.append(f'<a href="{REPO_URL}/releases/tag/{tag}" '
                 'class="changelog-link">release</a>')
    header = (f'## {version_str(version)} <small>{format_date(date, lang)}</small>'
              f' &nbsp; {" · ".join(links)}')

    draft = [f'<!-- {DRAFT_MARKER}: rewrite the commits below as user-facing '
             'bullets ("- **Area**: what changed for the reader"), then delete '
             'this whole comment. `make site` refuses to deploy while it is here.']
    for repo, lines in commits.items():
        draft.append(f'{repo}:')
        draft.extend(f'  {line}' for line in lines)
        if not lines:
            draft.append('  (no commits)')
    draft.append('-->')
    return header + '\n\n' + '\n'.join(draft) + '\n\n'


def insert_sections(text, sections):
    """Insert sections newest-first, right before the first existing one."""
    m = re.search(r'^## ', text, re.MULTILINE)
    block = ''.join(reversed(sections))
    if m:
        return text[:m.start()] + block + text[m.start():]
    if not text.endswith('\n\n'):
        text = text.rstrip('\n') + '\n\n'
    return text + block


def check_section(text, version):
    """None when the section is publishable, else 'missing', 'draft' or 'empty'."""
    start = re.search(rf'^## {re.escape(version_str(version))}\b', text, re.MULTILINE)
    if not start:
        return 'missing'
    rest = text[start.end():]
    nxt = re.search(r'^## ', rest, re.MULTILINE)
    body = rest[:nxt.start()] if nxt else rest
    if DRAFT_MARKER in body:
        return 'draft'
    if not re.search(r'^- ', body, re.MULTILINE):
        return 'empty'
    return None


# --- Git and filesystem --------------------------------------------------------

def git(repo, *args):
    return subprocess.run(['git', '-C', repo, *args], check=True,
                          capture_output=True, text=True).stdout


def app_tags():
    if not os.path.isdir(os.path.join(APP_REPO, '.git')):
        sys.exit(f'App repo not found at {APP_REPO}; run from the workspace checkout.')
    return git(APP_REPO, 'tag', '--list').split()


def tag_date(tag):
    return dt.date.fromisoformat(git(APP_REPO, 'log', '-1', '--format=%cs', tag).strip())


def tag_exists(repo, tag):
    return subprocess.run(['git', '-C', repo, 'rev-parse', '-q', '--verify', f'{tag}^{{commit}}'],
                          capture_output=True).returncode == 0


def commits_between(prev_tag, tag):
    """Commit subjects per repo, from prev_tag (exclusive) to tag, or HEAD when
    the tag is not laid yet."""
    out = {}
    for name in COMMIT_REPOS:
        repo = os.path.join(WORKSPACE_DIR, name)
        if not os.path.isdir(repo):
            continue
        upper = tag if tag_exists(repo, tag) else 'HEAD'
        if prev_tag and not tag_exists(repo, prev_tag):
            out[name] = [f'(previous tag {prev_tag} not found in this repo)']
            continue
        rng = f'{prev_tag}..{upper}' if prev_tag else upper
        log = git(repo, 'log', '--format=%h %s', '--no-merges', rng)
        out[name] = log.splitlines()
    return out


def changelog_files():
    files = sorted(f for f in os.listdir(CHANGELOG_DIR) if f.endswith('.md'))
    if not files:
        sys.exit(f'No changelog file in {CHANGELOG_DIR}.')
    return {f[:-3]: os.path.join(CHANGELOG_DIR, f) for f in files}


def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def write(path, text):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)


# --- Commands ------------------------------------------------------------------

def parse_version(arg):
    m = re.fullmatch(r'v?(\d+)\.(\d+)\.(\d+)', arg)
    if not m:
        sys.exit(f'Invalid version "{arg}", expected x.y.z')
    return tuple(int(n) for n in m.groups())


def cmd_latest():
    releases = release_tags(app_tags())
    if not releases:
        sys.exit('No version tag in the app repo.')
    print(version_str(max(releases)))


def cmd_scaffold(arg):
    files = changelog_files()
    reference = read(files[DEFAULT_LANG] if DEFAULT_LANG in files else next(iter(files.values())))
    documented = documented_versions(reference)
    releases = release_tags(app_tags())

    if arg:
        version = parse_version(arg)
        if version in documented:
            sys.exit(f'{version_str(version)} is already documented.')
        targets = [version]
    else:
        newest = max(documented) if documented else (0, 0, 0)
        targets = sorted(v for v in releases if v > newest)
        if not targets:
            print(f'Changelog is up to date (newest documented: {version_str(newest)}).')
            return

    sections = {lang: [] for lang in files}
    for version in targets:
        tag = releases.get(version, f'v{version_str(version)}')
        prev = previous_tag(releases, version)
        if version in releases:
            date = tag_date(tag)
        else:
            date = dt.date.today()
            print(f'Tag {tag} does not exist yet: dated today, commits up to HEAD.')
        commits = commits_between(prev, tag)
        for lang in files:
            sections[lang].append(render_section(version, tag, prev, date, lang, commits))
        print(f'Scaffolded {version_str(version)} ({prev or "first release"} -> {tag}, {date})')

    for lang, path in files.items():
        write(path, insert_sections(read(path), sections[lang]))
    print(f'Updated: {", ".join(os.path.relpath(p, SITE_DIR) for p in files.values())}')
    print('Now write the bullets and remove the draft comments.')


def cmd_check(arg):
    version = parse_version(arg)
    problems = []
    for lang, path in changelog_files().items():
        status = check_section(read(path), version)
        if status:
            problems.append(f'  {os.path.relpath(path, SITE_DIR)}: {status}')
    if problems:
        print(f'Changelog {version_str(version)} is not ready to publish:')
        print('\n'.join(problems))
        print('Run `make changelog` to scaffold it, then write the bullets and '
              'delete the draft comment.')
        sys.exit(1)
    print(f'Changelog {version_str(version)} OK in every language.')


def main(argv):
    if argv and argv[0] == '--latest':
        cmd_latest()
    elif argv and argv[0] == '--check':
        if len(argv) != 2:
            sys.exit('Usage: changelog.py --check x.y.z')
        cmd_check(argv[1])
    elif len(argv) <= 1:
        cmd_scaffold(argv[0] if argv else None)
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main(sys.argv[1:])
