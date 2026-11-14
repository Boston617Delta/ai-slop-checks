# ai-slop-checks

Checklists, plus skills for Claude Code and Codex, that catch the patterns that make copy and web design read as generated. They work best for freelancers, solo marketers, and small agencies who use AI in client work and need every deliverable to sound like a real person who knows the subject.

## What's here

| Path | What it is |
|---|---|
| `copy/ai-slop-check/` | A skill for Claude Code or Codex that flags AI writing patterns in marketing copy, quotes each sentence, and rewrites it. It ships with a pattern checker script, an optional second edit by a different model, and an optional open-source AI-text detector. |
| `copy/banned-ai-copy-patterns.md` | The same patterns as a plain checklist, with a prompt you can use in ChatGPT or Claude chat. |
| `content/ai-content-prepublish-checklist.md` | A gate for AI-assisted blog posts and landing pages before they go live, based on what gets scaled AI content demoted. |
| `design/ai-design-tells/` | A skill for Claude Code or Codex for spotting generic, templated design and fixing it without throwing out the brand. |

## Install the skills

Both skills work in Claude Code and in Codex. Copy the skill folders into whichever you use:

```bash
git clone https://github.com/Boston617Delta/ai-slop-checks.git

# Claude Code
mkdir -p ~/.claude/skills
cp -R ai-slop-checks/copy/ai-slop-check ai-slop-checks/design/ai-design-tells ~/.claude/skills/

# Codex
mkdir -p ~/.codex/skills
cp -R ai-slop-checks/copy/ai-slop-check ai-slop-checks/design/ai-design-tells ~/.codex/skills/
```

Then ask it to "run an AI slop check on this draft" or "review this page for AI design tells." The checklists need no install, and the copy checklist includes a prompt for ChatGPT or Claude chat.

## The copy skill's scripts

- `scripts/check_tells.py` flags the mechanical patterns (repetition, false contrasts, staccato runs, filler, stock reveals, leaked chatbot phrasing, buzzwords, colons, em dashes, arrows) with line numbers. Python standard library only, no network.
- `scripts/second_pass.sh` hands a draft to a different model family for an edit, Codex for a Claude draft or Claude for a ChatGPT draft, because a model doesn't hear its own habits. Without the other CLI installed it prints a prompt to paste instead.
- `scripts/detect_ai.sh` scores a draft with [Desklib's AI-text detector](https://huggingface.co/desklib/ai-text-detector-v1.01) for the whole draft, each section and each long paragraph. It needs [uv](https://docs.astral.sh/uv/); the first run builds a Python venv and downloads the model (about 1.7 GB), and later runs work offline. Treat the score as a weak signal. A low score never clears a draft.

## What these checks don't do

None of them can tell whether a person or a model wrote something, the detector included. They flag patterns that weaken writing and design, whoever produced them, and they leave the decisions to you.

## Credits

The copy skill and the banned-patterns checklist are original to this repo, including the specific AI phrases and sentence patterns they flag. The idea of a scripted check before and after the model edit, and of a second edit by a rival model, comes from [SlopMonster](https://github.com/ItsssssJack/SlopMonster) (MIT); the rules and scripts here are written for this repo. The detector downloads [desklib/ai-text-detector-v1.01](https://huggingface.co/desklib/ai-text-detector-v1.01) (MIT) at runtime, and none of its weights are stored here.

The pre-publish checklist starts from the content strategies Lily Ray examined in her Search Engine Journal article "It Works Until It Doesn't: AI Content Strategies That Backfire," and adds its own checks: the AI phrases and sentence patterns to cut, a logo-swap test for originality, Google's guidance on reviewing AI content, and pacing for new pages.

The design skill adds its own repair guidance, defaults, and the open-ended ruled columns check to a catalog of rule topics adapted from [Impeccable](https://github.com/pbakaus/impeccable) by Paul Bakaus (Apache License 2.0; see `NOTICE`).

## License

MIT for everything except the Impeccable-derived material described above, which stays under Apache 2.0.
