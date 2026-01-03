---
layout: post
title: "The gap"
date: 2026-01-04
ai: written
---

The capabilities are already mind-boggling. GPT-4 can reason through complex problems. Claude can write code and hold nuanced conversations. These models can analyse documents, summarise meetings, draft emails, and answer questions that would have seemed like science fiction five years ago.

So why does it still feel like AI isn't *doing* anything in most organisations?

The answer isn't the models. The answer is everything around them.

## Three walls

**Integration friction.** Enterprise data lives in fifteen different systems, each with its own API - or worse, no API at all. Connecting them is expensive, fragile, and deeply unsexy. Nobody gets promoted for building a connector between Salesforce and the legacy ticketing system. So it doesn't get done, and the AI that could transform workflows can't access the data it needs.

**Scattered documentation.** Policies live in SharePoint, maybe. Exceptions live in email threads. Precedents live in people's heads. The actual process - the way things really work - lives in the gap between the documented process and reality. An AI can only work with what it can see, and most organisational knowledge is invisible.

**Workflows nobody wants to touch.** Every organisation has processes that "just work" - fragile, undocumented, politically owned. Nobody wants to be the person who breaks the thing that's been running for years. So these workflows persist, immune to improvement, while AI gets bolted onto the edges instead of transforming the core.

These aren't technical problems. They're *institutional* problems. And they're why the gap between AI capability and AI implementation keeps widening.

## The deeper issue: context is nowhere

Here's what I keep running into. You can give an AI access to your policies. You can connect it to your systems of record. You can even give it a clear goal. And it will still make decisions that feel *wrong* - technically correct but missing something essential.

What's missing is context.

Not data. Context. The difference is everything.

Data tells you the policy says customers get 30-day payment terms. Context tells you this particular customer has been with you for fifteen years and always pays early, so when they ask for 45 days during a rough quarter, you say yes. Data tells you the escalation process requires three levels of approval. Context tells you that when Sarah from operations flags something, you skip the process because she's been right every time.

This context currently lives in Slack threads, hallway conversations, deal desk calls, and people's heads. It's the institutional memory that makes organisations actually function. And it's almost entirely inaccessible to AI.

## Context graphs

I've been reading about a concept called [context graphs](https://foundationcapital.com/context-graphs-ais-trillion-dollar-opportunity/) - the idea that there's a missing infrastructure layer between systems of record (where data lives) and AI agents (where decisions happen).

Systems of record tell you what the rules are. Context graphs capture how those rules actually get applied - the exceptions, precedents, and judgment calls that reflect reality rather than policy.

The framing clicked for me: rules tell an agent what *should* happen in general, but context provides the situational awareness needed for intelligent exceptions. Without context, you get AI that follows rules rigidly. With context, you get AI that can exercise something like judgment.

This is the trillion-dollar infrastructure gap. Not better models - better context.

## Where the leverage actually is

I'm an IT Manager, not a VC. I don't think about trillion-dollar opportunities. I think about what I can actually implement next quarter that makes things work better.

Here's what I'm taking from this:

**Stop chasing frontier models.** The capabilities already exceed what most organisations can absorb. GPT-3.5 is more than enough for 90% of use cases if you could just get it connected to the right data with the right context.

**The work is in the messy middle.** Integration, documentation, workflow mapping - this is where the leverage is. It's unglamorous. It doesn't make good demos. But it's the difference between AI as a toy and AI as infrastructure.

**Start capturing context deliberately.** This is why I built [Arc](/2025/12/29/building-arc-a-thinking-partner-that-remembers/). Not because I needed a chatbot, but because I needed a system that remembered context across sessions. The same principle applies at the organisational level. Every decision, exception, and precedent that gets captured is context that makes AI more useful.

**The opportunity is implementation, not invention.** The models exist. The capabilities exist. What doesn't exist - yet - is the connective tissue that lets them actually work inside real organisations with real constraints and real institutional complexity.

The people who figure out context capture and integration will quietly build the most valuable AI infrastructure. Not by making better models, but by making existing models actually useful.

The gap isn't capability. The gap is context. And that's where the work is.
