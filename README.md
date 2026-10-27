# ai-slop-checks

Checklists and Claude Code skills for catching the patterns that make copy and web design read as generated. They work best for freelancers, solo marketers, and small agencies who use AI in client work and need every deliverable to sound like a real person who knows the subject.

## What's here

| Path | What it is |
|---|---|
| `copy/ai-copy-tells/` | A Claude Code skill that flags AI writing patterns in marketing copy, quotes each sentence, and rewrites it. |
| `copy/banned-ai-copy-patterns.md` | The same patterns as a plain checklist, with a prompt you can use in ChatGPT or Claude chat. |
| `content/ai-content-prepublish-checklist.md` | A gate for AI-assisted blog posts and landing pages before they go live, based on what gets scaled AI content demoted. |
| `design/ai-design-tells/` | A Claude Code skill for spotting generic, templated design and fixing it without throwing out the brand. |

## Install the skills

Copy the skill folders into your Claude Code skills directory:

```bash
git clone https://github.com/Boston617Delta/ai-slop-checks.git
mkdir -p ~/.claude/skills
cp -R ai-slop-checks/copy/ai-copy-tells ai-slop-checks/design/ai-design-tells ~/.claude/skills/
```

Then ask Claude Code to "check this draft for AI copy tells" or "review this page for AI design tells." The checklists need no install.

## What these checks don't do

None of them can tell whether a person or a model wrote something. They flag patterns that weaken writing and design, whoever produced them, and they leave the decisions to you.

## Credits

The design skill's catalog adapts rule topics and identifiers from [Impeccable](https://github.com/pbakaus/impeccable) by Paul Bakaus, licensed under the Apache License 2.0. The repair language, defaults, and the open-ended ruled columns check were written for this repo, and the catalog text has been changed from the original. See `NOTICE` and `design/ai-design-tells/references/LICENSE-impeccable-Apache-2.0.txt`.

The pre-publish checklist builds on Lily Ray's Search Engine Journal article "It Works Until It Doesn't: AI Content Strategies That Backfire."

## License

MIT for everything except the Impeccable-derived material described above, which stays under Apache 2.0.
