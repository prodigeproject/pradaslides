---
name: pradaslides
description: Create, redesign, critique, or plan audience-ready presentations and PowerPoint decks from a short prompt or source material. Use for portfolios, work/result reviews, proposals, sales decks, investor pitches, strategy or decision decks, research and technical talks, lessons, keynotes, reports, product launches, and reusable presentation templates. Infers user intent, audience, desired change, narrative, evidence needs, visual direction, delivery mode, and the best available slide runtime; produces editable PPTX, web slides, PDF, or a production-ready deck plan with rigorous content, visual, accessibility, and render QA.
---

# PradaSlides

Turn a minimal request into a presentation with a clear communication job, credible content, deliberate audience journey, coherent visual system, and verified delivery artifact. Match the user's language unless they request another.

## Operating stance

- Treat slides as an audience experience, not a decorated document.
- Optimize for the user's intended change: a decision, belief, action, understanding, trust, or remembered impression.
- Infer sensible defaults from the material. Ask a question only when the answer would materially change the argument, artifact type, confidentiality, or irreversible work.
- Keep facts, strategy, design intent, build source, previews, and deliverables in separate owned artifacts.
- Use the best slide-production capability already available in the host agent. Do not require a Codex-specific tool.
- Preserve user files. Work in a new project directory unless the user explicitly requests an in-place edit.

## Start here

1. Classify the task: `new`, `redesign`, `fill-template`, `enhance-existing`, `critique`, or `plan-only`.
2. Read [intent-playbooks.md](references/intent-playbooks.md) and select one primary intent plus, when useful, one secondary intent.
3. Create the project contracts from [artifact-contracts.md](references/artifact-contracts.md). For a fresh workspace, run:

   ```bash
   python scripts/bootstrap_project.py --output <project-dir> --intent <intent>
   ```

4. Scan the runtime when the host's slide capabilities are not already obvious:

   ```bash
   python scripts/capability_scan.py --json
   ```

5. Read [capability-orchestration.md](references/capability-orchestration.md), declare model/tool/runtime capabilities in `capability-profile.json`, and resolve a conservative execution route:

   ```bash
   python scripts/resolve_capabilities.py --profile <project-dir>/capability-profile.json --brief <project-dir>/brief.json --scan-local --output <project-dir>/execution-plan.json
   ```

6. Follow the workflow below. Do not start visual slide construction before the brief, source ledger, capability route, design system, topology route, generation decision, and deck plan are coherent.

## Workflow

### 1. Establish the communication contract

Write this sentence before outlining:

> By the end, **[audience]** should **[think/feel/do]** because **[central takeaway]**.

Resolve or infer:

- audience, context, stakes, prior belief, objections, and decision authority;
- presentation intent and delivery mode: live, leave-behind, asynchronous, or hybrid;
- desired `from → to` shift and final audience action;
- available time, slide-count constraint, aspect ratio, language, brand, and output format;
- required evidence, source boundaries, confidentiality, and editability.

Record the result in `brief.json`. Validate it:

```bash
python scripts/validate_brief.py <project-dir>/brief.json
```

Use `assumptions` for inferred values. Never disguise an assumption as a user instruction.

### 2. Route the artifact and runtime

Use the resolved execution plan. Never assume that a multimodal model also has slide authoring or rendering, and never assume a text-only model can semantically inspect media. Treat separately connected vision, image-generation, or video-generation models as delegated capabilities with explicit handoff packets, provenance, acceptance checks, and fallbacks.

Choose one artifact route:

| Request shape | Route |
|---|---|
| New deck from a goal, topic, or sources | `new` |
| Improve an existing deck with freedom to re-outline | `redesign` |
| Keep native slide shells and replace content | `fill-template` |
| Keep visible slides stable; add notes, transitions, or delivery support | `enhance-existing` |
| Diagnose and recommend without changing files | `critique` |
| Produce strategy, outline, copy, and visual specification only | `plan-only` |

Then choose a production runtime using [runtime-and-delivery.md](references/runtime-and-delivery.md). Prefer:

1. the host's native presentation tool when it can create and render the required artifact;
2. native editable PPTX generation for ordinary business delivery;
3. fixed-stage HTML or Slidev for interactive, code-heavy, or web-native talks;
4. PDF only when editability is unnecessary;
5. raster-first PPTX only when the user explicitly accepts limited editability and accessibility.

If an existing deck must preserve wording, order, or appearance, treat those as invariants and record them in `brief.json`.

### 3. Inspect sources and build the evidence ledger

- Inventory every supplied file before outlining.
- Extract text, tables, charts, images, notes, metadata, and page/slide structure with the appropriate host tools.
- For PDFs or visually meaningful source files, inspect both extracted content and rendered pages.
- For attached photos, videos, logos, screenshots, charts, or illustrations, read [media-intelligence.md](references/media-intelligence.md), generate `asset-manifest.json`, and visually inspect every asset or representative video keyframe before locking the outline.
- If image/video understanding is unavailable, keep semantic review pending and use a human or delegated reviewer. Metadata alone cannot authorize placement. If generation exists without vision, generated media requires external visual approval before final use.
- Record every claim, metric, quotation, and visual asset in `source-ledger.json` with source location and status.
- Mark invented demo values as `scenario`; display that label on-slide when the distinction matters.
- Research only factual gaps that matter to the communication job. Prefer primary and authoritative sources.
- Never fabricate citations, metrics, customer claims, testimonials, market sizes, or implementation results.

Validate the ledger before it becomes slide evidence:

```bash
python scripts/validate_source_ledger.py <project-dir>/source-ledger.json
```

Create a technical asset inventory and review contact sheet when media is present:

```bash
python scripts/analyze_assets.py <project-dir>/assets --output <project-dir>/asset-manifest.json --contact-sheet <project-dir>/previews/asset-contact-sheet.png --keyframes-dir <project-dir>/previews/video-keyframes
```

Enrich the generated manifest with semantic roles, subject, message, focal point, text-safe regions, crop tolerance, rights, sensitivity, and intended slide use. Technical metadata cannot determine meaning by itself.

```bash
python scripts/validate_asset_manifest.py <project-dir>/asset-manifest.json --require-reviewed
```

Read [content-and-narrative.md](references/content-and-narrative.md) before planning evidence-heavy decks.

### 4. Design the audience journey

Construct the journey around the audience's mental state, not the source document's chapter order. Use only the phases the intent needs:

`attention → orientation → tension → insight → proof → resolution → decision → retention`

For each phase, specify:

- what the audience currently believes or needs;
- the question the next slide answers;
- the emotional or cognitive load;
- the proof required to advance;
- the transition to the next phase.

Avoid artificial drama. A scientific briefing may emphasize orientation and proof; a portfolio may emphasize identity, selected work, process, outcomes, and fit.

### 5. Establish the visual system and topology registry

Read [design-and-visuals.md](references/design-and-visuals.md) and [topology-and-layouts.md](references/topology-and-layouts.md). Edit `design-system.json` and use `layout-manifest.json` as the default portable topology registry.

Define:

- one intent-fit visual direction and a relevant supplied-reference quality floor;
- canvas, grid, margins, type scale, palette roles, image treatment, and slide furniture;
- deck-level rhythm: topology variety, focal-mass changes, tone shifts, repetition anchors, and density;
- reusable topology/layout entries with roles, relationships, slots, media capacity, tone support, guardrails, and target-runtime fidelity.

Validate both contracts:

```bash
python scripts/validate_design_system.py <project-dir>/design-system.json
python scripts/validate_layout_manifest.py <project-dir>/layout-manifest.json
```

Select layout by the relationship the audience must perceive, not by decoration or template name. Use `role → relationship → topology → layout → safe slots → style`. Require a `layout_rationale` for any `custom-*` layout.

### 6. Build the deck plan and visual-generation plan

Create `deck-plan.json`. Each content slide must have:

- one `job` and one `claim`;
- a takeaway title that communicates the claim;
- evidence and its source IDs;
- a visual role and chosen visual form;
- audience journey phase and transition;
- speaker-note purpose;
- layout family, registered `layout_id`, topology, tone, focal emphasis, and density/slot budget.
- stable `asset_ids` and a resolved `media_plan` when media is used; in strict visual mode, multi-asset slides require one complete `asset_treatments` entry per asset so logos, heroes, screenshots, and video do not inherit the same crop or fallback.

Exceptions: cover, section divider, deliberate pause, and closing identity slides may use non-claim titles.

Apply these tests:

- **So what?** The claim matters to this audience.
- **Why true?** Evidence supports the claim.
- **Why now/next?** The sequence creates momentum.
- **Why this visual?** The visual performs a communication task.
- **What should remain?** The audience can repeat the central takeaway after the deck.

Lint before building:

```bash
python scripts/lint_deck_plan.py <project-dir>/deck-plan.json --brief <project-dir>/brief.json --source-ledger <project-dir>/source-ledger.json --asset-manifest <project-dir>/asset-manifest.json --design-system <project-dir>/design-system.json --layout-manifest <project-dir>/layout-manifest.json --strict-visual
```

If image or video generation is usable, read [generative-visuals.md](references/generative-visuals.md) and resolve `visual-generation-plan.json`. Capability awareness must activate an opportunity audit; do not leave generation as an unused checkbox.

```bash
python scripts/validate_visual_generation_plan.py <project-dir>/visual-generation-plan.json --require-resolved
```

When generation is available and the user asks for a polished, distinctive, visual, launch-quality, portfolio-quality, or reference-matched deck, default to at least one original candidate unless supplied media already performs every important hero/concept job or generation creates factual/brand risk. Record a concrete reason for `skip`.

If the user provides references, infer transferable principles rather than cloning the composition. If direction is genuinely ambiguous and the choice is consequential, present up to three distinct visual routes with short rationale; otherwise select one and proceed.

Hard visual rules:

- Group before styling; use proximity, alignment, repetition, and contrast to expose structure.
- Use whitespace as organization, not as unused decoration.
- Use one dominant visual idea per slide.
- Meet the reference-quality floor: recognizable identity, decisive scale contrast, inspectable proof, meaningful topology variation, and coherent tone rhythm.
- Treat a visual cluster as a prior, never a typography answer. Resolve the specific product's positioning, audience, personality, proof density, interaction model, language, and brand assets before choosing families, scale, weight, tracking, case, and type color. Two products in the same category should not inherit the same type system without a written rationale.
- Treat an image slot as a media opportunity, never a fixed template. Resolve each asset's narrative job, focal subject, crop tolerance, text-safe region, scale, and relationship to copy before selecting full bleed, split crop, editorial window, contact sheet, diptych, detail crop, device stage, panorama, mask, or gallery choreography. Repeat a composition only when repetition is an intentional deck anchor.
- Keep authoring and audit language off the audience-facing canvas. Reference IDs, transfer principles, avoid rules, asset credits, crop labels, topology names, benchmark scores, and QA markers belong in notes or metadata unless the audience genuinely needs them.
- Treat photographs, diagrams, tables, and charts as evidence carriers.
- Avoid generic business imagery, ornamental dashboards, arbitrary blobs, and repetitive card grids.
- Do not let CSS gradients, empty device shells, avatar silhouettes, or abstract SVG objects impersonate photography, product evidence, or a finished hero. When a supplied reference derives its quality from real media, use relevant supplied or rights-compatible sourced media, or record a blocking media gap.
- Do not ask an image model to render core slide copy, charts, or exact labels.
- Maintain projection-safe type. Default minimums: title `35 pt`, subhead `24 pt`, body `16 pt`; use larger text for live speaking decks.
- Keep slide-edge safety margins and account for renderer differences.

### 7. Produce content and visuals together

- Write audience-facing copy, not production notes.
- Prefer concise claim titles and concrete language.
- Separate slide copy from speaker notes and leave-behind detail.
- Match density to delivery mode: `speaking`, `hybrid`, or `reading`.
- Use native text, charts, tables, and shapes when editability matters.
- Use generated or searched imagery only when it adds specific explanatory or emotional value.
- Honor an explicit preference for sourced photography over generation. Search rights-compatible libraries, select by subject and crop fitness, download the chosen asset locally, record its source page and license, and never depend on a remote hotlink during delivery.
- For usable generation capability, create only assets approved in `visual-generation-plan.json`, inspect every result, preserve prompt/provenance, and add the selected output to `asset-manifest.json`.
- Give each generated visual a unique slide job. Use one hero once by default; generate a different asset for a different subject, crop, or narrative job.
- Keep actual logos, people, product UI, data, charts, tables, diagrams, and exact labels sourced or native. Generated art is not factual proof.
- Reference attached media by stable `asset_ids`; specify placement intent, crop mode, focal anchor, alt text, and fallback behavior in the deck plan.
- Preserve per-asset invariants: logos and assets with `crop_tolerance: none` use only `contain` or `none`; use native zoom/callout treatments instead of destructive cropping.
- Use a table for exact lookup, a graph for patterns, and a diagram for relationships or process.
- Select charts by the question being answered, not by visual novelty.
- Give sources near the claim or in notes according to the delivery contract.

### 8. Build through an owned intermediate representation

Keep `brief.json`, `source-ledger.json`, `deck-plan.json`, and the actual authoring source as the source of truth. Never use rendered PNGs as the editable source.

When generating PPTX:

- create native editable elements where practical;
- preserve theme, master, or placeholder constraints when required;
- include speaker notes when the runtime supports them;
- avoid hidden dependencies on remote services;
- make output deterministic enough to repair individual slides.

When generating web slides:

- use a fixed stage, not responsive page flow, for slide composition;
- read [html-presenter-console.md](references/html-presenter-console.md) and scaffold the dependency-free console when a presentation-product experience is useful;
- provide thumbnails, keyboard navigation, chrome-free presentation mode, speaker notes, safe display controls, and honest export actions;
- center the transformed fixed stage explicitly with absolute `50%/50%` positioning plus `translate(-50%, -50%) scale(...)`; do not rely on grid centering for an oversized unscaled canvas;
- keep console chrome outside the slide canvas and outside PDF/PPTX exports;
- bind authored media to the plan: use `data-asset-id` on rendered assets, `data-poster-asset-id` for a separately planned video poster, and `background.assetId` for runtime-created background media;
- test export separately from browser display.

```bash
python scripts/scaffold_presenter.py --output <project-dir>/presenter --deck-plan <project-dir>/deck-plan.json --design-system <project-dir>/design-system.json
```

The scaffold is an authoring start, not a deliverable. Replace each slide's body, clear every `authoring.incomplete` flag, and run visual QA.

When Chromium and Node.js are available, run the portable browser check:

```bash
node scripts/qa_html_presenter.mjs --entry <project-dir>/presenter/index.html --deck-plan <project-dir>/deck-plan.json --count <slide-count> --output <project-dir>/qa/html-presenter.json --render-dir <project-dir>/renders/slides --montage <project-dir>/renders/slide-montage.png --console-shot <project-dir>/renders/console/presenter-console.png
```

It checks fixed-stage geometry, presenter-viewport stage fit, plan-to-DOM asset identity, image/video contracts, placeholders, out-of-bounds elements, clipped content, title lines, body text size, suspicious text encoding, thumbnails, console and interactions, deep links, print geometry, draft status, and inspector-toggle geometry. Exhaustive reference coverage additionally activates topology/layout/tone/density diversity and reference-to-DOM trace gates. It does not replace visual review.

### 9. Render, inspect, repair

Read [qa.md](references/qa.md). Rendering is mandatory for created or edited decks.

1. Run structural validation and resolve all blocking errors.
2. Render every slide/page to an image.
3. Inspect the full montage for rhythm, repetition, pacing, and outliers.
4. Inspect every slide at full size for overlap, clipping, wrapping, contrast, alignment, image crop, chart semantics, citation fit, and empty placeholders.
5. Repair the authoring source, re-export, and re-render affected slides.
6. Repeat until no blocking issue remains. Do not declare success from code inspection alone.

For reference-led HTML tuning, also read [reference-benchmarking.md](references/reference-benchmarking.md). Populate `reference-benchmark.json` with the supplied references, transferable principles, anti-copy constraints, evidence-backed scores, and repair history. PNG renders are QA evidence; keep the HTML entrypoint as the deliverable.

Before changing an existing benchmark candidate, read [iteration-versioning.md](references/iteration-versioning.md) and freeze the current candidate. Never overwrite the only inspectable evidence for an earlier tuning round. Label retrospective or different-input artifacts honestly; only same-prompt, same-content, same-capability runs qualify for direct V-to-V scoring.

Distinguish representative cluster sampling from proof against every supplied reference. If the user explicitly requires the baseline to account for every reference, declare `coverage.mode` as `mapped-all-references` or build a dedicated `one-slide-per-reference` stress fixture. Every reference then needs a unique, inspectable mapping to an original HTML response with an in-range slide ID, individually specific response text, and passing status. Bind `referenceId` or `referenceIds` in the slide data so browser QA can trace the mapping to rendered DOM. Do not report cluster sampling as exhaustive coverage, and do not embed the source reference merely to satisfy the mapping.

```bash
python scripts/validate_reference_benchmark.py <project-dir>/reference-benchmark.json --require-final
```

Do not let structural completeness or an impressive cover conceal weak visible craft. A final HTML benchmark needs every universal criterion at or above its declared floor and no unresolved blocker.

Once the benchmark contract is populated, rerun the complete HTML loop with:

```bash
python scripts/run_html_benchmark.py --project <project-dir> --entry presenter/index.html --count <slide-count>
```

If rendering or image understanding is unavailable, do not counterfeit this loop. Record an external review gate and deliver a draft/plan rather than claiming final visual QA.

For PPTX package inspection:

```bash
python scripts/inspect_pptx.py <deck.pptx> --json <project-dir>/qa/pptx-structure.json
```

Record results in `qa-report.json`. A maximum repair count is a scheduling aid, not permission to ship a broken deck.

### 10. Deliver clearly

Deliver the requested presentation plus the useful supporting artifacts:

- final editable source and/or PPTX;
- PDF or preview montage when useful;
- `qa-report.json`;
- `source-ledger.json` for sourced decks;
- a short note listing assumptions, editability limitations, unresolved evidence gaps, and fonts or external assets required.

Open with the outcome. Do not bury the deliverable path under process narration.

## Reference router

| Need | Read |
|---|---|
| Select intent, arc, density, and closing action | [intent-playbooks.md](references/intent-playbooks.md) |
| Research, evidence, claims, story, titles, notes | [content-and-narrative.md](references/content-and-narrative.md) |
| Grids, typography, color, imagery, charts, diagrams | [design-and-visuals.md](references/design-and-visuals.md) |
| Select product-specific typography, brand voice, scale, roles, and fallbacks | [typography-and-voice.md](references/typography-and-voice.md) |
| Choreograph photos and product media by intent without falling into repeated slots | [media-composition.md](references/media-composition.md) |
| Select topology, layout roles, safe slots, variation, and visual-quality floor | [topology-and-layouts.md](references/topology-and-layouts.md) |
| Analyze and place attached photos, video, logos, screenshots, and illustrations | [media-intelligence.md](references/media-intelligence.md) |
| Activate image/video generation, uniqueness, prompt packets, provenance, and review | [generative-visuals.md](references/generative-visuals.md) |
| Negotiate LLM, vision, generation, delegated-model, authoring, and QA capabilities | [capability-orchestration.md](references/capability-orchestration.md) |
| Build a fixed-stage HTML slide product with thumbnails, controls, notes, Present, and export | [html-presenter-console.md](references/html-presenter-console.md) |
| Benchmark rendered HTML against supplied visual references without cloning | [reference-benchmarking.md](references/reference-benchmarking.md) |
| Freeze tuning iterations and build honest V-to-V comparisons | [iteration-versioning.md](references/iteration-versioning.md) |
| Select runtime, preserve editability, export and package | [runtime-and-delivery.md](references/runtime-and-delivery.md) |
| Define or inspect JSON work products | [artifact-contracts.md](references/artifact-contracts.md) |
| Run content, visual, technical, and accessibility QA | [qa.md](references/qa.md) |

## Non-negotiable acceptance criteria

- The deck's communication job is explicit.
- The primary intent and audience shift are visible in the structure.
- Every substantive slide has one job, one claim, and adequate proof.
- Titles communicate takeaways except for documented slide-role exceptions.
- Facts are sourced or clearly labeled as assumptions/scenarios.
- The visual system is coherent without making every page identical.
- Typography expresses the specific product and audience rather than merely its broad category; family, scale, weight, tracking, case, color, and fallback choices have an explicit rationale.
- Media placement expresses the slide job and product character; crops, masks, scale, sequencing, and image-to-copy relationships do not collapse into a repeated photo slot.
- Audience-facing slides contain no internal reference, audit, source-credit, crop, topology, or generation labels unless explicitly required for the audience.
- Every slide uses an explicit relationship, topology, registered/custom layout, safe slot budget, tone, and focal emphasis.
- The deck meets its intent-relative supplied-reference quality floor and passes thumbnail/squint tests.
- A reference-led HTML project has a final `reference-benchmark.json`; every universal criterion includes render evidence, meets its floor, and has no blocker. When exhaustive reference coverage was requested, every supplied reference also has a validated passing coverage mapping in the declared mode.
- Every modified tuning candidate has an immutable predecessor snapshot, an iteration manifest, and an explicit comparability status.
- Image/video generation availability produced a resolved `use`, `skip`, `unavailable`, or `delegated` decision; every generated asset has a unique job, provenance, and visual review.
- Every used attachment has reviewed semantics, rights, placement, crop, focal anchor, safe region, fallback, and alt text; strict multi-asset slides resolve these per asset.
- Copy fits the delivery mode and remains readable.
- Core content remains editable unless the user accepted another trade-off.
- Every slide was rendered and visually inspected.
- Capability-dependent work was performed only by verified or explicitly delegated capabilities; fallbacks and external review gates are disclosed.
- The final artifact opens, contains no placeholders, and matches the requested format.
