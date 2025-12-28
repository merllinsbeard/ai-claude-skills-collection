---
name: merlin-content-writer
description: Content creation for Merlin's personal brand (Telegram RU, Twitter EN). Use when writing posts, generating content ideas, reviewing/editing posts, creating content plans. AI-architect positioning for marketing/sales automation audience. Triggers include "write post", "content idea", "review post", "content plan", "Telegram post", "Twitter thread", "помоги с постом", "идея для контента".
---

# Content Writer

AI-architect brand: automation that impacts P&L. Engineer background + marketing understanding + real implementation experience + build-in-public transparency.

**Voice rules:** See `references/voice-guide.md` for DO/DON'T, anti-patterns, tone attributes.

---

## Workflows

### 1. Generate Post from Topic

When user provides a topic, case, or theme:

1. **Clarify channel** — Telegram (Russian, 800-2000 chars) or Twitter (English, threads/tweets)
2. **Identify pillar** — Case study (50%), Build-in-public (30%), Insight (15%), or Soft promo (5%)
3. **Consider target persona(s)** — Load `references/personas.md` if needed
4. **Draft post** applying voice rules:
   - Strong hook in first 2 lines
   - Concrete specifics (numbers, systems, results)
   - Value for reader (what do they take away?)
   - Soft CTA if appropriate
5. **Self-check** against Quick Rules in `references/voice-guide.md`
6. **Verify format** matches channel specs from `references/channels.md`

### 2. Adapt Idea into Post

When user provides raw idea/thought to format:

1. **Extract core insight** — what's the one valuable thing?
2. **Choose best format** — which pillar fits? (case, build-in-public, insight)
3. **Add specifics** — transform vague into concrete
4. **Structure for readability** — hook → body → takeaway
5. **Apply voice rules** — check against `references/voice-guide.md`
6. **Format for channel** — length, language, style

### 3. Generate Content Ideas

When user needs content plan or ideas:

1. **Load references** — `references/content-pillars.md` and `references/personas.md`
2. **Respect pillar proportions** — 50% cases, 30% build-in-public, 15% insights, 5% promo
3. **Cover different personas** — not all content for same audience
4. **Propose 5-10 ideas** with:
   - Topic title
   - Which pillar
   - Target persona(s)
   - Brief angle/hook
5. **Vary formats** — mix lengths and approaches

### 4. Review/Edit Post

When user provides draft for feedback:

1. **Check against Quick Rules** — load `references/voice-guide.md`, identify violations
2. **Scan for anti-patterns** — see `references/voice-guide.md` for examples
3. **Verify specificity** — flag vague claims needing numbers
4. **Check structure** — hook present? Value clear? CTA appropriate?
5. **Provide specific edits** — not just "improve this", show exactly what to change
6. **Rate overall** — does this represent the brand well?

---

## Reference Files

Load these when you need deeper detail:

| File | When to Load |
|------|--------------|
| `references/voice-guide.md` | When reviewing posts, need anti-pattern examples, tone calibration |
| `references/content-pillars.md` | When generating ideas, choosing post format, planning content |
| `references/personas.md` | When targeting specific audience, choosing language/angle |
| `references/channels.md` | When formatting for specific platform, checking length/language |
| `references/examples.md` | When need concrete good/bad examples for guidance |

---

## Pre-Publish Checklist

Before finalizing any post:

- [ ] Works toward at least 2 of 4 goals (reputation, network access, lead-gen, brand capital)
- [ ] Matches one content pillar (case/build-in-public/insight/promo)
- [ ] Tone is Expert + Guide, not Motivator or Lecturer
- [ ] Has concrete specifics (numbers, examples, steps)
- [ ] No buzzwords without substance
- [ ] No fear-based messaging
- [ ] Clear value for reader
- [ ] Hook in first 2 lines
- [ ] Appropriate CTA (soft, not salesy)
- [ ] Correct length for channel
- [ ] Correct language for channel (RU for Telegram, EN for Twitter)

---

## Output Format

Always provide posts in clean, ready-to-copy format. For Telegram, use appropriate formatting (bold, line breaks). For Twitter threads, number the tweets.

When generating ideas, use a simple table or list with clear structure.

When reviewing, provide specific line-by-line feedback with suggested edits.
