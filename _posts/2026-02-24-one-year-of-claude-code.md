---
layout: post
title: "One year of Claude Code"
date: 2026-02-24
ai: assisted
---

I remember the moment it clicked.

I was building **Nexus** - an integration platform for work that automates document control and project creation across SharePoint, Teams, and Microsoft 365. FastAPI, async Python, Graph API, webhook subscriptions, background workers. A real system, running in production, handling real business operations.

I am not a software developer. I'm an IT manager. Six months earlier, I would have been scoping this as a vendor engagement or a long series of Power Automate flows stitched together with prayer.

Instead, I built it in Claude Code. And it worked.

## Five months

Claude Code launched on February 24, 2025. It turns one today.

I didn't pick it up at launch. I was sceptical that it would fit into my workflow. I wasn't writing code every day. I started using it in September 2025, just five months ago, and in that time the gap between what I could do and what I *can* do has become difficult to explain to people who haven't experienced it.

I've built **Arc**, an [AI assistant](https://tim.neilen.com.au/2025/12/29/building-arc-a-thinking-partner-that-remembers/) that persists context across sessions and captures institutional knowledge. I've shipped [AI Scorecard](https://aiscorecard.com.au) - an AI readiness assessment for Australian SMBs, a [tenant maintenance letter generator](https://rentfix.com.au) - both live, both with real users. I've designed multi-agent content workflows with scoring rubrics and parallel review. I've written more in three months than I did in the previous four years combined.

But the thing that's changed most isn't the output. It's how I think.

## Patterns

When you work across enough domains with the same tool - infrastructure automation, document management, web applications, knowledge systems, content generation - you start to see the shape underneath. The patterns repeat.

Every system I've built has the same bones: capture intent in plain language, structure it into something a machine can act on, build a feedback loop so the output improves over time. Nexus does it with SharePoint webhooks and state machines. [Overwatch](https://tim.neilen.com.au/2026/02/06/file-system-as-context/) does it with CLAUDE.md files and git. AI Scorecard does it with a questionnaire and a scoring model. Different domains. Same architecture.

I wouldn't have seen that pattern if I'd only worked in one domain. Claude Code let me work in all of them, fast enough that the connections became visible.

The value isn't generating code faster. The value is that you move across domains quickly enough to recognise what they have in common.

## The speed of this thing

The tool I picked up in September is not the tool I'm using today. In five months it's gone from a capable file editor to something that runs background agents, fires hooks before and after every action, connects to external systems through MCP, and orchestrates subagents with specialised capabilities. The pace of development is unlike anything I've experienced in twenty years of working with technology.

I keep adjusting my mental model of what it can do, and by the time I've adjusted, it's moved again.

## What was hard

The learning curve isn't the tool itself - the terminal interface is straightforward. The hard part is learning to *think in systems* rather than tasks. Early on, I'd ask Claude Code to fix a specific bug or write a specific function. That works, but it's using a chainsaw to cut paper.

The shift was learning to describe architecture. To brief intent rather than dictate steps. To treat the AI as a collaborator on design, not just an executor of instructions. That took weeks of bad habits and wasted context windows before it clicked.

And there are still days when it confidently builds something wrong and I spend an hour unwinding it. The tool is powerful. It is not infallible. Knowing the difference matters more than most people realise.

## The next year

I don't know what this looks like by 2027. That's not a throwaway line. I genuinely don't know. The trajectory is steep enough that predictions feel pointless.

What I do know is that the patterns keep compounding. Every system I build teaches me something about the next one. Every CLAUDE.md file makes the next session sharper. The returns aren't linear.

One year in, and I'm still finding new floors.
