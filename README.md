# PradaSlides

PradaSlides is an agent skill for creating audience-ready presentations from a short prompt or source material. It turns a request into a clear communication brief, evidence-aware narrative, product-specific visual direction, editable slide plan, and a verified delivery route for PPTX, HTML slides, PDF, or planning-only work.

## What it covers

- portfolios, work/result reviews, proposals, sales and investor decks;
- strategy, research, technical, teaching, report, keynote, and template-system presentations;
- supplied photos, logos, screenshots, charts, and video with explicit media roles and crop decisions;
- capability-aware routing for text-only, vision, image-generation, video-generation, and delegated runtimes;
- visual QA for contrast, typography, frame selection, crop integrity, topology rhythm, and presenter-stage fit.

## Install

Clone the repository, then install it into an explicit agent skills directory:

```bash
python scripts/install_skill.py --target <agent-skills-directory>
```

For an existing installation, use `--replace`; the installer preserves a backup.

## Use

Ask the agent to use `$pradaslides`, then provide the presentation goal, audience, source material, required format, and any brand or visual references. The skill will infer sensible defaults when doing so is safe and will preserve user assets.

To start a standalone project workspace:

```bash
python scripts/bootstrap_project.py --output <project-dir> --intent portfolio
```

See [SKILL.md](SKILL.md) for the full workflow and [references/](references/) for the focused guidance.

## Validate

```bash
python scripts/self_test.py
python scripts/validate_design_system.py assets/starter/design-system.json
```

## Contributing

Keep changes focused on reusable agent behavior. Do not add user assets, credentials, source material without permission, or flattened slide exports as skill assets. Run the validation commands above before opening a pull request.

## License

Released under the [MIT License](LICENSE).
