"""Unit tests for the changelog scaffolding helpers.

Run: python3 _build/test_changelog.py
"""
import datetime as dt
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import changelog as cl  # noqa: E402

FRONTMATTER = "---\ntitle: Changelog\n---\n\n"
SECTION_119 = (
    "## 1.1.9 <small>3 septembre 2026</small> &nbsp; <a href=\"x\">diff</a>\n\n"
    "- **Import** : lu\n\n"
)
SECTION_118 = (
    "## 1.1.8 <small>1er septembre 2026</small> &nbsp; <a href=\"y\">diff</a>\n\n"
    "- **Fiche livre** : ok\n"
)


class ParseTagTests(unittest.TestCase):
    def test_stable_tag(self):
        self.assertEqual(cl.parse_tag('v1.1.9'), ((1, 1, 9), cl.STABLE))

    def test_prerelease_tag(self):
        self.assertEqual(cl.parse_tag('v1.1.8-beta.3'), ((1, 1, 8), (0, 'beta', 3)))

    def test_prerelease_sorts_before_stable(self):
        self.assertLess(cl.parse_tag('v1.1.8-beta.3')[1], cl.parse_tag('v1.1.8')[1])

    def test_foreign_tag_is_ignored(self):
        self.assertIsNone(cl.parse_tag('hub-2.0'))
        self.assertIsNone(cl.parse_tag('1.1.9'))


class ReleaseTagTests(unittest.TestCase):
    TAGS = ['v1.1.7-beta.0', 'v1.1.7-beta.1', 'v1.1.8-beta.0', 'v1.1.9-beta.0',
            'v1.1.9', 'v1.1.10', 'hub-1.0']

    def test_one_release_tag_per_version_newest_prerelease_or_stable(self):
        self.assertEqual(cl.release_tags(self.TAGS), {
            (1, 1, 7): 'v1.1.7-beta.1',
            (1, 1, 8): 'v1.1.8-beta.0',
            (1, 1, 9): 'v1.1.9',
            (1, 1, 10): 'v1.1.10',
        })

    def test_previous_release_tag_follows_version_order(self):
        rel = cl.release_tags(self.TAGS)
        self.assertEqual(cl.previous_tag(rel, (1, 1, 9)), 'v1.1.8-beta.0')
        self.assertEqual(cl.previous_tag(rel, (1, 1, 10)), 'v1.1.9')
        # An unreleased version still gets the newest tag below it.
        self.assertEqual(cl.previous_tag(rel, (1, 1, 11)), 'v1.1.10')
        self.assertIsNone(cl.previous_tag(rel, (1, 1, 7)))


class DateFormatTests(unittest.TestCase):
    def test_french(self):
        self.assertEqual(cl.format_date(dt.date(2026, 9, 3), 'fr'), '3 septembre 2026')
        self.assertEqual(cl.format_date(dt.date(2026, 9, 1), 'fr'), '1er septembre 2026')
        self.assertEqual(cl.format_date(dt.date(2026, 8, 29), 'fr'), '29 août 2026')

    def test_english(self):
        self.assertEqual(cl.format_date(dt.date(2026, 9, 3), 'en'), 'September 3, 2026')

    def test_unknown_language_falls_back_to_iso(self):
        self.assertEqual(cl.format_date(dt.date(2026, 9, 3), 'pt'), '2026-09-03')


class DocumentedVersionsTests(unittest.TestCase):
    def test_reads_h2_versions(self):
        text = FRONTMATTER + SECTION_119 + SECTION_118
        self.assertEqual(cl.documented_versions(text), {(1, 1, 9), (1, 1, 8)})

    def test_empty_changelog(self):
        self.assertEqual(cl.documented_versions(FRONTMATTER), set())


class RenderSectionTests(unittest.TestCase):
    def test_header_matches_existing_convention(self):
        section = cl.render_section(
            version=(1, 1, 10), tag='v1.1.10', prev_tag='v1.1.9',
            date=dt.date(2026, 9, 10), lang='fr',
            commits={'bibliogenius-app': ['abc1234 fix: thing']})
        self.assertTrue(section.startswith(
            '## 1.1.10 <small>10 septembre 2026</small> &nbsp; '
            '<a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/'
            'v1.1.9...v1.1.10" class="changelog-link">diff</a> · '
            '<a href="https://codeberg.org/bibliogenius/bibliogenius-app/releases/tag/'
            'v1.1.10" class="changelog-link">release</a>\n'))
        self.assertIn(cl.DRAFT_MARKER, section)
        self.assertIn('abc1234 fix: thing', section)
        self.assertTrue(section.endswith('\n\n'))

    def test_first_release_has_no_diff_link(self):
        section = cl.render_section(
            version=(1, 0, 0), tag='v1.0.0', prev_tag=None,
            date=dt.date(2026, 1, 1), lang='en', commits={})
        self.assertNotIn('compare/', section)
        self.assertIn('releases/tag/v1.0.0', section)


class InsertSectionsTests(unittest.TestCase):
    def test_new_sections_go_newest_first_before_existing_ones(self):
        text = FRONTMATTER + SECTION_119
        s10 = '## 1.1.10 <small>d</small>\n\n- a\n\n'
        s11 = '## 1.1.11 <small>d</small>\n\n- b\n\n'
        out = cl.insert_sections(text, [s10, s11])
        self.assertEqual(out, FRONTMATTER + s11 + s10 + SECTION_119)

    def test_insert_into_changelog_without_sections(self):
        out = cl.insert_sections(FRONTMATTER.rstrip('\n') + '\n', ['## 1.0.0\n\n- a\n\n'])
        self.assertEqual(out, FRONTMATTER + '## 1.0.0\n\n- a\n\n')


class CheckSectionTests(unittest.TestCase):
    def test_written_section_passes(self):
        text = FRONTMATTER + SECTION_119 + SECTION_118
        self.assertIsNone(cl.check_section(text, (1, 1, 9)))
        self.assertIsNone(cl.check_section(text, (1, 1, 8)))

    def test_missing_section_fails(self):
        self.assertEqual(cl.check_section(FRONTMATTER + SECTION_119, (1, 1, 10)), 'missing')

    def test_draft_marker_fails(self):
        draft = cl.render_section(
            version=(1, 1, 10), tag='v1.1.10', prev_tag='v1.1.9',
            date=dt.date(2026, 9, 10), lang='fr', commits={})
        text = cl.insert_sections(FRONTMATTER + SECTION_119, [draft])
        self.assertEqual(cl.check_section(text, (1, 1, 10)), 'draft')
        # The older, finished section is unaffected by the draft above it.
        self.assertIsNone(cl.check_section(text, (1, 1, 9)))

    def test_section_without_bullets_fails(self):
        text = FRONTMATTER + '## 1.1.10 <small>d</small>\n\n' + SECTION_119
        self.assertEqual(cl.check_section(text, (1, 1, 10)), 'empty')


if __name__ == '__main__':
    unittest.main()
