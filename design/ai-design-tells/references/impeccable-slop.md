# Impeccable: complete design checklist

Updated October 9, 2026. A maintained practical reference for the `ai-design-tells` skill.

## Scope and source

Coverage: all **67 visible catalog entries**, the **11 linked examples**, three era demonstrations, and the page’s three review methods. The page advertises 65 entries / 59 detector rules plus six judgment checks; its actual HTML contains 67 cards. The official rule pack contains 59 IDs. The extra two source-labeled cards (`layout-transition`, `image-hover-transform`) are absent from that pack, so retain them as manual review checks rather than promising automated coverage.

The 59 official rule definitions are Apache-2.0 licensed: [Impeccable rule pack](https://github.com/pbakaus/impeccable/blob/main/crates/live/assets/antipatterns.json), [license](https://github.com/pbakaus/impeccable/blob/main/LICENSE). This document adapts their topics with original diagnostics, repairs, and contextual exceptions. The other eight checks are independently worded review prompts mapped to the [public catalog](https://impeccable.style/slop/). No demo artwork or screenshot is reproduced.

## How to use this checklist

- For a focused edit, read the affected category. For an explicit whole-page audit, cover all applicable categories and the main visitor task.
- **System** means compare with documented project decisions; **Taste** means inspect fit and cumulative repetition; **Quality** means investigate a potential usability or execution defect. None establishes AI authorship.
- **S** = page labels source inspection; **B** = rendered/browser evidence; **R** = design judgment. These are source classifications, not a promise about the installed engine. Source flags still need context; a visual claim needs a render or screenshot.
- Record each applicable check as issue, intentional/keep, not applicable, or unverified. Missing evidence is not a pass. Do not force 67 findings.
- A useful finding identifies location, evidence, consequence, repair, and what to preserve. Prioritize blocked tasks, unreadable content, missing proof, and broken behavior before decorative preferences.
- Default: no gray or muted gray readable text, including notes and footer text. Use the primary text color and preserve accessible accents. Preserve the brand's approved type and colors.

## Contents

1. Design-system consistency
2. Surface treatments
3. Typography
4. Color and contrast
5. Layout and spacing
6. Motion
7. Copy
8. Imagery
9. General execution
10. Demonstrations and review methods

## Design-system consistency (4)

| Check / source ID | Kind / evidence | Inspect | Repair or intentional exception |
| --- | --- | --- | --- |
| [Unrecorded typeface](https://impeccable.style/slop/#rule-design-system-font)<br>`design-system-font` | System / S | Compare computed families and fallback stacks with the project record. | Use the existing role or document an approved addition; a fallback is not automatically drift. |
| [Unrecorded color](https://impeccable.style/slop/#rule-design-system-color)<br>`design-system-color` | System / S | Compare visible colors, including states and themes, with palette roles. | Reuse a role; record an intentional new state. Preserve authentic image colors and data encodings. |
| [Unrecorded corner shape](https://impeccable.style/slop/#rule-design-system-radius)<br>`design-system-radius` | System / S | Check radii against documented component sizes and shapes. | Use the appropriate token; record a deliberate exception such as an avatar or circular control. |
| [Unrecorded type size](https://impeccable.style/slop/#rule-design-system-font-size)<br>`design-system-font-size` | System / S | Compare role sizes and responsive expressions with the documented scale. | Resolve accidental one-offs. Keep fluid sizing or an authorized new role and document it. |

## Surface treatments (8)

| Check / source ID | Kind / evidence | Inspect | Repair or intentional exception |
| --- | --- | --- | --- |
| [Background grid used as ornament](https://impeccable.style/slop/#rule-codex-grid-background)<br>`codex-grid-background` | Taste / S | Ask whether the lines help someone align, measure, or navigate. | Remove distracting decoration. Keep meaningful grids in maps, editors, or a specifically approved identity. |
| [Heavy colored card outline](https://impeccable.style/slop/#rule-border-accent-on-rounded)<br>`border-accent-on-rounded` | Taste / S | Inspect whether the outline dominates the content or awkwardly follows curved corners. | Reduce its prominence using system borders. Keep a strong outline for a real selected or warning state. |
| [Blurred panels throughout](https://impeccable.style/slop/#rule-glassmorphism)<br>`glassmorphism` | Taste / R | Check whether transparency clarifies layers. | Use opaque surfaces where readability suffers; retain purposeful translucency. |
| [Decorative stripe on every panel](https://impeccable.style/slop/#rule-side-tab)<br>`side-tab` | Taste / S | Check whether the stripe implies status that the content does not have. | Reserve accents for meaningful states or categories. Ordinary prose can use spacing or a divider. |
| [Multiple competing surface edges](https://impeccable.style/slop/#rule-gpt-thin-border-wide-shadow)<br>`gpt-thin-border-wide-shadow` | Taste / S | Inspect the combined hairline and broad shadow at actual rendered size. | Choose a clear boundary treatment. Combine them only when a layered surface needs both. |
| [Striped filler texture](https://impeccable.style/slop/#rule-repeating-stripes-gradient)<br>`repeating-stripes-gradient` | Taste / S | Ask whether repeated stripes explain material, progress, or a real state. | Simplify background noise. Keep stripes for a documented brand texture or meaningful encoding. |
| [Corners consume the card](https://impeccable.style/slop/#rule-over-round)<br>`over-round` | Taste / R | Inspect available content space. | Fit radius to component dimensions; preserve deliberately playful shapes. |
| [Unfinished vector artwork](https://impeccable.style/slop/#rule-sketchy-svg)<br>`sketchy-svg` | Taste / R | Inspect illustration craft and consistency. | Replace or finish weak artwork; retain intentional sketch styling. |

## Typography (11)

| Check / source ID | Kind / evidence | Inspect | Repair or intentional exception |
| --- | --- | --- | --- |
| [Redundant heading prelabel](https://impeccable.style/slop/#rule-kicker-above-heading)<br>`kicker-above-heading` | Taste / S | Read the label and heading together; does each contribute distinct context? | Delete duplication or move useful context into the title or metadata. |
| [Control labels too small](https://impeccable.style/slop/#rule-undersized-ui-text)<br>`undersized-ui-text` | Quality / S | Read navigation, footer links, and controls at normal zoom on a phone. | Increase size within the system and check wrapping. Dense interfaces still need legible labels and usable targets. |
| [Roles look equally prominent](https://impeccable.style/slop/#rule-flat-type-hierarchy)<br>`flat-type-hierarchy` | Taste / S | Scan headings, labels, and paragraphs without reading every word. | Differentiate roles with size, weight, and grouping. Keep intentionally quiet hierarchy if scanning remains easy; never fade supporting text. |
| [Decorative icon box before each title](https://impeccable.style/slop/#rule-icon-tile-stack)<br>`icon-tile-stack` | Taste / S | Compare icon prominence with the information it introduces. | Remove the tile or integrate a useful icon beside its label. Preserve recognizable action and status symbols. |
| [Editorial typography applied by reflex](https://impeccable.style/slop/#rule-italic-serif-display)<br>`italic-serif-display` | Taste / S | Check whether large italic serif type fits the subject and established identity. | Tune role, wrapping, and scale to the page. Keep an approved serif treatment; changing fonts is not the default repair. |
| [Hero label resembles a button](https://impeccable.style/slop/#rule-hero-eyebrow-chip)<br>`hero-eyebrow-chip` | Taste / S | Check whether the chip is actionable, informative, or merely repeats the message. | Use plain metadata or remove it. Preserve an actual status or announcement link with clear behavior. |
| [Headline crowds out the offer](https://impeccable.style/slop/#rule-oversized-h1)<br>`oversized-h1` | Taste / S | Inspect the first viewport with real copy and narrow screens. | Balance title, explanation, imagery, and primary action. A short display name can stay large if the composition works. |
| [Letters collide](https://impeccable.style/slop/#rule-extreme-negative-tracking)<br>`extreme-negative-tracking` | Taste / S | Inspect character separation in the actual font at each size. | Relax tracking until words remain clear. A display-specific optical adjustment need not become a body-text rule. |
| [Default font choice lacks a reason](https://impeccable.style/slop/#rule-overused-font)<br>`overused-font` | Taste / S | Compare the typography with audience, reading needs, and brand references. | Specify roles and tune them first. Retain suitable established fonts; use familiarity alone as no reason to replace them. |
| [One family lacks useful role contrast](https://impeccable.style/slop/#rule-single-font)<br>`single-font` | Taste / R | Inspect hierarchy before adding fonts. | Tune weight, size, and spacing; add a family only if needed. |
| [Paragraphs in capitals](https://impeccable.style/slop/#rule-all-caps-body)<br>`all-caps-body` | Quality / S | Read long uppercase passages on narrow screens. | Use sentence case for reading copy. Keep brief identifiers or branding when required and readable. |

## Color and contrast (7)

| Check / source ID | Kind / evidence | Inspect | Repair or intentional exception |
| --- | --- | --- | --- |
| [Colored glow behind the page](https://impeccable.style/slop/#rule-radial-halo)<br>`radial-halo` | Taste / S | Check whether the halo changes contrast or steals emphasis from content. | Remove gratuitous lighting; preserve a specific visual direction when it supports the subject and readable foreground. |
| [Floating haze behind a section](https://impeccable.style/slop/#rule-radial-spotlight-glow)<br>`radial-spotlight-glow` | Taste / S | Ask why this section needs special lighting rather than clearer hierarchy. | Resolve emphasis through content order, grouping, or palette roles. Keep intentional lighting for a meaningful scene. |
| [Palette chosen from familiar defaults](https://impeccable.style/slop/#rule-ai-color-palette)<br>`ai-color-palette` | Taste / S | Check the relationship between colors, brand, and action/state roles. | Use a considered palette. An approved brand color remains; purple or cyan alone establishes neither poor design nor AI authorship. |
| [Glowing accents overwhelm dark mode](https://impeccable.style/slop/#rule-dark-glow)<br>`dark-glow` | Taste / S | Inspect cumulative glow across text, borders, buttons, and backgrounds. | Reduce competing emphasis and retain legible ink. Keep purposeful lighting or selected-state emphasis when justified. |
| [Color changes within readable text](https://impeccable.style/slop/#rule-gradient-text)<br>`gradient-text` | Taste / S | Check readability across the entire gradient, including image or theme backgrounds. | Prefer a solid role color unless the gradient is a considered identity detail. Keep essential metric labels plainly readable. |
| [Readable text appears washed out](https://impeccable.style/slop/#rule-gray-on-color)<br>`gray-on-color` | Quality / S | Inspect text against its actual colored surface, including transparency. | By default, use the primary text color for all readable roles. Use size, weight, and position for hierarchy. |
| [Warm neutral chosen automatically](https://impeccable.style/slop/#rule-cream-palette)<br>`cream-palette` | Taste / S | Check whether the neutral has a role in the actual identity. | Keep intentional cream and beige. Make accent, ink, surface, and state choices explicit instead of substituting another default palette. |

## Layout and spacing (12)

| Check / source ID | Kind / evidence | Inspect | Repair or intentional exception |
| --- | --- | --- | --- |
| [Tiny decorative section numbers](https://impeccable.style/slop/#rule-numbered-section-labels)<br>`numbered-section-labels` | Taste / S | Check whether numbering supports sequence, navigation, or references. | Remove decorative bookkeeping. Keep real steps, indexes, and chapter references at readable sizes. |
| [Carousel edges crowd cards](https://impeccable.style/slop/#rule-edge-flush-cards)<br>`edge-flush-cards` | Quality / B | Inspect the start/end of horizontal scroll areas and focus outlines. | Add intentional inset and scroll padding; keep previewing the next item if it communicates more content without clipping controls. |
| [Overlay covers reading content](https://impeccable.style/slop/#rule-text-occlusion)<br>`text-occlusion` | Quality / B | Test banners, sticky elements, dialogs, and floating actions in affected states. | Reserve space, reposition, or permit dismissal. Check zoom and mobile; closing an overlay must restore usable focus. |
| [Opening columns lose balance](https://impeccable.style/slop/#rule-first-viewport-column-overflow)<br>`first-viewport-column-overflow` | Quality / B | Inspect real text, image dimensions, and viewport height together. | Tune grid proportions or stacking. Keep intentional asymmetry; fix clipping or misplaced actions rather than forcing equal heights. |
| [Title visually joins the wrong section](https://impeccable.style/slop/#rule-heading-rhythm)<br>`heading-rhythm` | Quality / B | Compare the gap above a heading with the gap to its own content. | Group the title with its content and separate sections consistently. Check combined padding, borders, and margins. |
| [Default metric strip in the hero](https://impeccable.style/slop/#rule-hero-metric-layout)<br>`hero-metric-layout` | Taste / R | Check relevance and evidence. | Promote a substantiated result when useful; move unrelated figures elsewhere. |
| [Every section uses matching tiles](https://impeccable.style/slop/#rule-identical-card-grids)<br>`identical-card-grids` | Taste / R | Compare content relationships. | Choose structure by content; retain a grid for comparable items. |
| [All relationships use the same gap](https://impeccable.style/slop/#rule-monotonous-spacing)<br>`monotonous-spacing` | Taste / S | Look for equal separation within groups and between unrelated sections. | Use the spacing scale to express relationships. Regular rhythm is appropriate for a genuine repeated list. |
| [Boxes contain more boxes](https://impeccable.style/slop/#rule-nested-cards)<br>`nested-cards` | Taste / S | Count meaningful object boundaries, rather than simply counting nested divs. | Flatten ornamental wrappers. Keep necessary grouping in interactive editors, real previews, or separately actionable items. |
| [Paragraph measure strains reading](https://impeccable.style/slop/#rule-line-length)<br>`line-length` | Quality / B | Read long lines at the largest supported width and with the actual font. | Choose a deliberate reading measure. Preserve shared section edges; avoid isolated narrow wrappers that create accidental gaps. |
| [Content escapes its intended area](https://impeccable.style/slop/#rule-text-overflow)<br>`text-overflow` | Quality / B | Test long titles, URLs, labels, and translated or user-entered strings. | Allow wrapping, shrink grid children, or provide intentional scrolling. Use truncation only when the full content remains available where needed. |
| [Menus disappear behind clipping](https://impeccable.style/slop/#rule-clipped-overflow-container)<br>`clipped-overflow-container` | Quality / B | Open dropdowns and popovers near container and viewport edges. | Adjust overflow, placement, or layering. Verify focus and dismissal after changes; higher z-index alone cannot escape a clipping ancestor. |

### Additional layout tell: open-ended ruled columns

Added from the author's observation of this treatment on multiple sites. This is a custom review check, separate from the 67 upstream entries.

- **Recognize:** a row of columns separated by thin vertical rules, often connected to a horizontal rule above, with no bottom rule or outer side borders. A nearby variant uses top/bottom horizontal rules while leaving the outside ends open. Inspect fact strips, service rows, and numbered processes for repeated use.
- **Flag:** the repeated open border treatment itself. A sensible sequence can still use this default visual styling. Do not dismiss the observation solely because the grid organizes comparable content.
- **Repair:** avoid this treatment by default. Use a plain fact line, facts beside real imagery, or a process list/timeline. Choose grouping and spacing for the actual text. Adding a full enclosing box is not the automatic correction.
- **Exception:** retain when a specifically approved reference or deliberate project decision requires this exact treatment. Identify it as a user-observed style tell; it is not proof of authorship or a new automated detector rule.

## Motion (6)

| Check / source ID | Kind / evidence | Inspect | Repair or intentional exception |
| --- | --- | --- | --- |
| [Animated dot implies live activity](https://impeccable.style/slop/#rule-pulsing-dot)<br>`pulsing-dot` | Taste / S | Check whether the indicator reflects actual changing information. | Use an honest static state when nothing is live. Real activity needs a clear label and reduced-motion treatment. |
| [Fake typing caret](https://impeccable.style/slop/#rule-blinking-cursor)<br>`blinking-cursor` | Taste / B | Check whether the caret belongs to an editable field or a necessary demonstration. | Remove ambient simulated typing. Keep real input behavior and demonstrations with an accessible, immediately readable alternative. |
| [Content scrolls without user action](https://impeccable.style/slop/#rule-marquee)<br>`marquee` | Taste / S | Check whether visitors can read, inspect, and activate moving items. | Prefer a stable list or user-controlled scroller. If movement is essential, provide pause behavior and a reduced-motion alternative. |
| [Motion overshoots by default](https://impeccable.style/slop/#rule-bounce-easing)<br>`bounce-easing` | Taste / S | Review repeated overshoot during everyday actions. | Choose settling behavior appropriate to the interaction. A deliberate playful spring can stay; test interruptions and reduced motion. |
| [Animation displaces surrounding content](https://impeccable.style/slop/#rule-layout-transition)<br>`layout-transition` | Quality / S / manual | Watch nearby elements during transitions. | Avoid disruptive reflow; preserve necessary expansion and check performance. |
| [Photos shift during hover](https://impeccable.style/slop/#rule-image-hover-transform)<br>`image-hover-transform` | Taste / S / manual | Check reading stability and interaction meaning. | Remove ornamental movement; retain useful preview feedback. |

## Copy (5)

| Check / source ID | Kind / evidence | Inspect | Repair or intentional exception |
| --- | --- | --- | --- |
| [One component repeats its message](https://impeccable.style/slop/#rule-repeated-container-text)<br>`repeated-container-text` | Quality / S | Read title, helper, placeholder, and error copy as a whole. | Give each text role distinct information. Keep repetition required for accessible names or understanding independent controls. |
| [Repeated punctuation rhythm](https://impeccable.style/slop/#rule-em-dash-overuse)<br>`em-dash-overuse` | Taste / S | Check whether many sentences rely on the same interruption pattern. | Rewrite for varied, direct sentences. Preserve a useful dash; do not blindly replace punctuation or numeric range markers. |
| [Claims lack a concrete referent](https://impeccable.style/slop/#rule-marketing-buzzword)<br>`marketing-buzzword` | Taste / S | Ask what action, audience, mechanism, or evidence the phrase names. | State the actual work and substantiated result. Keep established technical terms when they explain something the reader needs. |
| [Manufactured rhetorical opposition](https://impeccable.style/slop/#rule-aphoristic-cadence)<br>`aphoristic-cadence` | Taste / S | Check whether the comparison answers a real reader concern. | State the claim directly and explain its mechanism. Use comparisons only when the distinction materially helps the reader decide. |
| [Dismissive shorthand substitutes for evidence](https://impeccable.style/slop/#rule-theater-slop-phrase)<br>`theater-slop-phrase` | Taste / S | Check whether a claim about performative work describes observable behavior. | Name the behavior and consequence. Retain a literal performance reference or supported quotation when relevant. |

## Imagery (4)

| Check / source ID | Kind / evidence | Inspect | Repair or intentional exception |
| --- | --- | --- | --- |
| [Primitive shapes stand in for finished art](https://impeccable.style/slop/#rule-shape-assembled-illustration)<br>`shape-assembled-illustration` | Taste / S | Inspect whether a scene explains the subject or merely fills the hero. | Use real subject imagery or intentionally crafted artwork. Simple shapes remain appropriate for icons, diagrams, and data graphics. |
| [Mask poorly approximates a natural edge](https://impeccable.style/slop/#rule-organic-clip-path)<br>`organic-clip-path` | Quality / S | Inspect cutouts at actual display size and multiple resolutions. | Use a prepared alpha matte or crafted asset for photographic contours. Keep deliberate geometric CSS crops. |
| [Produced image is barely visible](https://impeccable.style/slop/#rule-buried-raster)<br>`buried-raster` | Quality / S | Inspect the image after gradients, blending, and opacity are applied. | Let meaningful material remain visible or remove an unused asset. Retain overlays necessary for text contrast without concealing the subject. |
| [Image fails or remains a dummy asset](https://impeccable.style/slop/#rule-broken-image)<br>`broken-image` | Quality / S | Check requests, actual pixels, loading behavior, and mobile crops. | Use the intended real asset, dimensions, and appropriate alt text. Provide a useful failure state; decorative imagery can have empty alt. |

## General execution (10)

| Check / source ID | Kind / evidence | Inspect | Repair or intentional exception |
| --- | --- | --- | --- |
| [Runtime errors interrupt the page](https://impeccable.style/slop/#rule-script-error)<br>`script-error` | Quality / B | Observe errors on load and during primary actions; identify ownership and impact. | Fix reproducible application failures, then retest the affected task. Distinguish unrelated extension errors from page defects. |
| [Content waits indefinitely for animation](https://impeccable.style/slop/#rule-content-hidden-at-rest)<br>`content-hidden-at-rest` | Quality / B | Inspect initial state, failed scripts, keyboard traversal, and reduced motion. | Make essential content available by default. Intentionally collapsed controls can stay collapsed if their trigger works and state is conveyed. |
| [Text crowds component boundaries](https://impeccable.style/slop/#rule-cramped-padding)<br>`cramped-padding` | Quality / B | Inspect long labels, wrapped paragraphs, and focus rings inside components. | Use appropriate spacing tokens and target dimensions. Preserve useful density without pressing text against borders. |
| [Paragraphs touch the viewport](https://impeccable.style/slop/#rule-body-text-viewport-edge)<br>`body-text-viewport-edge` | Quality / B | Check gutters at narrow widths, zoom, and alternate orientation. | Apply shared responsive gutters to reading content. An edge-to-edge image does not justify edge-to-edge body text. |
| [Paragraphs produce uneven word gaps](https://impeccable.style/slop/#rule-justified-text)<br>`justified-text` | Quality / S | Inspect narrow columns and the real language’s hyphenation. | Default web prose to start alignment. Retain carefully set publication typography when spacing is verified at each layout. |
| [Text merges with its background](https://impeccable.style/slop/#rule-low-contrast)<br>`low-contrast` | Quality / S | Check actual foreground/background pairs, states, images, and opacity. | Meet the applicable contrast target; WCAG AA uses 4.5:1 for ordinary text and 3:1 for qualifying large text. Rendered verification is still needed. |
| [Heading hierarchy does not match structure](https://impeccable.style/slop/#rule-skipped-heading)<br>`skipped-heading` | Quality / S | Read the semantic outline independently of visual font sizes. | Assign levels by nesting and style them separately. Distinguish a real skipped subsection from a standalone reusable fragment. |
| [Reading lines crowd each other](https://impeccable.style/slop/#rule-tight-leading)<br>`tight-leading` | Quality / S | Inspect multi-line text in the chosen font and measure. | Start reading prose near 1.5 line height and tune it. Short display titles can use tighter leading if their wraps remain clear. |
| [Body or notes require magnification](https://impeccable.style/slop/#rule-tiny-text)<br>`tiny-text` | Quality / S | Read paragraphs, caveats, and legal information at normal zoom. | Start body text around 16px and evaluate the actual face. Keep notes readable at full contrast; no universal pixel value proves usability. |
| [Body letters are spread apart](https://impeccable.style/slop/#rule-wide-tracking)<br>`wide-tracking` | Quality / S | Read paragraphs and watch how spacing changes word recognition. | Keep prose near natural font spacing. Retain considered short-label tracking. |

## Demonstrations and review methods

### Three era demonstrations

The [era comparison](https://impeccable.style/slop/#see-it) includes 2022, 2025, and 2026 examples. Use them to compare clusters of repeated choices, including glowing gradients, editorial neutrals, and neobrutalist composition. They are exaggerated teaching examples, not evidence of model attribution or universal style bans.

### Eleven linked scenarios

These links preserve the page’s complete gallery. The review questions below are our application of the checklist.

| Example | What to review in our work |
| --- | --- |
| [Gradient repetition](https://impeccable.style/antipattern-examples/purple-gradients.html) | Decide which element deserves emphasis and remove competing decorative color effects. |
| [Effects as identity](https://impeccable.style/antipattern-examples/lazy-cool.html) | Identify a purpose for each material, glow, and layer; keep foreground content readable. |
| [Animation overload](https://impeccable.style/antipattern-examples/lazy-impact.html) | Rank actions by importance; review repeated motion, interruption, and reduced-motion states together. |
| [Card stripes](https://impeccable.style/antipattern-examples/thick-border-cards.html) | Check whether an accent conveys a real state rather than implying a warning everywhere. |
| [Excessive containment](https://impeccable.style/antipattern-examples/cardocalypse.html) | Remove wrappers that do not represent a separate object or action. |
| [Repeated composition](https://impeccable.style/antipattern-examples/layout-templates.html) | Let the visitor’s questions and actual proof determine each section’s structure. |
| [Default typography](https://impeccable.style/antipattern-examples/inter-everywhere.html) | Document why the font and role system fit; preserve suitable established type. |
| [Icons dominate content](https://impeccable.style/antipattern-examples/massive-icons.html) | Compare visual prominence with usefulness; protect meaningful action icons. |
| [Unreadable color pairs](https://impeccable.style/antipattern-examples/bad-contrast.html) | Evaluate real backgrounds, small labels, and interaction states. |
| [Repeated component copy](https://impeccable.style/antipattern-examples/redundant-ux-writing.html) | Give the label, hint, and error separate jobs; preserve necessary accessible names. |
| [Oversized dialog task](https://impeccable.style/antipattern-examples/modal-abuse.html) | Consider a dedicated page when a task needs extensive navigation or multiple regions. Keep dialogs for contained tasks; inspect focus, dismissal, scrolling, and mobile fit. |

### Practical review paths

The catalog offers [source/URL detection](https://impeccable.style/docs/detect/), [critique](https://impeccable.style/docs/critique/), and a [Chrome extension](https://impeccable.style/slop/#run-it). Use a method appropriate to the evidence needed.

- Source detection can locate candidates without claiming to have seen them on screen. Verify supported rules against the actual installed version.
- Browser inspection is needed for geometry, occlusion, open menus, working behavior, and rendered typography. Use authorized preview access and label unavailable states as unverified.
- Design judgment decides whether the composition fits the brief. An automated warning does not override an approved identity.
- If a detector must be ignored for an intentional choice, scope the exception to that choice and document the reason. Do not suppress an entire category to obtain a clean report.

Adding this checklist does not enable hooks, install a browser extension, run a live-site scan, or change website styles. Use the checklist during requested design work, then update DESIGN.md with the specific decisions that actually govern that project.

## Attribution and maintenance

Rule topics and stable identifiers adapted from Paul Bakaus’s Impeccable project under Apache License 2.0. Original repair language and the author's default preferences added October 9, 2026. A copy of the license is supplied as `LICENSE-impeccable-Apache-2.0.txt` alongside the skill reference. The upstream notice concerns platform-design reference files, which are not included in this checklist.

When refreshing the reference, recount actual catalog cards, compare rule IDs with the current official pack, and update the evidence classifications. Preserve justified project exceptions. Treat newly added styles as questions to evaluate rather than permanent prohibitions.
