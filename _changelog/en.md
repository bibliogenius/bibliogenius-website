---
title: Changelog
meta_description: "BiblioGenius version history: new features, fixes and improvements."
hero_title: Changelog
hero_subtitle: Version history and changes
nav_home: Home
nav_story: Our Story
nav_docs: Documentation
nav_contribute: Contribute
nav_blog: Blog
nav_changelog: Changelog
lang_label: Language
lang_name: English
footer_text: "BiblioGenius &mdash; Open Source, local, encrypted."
---

## 0.8.9 <small>April 8, 2026</small> &nbsp; <a href="https://github.com/bibliogenius/bibliogenius-app/compare/v0.8.8-beta.6...v0.8.9-beta.12" class="changelog-link">diff</a> · <a href="https://github.com/bibliogenius/bibliogenius-app/releases/tag/v0.8.9-beta.12" class="changelog-link">release</a>

- **Page count**: page count field on book details, add/edit forms and search
- **Configurable loan duration**: customize loan duration in settings
- **Book forms**: redesigned add/edit book forms for better UX
- **Network peers**: peer avatars (LAN and relay via hub), tap peer card to open library directly, peer list polish (status dot, skeleton, full-screen QR) and network screen UX
- **Relay robustness (5G/4G)**: reliable credential republish on reconnect, offline fallback, 502 circuit breaker, nodeId refresh, sync timeout
- **Hub profile**: profile recovery code, hardened Keychain backup, registration 401 back-off
- **Multi-device sync**: fixed synchronization of authors, notes, copies and metadata between linked devices
- **Search**: improved external source reliability, relevance scoring, protection against concurrent searches
- **i18n**: completed ES/DE translations (cover, loans, notes, recovery)
- **Security & stability**: sensitive logs gated in debug and identifiers redacted, Inventaire deserialization fix, localized default library name fix

## 0.8.8 <small>March 23, 2026</small> &nbsp; <a href="https://github.com/bibliogenius/bibliogenius-app/compare/v0.8.7-beta.3...v0.8.8-beta.6" class="changelog-link">diff</a> · <a href="https://github.com/bibliogenius/bibliogenius-app/releases/tag/v0.8.8-beta.6" class="changelog-link">release</a>

- **Multi-device sync (E2EE)**: end-to-end encrypted synchronization between linked devices, bidirectional pairing, backfill and deduplication
- **Book notes**: add notes to books with voice dictation support
- **Private books**: hide books from network peers
- **Book descriptions**: automatic retrieval from OpenLibrary and SUDOC
- **Hangman game**: new mini-game added to the games hub
- **Onboarding**: sequenced flash messages and welcome design overhaul
- **Stability**: fixed crashes on first launch and first scan, Android Keystore recovery

## 0.8.7 <small>March 17, 2026</small> &nbsp; <a href="https://github.com/bibliogenius/bibliogenius-app/compare/v0.8.6-alpha.6...v0.8.7-beta.3" class="changelog-link">diff</a> · <a href="https://github.com/bibliogenius/bibliogenius-app/releases/tag/v0.8.7-beta.3" class="changelog-link">release</a>

- **macOS DMG**: distribution via DMG with hardened runtime and resilient Keychain fallback
- **Device fingerprint**: register device model and fingerprint on the hub
- **Peer stability**: catalog refresh, offline cache, peer name persistence
- **Notifications**: complete UX overhaul, borrowed filter, peer name fix
- **Compatibility**: `ClipRect` fix for Flutter 3.38

## 0.8.6 <small>March 13, 2026</small> &nbsp; <a href="https://github.com/bibliogenius/bibliogenius-app/compare/v0.8.5-beta.6...v0.8.6-alpha.6" class="changelog-link">diff</a> · <a href="https://github.com/bibliogenius/bibliogenius-app/releases/tag/v0.8.6-alpha.3" class="changelog-link">release</a>

- **Unified hub catalog**: consistent rendering and faster peer library loading
- **Mass scan**: batch scanning feature with redirect to scanned shelf
- **Statistics**: enriched quantity and quality, colors harmonized with profile
- **Localization**: added Italian, Turkish fixes, i18n cleanup
- **UI**: logo, search toggle, bottom nav border, operation log dates

## 0.8.5 <small>March 7, 2026</small> &nbsp; <a href="https://github.com/bibliogenius/bibliogenius-app/compare/v0.8.4-alpha.4...v0.8.5-beta.6" class="changelog-link">diff</a> · <a href="https://github.com/bibliogenius/bibliogenius-app/tree/v0.8.5-beta.6" class="changelog-link">tag</a>

- **Activity feed**: new activity stream with "new" badges
- **Borrow management**: borrow requests, notification UX, tap-to-edit reading status badge
- **Network discovery**: cross-reference mDNS names with saved peers, 5G sync fallback
- **UI**: bottom navigation bar option, instant cover refresh, share quick action

## 0.8.4 <small>March 4, 2026</small> &nbsp; <a href="https://github.com/bibliogenius/bibliogenius-app/compare/v0.8.2-alpha.3...v0.8.4-alpha.4" class="changelog-link">diff</a> · <a href="https://github.com/bibliogenius/bibliogenius-app/tree/v0.8.4-alpha.4" class="changelog-link">tag</a>

- **Hub directory**: Explore screen, library follow/unfollow, incoming requests
- **Collections**: refactored to FFI direct, grouped in library view
- **Web browsing**: connect and browse peer libraries via web browser
- **Device sync**: sync safety module with review screen
- **Covers**: capture covers with device camera

## 0.8.2 <small>February 26, 2026</small> &nbsp; <a href="https://github.com/bibliogenius/bibliogenius-app/compare/v0.8.1-alpha.2...v0.8.2-alpha.3" class="changelog-link">diff</a> · <a href="https://github.com/bibliogenius/bibliogenius-app/tree/v0.8.2-alpha.3" class="changelog-link">tag</a>

- **Short invite links**: simplified profile sharing with short URL via the hub
- **Share button**: new profile share button
- **Accessibility**: accessibility prerequisites added (work in progress)

## 0.8.1 <small>February 25, 2026</small> &nbsp; <a href="https://github.com/bibliogenius/bibliogenius-app/compare/v0.8.0-alpha.2...v0.8.1-alpha.2" class="changelog-link">diff</a> · <a href="https://github.com/bibliogenius/bibliogenius-app/tree/v0.8.1-alpha.2" class="changelog-link">tag</a>

- **Memory game**: new mini-game using your library covers, with leaderboard and animations
- **Sliding puzzle**: cover-based puzzle game with dedicated screen and games hub
- **Help**: enriched help section
- **Translations**: added Portuguese and Turkish

## 0.8.0 <small>February 20, 2026</small> &nbsp; <a href="https://github.com/bibliogenius/bibliogenius-app/compare/v0.7.2-alpha.2...v0.8.0-alpha.2" class="changelog-link">diff</a> · <a href="https://github.com/bibliogenius/bibliogenius-app/tree/v0.8.0-alpha.2" class="changelog-link">tag</a>

- **End-to-end encryption (E2EE)**: QR code v2 key exchange, E2EE indicator in UI, encrypted loan requests
- **Relay hub**: relay hub settings UI and API integration
- **AGPL-3.0 license**: project relicensed to AGPL-3.0
- **CJK support**: fallback fonts for Japanese, Chinese and Korean, .po skeleton files
- **Languages**: added Bulgarian, regional variant support (pt-BR, zh-TW...)
- **Loans**: configurable auto-approve, pending request counter

## 0.7.2 <small>February 13, 2026</small> &nbsp; <a href="https://github.com/bibliogenius/bibliogenius-app/compare/v0.7.1-alpha.7...v0.7.2-alpha.2" class="changelog-link">diff</a> · <a href="https://github.com/bibliogenius/bibliogenius-app/tree/v0.7.2-alpha.2" class="changelog-link">tag</a>

- **Internationalization**: translations migrated to .po files, multi-language search
- **Theme**: theme customization in settings, default theme optimization
- **UX audit**: persona-based fixes, search deduplication, 4 major friction points resolved
- **Leaderboard**: fixed leaderboard display on profile and between peers

## 0.7.1 <small>February 10, 2026</small> &nbsp; <a href="https://github.com/bibliogenius/bibliogenius-app/compare/v0.7.0-alpha.1...v0.7.1-alpha.7" class="changelog-link">diff</a> · <a href="https://github.com/bibliogenius/bibliogenius-app/tree/v0.7.1-alpha.7" class="changelog-link">tag</a>

- **Leaderboard module**: gamification leaderboard across connected libraries

## 0.7.0 <small>February 6, 2026</small> &nbsp; <a href="https://github.com/bibliogenius/bibliogenius-app/compare/v0.6.6-alpha.4...v0.7.0-alpha.1" class="changelog-link">diff</a> · <a href="https://github.com/bibliogenius/bibliogenius-app/tree/v0.7.0-alpha.1" class="changelog-link">tag</a>

- **P2P discovery**: mDNS hostname.local fallback, removed 127.0.0.1 fallback
- **Clean architecture**: migrated Flutter screens to Repository pattern
- **Database path**: installation folder migration
- **Optimizations**: reading status, online search, import, peer caching

## 0.6.6 <small>January 25, 2026</small> &nbsp; <a href="https://github.com/bibliogenius/bibliogenius-app/compare/v0.6.5-alpha.21...v0.6.6-alpha.4" class="changelog-link">diff</a> · <a href="https://github.com/bibliogenius/bibliogenius-app/tree/v0.6.6-alpha.4" class="changelog-link">tag</a>

- **Borrowing and loans**: fixes and improvements to the borrowing feature
- **UX/UI**: improved empty states, avatar visibility management, search enhancement
- **Statistics**: statistics page and dashboard display improvements
- **Quick actions**: new quick actions button in the top banner
- **Simplified install**: removed setup wizard, auto-initialization, ES/DE support

## 0.6.5 <small>January 12, 2026</small> &nbsp; <a href="https://github.com/bibliogenius/bibliogenius-app/tree/v0.6.5-alpha.21" class="changelog-link">tag</a>

- **Initial alpha release**: personal library management, book add/scan, online search
- **Local network**: peer discovery via mDNS, neighbor library browsing
- **Interface**: dashboard, collections, shelves, profile with gamification badges
