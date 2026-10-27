---
name: ai-design-tells
description: Identify and fix generic AI design patterns in websites, landing pages, portfolios, and product interfaces. Use for requests about AI design tells, AI slop, a vibe-coded appearance, templated layouts, or preventing generic design during a build. Supports visual audits, focused repairs, and design briefs; does not infer authorship or replace a supplied brand system or visual target.
---

# AI Design Tells

Make the interface feel intentionally designed for its subject, audience, and task. Use the same discipline as a copy editing pass: identify the pattern, locate the evidence, explain its effect, make a specific correction, and review the result.

## Ground rules

- A visual pattern cannot establish AI authorship. Describe observable repetition, poor fit, or unfinished execution. Do not assign an AI probability or a pseudo-scientific “human” score.
- Preserve the user's chosen identity, approved references, real content, and working behavior. A critique is not authorization to rebuild a site.
- Fonts, purple, gradients, cards, symmetry, serif headings, and minimalism are legitimate choices. Flag their unconsidered use or cumulative repetition, rather than banning them.
- Distinguish a taste preference from a usability defect. Familiar navigation and standard controls often help people.
- Do not invent testimonials, metrics, logos, credentials, product screenshots, or research findings to make a design feel more credible.

## Default preferences (edit these to match your brand)

- Do not use gray or muted gray for readable text by default. Body copy, supporting descriptions, metadata, social links, and footer text should use the primary text color: dark ink on light surfaces and bright cream or white on dark surfaces. Create hierarchy through size, weight, spacing, and placement rather than faded text. Preserve accessible accent colors for links and actions. Apply a different text palette only when the user explicitly requests it or a specific brand requirement overrides it.
- Flag open-ended ruled column grids: internal vertical dividers, often joined to a top horizontal rule, with no bottom rule or outer side borders. This repeated treatment in fact strips and process sections reads as a template default. Avoid it by default; inspect the border treatment itself even when the content legitimately forms a sequence. See the specific repair in [references/patterns.md](references/patterns.md).

## Start with evidence

Read relevant brand guidance, `DESIGN.md`, existing components, and supplied references. Identify the audience, page purpose, primary action, and material worth preserving. Ask only for missing context that would change the recommendation.

For an existing interface, inspect the rendered page or supplied screenshots before claiming visual findings. Capture the relevant desktop and mobile states when tools permit. Read code to explain a finding, not to claim you have seen the render. If preview access is blocked, provide a clearly labeled source review and identify what remains unverified.

Use [references/patterns.md](references/patterns.md) as a diagnostic menu. For an Impeccable catalog request or an exhaustive anti-pattern audit, use [references/impeccable-slop.md](references/impeccable-slop.md): all 67 catalog entries, 11 example scenarios, era comparisons, and review methods, with inspections, repairs, and contextual exceptions. For a focused edit, read only the affected categories; do not expand every edit into a full audit. Preserve project decisions and distinguish source flags, browser evidence, and judgment. For research provenance or updating the menu, read [references/research.md](references/research.md). Do not browse again for every routine use.

## Choose the requested mode

### Audit

Review the main visitor path, rather than merely counting fashionable components. Work from the largest issue to the smallest:

1. Subject and content: could another business use this unchanged after swapping its name?
2. Structure: does the order answer the visitor's actual questions?
3. Hierarchy: does prominence reflect importance?
4. Visual choices: are repeated treatments appropriate to their content?
5. Execution: does the design survive real text, mobile screens, focus, and interaction?

For each material finding, give the location or screenshot, observed pattern, consequence, specific repair, and anything worth keeping. Label evidence as rendered, screenshot-only, or source-only. Prioritize blocked tasks and missing proof before decorative preferences. Do not force a finding in every category.

### Repair

When changes are requested, agree on scope from the existing request and implement the highest-impact corrections. Preserve the established system unless the user asks to reshape it. A radius adjustment alone cannot repair weak information architecture. A font swap alone cannot create an identity.

Use assets with a connection to the actual subject. Match crop, resolution, and composition to their placement. Resolve unclear interactions and unfinished states. Review the changed page at desktop and mobile sizes, plus the interaction states affected. Report exactly what was verified and any remaining limits.

### Prevention / design brief

Before a new build, establish concrete choices instead of adjectives such as “premium” or “make it pop.” Reuse an existing `DESIGN.md`; write or update one only when requested or needed for the authorized build.

Every design brief should identify what is specific to this business and how the page will make that visible. Use supplied people, products, places, expertise, work, and substantiated evidence as inputs. Connect those inputs to composition, imagery, type, and emphasis, with a reason tied to the visitor's task. Record missing assets as gaps; do not invent uniqueness or proof.

When concept exploration is in scope, compare meaningful differences in structure, content order, and what leads the page. Color and font changes alone provide limited alternatives. Establish a direction before generating, then evaluate and refine the output against it. Explain why the selected composition fits the business. For a focused edit, build on the approved direction without requiring a new concept exercise.

Record:

- Audience, task, primary action, and real content or proof.
- Specific business characteristics, available assets, and the visible design decisions they inform.
- References with a named detail to borrow from each, and why it fits.
- Typography roles, line lengths, and intended heading behavior.
- Palette roles, contrast, spacing, layout, and component rules.
- Asset direction and purposeful motion.
- Project-specific patterns to avoid, with reasons and allowed exceptions.

Tie distinctive choices to the subject. Do not automatically replace a generic SaaS style with a generic editorial style. Follow any applicable visual selection workflow; this skill does not waive it.

## Review the result

- What makes this business recognizable, and where is that visible? If swapping the name leaves the page equally suitable for unrelated businesses, revisit its content and composition.
- Does the strongest content receive the strongest emphasis?
- Does every section add something needed?
- Do repeated components represent comparable information?
- Can visitors understand the main action and what happens next?
- Do real headlines, long labels, and narrow screens still work?
- Are contrast, focus, and reduced-motion behavior checked where relevant?
- Does the result still express the user's brand and chosen direction?

Stop once the requested corrections are sufficiently verified. No added novelty, random asymmetry, extra animation, or more expensive technology solely to look less AI-generated.

## Handoff

For an audit, return a short verdict and prioritized findings with evidence and repairs. For implementation, lead with the result, then summarize changes and verification. For a brief, deliver reusable decisions and explain the few consequential choices. Never claim a rendered audit or accessibility compliance from source inspection alone.
