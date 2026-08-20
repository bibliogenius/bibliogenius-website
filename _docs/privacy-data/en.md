---
title: Where is my data stored
description: What stays on your device, what leaves it, and how you keep control
order: 12
group: data
---

BiblioGenius is local-first: your library lives in a database on your device, and the app works with no account and no connection. Whatever leaves the device only leaves because you asked for it, and this page says exactly what, when and where to.

## On your device

Your books, shelves, collections, tags, copies, loans and contacts are stored locally. You can use the whole app offline: add books by hand, organize them, track your reading.

## What leaves the device, and when

- **Searches in external catalogues.** When you scan an ISBN or search for a title, the query goes out to the enabled sources (BnF, OpenLibrary, Inventaire and others). Those sources therefore see what you are looking for. You choose which ones to query in Settings > Search sources.
- **Covers and metadata** are downloaded from those same sources, then kept on your device.
- **Sharing with your contacts.** When a connected library browses your catalogue, your device answers it directly, end-to-end encrypted. On a local Wi-Fi network the exchange never leaves that network. Remotely, it goes through a relay that only ever sees encrypted data.
- **The online directory**, if you enable "Make me visible to other libraries". You can require your approval before a new follower reaches your shared books. Your city stays a local preference until you choose to share it.
- **The encrypted account**, if you create one. The server then only stores encrypted blocks, unreadable to it. See [Encrypted account and multiple devices](account-sync.html).

None of this is turned on for you.

## Choosing what others see

Enable "Private books" in the settings to unlock the Private option on each book: a private book stays in your library but never shows up to others, neither on your public profile nor in network searches.

To check rather than trust, open **"What other libraries see"**: this list is the exact answer your device sends to a library browsing your catalogue, produced by the same code, with no cosmetic recomputation.

## Backups

You can take your data out at any time from **Settings > Backup and recovery**: portable export, CSV export readable in a spreadsheet, or a restorable encrypted archive. See [Exporting and backing up](export-backup.html).

## Encryption

Exchanges between libraries are end-to-end encrypted. So are the encrypted account and full backups, with a key derived from your passphrase: we have no technical means of reading your data.

## Deleting my data

On the device, the settings let you erase your books or start over. To delete an online account, follow the procedure on the [Data deletion](../data-deletion.html) page.
