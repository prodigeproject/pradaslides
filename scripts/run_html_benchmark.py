#!/usr/bin/env python3
"""Run PradaSlides HTML browser QA, renders, montage, and reference-floor validation."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from _report import emit_report, load_json
from validate_reference_benchmark import validate as validate_reference_benchmark


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, type=Path)
    parser.add_argument("--entry", default="presenter/index.html")
    parser.add_argument("--count", required=True, type=int)
    parser.add_argument("--node", default="node")
    parser.add_argument("--chrome")
    parser.add_argument("--allow-draft-benchmark", action="store_true")
    args = parser.parse_args()

    project = args.project.expanduser().resolve()
    entry = (project / args.entry).resolve()
    if not entry.is_file():
        print(f"ERROR: HTML entrypoint not found: {entry}")
        return 1
    if args.count < 1:
        print("ERROR: --count must be positive")
        return 1

    script = Path(__file__).resolve().with_name("qa_html_presenter.mjs")
    report = project / "qa" / "html-presenter.json"
    render_dir = project / "renders" / "slides"
    montage = project / "renders" / "slide-montage.png"
    console = project / "renders" / "console" / "presenter-console.png"
    benchmark_path = project / "reference-benchmark.json"
    if not benchmark_path.is_file():
        print(f"ERROR: reference benchmark not found: {benchmark_path}")
        return 1
    benchmark = load_json(benchmark_path)
    command = [
        args.node,
        str(script),
        "--entry",
        str(entry),
        "--count",
        str(args.count),
        "--output",
        str(report),
        "--render-dir",
        str(render_dir),
        "--montage",
        str(montage),
        "--console-shot",
        str(console),
    ]
    deck_plan = project / "deck-plan.json"
    if deck_plan.is_file():
        command.extend(["--deck-plan", str(deck_plan)])
    coverage_mode = (benchmark.get("coverage") or {}).get("mode")
    if coverage_mode in {"mapped-all-references", "one-slide-per-reference"}:
        command.extend(["--require-diversity", "--reference-benchmark", str(benchmark_path)])
    if args.chrome:
        command.extend(["--chrome", args.chrome])
    try:
        qa = subprocess.run(command, check=False)
    except FileNotFoundError:
        print(f"ERROR: Node.js executable not found: {args.node}")
        return 1
    if qa.returncode:
        print("HTML benchmark stopped: browser QA failed. Repair the HTML source and rerun.")
        return qa.returncode

    diagnostics = validate_reference_benchmark(
        benchmark, not args.allow_draft_benchmark, project
    )
    verdict = emit_report("reference benchmark validation", diagnostics)
    if verdict:
        print("HTML benchmark stopped: update evidence-backed scores or repair remaining floor failures.")
        return verdict

    print("HTML benchmark loop: PASSED")
    print(f"  entrypoint: {entry}")
    print(f"  browser QA: {report}")
    print(f"  montage: {montage}")
    print(f"  console: {console}")
    print(f"  reference floor: {benchmark_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
