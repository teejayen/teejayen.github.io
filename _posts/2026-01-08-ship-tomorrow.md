---
layout: post
title: "Ship tomorrow"
date: 2026-01-08
ai: written
---

I shipped something publicly overnight. A small tool - [vex](https://github.com/teejayen/vex) - that batch-processes screenshots through Claude's vision API and extracts searchable content. Recipes become text. Error messages become findable. 12,000 screenshots sitting useless in folders become a searchable knowledge base.

Building it took less than 30 minutes. The core logic was straightforward. Claude wrote most of the code. I directed, tested, iterated. Working version, ready to use locally.

Then came the polishing. Checking model names against official docs. Security review for hardcoded secrets. License deliberation (MIT? GPL? Back to MIT). README rewrites. Batch API edge cases. Testing every command. Making sure the commit history was clean.

Two and a half hours later, I pushed. It was 1:21am.

There's a voice that says "if you're going to do it, do it properly." And there's truth in that. The security check found nothing, but I would have worried if I hadn't done it. The edge cases I fixed would have embarrassed me later. The README matters because people will actually read it.

This could have waited until today - but the polishing felt urgent because I was in flow. Momentum is real, but so is the 1am decision-making that leads you to accidentally include private details in a public repo (I caught it, barely, and added a pre-commit hook to make sure it doesn't happen again).

The constraint I forgot: not everything that can be done tonight should be done tonight.

Shipping matters. Polish matters too. But the 2.5 hours of polish that followed 30 minutes of building? That ratio tells a story about where perfectionism lives. And that ratio at 1am, when judgment fades and mistakes creep in - that's the trap.

The polish wasn't wrong. The timing was.
