---
title: Encrypted account and multiple devices
description: The BiblioGenius encrypted account keeps a copy of your library that only you can read, so nothing is lost and every device shows the same shelves.
order: 14
group: data
---

BiblioGenius runs on your device first, with no account. The encrypted account is optional: it keeps an encrypted copy of your library that only you can read. It serves three purposes: losing nothing, finding your library again on a new device, and using it with several people.

You will find it in **Settings > Backup and recovery > Encrypted account**.

## What the server sees

Nothing readable. Your books are encrypted on your device before they are sent, with a key derived from your passphrase. The server only stores encrypted blocks: neither we, nor a hosting provider, nor anyone who got hold of the database can read your titles, your notes or your contacts.

The trade-off is straightforward: nobody can give you back access to your data if you lose your secrets.

## Creating an account

You need an email address, a passphrase, and a name for this device.

**Your passphrase cannot be reset.** When the account is created, the app shows a **24-word recovery phrase**: it is the only way to recover the account if you forget the passphrase. It is displayed once and never stored. Write it down in order, on paper or in a password manager.

That same recovery phrase can be used as the secret for your full backups, see [Exporting and backing up](export-backup.html).

## What syncs, and what does not

Syncs: your books, authors, tags, collections, copies, loans, contacts and custom covers.

Does not sync: device-specific settings, and the **encrypted pairings with your contacts**. Pairing is done device by device, by design: the key that links you to another library never leaves the device that created it.

That is why, on a new device, your contacts may show up in a "Known libraries" section marked "Not paired on this device". To connect to them from that new device, pair again: share your invitation link or accept theirs.

## Adding a device

1. On the new device, choose "Add this device from another device": it displays a QR code.
2. On a device that is already signed in, open **Encrypted account > Add a device** and scan that code.
3. The existing device then displays an authorization code, which the new device scans in turn.

Only scan these codes in person, directly between your two devices. Never send them by message or as a photo.

If your two devices are not side by side, "Join an existing account" does the same thing with your email and your passphrase.

## Syncing

Syncing happens on its own, periodically and when you come back to the app. The **Sync now** button forces an immediate cycle.

If the message reports a partial sync, some items could not be applied on this device, usually because one of your devices runs an older version. Update them, then sync again.

## Sharing access with other people

From the same screen, "Share access to my library" lets another person join the account from their device, with your email and your passphrase. They then appear as an authorized device.

Be clear about what this means: **anyone sharing this account has full access to it**, and permanently revoking an access is not possible yet. This is a trust-based feature, designed for a household.

## Removing a device, signing out

Removing a device stops it from syncing, but it keeps the data it already downloaded: this is not a security lock. You can add it back later.

Signing out on a device stops its syncing without touching the account or your other devices. You reconnect it later with your passphrase.

## If you lose everything

With the recovery phrase, you get the account back. Without the passphrase and without the recovery phrase, the account data is permanently unreadable, including for us. That is the price of end-to-end encryption, and it is also why a local full backup remains a good idea.
