---
title: Bulk-update your book data
description: BiblioGenius fills in the missing data across your whole library in one pass: summary, publisher, page count and cover.
order: 4
group: library
---

BiblioGenius can automatically fill in the missing data for your books, across your whole library in a single operation, instead of editing them one by one.

## Run the bulk update

1. On the dashboard, find the **Library completeness** card (it shows the percentage of complete books).
2. Tap the card to open the **Complete my library** screen.
3. Choose the batch size with the **In batches of:** selector. You can process **10**, **20** (the default) or **30** books at a time, or pick **All** to go through the whole library at once.
4. Tap **Complete** (the button shows the number of books in the batch, for example "Complete 20 books").
5. BiblioGenius searches for the missing information and fills in, for each affected book: the summary, publisher, page count, publication year and cover image.
6. Progress is shown as "X of Y books". At the end of a batch the run pauses: tap **Resume** to move on to the next batch, or **Run it again** or **Discard** the search.

## Why process in batches

Completing a large library all at once can take a while. By working in batches of 10, 20 or 30 books, you see results sooner, you stay in control, and you can stop whenever you want and resume later right where you left off. The **All** option is still there if you would rather run everything in one go.

## Track and filter

- The **To complete** tab lists books with missing data; the **Recent** tab shows the ones that were just completed.
- Filters let you target a specific missing field, or isolate books **without an ISBN**.

## Repair a library imported without ISBNs

If you imported your library from a file and your books arrived **without ISBNs**, the automatic update cannot help them: the ISBN is precisely what it uses to identify a book. Rather than typing them in one by one, hand the original file back.

1. Open the **Complete my library** screen, then the **No ISBN** filter.
2. Tap **Complete from the file** and pick the file your books came from.
3. If no ISBN column is recognised, BiblioGenius shows the file's headers and asks which one carries the ISBN.
4. A summary reports how many rows were read, how many books were completed, how many found no match and how many were ambiguous.

This mode **never adds a book**: it only fills the ISBN, publisher and publication year of books already there, and only where those fields are empty. A row that could designate two books at once is never guessed: it is listed, and the choice is yours. The whole completion can be undone in one gesture from the **Recent** tab.

Once the ISBNs are back, the bulk update described above becomes possible again, and covers and summaries arrive on their own.

## Undo a change

Afterwards, you can undo the fill per book, or per field. Values you entered yourself are protected: they are never overwritten or reverted by mistake.

## Good to know

- The update only applies to books you **own**.
- An **ISBN** is required to look up the data: books without an ISBN are flagged and skipped. Add an ISBN from the book's page, or, if they all came from one file, see "Repair a library imported without ISBNs" above.
- If no source provides the information, the field stays empty; you can then fill it in manually from the book's page.
