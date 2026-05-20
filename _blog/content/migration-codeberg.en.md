+++
title = "BiblioGenius is moving from GitHub to Codeberg"
slug = "github-to-codeberg"
description = "Our GitHub account was suspended overnight, without warning. The project's code now lives on Codeberg, a non-profit, open-source platform. Here is what happened, and what it changes (or not) for you."
date = 2026-05-20
updated = 2026-05-20
template = "blog/page.html"

[extra]
tags = ["announcement"]
+++

BiblioGenius has repeated one simple idea since day one: your books belong to you, your data stays with you. On 4 May, we got a very concrete reminder of why that principle matters.

## First things first: your app does not move

If you use BiblioGenius to manage your library, **everything is fine, you can stop reading here**. This story is only about where the project's *source code* is stored: the "recipe" of the application, the one developers read and improve. The app, your books, your loans, your data: nothing is touched, nothing is lost, you have nothing to do.

The rest will mostly interest the curious, and the people who contribute to the project.

## What happened

Until now, the BiblioGenius code was hosted on **GitHub**, the world's best-known platform for storing code and collaborating on it. A free, convenient service, used by millions of developers.

On 4 May, **our GitHub account was suspended**. No notice, no explanation, no warning email. Overnight, all of the project's code and its history became inaccessible, for us and for contributors alike.

The most likely cause comes down to one line in the terms of service: GitHub allows **only one free account per person**. No warning, no grace period to fix it: just a switch flipped off.

As a result, the **issues** (the list of known bugs and pending tasks) disappeared along with the account. It was above all an internal to-do list, and it is being rebuilt on the new platform.

## The lesson

There is a small irony here. BiblioGenius is a project that stands for digital sovereignty: not depending on a single platform that can change its rules, lock you in, or cut off your access without being accountable. And we just went through exactly that, for real, on our own code.

A single entry point, controlled by a single company, is a point of fragility. The right answer is not to complain: it is to choose hosting that is consistent with the project's values.

## The new home: Codeberg

BiblioGenius now lives on **Codeberg**.

Codeberg is the equivalent of GitHub (a place to host code and collaborate), but with a fundamental difference: it is run by a **non-profit association**, based in Germany, not by a multinational. The software that powers Codeberg, *Forgejo*, is itself open source: it can be inspected, copied, and installed elsewhere.

In other words: BiblioGenius is open source, and so is the platform that now hosts its code. That is more consistent, and it is even what we should have done sooner.

The project is here:

- **Organization**: <https://codeberg.org/bibliogenius>
- **Server** (Rust): <https://codeberg.org/bibliogenius/bibliogenius>
- **App** (Flutter): <https://codeberg.org/bibliogenius/bibliogenius-app>
- **Hub**: <https://codeberg.org/bibliogenius/bibliogenius-hub>
- **Dev environment**: <https://codeberg.org/bibliogenius/bibliogenius-env>

## Do you contribute to the project? (technical part)

If you have a local clone of a repository, just point it at the new address. From inside the repository:

```
git remote set-url origin https://codeberg.org/bibliogenius/<repo>.git
```

For example, for the app:

```
git remote set-url origin https://codeberg.org/bibliogenius/bibliogenius-app.git
```

To open an issue or a *pull request*, you will need a **Codeberg account** (free), and nothing more. No need to be added to the organization: you fork the repository, push to your fork, open a pull request. The classic open-source flow.

## Did you contribute, and did we lose touch?

This is the most delicate part of the migration. Because the GitHub account went down without warning, **we lost the way to reach some people again**, translators above all.

If you once sent us a translation, reported a bug, proposed a fix or an idea, and you are reading these lines: **write to us**. We would sincerely like to reconnect, and make sure your contribution was not forgotten in the move.

One single point of contact: [contact@bibliogenius.org](mailto:contact@bibliogenius.org).

## What about downloads?

The installable versions for **Linux and Windows** were distributed through GitHub. They are therefore temporarily unavailable, while a new download channel is set up. The iOS, Android and macOS apps go through the App Store and Google Play, and are not affected. Need a build in the meantime? Write to us, we will sort you out.

The migration is complete: BiblioGenius now runs entirely on Codeberg. That is where development continues, and where you can follow the project.
