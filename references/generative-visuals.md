# Generative visual strategy

## Principle

Capability awareness must change the work. When image or video generation is available, inspect the deck for a communication job that supplied media, native shapes, charts, or typography cannot perform as effectively. Use the declared material language, edge language, image system, and slide family to make this decision; then record it in `visual-generation-plan.json`.

Do not generate imagery merely to prove the capability exists. Do not ignore the capability when a custom visual would materially raise distinctiveness, explanation, emotional entry, or audience recall.

## Required opportunity audit

For every new or redesigned deck, resolve one of four decisions:

- `use`: generate one or more visual candidates for a named slide job;
- `skip`: supplied or native visuals already perform every important job; record why generation would add no value or introduce risk;
- `unavailable`: no usable generation capability exists;
- `delegated`: a separate model/tool will generate through a handoff packet.

Do not leave `pending` before authoring starts. When generation is usable and the user asks for a polished, distinctive, visual, launch-quality, portfolio-quality, or reference-matched deck, default to `use` unless a concrete risk or supplied-asset advantage justifies `skip`.

## Good generation jobs

Generate for:

- an original cover or section hero that embodies the central idea;
- a conceptual scene that cannot be photographed or sourced responsibly;
- a product or packaging concept clearly labeled as illustrative;
- an explanatory illustration where exact text/data remain native;
- a visual metaphor that materially improves recall;
- a controlled texture, environment, or object used as art direction;
- a fictional scenario image when its non-factual status is clear and it does not impersonate evidence.

Prefer native or sourced media for:

- logos and brand marks;
- actual people, customers, facilities, products, or events;
- UI screenshots and product states;
- charts, exact data, tables, diagrams, legal/medical/scientific evidence;
- quotations, core copy, and anything requiring exact typography;
- visual proof that must be auditable.

## Distinctness and reuse

Every generated visual needs a unique job and placement contract.

- Use one final generated image on one slide by default.
- Do not reuse the same hero as a cover, section background, and closing wallpaper.
- Generate a new asset when another slide needs a materially different subject, crop, or narrative job.
- A recurring abstract texture may be reused only as low-contrast background furniture, not as repeated primary proof.
- Keep generated imagery visually distinct from supplied screenshots, charts, and work samples while preserving the deck's palette, material language, and crop system.
- Do not create several near-identical images that make the deck feel like a generated-image carousel.

## Generation budget

Start small:

| Deck type | Candidate budget | Typical final use |
|---|---:|---:|
| Executive proposal/report | 1–3 images | 1 hero or conceptual proof visual |
| Portfolio/case study | 1–3 images | 0–2 supporting visuals; never replace real work |
| Keynote/product launch | 2–5 images | 1–3 hero/scene assets |
| Teaching/research | 1–3 images | 0–2 explanatory illustrations |
| Async report | 1–2 images | 0–1 section/context visual |

Generate candidates only for plausible placements. Review before requesting additional variants. More assets do not imply better slides.

## Prompt from the layout

Lock the slide's topology, slide family, crop, and text-safe zone before prompting. Include:

- intended slide and communication job;
- use case: natural photo, product mockup, stylized concept, explanatory illustration, and so on;
- subject and scene;
- visual character and material language;
- intended edge relationship and how the asset meets native text/shapes;
- wide/portrait/square aspect and focal placement;
- text-safe negative space required by the layout;
- palette relationship to the design system;
- exact invariants and forbidden content;
- no rendered text, logo, watermark, chart, or UI unless the operation explicitly requires and can validate it;
- desired difference from other deck visuals.

The prompt must identify whether the asset is illustrative atmosphere, concept, texture, or could be mistaken for factual proof. Never use generation to repair a missing factual work sample when the deck claims to show actual work.

Example handoff packet:

```json
{
  "id": "IMG-P01-01",
  "slide_ids": ["P01"],
  "purpose": "Create a distinctive cover entry for a controlled-flow proposal",
  "use_case": "stylized-concept",
  "asset_type": "full-bleed cover hero",
  "narrative_job": "turn fragmented handoffs into one controlled path",
  "composition": "16:9; calm left text-safe field; focal sculpture on right",
  "difference_from_other_visuals": "conceptual hero; all later proof uses native diagrams or supplied UI",
  "prompt": "Provider-ready generation instruction",
  "constraints": ["no text", "no logo", "no dashboard", "brand-safe palette"],
  "avoid": ["stock-office scene", "sci-fi neon", "flowchart boxes"],
  "expected_output": "assets/generated/P01-orchestration-hero.png",
  "review": {
    "required": true,
    "reviewer": "vision-capable current agent",
    "checks": ["prompt adherence", "safe crop", "artifact scan", "distinctness", "brand fit"]
  },
  "fallback": "typographic hero with native process motif",
  "provenance": {
    "provider": "declared tool",
    "model": null,
    "created_at": null,
    "prompt_saved": true
  },
  "status": "planned"
}
```

## Integrated and delegated capability routes

### Generation plus vision in one model/tool environment

Generate, inspect the result, repair once with a targeted change, save the final asset into the project, and add it to `asset-manifest.json` as `generated-illustration`, `generated-concept`, or another explicit role.

### Generation available but vision unavailable

Generate only as a draft. Mark `needs-visual-review`, require a user or delegated vision reviewer, and keep a non-generated fallback. Do not place the asset in a final deck until review passes.

### Generation delegated to a separate model

Send a self-contained file-based handoff packet. Preserve operation ID, prompt, inputs, output path, provider, and acceptance checks. The main agent owns placement and final QA.

### No generation capability

Use supplied assets, licensed search where allowed, native data graphics, diagrams, typography, or a deliberate image-free direction. Do not leave empty image slots.

## Review gates

Inspect each generated image for:

- intended subject and narrative job;
- composition, crop, and text-safe zone;
- anatomy, geometry, reflections, repeated objects, and other artifacts;
- unintended text, marks, logos, UI, or watermarks;
- resemblance to protected brands or copyrighted characters;
- factual implication: whether the image could be mistaken for actual evidence;
- brand and palette fit;
- distinctness from other deck visuals;
- resolution and target-runtime rendering;
- accessibility and alt text.

Save the prompt and provenance. Generated visuals are sources with a different evidence class; they do not validate a factual claim.

## Video generation

Use video generation only when motion itself explains a change, mechanism, sequence, or atmosphere that a static visual cannot. Require a poster, caption, static fallback, playback/package test, and honest disclosure. Do not generate video simply because a video model is available.
