# Media Composition

Use this reference after asset semantics are reviewed and before choosing a slide layout. The objective is not to “place an image.” The objective is to make the media perform a narrative job while preserving the subject, evidence, and brand character.

## 1. Begin with the product and slide job

Resolve:

- presentation intent and delivery mode;
- product, person, or organization being represented;
- audience and desired response;
- slide claim and proof need;
- whether the image is identity, context, process, product proof, detail proof, atmosphere, comparison, sequence, or transition;
- whether the audience must inspect the full object, a human expression, construction detail, UI state, spatial relationship, or change over time.

A broad category is not enough. Two fashion portfolios can need different media systems: a pattern maker may foreground hands, paper patterns, fit, seams, and construction sequence; a campaign photographer may foreground full-bleed mood, edit rhythm, and selected frames.

## 2. Build an asset-role map

For every used asset, record:

| Field | Meaning |
|---|---|
| `asset_id` | Stable identity across plan, source, and output |
| `narrative_job` | Identity, context, process, proof, detail, outcome, transition |
| `subject` | What the audience should look at |
| `focal_anchor` | Face, hands, object, screen, seam, chart point, or spatial center |
| `text_safe_region` | Area that can safely carry copy, if any |
| `crop_tolerance` | None, low, medium, high |
| `required_context` | What must remain visible for the image to make sense |
| `sequence_role` | Establishing, step, detail, reveal, outcome |
| `rights_and_credit` | Provenance stored outside the slide face unless audience-required |
| `fallback` | Contain, alternate crop, alternate asset, or media-gap state |

Do not infer semantic placement from dimensions or file names alone.

## 3. Choose a composition family

Select the smallest family that makes the relationship clear.

### Full bleed

Use for identity, atmosphere, human presence, or a decisive product reveal. Maintain a controlled text-safe zone or place copy on an opaque surface. Do not use full bleed for an image whose evidence depends on seeing its complete boundary.

### Editorial window

Use a tall or wide crop surrounded by meaningful whitespace. Best for luxury objects, fashion portraits, material studies, and quiet personal portfolios. The whitespace should frame the subject and support type scale, not feel like an empty template.

### Split image and claim

Use when image and explanation carry comparable weight. Vary the split ratio based on the focal subject and copy density; do not default to 50/50.

### Diptych or before/after

Use when two views produce meaning together: draft versus fitted garment, front versus detail, interface versus outcome, person versus work. Make one panel dominant when the views are not equally important.

### Contact sheet to selection

Use for portfolio editing, collection breadth, or process evidence. Establish several frames, then give one selected frame dominant scale. Avoid a uniform gallery that makes every image equally important.

### Detail crop

Use when craft or construction is the claim: seam, bead, lace, texture, cut line, annotation, screen state, or mechanism. Pair with an establishing view if the detail loses context by itself.

### Panoramic band

Use for timeline, environment, process horizon, or a sequence that benefits from lateral reading. Keep titles and proof outside the band when overlay contrast would be unstable.

### Device or artifact stage

Use when a screen, pattern, document, garment, packaging, or physical object must be inspected. Present it as evidence with enough scale and boundary; do not use an empty device shell or fake UI as a substitute for the artifact.

### Organic or geometric mask

Use when the mask reinforces the brand or subject: a curve for soft tailoring, an angled crop for technical precision, an arch for architecture, or a circle for a portrait focal point. The mask must not remove evidence or become decorative noise.

### Frame selection by evidence

Choose the frame from what must remain legible, then vary it across the deck:

| Asset/job | Prefer | Avoid |
|---|---|---|
| Full garment / silhouette | Tall editorial window, full-bleed look, or contained vertical proof | Cropping hem, sleeve, or proportion merely to fit a recurring arch |
| Maker portrait / identity | One decisive portrait window or full bleed with a clear text zone | Repeating the same portrait shell on every biography-like slide |
| Hands, patterns, cutting | Wide evidence field, process strip, or sequence with the work surface visible | Narrow portrait crop that hides the action and tool relationship |
| Macro craft detail | Edge-to-edge detail plus an establishing inset when context matters | Decorative curve that obscures the detail it is meant to prove |
| Collection breadth | Contact sheet with one selected dominant look | Uniform gallery where every photo has identical weight |
| Event / team proof | Straight contained photograph with a factual caption | Treating contextual evidence as atmospheric decoration |

An arch, angled cut, circle, or organic mask is a scarce emphasis device. Use it when it makes the subject more legible; otherwise choose a clean edge. Do not reuse the same frame silhouette more than twice in a short deck unless it is an explicit series.

### Layered collage

Use when the story is genuinely cumulative: moodboard, process wall, materials, creator identity, or a multi-source case. Establish hierarchy through scale, overlap, rotation, and depth. Do not build an arbitrary scrapbook.

## 4. Create variation without losing coherence

Across a deck:

- keep one or two recurring anchors such as margin, caption treatment, tone, or image edge;
- vary focal mass, crop direction, image count, and negative-space distribution;
- alternate immersive, analytical, and quiet pages according to the narrative;
- avoid using the same split or card shell on consecutive slides unless it signals an intentional series;
- do not reuse the same image more than once by default;
- when an image must recur, change its job and treatment rather than presenting the same crop twice.

Use a rhythm map before authoring:

`immersive hero → quiet profile → analytical proof → process sequence → portfolio breadth → detail proof → outcome → clean close`

## 5. Attached people, logos, and products

- Do not generate or replace a real person, logo, garment, product, UI, or evidentiary artifact when the supplied asset should remain factual.
- Preserve face, hands, garment silhouette, logo clear space, and critical construction details.
- Use `contain` for logos and low-crop-tolerance artifacts.
- Use image generation only for a missing atmospheric or conceptual job, and keep it visually distinct from factual evidence.
- Place photo provenance and license in the source ledger or speaker notes. Do not print photographer/source labels over portfolio imagery unless the audience contract calls for credits.

## 6. Audience-facing cleanliness

Never expose these on a final slide unless they are audience content:

- reference IDs or version markers;
- “transfer principle,” “avoid,” “layout,” “topology,” or prompt labels;
- asset index numbers and crop instructions;
- stock-photo provider or photographer credits;
- benchmark scores, QA warnings, placeholder captions, generation status, or provenance notes.

Keep them in `source-ledger.json`, `asset-manifest.json`, slide notes, or QA artifacts.

## 7. Visual QA

For every slide, inspect:

- the intended focal subject is visible at presentation scale;
- faces, hands, product boundaries, and important details are not accidentally cropped;
- the image has a specific role beyond decoration;
- text does not compete with high-frequency image regions;
- multiple images have an obvious hierarchy and reading order;
- full bleed, masks, and overlaps remain inside the slide canvas;
- the layout differs from adjacent pages for a reason;
- no internal production label remains visible;
- source and asset identity remain traceable outside the slide face.

For the full deck, inspect the montage for repeated silhouettes. If three or more pages feel like the same photo slot with different content, revise the composition route before polishing micro-details.
