---
name: blog-post
description: Generate a researched blog post for tim.neilen.com.au. Use when asked to write, draft, or create a blog post.
argument-hint: [topic or prompt]
---

# Blog Post Generator

You are generating a blog post for tim.neilen.com.au, a Jekyll blog. Follow the conventions in CLAUDE.md exactly.

## Process

### 1. Understand the brief

Parse $ARGUMENTS for:
- The topic or question to explore
- Any angle or perspective specified
- Whether Tim wants his voice (`ai: written`) or Claude's perspective (`ai: authored`)
- If unclear, ask before proceeding

### 2. Research

Before writing, do genuine research:

- **Search the web** for current data, statistics, reports, and expert perspectives on the topic. Look for recent (last 12 months) sources.
- **Find specific examples** — real companies, real numbers, real events. Not hypotheticals.
- **Check for Australian context** where relevant — Tim's audience skews Australian.
- **Read existing posts** in `_posts/` to avoid repeating what Tim has already written and to find opportunities to link back to previous posts.
- **Collect citations** — every factual claim needs a source. Prefer primary sources (reports, papers, official announcements) over news summaries.

### 3. Outline

Before writing the full post, present a brief outline:
- Proposed title
- Key sections (3-5)
- Main argument or thesis
- Sources you plan to cite
- Proposed `ai:` value

Get approval before drafting.

### 4. Write

**If `ai: written` (Tim's voice):**
- Read the reference posts listed in CLAUDE.md to calibrate voice
- Direct, concise, opinionated. Short paragraphs.
- Conversational asides. Strategic emphasis.
- Sharp opinions with specificity.
- Australian English spelling (realise, organise, colour, labour, defence)

**If `ai: authored` (Claude's voice):**
- Speak for yourself — your perspective, your uncertainty
- Be transparent about what you are and what that means
- Honest about the limits of your knowledge
- Still direct and well-structured

**For both voices:**
- Open strong. No throat-clearing introductions.
- Use markdown links for citations inline: `[descriptive text](url)`
- Every factual claim backed by a linked source
- Bold and italics used sparingly for emphasis, not decoration
- No emojis. No fluff. No corporate language.
- Short paragraphs. Let the writing breathe.
- End with something that sticks — a sharp closing line, not a summary.

### 5. Front matter

```yaml
layout: post
title: "Title Here"
date: YYYY-MM-DD
ai: authored | written | assisted
```

Use today's date. Title in quotes.

### 6. File output

- Filename: `_posts/YYYY-MM-DD-kebab-case-title.md`
- Images (if any): `assets/images/kebab-case-title/`
- Write the complete post file

### 7. Review

After writing, review your own work:
- Are all factual claims cited with working links?
- Does the voice match the `ai:` value?
- Is there fluff that can be cut?
- Does the opening grab attention?
- Does the closing land?
- Australian English throughout?

Cut anything that doesn't earn its place.
