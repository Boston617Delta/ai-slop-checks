# Research basis

Researched September 29, 2026. Sources support design review heuristics, not reliable attribution of AI authorship. No prevalence percentages or detection accuracy are claimed. The diagnostic matrix and repair workflow are an original practical synthesis.

## Primary sources

### Anthropic: convergence and direction

[Improving frontend design through Skills](https://claude.com/blog/improving-frontend-design-through-skills), November 12, 2025.

Anthropic describes recurring default typography, purple gradients, and layouts in underspecified frontend requests. It also acknowledges that attempts to avoid defaults can converge on new repeated choices. Use concrete art direction; treat the article's prescriptive font and animation suggestions as examples, not universal prohibitions or mandatory effects.

### Anthropic: newer default aesthetics

[Frontend Design skill](https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md), live source inspected September 29, 2026.

Its guidance flags several recurring styles, including cream with serif type, dark neon palettes, newspaper treatments, repeated rounded cards, and decorative metadata. It explicitly allows these when the brief calls for them. Takeaway: an avoidance list needs contextual exceptions. This file can change; these observations describe the inspected version.

### Nielsen Norman Group: realistic design context

[AI Prototyping in Real Design Contexts](https://www.nngroup.com/articles/ai-prototyping/), October 24, 2025; page states last review August 19, 2026.

NN/G evaluated tools using a real training-profile redesign and several levels of prompting detail. Generic styling and limited design judgment persisted without extensive direction. This is a scoped evaluation, not evidence about every current tool or every generated page. Use it to justify grounding review in actual user tasks and supplied design artifacts.

### Nielsen Norman Group: prompt specificity and hierarchy

[Prompt to Design Interfaces](https://www.nngroup.com/articles/vague-prototyping/), inspected September 29, 2026.

Their examples show repeated elements, disrupted information flow, and poor emphasis from vague instructions. More detailed direction improved results. This supports checking content order and redundancy before spending effort on surface styling.

### Vercel: interface execution

[Web Interface Guidelines](https://vercel.com/design/guidelines), live guidance inspected September 29, 2026.

Use this as a practical quality reference for usable controls, responsive layouts, meaningful animation, and complete interaction states. It is an interface guideline, not an AI-design detection study.

## User-supplied references

- [Adam: landing-page design](https://www.tiktok.com/t/ZP8wjnCeS/)
- [Janus Tiu: intentional interfaces and design.md](https://www.tiktok.com/t/ZP8w6dCJ4/)
- [Lenar: recurring vibe-coded design patterns](https://www.tiktok.com/t/ZP8wjo7JW/)

These prompted the research. Earlier in this conversation, captions and selected visible frames were inspected; full audio and a complete transcript were not reviewed. Do not attribute a complete trend list or empirical claims to these videos.

## Limits and maintenance

The appearance of human-designed templates overlaps with generated work. Treat isolated style choices as prompts for inquiry, not proof. Repair recommendations are design judgments that should be checked against the specific brief and render. Update the pattern menu when repeated real projects or refreshed primary sources warrant it; avoid accumulating rules from isolated dislikes.

## Impeccable catalog expansion, October 9, 2026

[Public catalog](https://impeccable.style/slop/) and [official rule pack](https://github.com/pbakaus/impeccable/blob/main/crates/live/assets/antipatterns.json), inspected October 9, 2026. The rule pack is Apache-2.0 licensed; see `LICENSE-impeccable-Apache-2.0.txt`. [impeccable-slop.md](impeccable-slop.md) adapts its topics with original checks, repair options, and author-specific exceptions.

Coverage was checked by unique HTML card IDs: 67 cards across nine categories, including six judgment checks; 11 gallery links; three era examples; three review methods. The page’s headline says 65, but its HTML has 67. The official pack has 59 entries; `layout-transition` and `image-hover-transform` appear on the page but are absent from that pack. They remain manual prompts, not promises about detector support.

The snapshot inventory is `impeccable-slop-inventory.json`. It records IDs, category, title, and source evidence label for maintenance, rather than copying full descriptions. These heuristics do not measure AI authorship and do not justify replacing approved serif typography, magenta, or a useful conventional layout.

## User-observed layout tell, October 9, 2026

The author identified the open-ended ruled column treatment in a site's fact strip and five-step process, and has encountered it repeatedly. The specific tell is internal vertical dividers with missing outer side boundaries and/or a bottom rule, often connected to a top horizontal rule. It was not explicitly covered by our earlier generic grid entries.

Added a custom diagnostic to `patterns.md` and a separate section in `impeccable-slop.md`, plus a default preference in the skill entrypoint. This addition records the author's observation and design preference, not measured prevalence, an upstream Impeccable rule, or an authorship inference. Review the geometry even when the content legitimately forms a sequence.

## Business-specific creative direction, October 10, 2026

[How To Stay Original While Designing With AI](https://dribbble.com/stories/2026/09/30/cl-eddie-lobanovskiy-unfold-staying-original-ai-design), Eddie Lobanovskiy / Unfold, published September 30, 2026; reviewed October 10, 2026.

The article describes setting direction before AI exploration, selecting and refining generated material, and reviewing interactive prototypes. It is a practitioner account with agency promotion, not a controlled comparison of tools or evidence that a named tool guarantees originality.

Practical application: every design brief identifies what is specific to the business and how the page makes it visible. Use real assets and evidence, explain the connection to the composition, and refine against an established direction. Meaningful concept alternatives vary structure and emphasis when exploration is in scope. Focused edits preserve the approved direction. No new tools, mandatory moodboard, or extra concept rounds are required by this addition.
