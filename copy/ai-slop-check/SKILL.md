---
name: ai-slop-check
description: Review marketing copy for the patterns that make writing read as machine-made, then rewrite each flagged sentence. Use for landing pages, ads, emails, cold outreach, social posts, video scripts, sales pages, popups, and bios, or when someone asks to "de-AI" a draft, check it for AI slop, or make it sound less like ChatGPT. Not for analytical reports, where qualified language is accuracy rather than weakness.
---

# AI Slop Check

Check a draft against the patterns below, quote every sentence that trips one, and rewrite it. The goal is copy that sounds like a specific person who knows the subject.

## Workflow

Paths below assume Claude Code. In Codex, swap `~/.claude/skills` for `~/.codex/skills`.

1. **Run the checker first.** It catches the mechanical tells (em dashes, colons, arrows, echoes, staccato runs, buzzwords, rejected phrasings, raw counts next to "clients") so your read can go to the judgment calls.
   ```bash
   python3 ~/.claude/skills/ai-slop-check/scripts/check_tells.py draft.md      # .md, .html, or .txt
   python3 ~/.claude/skills/ai-slop-check/scripts/check_tells.py --text "paste copy"
   python3 ~/.claude/skills/ai-slop-check/scripts/check_tells.py draft.md --skip hedge   # regulated copy
   ```
   It prints line number, rule and the quoted sentence, and exits 1 when anything is flagged. Run `--list-rules` for the rule names. The colon and em-dash house rules are on by default; `--skip colon,em-dash` turns them off for a writer whose style allows them. A hit is a prompt to reread the sentence, not a verdict: a quoted headline, a real list intro, or a compliance-required hedge can stay. Never dodge a rule by hiding prose in code formatting.
2. **Read the draft yourself** against the patterns below. The checker can't judge whether a line escalates, whether a contrast is earned, or whether a claim is true.
3. **Rewrite** each flagged sentence (see How to report).
4. **Optional second pass by a different model family.** A model doesn't hear its own habits. For a draft Claude wrote:
   ```bash
   ~/.claude/skills/ai-slop-check/scripts/second_pass.sh draft.md > edited.md 2> notes.txt
   ```
   Use `WRITER=gpt` when ChatGPT or Codex drafted it, so Claude does the pass. If the rival CLI isn't installed the script prints the prompt plus draft and exits 127, so paste that into the other model's chat. Compare the result with the original for changed facts, lost links and invented proof before accepting anything.
5. **Run the Desklib detector** on long-form drafts (blog posts, sales pages, emails over a few paragraphs). It's an open-source model (desklib/ai-text-detector-v1.01, MIT; its model card says it led the RAID detection benchmark when submitted) that scores text from 0 (human) to 1 (AI) for the whole draft, each section, and each paragraph of 40+ words.
   ```bash
   ~/.claude/skills/ai-slop-check/scripts/detect_ai.sh draft.md         # .md, .html, or .txt
   ~/.claude/skills/ai-slop-check/scripts/detect_ai.sh --text "one paragraph"
   ~/.claude/skills/ai-slop-check/scripts/detect_ai.sh page.html --threshold 0.4
   ```
   First run builds a venv in `~/.local/share/ai-slop-check/desklib-venv` with uv and downloads the model (about 1.7 GB); after that it runs offline in about 15 seconds. On HTML it reads the `<article>` and skips the sources list, prompt boxes, code and figures. Exit 1 means the whole draft or a paragraph hit the threshold (default 0.5). Treat it as a weak signal: it has rated drafts a human editor rejected as slop as human-written too, so a low score never clears a draft. A flagged paragraph gets reread against the patterns and rewritten; when testing rewrites of one paragraph, score each variant with `--text` and keep the one that reads right and scores lowest. Report the whole-draft score and any flagged paragraph, never as proof of who wrote it.
6. **Rerun the checker** (and the detector, if you rewrote paragraphs) on the final copy, including right before staging. Report any flag you kept on purpose and why.

## Ground rules

- A pattern doesn't prove a person or a model wrote the text. Flag the sentence, explain the effect on the reader, and fix it. Don't invent an "AI score" yourself; the only score reported is the Desklib detector's, labeled as a weak signal.
- Keep the writer's facts, offer, and voice. Rewrite the flagged sentence only; don't rebuild the piece.
- Never add proof that isn't in the source material. If a claim needs a number, case, or testimonial the writer hasn't supplied, mark it as a question for them.
- Accuracy and compliance come first. Medical, legal, financial, and insurance claims keep whatever qualification their rules require. When a claim can't be made with confidence, cut the claim rather than hedge it.

## Structural patterns

**1. The parallel repetition stack (check this first).** The same word, phrase, or sentence skeleton repeated two or more times in a row for rhythm.
- "More leads. More calls. More revenue."
- "Same close rate. Same conversion. Different result."
- "No inspections. No appraisals. No banks."

Each line should add new information or move the argument forward. If two consecutive lines open with the same word or use the same structure, rewrite one so it escalates instead of echoing.

**2. The false contrast.** "It's not X. It's not Y. It's Z." or "This isn't a tool, it's a system." If a contrast matters, show it with a real comparison or a short story.

**3. Three short sentences in a row.** "This works. It's proven. Here's why." Vary sentence length. A line break is a pacing device, not permission to fragment a thought.

**4. The rhetorical section opener.** "But what does that actually mean?" or "So, how does it work?" Move between sections with a statement.

**5. The "imagine" opener.** "Imagine waking up to a calendar full of booked calls." Open with a fact, a direct challenge, or a specific number.

## Filler transitions

Cut or replace: "Let's dive in," "Here's the thing," "At the end of the day," "In today's fast-paced digital world," "Whether you're a [X] or a [Y]," "More on that later," "But wait, there's more."

## Hedging (persuasive copy only)

Persuasive copy carries conviction. Cut "might," "could potentially," "in many cases," "often," and "usually," then back the statement with specific proof: not "this could potentially double your leads" but the real result you can show. If there's no proof, cut the claim. This rule doesn't apply to reports, audits, or regulated claims (see Ground rules).

## Rejected phrasings

Patterns a reader flagged as "I would never say this." Treat each as a pattern, not a phrase.

- **Pedantic qualifier.** "...in the way the word suggests." Say the plain claim.
- **"It's easy" reassurance.** "That's the whole job," "only takes about fifteen minutes." State a time once, flatly, with no "only" or "that's all."
- **Denial nobody raised.** "...and laziness has nothing to do with it." Cut it.
- **Announcing what's coming.** "I want to show you," "hiding in plain sight," "the posts below." Show the thing.
- **"It's simple" framing.** Give the step; never call it simple.
- **Vague referents and invented labels.** "Connect the two," "the lightweight version." Name the actual thing.
- **Folksy justification.** "The boring way," "which is exactly why."
- **Lesson-learned setup.** "I learned why X matters." Tell what happened.
- **Coaching voice and fake precision.** "You're the only one who knows," "in ten seconds," "upgrade what comes back." Say what the reader gets.
- **Reference the reader can't follow yet.** Pointing at a section or level the reader hasn't reached. Name the task instead.

## Buzzwords

Replace with what actually happens: delve, seamless, unlock, unleash, elevate, leverage, robust, empower, streamline, game-changing, revolutionize, transformative, tapestry, testament to, unparalleled, supercharge, effortless, cutting-edge, world-class, holistic, synergy, journey, realm, landscape, embark, curated, pivotal, foster.

## Proof

Any number sitting next to clients, customers, leads or calls needs a source the writer supplied. Multipliers and percentages are fine when they're real; raw client or lead counts don't go in public copy.

## Formatting

- No emoji unless the platform expects them, and never in sales pages, scripts, or email.
- No arrows (→ or any arrow glyph) in CTAs, buttons, link text or "Read more" links.
- Almost no exclamation points. Urgency comes from the offer and the proof.
- No five- or six-sentence paragraph blocks in long-form copy.
- Optional house rule: no colons except to introduce a bulleted or numbered list underneath, including in headings and titles. A setup-then-payoff colon reads as a formula. Join the halves into one sentence rather than splitting them into two.
- Optional house rule: no em dashes. Use commas, colons, or periods. Turn it off if your style allows them.

## How to report

For each hit, give:
1. The pattern number or name.
2. The exact sentence, quoted.
3. One line on why it weakens the copy for the reader.
4. A rewrite that keeps the meaning.

Then reread the full draft once more, because rewrites can create new repetition. End with a count of hits by pattern so the writer can see their habits.
