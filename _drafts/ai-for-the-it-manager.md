---
layout: post
title: "AI for the IT Manager"
date: 2026-01-08
ai: written
---

The pitch deck version of AI in enterprise is agents autonomously running your infrastructure, making decisions, fixing issues before you know they exist.

The reality - at least for now - is more mundane. And more useful.

I'm an IT Manager at a ~100 person engineering firm. I've spent the last two years actually using AI in my day job. Not demos. Not proofs of concept for executive presentations. Actual daily use that's changed how I work.

Here's what's actually working.

## The second brain that never forgets

The single biggest win is using Claude Code as an always-available context holder. I built a system called Overwatch that knows my job - the company context, the projects I'm running, the decisions I've made, the problems I've solved before.

The architecture is the same pattern I wrote about in building [Arc](/2025/12/29/building-arc-a-thinking-partner-that-remembers/): a git-backed repository of markdown files, CLAUDE.md at the root, decisions captured with reasoning, sessions logged automatically. Arc is for personal thinking; Overwatch is for work.

The compound effect is significant. Three months of captured context means the AI is genuinely useful as a thought partner. It remembers that we tried X approach on Y project and it didn't work because of Z. That institutional memory - the kind that usually lives in someone's head and walks out the door when they leave - is now persistent and searchable.

## Calendar-aware task management

I built integration between my task system and Microsoft 365 calendar. The AI looks at my meeting load for the day and adjusts recommendations accordingly.

Heavy meeting day (>50% of time in meetings): Quick wins and coordination tasks only. You're already in meeting mode - lean into it.

Light meeting day (<25% meetings): Deep work. Architecture, planning, complex debugging. Protect these days ruthlessly.

Fragmented day: Match task size to available gaps. Don't start something that needs two hours when you have thirty-minute windows.

This sounds obvious. I even [wrote about calendar-aware automation back in 2018](/2018/07/31/updating-slack-status-based-on-outlook-calendar/) - but that was just status updates. The AI version actually reasons about what kind of work fits the day: "Today is 67% meetings. Focus on follow-ups and quick tasks. Save the IMS architecture work for Thursday when you have a 4-hour block."

Simple. Useful. Actually changes behaviour.

## Meeting transcript to action items

Microsoft Teams generates transcripts. They're long, messy, and nobody reads them. But they contain the commitments people made.

I built a skill that processes meeting transcripts and extracts action items. Who committed to what, by when. These get routed into my task system automatically.

The time savings compound. I used to spend 15-20 minutes after each meeting writing up notes and capturing actions. Now I dump the transcript and get structured output in seconds. Multiply that by 5-8 meetings a day, and it's an hour or more reclaimed.

## Research and analysis on tap

IT Manager work involves a lot of "I need to understand this thing well enough to make a decision" work. Vendor evaluation. Technology comparison. Policy implications. Compliance requirements.

The AI handles first-pass research faster and more thoroughly than I can. I ask it to analyse three different approaches to a problem, it comes back with structured comparison, trade-offs, recommendations, and questions I should be asking.

I still make the decisions. But the prep work that used to take hours now takes minutes. And the quality is often higher because the AI catches angles I would have missed.

## Compliance support

We're working toward Essential Eight Maturity Level 2, as well as ISO27001. The compliance framework is extensive - implementation requirements, evidence needs, and ongoing monitoring.

I built skills that help with gap analysis, evidence collection, and tracking. The AI knows the framework, knows our environment, and can identify where we're compliant vs where we have gaps. It drafts implementation plans and evidence documentation.

This doesn't replace the hard work of actually implementing controls. But it dramatically reduces the overhead of understanding what needs to be done and tracking progress against it.

## What's not working

Adoption by others. I've deployed Open WebUI across the organisation. Usage is low. Engineers are busy with billable work and don't have time to learn new tools. The value proposition isn't compelling enough to overcome the friction of changing behaviour.

This is the pattern I keep seeing: AI tools that work technically but fail at adoption. Change management is the hard part, not the technology.

I've also hit limits with anything that requires real-time integration with production systems. The AI is great for analysis, research, planning, and decision support. It's not ready - at least in how I'm using it - for autonomous action in production environments. The risk/reward doesn't make sense yet.

## The meta lesson

None of this is frontier AI. I'm not using the latest model releases. I'm not building autonomous agents that make decisions without human oversight. I'm not doing anything that would make a good conference talk.

What I'm doing is taking existing, stable capabilities and actually integrating them into daily workflows. The gap between AI capability and AI value isn't the models - it's the connective tissue. The context. The integration. The habit formation.

If you're an IT Manager wondering where to start, this is my advice: pick one workflow that involves a lot of context-dependent thinking, build the scaffolding to give an AI that context, and use it consistently for a month.

[The compound effect](/2026/01/01/seven-years-of-compounding/) will surprise you.
