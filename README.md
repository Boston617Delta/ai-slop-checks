# ai-slop-checks

Checklists and skills for Claude Code and Codex for catching the patterns that make copy and web design read as generated. They work best for freelancers, solo marketers, and small agencies who use AI in client work and need every deliverable to sound like a real person who knows the subject.

## What's here

| Path | What it is |
|---|---|
| `copy/ai-copy-tells/` | A skill for Claude Code or Codex that flags AI writing patterns in marketing copy, quotes each sentence, and rewrites it. |
| `copy/banned-ai-copy-patterns.md` | The same patterns as a plain checklist, with a prompt you can use in ChatGPT or Claude chat. |
| `content/ai-content-prepublish-checklist.md` | A gate for AI-assisted blog posts and landing pages before they go live, based on what gets scaled AI content demoted. |
| `design/ai-design-tells/` | A skill for Claude Code or Codex for spotting generic, templated design and fixing it without throwing out the brand. |

## Install the skills

Both skills work in Claude Code and in Codex. Copy the skill folders into whichever you use:

```bash
git clone https://github.com/Boston617Delta/ai-slop-checks.git

# Claude Code
mkdir -p ~/.claude/skills
cp -R ai-slop-checks/copy/ai-copy-tells ai-slop-checks/design/ai-design-tells ~/.claude/skills/

# Codex
mkdir -p ~/.codex/skills
cp -R ai-slop-checks/copy/ai-copy-tells ai-slop-checks/design/ai-design-tells ~/.codex/skills/
```

Then ask it to "check this draft for AI copy tells" or "review this page for AI design tells." The checklists need no install, and the copy checklist includes a prompt for ChatGPT or Claude chat.

## What these checks don't do

None of them can tell whether a person or a model wrote something. They flag patterns that weaken writing and design, whoever produced them, and they leave the decisions to you.

## Credits

The copy skill and the banned-patterns checklist are original to this repo, including the specific AI phrases and sentence patterns they flag.

The pre-publish checklist starts from the content strategies Lily Ray examined in her Search Engine Journal article "It Works Until It Doesn't: AI Content Strategies That Backfire," and adds its own checks: the AI phrases and sentence patterns to cut, a logo-swap test for originality, Google's guidance on reviewing AI content, and pacing for new pages.

The design skill adds its own repair guidance, defaults, and the open-ended ruled columns check to a catalog of rule topics adapted from [Impeccable](https://github.com/pbakaus/impeccable) by Paul Bakaus (Apache License 2.0; see `NOTICE`).

## License

MIT for everything except the Impeccable-derived material described above, which stays under Apache 2.0.
