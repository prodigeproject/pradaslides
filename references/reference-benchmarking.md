# Reference-relative HTML benchmarking

Use references as a quality floor and design constraint, not as a template library. A candidate passes when it reaches the transferable craft of the relevant reference cluster while retaining an original composition and an intent-fit story.

## Separate relevance from quality

A business proposal does not need to resemble a fashion lookbook. It can still be held to the lookbook's crop discipline, type-role clarity, scale contrast, and rhythm. Record each reference as:

- `selected` when it directly informs the art direction;
- `quality-floor` when one or more craft principles apply across intents;
- `not-applicable` only when a principle would damage the communication job, with a reason.

Never average unrelated styles into a single visual direction. Select one direction, then use the corpus union to test craft.

## Prove corpus coverage when the user requires every reference

Cluster coverage is not the same as individual-reference coverage. When the user explicitly requires the baseline to account for every supplied reference, add a `coverage` contract to `reference-benchmark.json`.

Use:

- `cluster-sampled` when representative references define the floor;
- `mapped-all-references` when every reference must influence at least one response but several references may share a slide;
- `one-slide-per-reference` for a dedicated stress fixture where every reference needs an independently inspectable response.

Every mapping requires `reference_id`, `slide_id`, a concise `response` explaining what original design decision transfers the principle, and `status`. In exhaustive modes, responses must contain at least eight words and must be individually specific; repeated generic descriptions are invalid. Final coverage may not omit a reference or retain a failed mapping. A one-slide-per-reference fixture must use unique in-range slide IDs.

Bind the contract to the live HTML. Add `referenceId` or `referenceIds` to the matching slide data. `run_html_benchmark.py` passes the benchmark into browser QA, which compares the rendered `data-reference-ids` with the expected mappings and raises `HTML_REFERENCE_TRACE` for missing, extra, or swapped IDs. This proves that coverage exists in the rendered slide sequence rather than only in the JSON report.

Do not satisfy coverage by embedding the reference image or recreating its marketplace composition. Prefer original HTML/CSS/SVG media proxies, native diagrams, typography, and geometry. The fixture proves range; it is not automatically an intent-fit user presentation.

Exhaustive modes also activate browser-measured composition diversity in `run_html_benchmark.py`. The QA report records unique topologies, layouts, tones, densities, combined signatures, signature ratio, and the longest consecutive topology run. A fixture fails when its mappings merely relabel a repeated macro shell. These metrics are a regression gate, not a substitute for human judgment about whether each composition is appropriate.

## Universal floor

Score ten dimensions after rendering:

1. **Identity:** recognizable by slide 1, coherent afterward.
2. **Hierarchy:** one focal region and deliberate reading order.
3. **Typography:** clear display/body/label roles and no emergency shrink.
4. **Composition:** relationship-aware grid, whitespace, alignment, and asymmetry.
5. **Media:** deliberate crop, focal anchor, mask, caption, and text-safe region.
6. **Proof:** inspectable evidence with concept/scenario/fact boundaries.
7. **Rhythm:** purposeful changes in topology, tone, focal mass, and density.
8. **Runtime:** fixed stage, thumbnails, navigation, notes, presentation mode, and honest export.
9. **Accessibility:** contrast, readable type, keyboard behavior, captions, and fallbacks.
10. **Originality:** principles transferred without cloning or generic card-wall fallback.

Do not self-award a pass from source code. Every score needs render evidence, a rationale, and a reviewer. A final benchmark has no criterion below its floor, records the automated browser-QA report alongside the renders, and has no unresolved blocker.

## HTML-only loop

Use this loop when HTML is the selected benchmark runtime:

1. author or tune the fixed-stage deck;
2. render every slide at the authored stage size;
3. render the presenter console at the target browser viewport;
4. build a montage and inspect rhythm at thumbnail scale;
5. inspect cover, densest slide, proof slide, media slide, and closing at full size;
6. record failures in `reference-benchmark.json`;
7. repair source HTML/CSS/JS, not the screenshots;
8. re-render changed pages and the montage;
9. validate with `--require-final` only when every floor passes.

```bash
python scripts/validate_reference_benchmark.py <project-dir>/reference-benchmark.json --require-final
```

After `reference-benchmark.json` is populated, run the complete HTML loop with one command:

```bash
python scripts/run_html_benchmark.py --project <project-dir> --entry presenter/index.html --count <slide-count>
```

This runs browser QA, writes fresh slide renders, creates the montage and console capture without an image-library dependency, and then validates the final reference floor. Exhaustive coverage modes automatically require DOM composition diversity. A failure stops the loop at the source that must be repaired.

PNG files are QA evidence only. The HTML entrypoint remains the deliverable.

## Anti-gaming rules

- Structural completeness cannot compensate for weak visible craft.
- A marketplace montage cannot prove body-text readability.
- A high score without evidence is invalid.
- `not-applicable` cannot hide a failed universal criterion.
- Generated art cannot score as product proof.
- UI screenshots score only when labels remain inspectable.
- A single strong cover cannot carry identity, rhythm, and proof scores for the whole deck.
- Cluster sampling cannot be reported as every-reference coverage; declare and validate the coverage mode.
- Unique reference IDs and titles cannot conceal one repeated macro shell; exhaustive fixtures must pass the DOM diversity gate.
- Repeated generic response prose cannot masquerade as individual treatment; exhaustive mapping responses must be specific and unique.
- Coverage JSON cannot drift from the rendered deck; reference IDs must pass plan-to-DOM trace.
- Reference similarity is not originality; copied topology should lower the score.
