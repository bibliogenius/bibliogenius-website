---
title: Exporting and backing up my library
description: BiblioGenius exports your catalog as CSV for a spreadsheet and produces a full encrypted backup that restores as is on another device.
order: 13
group: data
---

Your books are yours: you can take them out of BiblioGenius at any time, either in a readable format or in an encrypted archive ready to be restored. Everything happens in **Settings > Backup and recovery**.

## Which file for which need

| Your need | The action to pick | What you get |
|---|---|---|
| Get everything back after a loss or a device change | Full backup | An encrypted `.bgbackup` archive |
| Archive your data or take it to another application | Export my catalogue | A portable file, re-importable into BiblioGenius |
| Read, sort or inventory your books in a spreadsheet | Export as CSV | A readable `.csv` file, not re-importable |

## Automatic backup

At the top of the section, a card tells you when this device was last backed up. With the 24 h automatic backup enabled, BiblioGenius creates an encrypted snapshot of your catalogue every day, **on this device only**. From that same card you can run it manually, restore one of the existing archives, or clear them all.

Automatic backup protects your data on the device. It does not carry it anywhere else: to move to another device, use a full backup or an encrypted account.

## Export my catalogue

Creates a portable, shareable file containing your books, authors, tags, collections and contacts. This is the format to choose to archive your data or reuse it in another application. It can be re-imported into BiblioGenius with "Restore my catalogue".

This file is not encrypted: store it the way you would store any personal document.

## Export as CSV (spreadsheet)

Creates a file with one row per book: title, authors, ISBN, publisher, year, language, ownership, reading status, rating, price, tags and date added. It is meant to be opened, sorted and filtered in a spreadsheet, for instance to build an inventory or an insurance list.

Headers and statuses are written in your language. The file name carries the date and the minute of the export, so a second export on the same day cannot overwrite a file your spreadsheet still has open.

**This file cannot be re-imported.** To restore your library, use the full backup.

## Full backup

Creates an encrypted archive of your whole library, restorable on this device or another one. You protect it with a passphrase of your choice, or with your recovery phrase if you have an encrypted account. Write that secret down: without it the archive is unreadable, including for us.

The **Include identity** option adds your library's cryptographic identity to the archive. It lets you move to a new device without redoing the encrypted pairing with each of your contacts.

## Restoring

- **Restore a full backup**: a wizard guides you, and you choose whether to merge the archive with your current library or replace it entirely.
- **Restore my catalogue**: re-imports a catalogue export file. Careful, this replaces all of your current data.
- **Undo the recent restore**: for 24 h after a restore, a tile offers to go back to the previous state. The app closes to finish the operation, just relaunch it afterwards.

## Good habit

Run a full backup before changing phones, before a restore, and before any bulk operation on your library. Keep it somewhere other than the device it protects.
