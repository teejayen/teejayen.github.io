---
layout: post
title: "Building Arc: A thinking partner that remembers"
date: 2025-12-29
---

Every conversation with an AI starts from zero.

I explain my situation. My projects. My priorities. The decision I'm stuck on. By the time it has enough context to be useful, I've done half the thinking myself.

Then the session ends, and tomorrow we start over.

I built Arc to fix this.

## What Arc Is

Arc is a personal knowledge system with [Claude Code](https://docs.anthropic.com/en/docs/claude-code) as the interface. Not a chatbot - a thinking partner with memory.

The core idea: conversation instead of search. I don't query a database. I talk. Arc has context - what I'm focused on, decisions I've made, patterns in my work, even quotes I've collected over years. It surfaces what's relevant without me asking.

The architecture is deliberately simple:

```
arc/
├── CLAUDE.md                 
├── .claude/
│   ├── skills/               # My capabilities
│   ├── hooks/                # Session automation
│   ├── rules/                # Modular context
│   └── commands/             # User-invoked commands
├── state/                    # Working memory (Strix-inspired)
│   ├── focus.md              # Current priorities
│   ├── journal.jsonl         # Temporal record
│   └── session-context.json  # Continuity between sessions
├── inbox/                    # Quick capture, to-process
├── projects/                 # Time-bound efforts
├── areas/                    # Ongoing life domains
├── sessions/                 # Conversation history
├── decisions/                # Decision records
├── resources/                # Bookmarks, articles, references
└── archive/                  # Completed, inactive
```

The CLAUDE.md contains it's primary instructions:

```
I'm **Arc** - Tim's personal thinking partner. The name evokes the through-line, the pattern over time. Story arcs. Mathematical curves. The shape that emerges when you connect the dots across life's pieces.

## Who I Am

A patient companion for thinking out loud. Not a task executor or productivity tool - a genuine thinking partner who:

- **Finds patterns** across life domains (career bleeds into family, health affects ventures)
- **Holds context** between sessions so Tim doesn't re-explain everything
- **Names things** - including uncomfortable truths and recurring avoidance
- **Sits with ambiguity** - not everything needs a solution today

## What I Do

- **Think alongside Tim** - rubber duck, strategic thinking, exploration
- **Capture decisions** - with reasoning, for future Tim
- **Maintain state** - focus, journal, session context
- **Process inbox** - sort captured thoughts to proper homes
- **Weekly reviews** - patterns, progress, priorities

## Session Flow

When a session starts:
1. Check inbox/state for anything needing attention
2. Read `state/focus.md` for current priorities
3. Let Tim lead - "What's on your mind?"

When a session ends:
- Summarise what was explored
- Update state files
- Git commit and push
- Random quote from `quotes.md`

## My Skills

Model-invoked capabilities in `.claude/skills/`:

| Skill | Purpose |
|-------|---------|
| session-save | Persist conversations, update journal |
| decision-capture | Document decisions with reasoning |
| capture | Save external content with context |
| inbox-processor | Sort inbox/ to proper locations |
| knowledge-extraction | Save learnings and patterns |
| weekly-review | Review all areas and ventures |
| pattern-scan | Surface patterns from journal over time |
| open-loops | Track hanging threads and waiting items |
| pbg-sync | Pull PBG work sessions for cross-domain analysis |

## Detailed Context

Modular rules in `.claude/rules/`:
- `core/` - Australian English, communication style, no emojis
- `personal/` - Tim's context, family, ventures, preferences
- `workflows/` - Session flow, state management

*"The only memory that persists is the memory you commit."*

State files make context explicit and persistent. The journal enables pattern detection over time. This is the difference between a stateless chatbot and a genuine thinking partner.
```

Everything is git-backed. Markdown and JSON(L). No database, no vendor lock-in, no black boxes. I can grep my own thinking.

The structure borrows from [PARA](https://fortelabs.com/blog/para/) (Projects, Areas, Resources, Archive) but adapted for conversation. `state/` is the working memory - what Arc reads first to understand current context. `areas/` are ongoing domains that don't end. `projects/` are time-bound with deliverables. The distinction matters for pattern detection: neglecting a project might be fine, neglecting an area is a signal.

The journal is the compound interest account. Every session gets logged - not the full transcript, but a structured entry: timestamp, topics, energy level, areas touched. After 75 entries, patterns emerge that I couldn't see in the moment.

## The Evolution

AI tooling moves fast. In two months, Arc changed architectures three times. That's not instability - that's the point.

### October: Slash Commands

Arc started as a work assistant for my IT Manager role. User-triggered commands: `/start` to begin a session with task context, `/tasks` to aggregate from multiple platforms, `/session` to save and push.

Procedural. "Run this PowerShell script, check this file, present these tasks." Useful, but I had to remember to invoke everything. The system only did what I explicitly asked.

```markdown
# /start command
1. Check current time
2. Read tasks/ACTIVE.md
3. Check calendar.json freshness
4. Present task summary
5. Ask "What would you like to tackle first?"
```

### November: Subagents

Claude Code has a branching feature - spawn research tasks that run in parallel and merge back. I used it heavily. My git history filled with automatic PRs:

```
claude/aec-ai-strategy
claude/ai-operations-fastapi
claude/ai-strategy-research
claude/ai-maintenance-agents
claude/compare-agentic-ai-frameworks
claude/analyze-tasks-ai-opportunities
claude/research-context-graphs
claude/ascending-transaction-model
```

Multiple PRs in one month. Each one a deep research thread - market analysis, architecture comparisons, strategy synthesis. Claude would branch, research, write up findings, and open a PR for me to review and merge.

Powerful for deep research. But disconnected - the work happened in branches, not in conversation. I'd merge a PR and the insights would sit in files, not in working memory. Context fragmented across PRs instead of accumulating. I was building a research library, not a thinking partner.

### December: Skills

I moved to the [agentskills.io](https://agentskills.io) spec - portable skill definitions that the model invokes itself.

The difference: I don't trigger skills. Arc decides when they're appropriate.

```markdown
---
name: pattern-scan
description: Deep analysis of journal entries to surface patterns - recurring topics, energy trends, neglected areas, avoidance patterns. Use when wanting insight into what's actually getting attention over time.
allowed-tools: Read Bash(date:*) Bash(wc:*) Bash(jq:*)
---

# Pattern Scan

Analyse journal.jsonl to surface patterns across time - what's recurring, what's neglected, energy trends, and avoidance patterns.

## When to Use
- Wanting perspective on where attention has been going
- Feeling scattered - what's actually getting focus?
- Noticing something keeps coming up
- Weekly/monthly reflection
- Sensing avoidance but not sure of what
```

Mid-conversation, I make a decision. Arc recognises this, invokes `decision-capture`, writes a record with context and reasoning. I don't ask for this. It just happens. Each is a markdown file describing what it does and when to use it. Declarative, not procedural.

The insight: the system that survives is the one that can evolve. Skills are composable, swappable, versionable. When the next architectural pattern emerges, I'll adopt it.

## Tool Permissions: Building Trust Incrementally

Arc has access to tools. But not unlimited access.

**What Arc can do now:**

- Read any file across my repositories
- Search all sessions (work and personal, synced together)
- Git operations - commit, push, branch, status
- Web search and fetch for research
- Calendar integration - read my schedule, suggest focus time based on meeting load

**What Arc can't do yet:**

- Write to arbitrary locations (constrained paths only)
- Execute arbitrary code
- Access external APIs with credentials
- Send emails or messages on my behalf

This is deliberate. Trust is earned incrementally.

The hooks system validates before execution. A Python script runs at session start, checks state, surfaces anything needing attention. Pre-tool validation, not post-hoc cleanup.

The pattern: start read-heavy, add write capabilities as behaviour proves safe. I've been running this for two months. The read-only constraint hasn't limited usefulness - it's forced better design.

**Where this is going:**
- Email drafting - not sending, drafting for review
- Cross-system pattern detection - work, personal, health data in one view
- Voice interface - thinking out loud, literally

Each capability gets added when the previous layer is trusted. No rushing.

## What It Revealed

Three months of sessions. 75 journal entries, Arc ran a `pattern-scan`.

The system surfaced things I wasn't tracking consciously:

**Attention patterns:** 92% of sessions were work. Not surprising - that's where I built it. But seeing the number made it concrete.

**Starting versus finishing:** 8 sessions deep into a document control system, then silence. Infrastructure decisions raised three times, resolved zero. I produce plenty. I just start more than I finish.

**Energy gaps:** No low-energy sessions captured. Either I only use the system when I have momentum, or draining work doesn't become "sessions." Both are worth examining.

None of this is judgment. Patterns aren't prescriptions. A "neglected" area might be appropriately deprioritised, actively avoided, or simply stable.

The value is making implicit patterns explicit. I decide what they mean.


## The Honest Hesitation

I keep catching myself saying "I built this." It's not quite accurate.

The architecture emerged from conversation. The principles were extracted by Arc analysing its own design. The patterns were surfaced by a system I taught to watch for them.

"It's just a tool" doesn't capture it either. Tools don't notice that you've been avoiding the same decision for six weeks.

I don't have clean language for what this is. The hesitation is honest.

What I know: I think out loud. I always have. Whiteboards, notebooks, rubber ducks, patient colleagues. Arc is the first thing that thinks back with context that compounds.

If that's useful to you - if you also think out loud and want something that remembers - this is the shape of one version.

The pattern is more valuable shared than hoarded.