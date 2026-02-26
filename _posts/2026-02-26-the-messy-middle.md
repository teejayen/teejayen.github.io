---
layout: post
title: "The messy middle"
date: 2026-02-26
ai: assisted
---

Most conversations about AI start in the wrong place. They start with the technology. What model to use. Which tool to buy. How to write better prompts. Someone shows a demo, everyone nods along, and then nothing changes.

I think the reason nothing changes is that the real problems don't look like AI problems. They look like a quoting process that takes three days. A senior team member who's the only person who knows how to price a complex job. Five different spreadsheets tracking the same customer information. A compliance requirement that everyone knows they need to meet but can't resource.

These are the problems worth solving. And most of them don't need AI at all.

## The messy middle

There's a gap between "we should use AI" and actually using it. I've started calling it the messy middle. It's the part where you have to do the boring work: audit your processes, figure out which data lives where, and ask uncomfortable questions about why things are done the way they're done. Nobody wants to talk about this part. It doesn't demo well. But it's where all the value is.

A trades business losing three hours per quote because the estimator manually checks supplier pricing, reviews past job costs across two systems, and writes everything up in Word - that's not an AI problem. That's a data and process problem. Fix the inputs, connect the systems, template the output. If you've done that work and the bottleneck is still the writing, the judgement calls, the client-specific phrasing? Now AI has something useful to do.

A professional services firm where every proposal is written from scratch because "every client is different"? Pull the last fifty proposals. The 80% that's identical should be templated. Automate the assembly. The remaining 20% - the scoping, the specific recommendations, the tone - that's where AI earns its keep.

A manufacturer tracking quality issues in emails and spreadsheets, with no shared defect taxonomy. The same issue described three different ways by three different shift supervisors. The conversation jumps straight to "predictive maintenance" and "AI-powered quality control" - but the data isn't structured. Standardise the capture first. Build a dashboard. Then layer on AI if the patterns are complex enough to warrant it.

An accounting practice spending hours every week chasing clients for the same documents, sending the same reminders, following up on the same overdue lodgements. Build the triggers, template the messages, automate the sequence. AI might help draft the escalation email that needs a different tone for a long-standing client. But the system that decides when to send it? That's just logic.

A not-for-profit writing every grant application from scratch when 80% of it - the organisational background, the capability statements, the evidence of impact - is identical every time. That 80% should exist as a maintained, reusable document. AI can adapt it to each funder's requirements and word limits. Without it, AI is just helping you rewrite the same paragraphs slightly differently each time.

A club sitting on years of POS data, booking history, and membership records - none of it connected. The instinct is "use AI to personalise our marketing." Personalise it with what? The member database hasn't been cleaned in three years, the POS data doesn't talk to the booking system, and nobody's segmented the membership beyond "active" and "lapsed." Connect the systems first. Build a single view of who's coming in, when, and what they're spending on. Even a basic automation - targeted offers based on visit frequency, stock ordering based on actual sales - delivers more value than an AI tool working with fragmented data.

The pattern is always the same: simplify first, automate second, apply AI third.

## Building something to test the idea

I wanted to make this thinking tangible. Not a slide deck. Something you could actually use. So I built [AI Scorecard](https://aiscorecard.com.au) - a self-assessment tool that asks Australian SMBs fifteen questions about their business operations.

Not "are you using AI" questions. Readiness questions. How accessible is your data? How documented are your processes? How does your team handle change? What does your quoting workflow actually look like? These are the things that determine whether AI will help or just add complexity.

The assessment scores across eight categories: AI Strategy, Data Readiness, Process Management, Technology Integration, Team Readiness, Customer Operations, Decision Intelligence, and Governance & Risk. Each one maps to an area where I think AI can work well - or fail because the foundations aren't there.

## Where the AI actually sits

Building this forced me to think carefully about where AI adds value in a pipeline and where it doesn't.

The scoring model is pure arithmetic. Weighted answers, category mapping, band calculation. Deterministic, auditable, fast. No AI needed.

The cost-of-inaction estimate uses industry-specific hourly rates, knowledge worker ratios, and penalty hours per weak answer. Again, no AI. Just a model that translates gaps into dollars - hours lost per week, annualised cost. Loss framing, because that's what cuts through. Not "imagine what you could gain" but "here's what the current state is costing you."

The lead routing is rule-based. Simple decision trees based on score combinations.

AI comes in exactly where it should: generating the narrative. After someone completes the assessment, their structured results go to Claude via the Anthropic API. The system prompt includes the full question set, the scoring model, industry-specific context, and whatever the respondent shared about their role and biggest challenge. Claude searches the web for context about their company, then generates a personalised insights report - structured JSON that renders into a three-page PDF.

The report reflects their actual answers back to them, explains why each gap matters in business terms, and gives one concrete action per priority area. Not a six-month roadmap. One thing to try this week.

There's also a ROI calculator that models the financial case for AI adoption across selected use cases. It projects savings over three years using a realistic adoption curve - 40% in year one, 70% in year two, 90% in year three - and accounts for training, the inevitable productivity dip, and tool costs. Claude then generates a phased implementation roadmap based on what they selected.

The prompt engineering was the interesting part. I wanted the output loss-framed and specific. Australian English. Grade-8 reading level. No corporate fluff. Concrete over abstract. The system prompt feeds Claude industry-specific triggers - for trades, lead with quoting speed and job documentation; for health, patient communications and recall automation - so the insights feel relevant rather than generic.

## The cross-cutting patterns

The industry examples above look different on the surface, but underneath they're the same handful of problems:

**Scattered data.** Customer records in one system, financial data in another, job history in a third, and none of them talking to each other. This is the single most common blocker. AI can't synthesise information that doesn't exist in a usable form. The fix is boring - clean the data, connect the systems, build a single source of truth. But without it, nothing else works.

**Undocumented processes.** The way things actually get done lives in people's heads, not in any system. Key person risk, inconsistent execution, slow onboarding. AI can help generate documentation - but only if someone maps the process first. You can't document what you haven't defined.

**Manual work that should be automated.** Follow-up sequences, reminders, status updates, reporting. Work that's repetitive, rule-based, and high-volume. This usually doesn't need AI at all. A workflow automation tool, a template, a trigger - the boring stuff. AI enters the picture only when the work requires judgement or language that can't be templated.

**Personalisation without foundation.** The desire to personalise communications, recommendations, or experiences - but without the data infrastructure to know who you're personalising for. Segmentation before personalisation. Data before segmentation.

Every industry dresses these problems up differently. But the foundations are the same.

## The multiplier problem

AI is a multiplier. That sounds good until you realise what it means... a multiplier applied to clean data and clear processes gives you leverage. A multiplier applied to messy data and undocumented processes gives you a faster mess.

The opportunity right now - especially for small and mid-sized businesses - isn't to adopt AI. It's to get ready for it. Fix the data. Map the processes. Figure out where time actually goes. Some of that you'll solve with a better spreadsheet. Some with a simple automation. And some - eventually - with AI that has clean inputs to work with.

That's the messy middle. Nobody's selling it. Nobody's demoing it at a conference. But every business that gets real value from AI went through it first - whether they called it that or not.

The tools are ready. The question is whether the foundations are.
