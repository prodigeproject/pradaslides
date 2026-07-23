# Tuning iteration versioning

Use this contract whenever a user asks to tune, benchmark, compare, or repeatedly improve a presentation candidate.

## Rule

Freeze the current candidate before mutation. Never use a version label for a state that cannot be reopened. Never reconstruct an overwritten version and present it as the original.

## Comparable run contract

A direct V-to-V comparison requires the same:

- user prompt and communication intent;
- content, claims, and evidence pack;
- reference inventory;
- output runtime and slide count;
- capability profile, including vision and generation availability;
- benchmark viewport and QA rules.

When any item changes, label the artifact `surviving-evidence`, `retrospective`, or `different-input`; do not compute a quality delta against it as if it were controlled.

## Files

Keep one immutable directory per controlled iteration:

```text
runs/
  v03/
    index.html
    iteration.json
    source/
    qa/
    renders/
  v04/
```

`iteration.json` must contain:

- `id`, `parent`, `created_at`, and `status`;
- prompt/input hashes or stable source paths;
- capability profile;
- tuning hypothesis;
- files changed;
- asset additions and removals;
- benchmark metrics and blockers;
- `comparable_to_parent` with a reason.

## Presentation surface

Expose a small HTML iteration index with:

- a visible version label outside the exported slide canvas;
- direct links to every surviving artifact;
- side-by-side previews when practical;
- an explicit warning for uncontrolled comparisons;
- the current promoted candidate.

## Promotion

Do not rewrite a frozen run. Create a new version, run QA, then update the manifest's `current` pointer. Keep rejected versions inspectable with their blockers.
