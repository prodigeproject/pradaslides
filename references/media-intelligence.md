# Media intelligence and placement

Attached media can change the story, not only the decoration. Analyze assets before locking the outline so the deck can use real evidence, brand identity, people, product behavior, and moments at an appropriate scale.

## Two-pass analysis

### Pass 1 — technical inventory

For every image, video, logo, or graphic, record:

- stable asset ID, local path, file type, byte size, and SHA-256;
- pixel dimensions, aspect ratio, orientation, color mode, alpha/transparency, and rough mean color;
- duplicate or near-duplicate status;
- for video: duration, frame size, frame rate, video/audio codec, and representative keyframes;
- likely filename hint such as logo, screenshot, portrait, chart, or demo;
- missing/corrupt file or unsupported format.

Run `scripts/analyze_assets.py` to generate the technical layer. Never infer slide meaning from filename or dimensions alone.

### Pass 2 — visual and semantic inspection

View every image at useful size. For a video, inspect the opening, middle, ending, major scene changes, and any moment the user identifies. Record:

- `role`: logo, hero/editorial, product evidence, screenshot/UI, chart/data, diagram/process, portrait/team, document proof, texture/background, icon, video/demo, or other;
- subject and context;
- the claim, emotion, or evidence it can support;
- focal point and gaze/directional movement;
- safe regions for text and regions that must stay unobscured;
- crop tolerance: none, low, medium, or high;
- legibility requirements for UI, labels, documents, or charts;
- visual quality and whether upscaling is acceptable;
- rights/permission, attribution, confidentiality, faces/minors, personal data, medical/financial sensitivity, and brand constraints;
- suitable journey phases and candidate slide jobs.

An asset remains `unclassified` until this pass is complete. Do not automatically place an unclassified asset.

## Decide whether the asset belongs

Use an asset only when it performs at least one job:

- **prove:** real output, screenshot, data, document, customer evidence;
- **explain:** mechanism, process, anatomy, architecture, sequence;
- **identify:** person, organization, product, place, or brand;
- **compare:** before/after, versions, alternatives, states;
- **orient:** establish context, environment, or chapter;
- **humanize:** show affected people or lived experience;
- **demonstrate:** show motion, interaction, behavior, or transformation;
- **set meaningful tone:** create a relevant emotional frame.

Exclude or defer media that is redundant, misleading, too weak to read, unlicensed, sensitive without permission, or unrelated to the communication job.

## Placement matrix

| Asset role | Default treatment | Content relationship | Avoid |
|---|---|---|---|
| Logo/brand mark | Native/vector where possible; preserve clear space and aspect | Identity, endorsement, ownership | stretching, recoloring, effects, logo wallpaper |
| Hero/editorial photo | Full bleed or large crop when crop-tolerant | Emotional/contextual anchor with short claim | tiny thumbnail, text across subject, generic use |
| Portrait/team | Large portrait, cutout, or disciplined grid | Role, credibility, story, quote | circular-avatar wall without hierarchy |
| Product photo | Large contained or cropped detail plus annotation | Feature, material, usage, proof | isolated product with no audience meaning |
| Screenshot/UI | Contain at readable scale; zoom/crop critical states | Demonstrate workflow or decision | full-screen UI shrunk unreadably, decorative device frames |
| Chart/data image | Contain or rebuild natively; preserve axes/labels | Evidence for a stated claim | crop, perspective, low resolution, unsupported conclusion |
| Diagram/process | Rebuild natively when labels must edit; otherwise contain | Relationship, sequence, ownership | arbitrary recoloring or removing boundaries |
| Document/certificate | Contained page/detail with source and annotation | Verification or provenance | unreadable whole page used as decoration |
| Texture/background | Full bleed, low semantic load, controlled contrast | Tone or section identity | competing with text or implying evidence |
| Icon | Small repeated semantic marker from one family | Scanning/category support | filler, mixed families, oversized ornament |
| Video/demo | Embedded or linked with poster, caption, duration, fallback | Motion, interaction, testimony, process | silent autoplay, no fallback, unsupported codec |

## Aspect-ratio routing

| Shape | Useful layouts | Notes |
|---|---|---|
| Panoramic/wide (`>2:1`) | full-width hero, section banner, top/bottom evidence band | protect subject from title/footer collision |
| Landscape (`1.2–2:1`) | split claim/evidence, large contained proof, full bleed | most flexible; crop according to focal point |
| Near-square (`0.85–1.2`) | feature panel, comparison pair, modular case proof | do not default to a grid unless items are equal |
| Portrait (`0.5–0.85`) | left/right column, biography, product/phone detail | preserve height; pair with vertical text flow |
| Tall (`<0.5`) | scroll/UI strip, timeline detail, full-height side rail | enlarge/crop sections rather than shrink the whole asset |

Aspect ratio suggests geometry, not meaning. A wide chart should still be contained; a portrait photo may be cropped if the focal point permits.

## Focal point and directionality

- Place text in a genuinely quiet region, not merely an area with lower average color.
- Keep faces, eyes, hands, products, labels, charts, and logos unobscured.
- Let gaze or movement point into the slide rather than out of the canvas when practical.
- If a subject faces right, a left-side image often leads naturally toward right-side copy; reverse when the actual safe area or sequence requires it.
- Use masks/gradients behind text only when they preserve the image's evidence and remain consistent with the visual system.
- Record crop coordinates or focal anchors so different renderers do not choose different crops.

## Logo handling

- Prefer SVG, EMF, or transparent high-resolution PNG.
- Preserve the original aspect ratio and brand clear space.
- Do not infer permission to recolor, outline, add shadows, animate, or place the logo on a conflicting background.
- Use repeated logos only for a real brand/partner reason; avoid a logo on every page unless the brand system requires it.
- For multiple partner logos, normalize optical size rather than raw bounding-box size and keep relationships/endorsement accurate.
- If the source has a solid background, do not remove it automatically when that background is part of the mark.

## Screenshots and UI

- Identify the exact interface state and the audience question it answers.
- Crop or zoom to the decisive interaction; keep navigation context only when needed.
- Rebuild callouts and annotations natively so they remain readable/editable.
- Hide or redact personal data, tokens, URLs, account names, and confidential content before use.
- Do not place multiple tiny phone/browser frames merely to signal “digital product.”
- When comparing states, align scale, viewport, and crop.

## Photos and people

- Use real people/assets with permission and accurate context.
- Avoid cropping at awkward joints or cutting off meaningful tools/products.
- Preserve skin tone and do not apply filters that change evidence.
- For testimonials, connect portrait, identity, quote, and permission.
- Do not infer identity, protected traits, emotion, diagnosis, or endorsement from appearance.
- Flag faces/minors and sensitive environments for user confirmation when needed.

## Video

Decide whether video is essential. Use it when motion or time is the evidence: a product interaction, prototype, before/after, mechanism, testimony, or performance.

Record:

- exact in/out time and intended duration;
- poster frame and caption;
- whether audio is required;
- captions/transcript and language;
- embedded versus local link versus external link;
- codec/container compatibility for the target environment;
- offline/network dependency;
- a static fallback slide or keyframe sequence;
- presenter cue and failure contingency in notes.

Do not autoplay with sound by default. Test the actual presentation machine when possible.

## Asset-to-story mapping

Map media after the communication job is clear but before the final slide plan:

1. Identify high-value evidence assets.
2. Let those assets anchor candidate claims and case-study sequences.
3. Place identity/context assets around the evidence rather than crowding it.
4. Assign each asset a primary slide and optional fallback use.
5. Avoid reusing the same hero image across multiple substantive slides; logos and deliberate motifs are exceptions.
6. If no asset can support a needed claim, source/create an appropriate asset or choose a native chart/diagram/text treatment.

Suggested journey roles:

| Journey phase | Useful media |
|---|---|
| Attention | meaningful hero, concrete scene, verified result, short demo |
| Orientation | map, environment, identity, product overview, advance organizer |
| Tension | before state, bottleneck screenshot, customer evidence, trend/chart |
| Insight | annotated evidence, diagram, contrast, close-up detail |
| Proof | actual result, case artifact, data, testimonial, document |
| Resolution | future-state mockup, workflow, roadmap, working demo |
| Decision | option comparison, scope visual, owner/timeline, commercial table |
| Retention | memorable identity, single synthesis image, contact/action lockup |

## Deck-plan media fields

For slides using attachments, add:

```json
{
  "asset_ids": ["A03"],
  "media_plan": {
    "purpose": "Show the tested checkout state that reduced abandonment",
    "treatment": "contained screenshot with a native zoom callout",
    "placement": "right 58% of canvas; claim and metric on left",
    "crop_mode": "contain",
    "focal_anchor": "center",
    "text_safe_region": "left",
    "fallback": "annotated still if embedded demo fails",
    "alt_text": "Checkout confirmation screen with the simplified three-step progress indicator"
  }
}
```

Use an empty `asset_ids` array and `media_plan: null` when no attachment is used.

When a slide uses more than one asset, a single shared crop/fallback instruction is ambiguous. In strict visual mode, add one `asset_treatments` entry per asset:

```json
{
  "asset_ids": ["A03", "A04"],
  "media_plan": {
    "purpose": "Pair restrained identity with a single-use conceptual hero",
    "treatment": "logo lockup over a full-bleed hero",
    "placement": "logo top left; hero full stage; copy in the protected left field",
    "crop_mode": "cover",
    "focal_anchor": "right center",
    "text_safe_region": "left 45 percent",
    "fallback": "typographic cover with text wordmark",
    "alt_text": "Conceptual orchestration scene with the product identity",
    "asset_treatments": [
      {
        "asset_id": "A03",
        "treatment": "unaltered vector logo",
        "placement": "top-left identity lockup",
        "crop_mode": "contain",
        "focal_anchor": "center",
        "text_safe_region": "own clear-space box",
        "fallback": "text wordmark",
        "alt_text": "Product wordmark"
      },
      {
        "asset_id": "A04",
        "treatment": "single-use full-bleed hero",
        "placement": "full stage with focal subject on the right",
        "crop_mode": "cover",
        "focal_anchor": "right center",
        "text_safe_region": "left 45 percent",
        "fallback": "native typographic composition",
        "alt_text": "Abstract system scene with a protected title field"
      }
    ]
  }
}
```

Every treatment must reference an asset used on that slide. A logo may use only `contain` or `none`. Any asset reviewed with `crop_tolerance: none` may also use only `contain` or `none`; use a native zoom/callout instead of destructive cropping.

## Media QA

- Every used asset ID exists in `asset-manifest.json`.
- Semantic role, subject, message, rights, sensitivity, crop tolerance, and alt text are resolved.
- Placement matches focal point and safe region.
- No distortion, accidental crop, blur, or low-resolution enlargement.
- Screenshot/chart/document labels remain readable.
- Logo clear space, colors, and aspect are preserved.
- Video plays offline/online as promised and has a tested fallback.
- Redactions survive export.
- Repeated images are intentional.
- The media actually supports the slide claim.
