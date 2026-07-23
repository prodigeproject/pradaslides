# Runtime routing and delivery

PradaSlides is runtime-agnostic. Detect what the host agent can actually understand, generate, build, render, inspect, and export. Read `capability-orchestration.md`; do not promise native editability from a renderer that only produces images or visual inspection from a text-only model.

## Capability scan

Run `scripts/capability_scan.py --json` when capabilities are unclear. Consider:

- PowerPoint-native generation library or host presentation API;
- Node.js and PptxGenJS;
- Python and `python-pptx`;
- HTML/JS and a headless browser;
- Slidev or another web-slide runtime;
- LibreOffice or Microsoft PowerPoint for rendering/round-trip verification;
- PDF renderer and image montage tools;
- image search/generation and chart/diagram tooling.

The scan reports presence, not fitness. Confirm that the selected runtime supports the required notes, charts, masters, media, fonts, and export path.

## Runtime matrix

| Runtime | Best for | Editability | Strengths | Constraints |
|---|---|---:|---|---|
| Host-native presentation API | General PPTX when available | High | integrated build/render workflow | host-specific behavior |
| PptxGenJS | Cross-platform native PPTX | High | text, shapes, images, tables, charts, notes, masters | agent owns layout and QA |
| `python-pptx` | Native PPTX and OOXML workflows | High | mature PPTX manipulation, template filling | limited rendering; some features require OOXML work |
| HTML → PPTX converter | Design-rich fixed slides with editable core elements | Mixed | browser layout plus PPTX export | CSS fidelity and rasterization boundaries |
| Fixed-stage HTML | Web-native, interactive, portable visual deck | Source-editable | strong layout, browser preview | not a native PPTX; export varies |
| Slidev | Technical talks, code, diagrams, animation | Source-editable | Markdown/Vue, presenter mode, code and math | theme/runtime dependency; PPTX importability is limited |
| SVG → DrawingML/PPTX | Deterministic visual authoring | High/mixed | explicit geometry and reusable validation | complex converter and native-structure concerns |
| Image-first generator | Fast art-directed pages | Low | visual novelty and fidelity | text errors, accessibility, editability, file size |

## Routing rules

### Native PPTX default

Use native PPTX when the user expects to edit, reuse, send to ordinary office users, apply masters, or preserve accessibility. Prefer native text, shapes, charts, and tables. Rasterize only visual effects that cannot be represented reliably.

For high-art-direction or reference-matched work, reconstruct the reference grammar rather than flattening each page: native type, rules, masks/shapes where reliable, page furniture, charts, tables, callouts, and exact labels; local raster only for photos, texture, approved art, and non-reconstructable high-fidelity detail. Read `art-direction-and-pptx-reconstruction.md` before selecting this route.

### Existing PPTX

Choose one mutation model:

- `redesign`: wording/order/layout may change; create a new deck.
- `fill-template`: keep native shells/masters and replace defined content slots.
- `enhance-existing`: preserve visible slides and add notes, transitions, timings, or narration.

Do not mix these models silently. Copy the source to a new output and preserve the original.

### Fixed-stage HTML

Use a fixed canvas such as `1600×900`, `1920×1080`, or `1280×720`; scale the stage for viewing instead of reflowing slide elements responsively. Read `html-presenter-console.md` and use `scripts/scaffold_presenter.py` when the output should feel like a presentation product rather than a bare page. Test thumbnails, keyboard navigation, focus, notes, chrome-free presenter mode, panel resizing, PDF export, and font loading. Use semantic HTML where practical.

Treat console controls as safe display overrides. They may change tone, transition, density within budget, and slide furniture. They must not silently rewrite claims, evidence, topology, chart data, or media crops. Keep all media paths relative so `file://` and static-server routes work.

### Slidev

Use for code-heavy or interactive talks where Markdown/Vue, syntax highlighting, math, diagrams, animations, and presenter tooling are central. Keep a fallback PDF and disclose that native PowerPoint editing is not the source-of-truth workflow.

### Image-first

Use only when the user explicitly accepts:

- limited text editability and searchability;
- weaker accessibility and reading order;
- possible OCR or generated-text errors;
- larger files;
- difficult chart/data correction.

If an editable export is reconstructed through OCR, segmentation, and inpainting, label it as reconstructed and inspect every recovered element.

## Intermediate representation

Keep a portable contract independent of the renderer:

`brief.json → source-ledger.json → design-system.json + layout-manifest.json → deck-plan.json + visual-generation-plan.json → authoring source → rendered preview → delivery artifact`

The capability route sits beside the content chain:

`capability-profile.json → execution-plan.json → delegated handoffs / runtime choice / QA gates`

The deck plan owns communication intent; the authoring source owns visible layout; rendered images are derived previews. Never patch the preview as if it were the source.

## Fonts

- Detect installed fonts when possible.
- Use licensed fonts and declare fallbacks.
- Test glyph coverage for the user's language.
- Embed fonts only when the runtime, license, and delivery target support it.
- Expect substitution across Windows, macOS, web, and PDF; render-test the target environment when possible.

## Aspect ratio and safe areas

Default to `16:9` unless the user or source requires another format. Preserve an existing deck's ratio unless a redesign explicitly changes it. Keep critical content inside a safety margin and account for footers, notes, subtitles, or UI chrome.

## Charts and data

Prefer native charts when the user must update data. Otherwise, use vector charts with an adjacent data source and reproducible generation step. Never deliver an unlabeled chart image without the data and source record.

## Notes, accessibility, and metadata

When supported:

- add speaker notes separately from slide copy;
- provide alt text or meaningful object names;
- maintain a logical reading order;
- include deck title, author/organization, language, and subject metadata;
- give charts a concise textual takeaway and source;
- avoid relying on color alone.

For attached video, confirm the selected runtime can embed or link the actual container/codec, preserve offline behavior, expose a poster frame, and provide a static fallback. Treat a linked local path as a delivery dependency and test it on the presentation machine.

## Rendering and round-trip verification

Use the strongest available check:

1. open and render with Microsoft PowerPoint when available;
2. render with LibreOffice for an independent compatibility check;
3. use a host-native renderer;
4. export to PDF and rasterize pages;
5. use browser screenshots for web slides.

Renderer success is necessary but not sufficient. Inspect visual output and package structure.

For editable reference-led PPTX, inspect both the montage and individual rendered slides for page silhouette, focal mass, type-role contrast, material/edge language, image crops, card discipline, slide-family rhythm, and native-versus-raster fidelity. A successful open or export does not prove visual parity.

## Delivery bundle

Use clear folders:

```text
project/
  brief.json
  source-ledger.json
  deck-plan.json
  src/
  assets/
  previews/
  qa/
  exports/
```

Keep temporary files outside `exports/`. Deliver only requested formats plus the supporting QA/source artifacts that make the deck maintainable.
