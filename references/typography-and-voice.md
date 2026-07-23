# Product-specific typography and voice

## Contents

1. Decision rule
2. Selection axes
3. Product examples
4. Type-role contract
5. Scale and color
6. Multi-product and reference fixtures
7. Capability and fallback handling
8. QA

## Decision rule

Use the broad visual cluster only as a prior. Do not map `product/UI` directly to one sans-serif stack, `editorial` directly to one serif, or `technology` directly to one geometric grotesk.

Choose typography after resolving the particular product. Typography should help the audience infer positioning and interaction character before reading all the copy.

For every deck, complete `typography.selection` in `design-system.json` before layout authoring.

## Selection axes

Resolve these axes:

| Axis | Question | Typography consequence |
|---|---|---|
| Product archetype | Commerce, developer tool, wellness app, luxury object, portfolio, infrastructure? | Determines expected reading behavior and acceptable expressiveness. |
| Positioning | Mass-market, premium, experimental, institutional, playful? | Changes contrast, refinement, width, weight, and whitespace. |
| Audience | Consumer, engineer, executive, buyer, creator, regulator? | Changes familiarity, density, label style, and accessibility margin. |
| Personality | Calm, energetic, rigorous, rebellious, intimate? | Changes family character, case, rhythm, and punctuation. |
| Proof density | Sparse hero, balanced narrative, dense analytical proof? | Changes headline width, body x-height, numeral clarity, and label compactness. |
| Interaction model | Spoken deck, product demo, async report, workshop? | Changes type size, line length, repetition, and annotation behavior. |
| Language and script | Latin, Indonesian, Arabic, CJK, multilingual? | Requires glyph coverage, diacritics, shaping, and line-break testing. |
| Brand assets | Existing logo, UI font, website, guideline, packaging? | Existing brand truth normally outranks a generic category convention. |

Record a short rationale that connects at least four axes to the selected system.

## Product examples

Products inside one category can require materially different type systems:

| Product/UI example | Suitable direction | Avoid |
|---|---|---|
| Consumer marketplace | Familiar UI sans, strong action weight, compact conversion labels | Developer-tool monospace everywhere |
| Developer-facing UI kit | Engineered grotesk plus monospace tokens and numerals | Friendly rounded consumer-app typography |
| AI fitness product | Humanist or subtly rounded display, open body text, energetic metric numerals | Cold enterprise SaaS neutrality |
| Personal portfolio platform | Authored serif/sans contrast, warmer pacing, expressive project titles | Generic product-dashboard typography |
| Premium fintech | Controlled grotesk, tabular numerals, high-tracking risk labels | Neon sci-fi display type as credibility substitute |
| Children’s learning app | Rounded, highly legible forms, generous line height, friendly color | Condensed uppercase identity type |

Do not reuse the same type stack merely because two decks share a product category.

## Type-role contract

Define roles before selecting exact sizes:

- `display`: central claims and chapter statements;
- `body`: explanations, evidence context, and readable narrative;
- `label`: kickers, sources, UI states, axes, and annotations;
- `numeral`: metrics, dates, prices, and ordered steps;
- `quote` when voice or testimony needs a distinct cadence.

Use no more than two primary families plus an optional mono/label family in a normal single-product deck. Variation should come from role, size, width, weight, style, tracking, case, and color before adding more families.

Keep one dominant product voice across the deck. Create chapter variants only when the narrative state changes, such as strategy versus proof, dark product demo versus light evidence, or person versus project.

## Scale and color

Choose size from delivery mode and copy shape, then tune it for product character:

- a premium object may use fewer, larger, lighter serif words;
- a developer tool may use a moderately sized engineered headline plus compact monospace labels;
- a creator portfolio may use compressed uppercase display type with extreme scale jumps;
- a wellness product may use an open humanist headline and generous body leading.

Do not solve overflow by shrinking below the delivery floor. Rewrite or change composition.

For a 1600×900 speaking or hybrid deck, use roughly 20–26px for normal body copy and reserve 14–18px for furniture, captions, source lines, and other genuinely secondary information. These are working ranges, not a substitute for rendering. When a slide has generous unused space, first increase the central claim, supporting explanation, proof scale, or the spacing relationship; do not fill the void with a smaller type block plus decoration.

Type color is part of the voice:

- use warm ink for editorial/luxury;
- use navy or near-black for institutional clarity;
- use vivid accent only for action, state, or identity;
- use muted type only for genuinely secondary metadata;
- preserve contrast independently of mood.

## Multi-product and reference fixtures

For one real product deck, use one primary type profile.

For a multi-product comparison, choose either:

- one neutral comparison system when analytical comparability is primary; or
- separate brand-faithful profiles when product identity is part of the evidence.

State the choice.

For a one-slide-per-reference stress fixture, each page may use a different profile because each page represents a separate hypothetical product. Bind a stable `typographyProfile` or `type-profile-*` class so the variation is inspectable and testable.

## Capability and fallback handling

Inspect supplied brand fonts when legally and technically usable. Never assume a named font exists.

For downloaded fonts:

- verify license and redistribution rights;
- store the file locally;
- declare correct weight/style metadata;
- test glyph coverage;
- retain source and license provenance.

When fonts cannot be bundled, use an explicit system stack and record the portability limitation. Never hotlink a remote font in the final presentation.

If the renderer substitutes fonts, rerun fit and line-break QA. A fallback is not valid merely because it loads.

## QA

Check:

- headline silhouette and line count;
- body line length and x-height;
- numeral distinction and tabular behavior where needed;
- label readability at projection distance;
- diacritics and multilingual glyphs;
- contrast in every tone;
- font availability and fallback rendering;
- coherence across chapters;
- visible differentiation from another product with different positioning;
- absence of arbitrary per-slide font switching.

Reject a type system when the rationale only says “modern,” “clean,” “professional,” or names the broad visual cluster.
