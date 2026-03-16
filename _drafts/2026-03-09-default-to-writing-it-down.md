---
layout: post
title: "Default to writing it down"
date: 2026-03-09
ai: written
---

Most productivity advice is about doing more. Read faster, type faster, automate faster. But the single habit that has compounded the most for me over the past seven years isn't about speed at all. It's about writing things down.

Not polished writing. Not blog posts (though those help too). Just the act of capturing what you know, what you decided, and why - before you forget.

## The forgetting tax

Every team pays a forgetting tax. Someone figures out why the deployment broke, fixes it, and moves on. Three months later, someone else hits the same issue. They spend the same hours debugging. The fix lives in someone's head, or buried in a Slack thread no one will ever search for.

This isn't a tooling problem. It's a defaults problem. The default for most people after solving something is to close the laptop and move on. The fix is simple: make your default to write it down first.

It doesn't need to be pretty. A few sentences in a shared doc, a comment in the ticket, a note in the runbook. The bar isn't quality - it's existence.

## Writing forces clarity

There's a well-known effect where explaining something reveals whether you actually understand it. Writing is the cheapest version of this. If you can't write a clear paragraph about why you chose option A over option B, you probably don't fully understand the tradeoffs yet.

I've lost count of the number of times I've started writing up a decision and realised halfway through that my reasoning had gaps. The writing didn't just document the decision - it improved it.

This is especially true for architecture decisions, incident reviews, and project scoping. The act of putting it in writing slows you down just enough to catch the things you'd otherwise gloss over in a meeting.

## The AI multiplier

Here's where this gets interesting. Everything you write down becomes context that AI can use.

I wrote [earlier this month]({% post_url 2026-03-07-your-ai-is-only-as-good-as-your-organisations-memory %}) about how your AI is only as good as your organisation's memory. The bottleneck for most AI tools isn't the model - it's the lack of written context to feed it. When you've been writing things down consistently, you have a library of decisions, processes, and reasoning that can be handed to an AI as context. When you haven't, you're starting from scratch every time.

This applies at the personal level too. My notes, blog posts, and documentation have become a second brain that I can point AI tools at. "Here's how I've approached this kind of problem before - now help me with this new one." The compounding effect is real: past writing makes present AI usage dramatically more effective.

If you're wondering why your AI tools feel shallow or generic, ask yourself how much written context you're actually giving them. The answer is usually "not enough."

## Practical defaults

I've tried to build writing into my defaults rather than relying on discipline:

**After fixing something non-obvious**, I write a short note before closing the ticket. Two or three sentences: what broke, why, and what fixed it. Future me (or future someone else) will be grateful.

**After making a decision**, I capture the options considered and why we chose what we chose. The "why not" is often more valuable than the "why" - it prevents someone from relitigating the same debate six months later.

**After learning something new**, I write a rough summary while it's fresh. It doesn't need to be a blog post. A note in my personal docs is enough. The goal is to have something to return to when the details have faded.

**Before asking for help**, I write up what I've tried and what I'm seeing. Half the time, the act of writing the question reveals the answer. The other half, I've got a clear, searchable artefact of the problem and solution.

## The compound curve

The value of writing things down isn't linear. The first few notes feel like overhead. But over months and years, you build a searchable body of knowledge that pays dividends you can't predict in advance.

Seven years of blog posts have given me something I didn't expect when I started: a record of how my thinking has evolved. I can look back at what I believed about a topic two years ago and see where I was right, where I was wrong, and where the landscape shifted. That kind of self-awareness is hard to get any other way.

At an organisational level, the effect is even more pronounced. Teams that write things down don't lose knowledge when people leave. They onboard new people faster. They make fewer repeated mistakes. They build on previous thinking instead of reinventing it.

None of this is revolutionary. But that's sort of the point. The most powerful habits aren't the clever ones - they're the obvious ones that most people skip because they don't feel productive in the moment.

Write it down. Your future self - and your future AI - will thank you.
