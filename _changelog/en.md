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

## 1.0.2 <small>June 19, 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v1.0.1-beta.3...v1.0.2-beta.2" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/releases/tag/v1.0.2-beta.2" class="changelog-link">release</a>

- **QR scanning on macOS**: fixed the scanner camera for both pairing and adding contacts
- **macOS identity**: fixed a case where your library identity could get out of sync on Mac and break peer connections
- **Search**: clearer message about the Google Books quota, and your preferred search sources are now kept
- **Statistics**: more readable author leaderboard on mobile
- **Dashboard**: connected contacts are now counted in the Contacts stat
- **Settings**: clearer online-sharing screen, fixed contact field, removed a misleading detected-libraries count
- **Network**: the contacts loading screen now scrolls correctly in landscape
- **Activity**: section icon shown in the activity banner
- **Theme**: brighter top bar in the brand colors

## 1.0.1 <small>June 18, 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v1.0.0-beta.9...v1.0.1-beta.3" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/releases/tag/v1.0.1-beta.3" class="changelog-link">release</a>

- **Complete my library**: a new screen and dashboard card to fill in your books' missing data all at once (summary, publisher, pages, cover)
- **Settings**: clearer, task-oriented layout and settings that are easier to find through search
- **Pairing**: clearer error messages, a check that the other device is reachable, the screen stays awake during the process, and QR-code pairing
- **Network**: your contacts' catalogues stay more up to date and reliable, with honest sync feedback
- **Linked devices**: clearer behavior in the interface
- **Search**: summaries now take your reading languages into account
- **Statistics**: more readable blocks, better suited to mobile
- **Dashboard**: new "Go further" section
- **Cleanup**: removed an old import screen that was no longer needed

## 1.0.0 <small>May 4, 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.9.2-beta.3...v1.0.0-beta.1" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/releases/tag/v1.0.0-beta.1" class="changelog-link">release</a>

- **Local backup (ADR-037)**: new encrypted `.bgbackup` format, restore wizard with rollback card, auto-backup scheduler with status card, guardrails blocking every escape route after a successful restore, full-backup teaser, FR/EN/DE/ES translations
- **Settings**: backup promoted to top-level, flattened Content section, removed System accordion, directory folded into the proper section
- **Network**: incoming follow requests are shown even when the directory is disabled
- **Robustness**: sober production error fallback in place of the dev red screen
- **iOS permissions**: corrected microphone usage description, localized permission strings, clarified scope for `NSPhotoLibraryUsageDescription`
- **Android permissions**: declared `RECORD_AUDIO` and the `RecognitionService` query for voice dictation

## 0.9.2 <small>April 29, 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.9.1-beta.4...v0.9.2-beta.3" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/releases/tag/v0.9.2-beta.3" class="changelog-link">release</a>

- **City sharing (ADR-035 phase 1+2)**: city picker, sync, display, directory filter via chip/button, share-city state hydration at startup, accessibility semantics on tap-to-filter chips
- **Hardened CityRepository**: validation, isolate, LRU cache, consumption of enriched records (admin1 + admin2) from ADR-036
- **Directory V1**: highlight banner for same-city libraries
- **Loans**: module split into two independent toggles (lend / borrow), Received/Sent sub-tabs gated independently per module, lending disabled by default on the bookseller preset
- **E2EE identity recovery**: recovery dialog instead of silently breaking peers, list of peers and devices to re-pair after a wipe
- **Activity carousel**: cap raised to 20 items, padded with latest added books
- **Search**: persistent Google Books toggle, UX guards when no API key is set, new generic `search` i18n key
- **Hub directory**: auto-setup of the relay and negative cache on 404
- **Profile**: removed `profileType` and `simplifiedMode` in favor of mode-driven behavior
- **Collections**: null-safe navigation from the book detail, auto-refresh of the list
- **Stability**: copy badge refreshed on book detail when returning from the copy manager, IME composition committed before reading the author controller in book forms
- **i18n**: 22 missing strings translated in Spanish and German, deduplication of the `badge_new` key across fr/en/es/de
- **Hub**: automatic push of the location country on settings change

## 0.9.1 <small>April 25, 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.9.0-beta.6...v0.9.1-beta.4" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/releases/tag/v0.9.1-beta.4" class="changelog-link">release</a>

- **International discovery v1.0**: full overhaul of curated lists in preparation for the international rollout
- **"Activity" carousel**: rebranded from "recently added", reading-first sort, "new" badge hidden when a status badge is already shown, ES/DE propagation
- **Library**: persistent sort control collapsed into a single pill with popup (empty-author entries at the bottom), collection grouping driven from settings, fixed progress bar
- **Peer book sheet**: draggable sheet with pinned header and persistent borrow CTA
- **Covers**: isolated peer cover cache with a user-controlled cap, warning badge when hub upload is pending retry, unified URL resolution via `CoverUrlResolver`
- **Loans (ADR-034)**: typed loan metadata, reader-extraction helper, fixed reading of the `/api/copies/borrowed` payload
- **Statistics**: count books marked read without a finished date, fix loan and pages-read cards stuck at 0
- **Book detail**: block deletion on active loans, preserve `addedAt` / `hubCoverUploadFailedAt`, coerce `DateTime` &rarr; ISO string in FFI updates
- **Network**: stale-connection badge on peer cards (ADR-032)
- **Collections**: option to also delete associated books when removing a collection
- **i18n**: "Gamification" renamed to "Accomplissements" (FR), Activity carousel strings and new badges propagated to ES and DE
- **Stability**: tap-to-mark-read in the notifications popover, localized shelf-deletion confirmation, library-rename replay when config is not yet hydrated

## 0.9.0 <small>April 17, 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.8.9-beta.17...v0.9.0-beta.6" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/releases/tag/v0.9.0-beta.6" class="changelog-link">release</a>

- **Peer delta sync (ADR-028 / ADR-029)**: peer catalog refreshes now use incremental deltas (adds, updates, deletes) instead of full pulls, dramatically reducing bandwidth and speeding up discovery of peer changes
- **Transparent fallback**: automatic fallback to the legacy full pull when the peer does not yet support the delta protocol
- **Local state preserved**: `firstSeenAt` and the online state are kept during delta refreshes (the "new" badge stays consistent)
- **Cross-device avatar sync (ADR-025)**: profile avatars now propagate across linked devices via `profile_changed`
- **Peer library self-heal (ADR-030)**: library UUID recovery via E2EE manifest, delta cursor preserved after a reset-recovery
- **Recently-added carousel**: new carousel of latest additions on own and peer libraries, collapsible variant driven by scroll, auto-hidden on small libraries
- **Sticky header**: collapsing header with sticky tabs on Library and Loans
- **Discover directory**: ungated entry with in-tab publish CTA, cover-grid catalog view, reliable "new" badge, incoming follow requests surfaced on the Discover card, explicit confirmation snackbars, approval and borrowing toggles unlocked with privacy-first defaults
- **Accessibility**: tooltips on 13 IconButtons, semantic labels for screen readers, `Semantics` headers on book detail
- **Settings**: visual grouping of module toggles into 4 sections, neutralized jargon, explicit confirmation on destructive network actions
- **Leaderboard**: startup module sync and UI harmonization, client-side refresh timeout with user feedback
- **Games hub**: hangman link added on the dashboard
- **Peer library UI**: cover grid by default with bounded RAM, restored color variety on book placeholders, "new" badge now driven by owner-supplied `added_at`
- **Hub directory**: clients now report their app version to the hub on register
- **Book cover**: avoid the OpenLibrary grey placeholder for unknown ISBNs
- **i18n**: 24 missing strings translated in Spanish and German

## 0.8.9 <small>April 13, 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.8.8-beta.6...v0.8.9-beta.17" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/releases/tag/v0.8.9-beta.17" class="changelog-link">release</a>

- **Public hub directory**: public directory enabled with UX guardrails and direct borrow requests from followed libraries
- **Real-time leaderboard (ADR-023)**: live leaderboard push, cache-first display, pre-warm on startup, reset scores button, skip direct on cellular
- **Loan reminders**: due-date reminder notifications, fixed deep-link targets for lent/returned events
- **Enriched book detail**: active loan status (borrower, due date, overdue badge), contact notes, copies stepper, borrow button disabled when book is already lent or borrowed
- **Live peer catalog**: subscribe to peer changes to refresh the library without manual action, re-check peer connectivity before sync to avoid stale offline paths
- **Controlled covers**: cap at 300&times;450, JPEG re-encode on upload, ETag cache, evict on 404, hub proxy for peer covers, propagation of custom covers to the hub
- **Page count**: page count field on book details, add/edit forms and search
- **Configurable loan duration**: customize loan duration in settings, pick borrowing peer from loan dialog
- **Book forms**: redesigned add/edit book forms for better UX
- **Network peers**: peer avatars (LAN and relay via hub), tap peer card to open library directly, peer list polish (status dot, skeleton, full-screen QR), share invite button in add-connection sheet
- **Relay robustness (5G/4G)**: reliable credential republish on reconnect, non-blocking sync, offline fallback, 502 circuit breaker, nodeId refresh, sync timeout
- **Hub profile**: profile recovery code, automatic recovery on 401 (retry with recovery code before purge), hardened Keychain backup, registration 401 back-off, Hub URL hidden in release, safeguards against permanent profile lockout
- **Multi-device sync**: fixed synchronization of authors, notes, copies and metadata between linked devices, library rename propagated to the hub
- **Search**: improved external source reliability, relevance scoring, protection against concurrent searches
- **i18n**: completed ES/DE translations (cover, loans, notes, recovery), "Copies" renamed to "Exemplaires" (fr)
- **Security & stability**: sensitive logs gated in debug and identifiers redacted, Inventaire deserialization fix, localized default library name fix

## 0.8.8 <small>March 23, 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.8.7-beta.3...v0.8.8-beta.6" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/releases/tag/v0.8.8-beta.6" class="changelog-link">release</a>

- **Multi-device sync (E2EE)**: end-to-end encrypted synchronization between linked devices, bidirectional pairing, backfill and deduplication
- **Book notes**: add notes to books with voice dictation support
- **Private books**: hide books from network peers
- **Book descriptions**: automatic retrieval from OpenLibrary and SUDOC
- **Hangman game**: new mini-game added to the games hub
- **Onboarding**: sequenced flash messages and welcome design overhaul
- **Stability**: fixed crashes on first launch and first scan, Android Keystore recovery

## 0.8.7 <small>March 17, 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.8.6-alpha.6...v0.8.7-beta.3" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/releases/tag/v0.8.7-beta.3" class="changelog-link">release</a>

- **macOS DMG**: distribution via DMG with hardened runtime and resilient Keychain fallback
- **Device fingerprint**: register device model and fingerprint on the hub
- **Peer stability**: catalog refresh, offline cache, peer name persistence
- **Notifications**: complete UX overhaul, borrowed filter, peer name fix
- **Compatibility**: `ClipRect` fix for Flutter 3.38

## 0.8.6 <small>March 13, 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.8.5-beta.6...v0.8.6-alpha.6" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/releases/tag/v0.8.6-alpha.3" class="changelog-link">release</a>

- **Unified hub catalog**: consistent rendering and faster peer library loading
- **Mass scan**: batch scanning feature with redirect to scanned shelf
- **Statistics**: enriched quantity and quality, colors harmonized with profile
- **Localization**: added Italian, Turkish fixes, i18n cleanup
- **UI**: logo, search toggle, bottom nav border, operation log dates

## 0.8.5 <small>March 7, 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.8.4-alpha.4...v0.8.5-beta.6" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/tree/v0.8.5-beta.6" class="changelog-link">tag</a>

- **Activity feed**: new activity stream with "new" badges
- **Borrow management**: borrow requests, notification UX, tap-to-edit reading status badge
- **Network discovery**: cross-reference mDNS names with saved peers, 5G sync fallback
- **UI**: bottom navigation bar option, instant cover refresh, share quick action

## 0.8.4 <small>March 4, 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.8.2-alpha.3...v0.8.4-alpha.4" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/tree/v0.8.4-alpha.4" class="changelog-link">tag</a>

- **Hub directory**: Explore screen, library follow/unfollow, incoming requests
- **Collections**: refactored to FFI direct, grouped in library view
- **Web browsing**: connect and browse peer libraries via web browser
- **Device sync**: sync safety module with review screen
- **Covers**: capture covers with device camera

## 0.8.2 <small>February 26, 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.8.1-alpha.2...v0.8.2-alpha.3" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/tree/v0.8.2-alpha.3" class="changelog-link">tag</a>

- **Short invite links**: simplified profile sharing with short URL via the hub
- **Share button**: new profile share button
- **Accessibility**: accessibility prerequisites added (work in progress)

## 0.8.1 <small>February 25, 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.8.0-alpha.2...v0.8.1-alpha.2" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/tree/v0.8.1-alpha.2" class="changelog-link">tag</a>

- **Memory game**: new mini-game using your library covers, with leaderboard and animations
- **Sliding puzzle**: cover-based puzzle game with dedicated screen and games hub
- **Help**: enriched help section
- **Translations**: added Portuguese and Turkish

## 0.8.0 <small>February 20, 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.7.2-alpha.2...v0.8.0-alpha.2" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/tree/v0.8.0-alpha.2" class="changelog-link">tag</a>

- **End-to-end encryption (E2EE)**: QR code v2 key exchange, E2EE indicator in UI, encrypted loan requests
- **Relay hub**: relay hub settings UI and API integration
- **AGPL-3.0 license**: project relicensed to AGPL-3.0
- **CJK support**: fallback fonts for Japanese, Chinese and Korean, .po skeleton files
- **Languages**: added Bulgarian, regional variant support (pt-BR, zh-TW...)
- **Loans**: configurable auto-approve, pending request counter

## 0.7.2 <small>February 13, 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.7.1-alpha.7...v0.7.2-alpha.2" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/tree/v0.7.2-alpha.2" class="changelog-link">tag</a>

- **Internationalization**: translations migrated to .po files, multi-language search
- **Theme**: theme customization in settings, default theme optimization
- **UX audit**: persona-based fixes, search deduplication, 4 major friction points resolved
- **Leaderboard**: fixed leaderboard display on profile and between peers

## 0.7.1 <small>February 10, 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.7.0-alpha.1...v0.7.1-alpha.7" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/tree/v0.7.1-alpha.7" class="changelog-link">tag</a>

- **Leaderboard module**: gamification leaderboard across connected libraries

## 0.7.0 <small>February 6, 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.6.6-alpha.4...v0.7.0-alpha.1" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/tree/v0.7.0-alpha.1" class="changelog-link">tag</a>

- **P2P discovery**: mDNS hostname.local fallback, removed 127.0.0.1 fallback
- **Clean architecture**: migrated Flutter screens to Repository pattern
- **Database path**: installation folder migration
- **Optimizations**: reading status, online search, import, peer caching

## 0.6.6 <small>January 25, 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/compare/v0.6.5-alpha.21...v0.6.6-alpha.4" class="changelog-link">diff</a> · <a href="https://codeberg.org/bibliogenius/bibliogenius-app/tree/v0.6.6-alpha.4" class="changelog-link">tag</a>

- **Borrowing and loans**: fixes and improvements to the borrowing feature
- **UX/UI**: improved empty states, avatar visibility management, search enhancement
- **Statistics**: statistics page and dashboard display improvements
- **Quick actions**: new quick actions button in the top banner
- **Simplified install**: removed setup wizard, auto-initialization, ES/DE support

## 0.6.5 <small>January 12, 2026</small> &nbsp; <a href="https://codeberg.org/bibliogenius/bibliogenius-app/tree/v0.6.5-alpha.21" class="changelog-link">tag</a>

- **Initial alpha release**: personal library management, book add/scan, online search
- **Local network**: peer discovery via mDNS, neighbor library browsing
- **Interface**: dashboard, collections, shelves, profile with gamification badges
