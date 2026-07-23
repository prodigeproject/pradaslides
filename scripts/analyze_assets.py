#!/usr/bin/env python3
"""Inventory attached images/video and create a review-ready asset manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
from fractions import Fraction
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET

from _report import write_json


IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".jfif", ".webp", ".gif", ".bmp", ".tif", ".tiff", ".svg", ".emf", ".wmf"}
VIDEO_EXTENSIONS = {".mp4", ".mov", ".m4v", ".webm", ".avi", ".mkv", ".mpeg", ".mpg"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def orientation(aspect: float | None) -> str | None:
    if aspect is None:
        return None
    if aspect > 2:
        return "panoramic"
    if aspect >= 1.2:
        return "landscape"
    if aspect >= 0.85:
        return "near-square"
    if aspect >= 0.5:
        return "portrait"
    return "tall"


def filename_hint(path: Path, kind: str) -> str:
    name = path.stem.casefold()
    tests = [
        ("logo", r"logo|brand[ _-]?mark|wordmark"),
        ("screenshot-ui", r"screen|screenshot|ui|ux|app|dashboard|mockup"),
        ("chart-data", r"chart|graph|plot|metric|analytics"),
        ("diagram-process", r"diagram|flow|process|architecture|map"),
        ("portrait-team", r"portrait|headshot|team|profile|person"),
        ("product", r"product|packaging|device"),
        ("video-demo", r"demo|walkthrough|prototype|recording"),
    ]
    for label, pattern in tests:
        if re.search(pattern, name):
            return label
    return "video" if kind == "video" else "unknown"


def image_metadata(path: Path) -> tuple[dict[str, Any], Any | None]:
    if path.suffix.lower() == ".svg":
        try:
            root = ET.parse(path).getroot()
            view_box = root.get("viewBox")
            width = height = None
            if view_box:
                values = [float(value) for value in re.split(r"[ ,]+", view_box.strip())]
                if len(values) == 4:
                    width, height = values[2], values[3]
            def numeric(value: str | None) -> float | None:
                if not value:
                    return None
                match = re.match(r"[-+]?\d*\.?\d+", value)
                return float(match.group()) if match else None
            width = width or numeric(root.get("width"))
            height = height or numeric(root.get("height"))
            aspect = round(width / height, 4) if width and height else None
            return {
                "format": "SVG",
                "vector": True,
                "width": width,
                "height": height,
                "aspect": aspect,
                "orientation": orientation(aspect),
                "view_box": view_box,
            }, None
        except (ET.ParseError, OSError, ValueError) as exc:
            return {"format": "SVG", "vector": True, "inspection_error": str(exc)}, None

    try:
        from PIL import Image, ImageStat
    except ImportError:
        return {"inspection_error": "Pillow is not installed"}, None

    try:
        image = Image.open(path)
        width, height = image.size
        aspect = round(width / height, 4) if height else None
        preview = image.convert("RGBA")
        preview.thumbnail((160, 160))
        rgb = preview.convert("RGB")
        mean = tuple(round(value) for value in ImageStat.Stat(rgb).mean[:3])
        has_alpha = "A" in image.getbands() or "transparency" in image.info
        alpha_bbox = None
        transparency_ratio = 0.0
        if has_alpha:
            alpha = image.convert("RGBA").getchannel("A")
            alpha_bbox = list(alpha.getbbox()) if alpha.getbbox() else None
            histogram = alpha.histogram()
            transparent = sum(histogram[:255])
            transparency_ratio = round(transparent / max(1, width * height), 4)
        metadata = {
            "format": image.format,
            "vector": False,
            "width": width,
            "height": height,
            "aspect": aspect,
            "orientation": orientation(aspect),
            "mode": image.mode,
            "frames": getattr(image, "n_frames", 1),
            "has_alpha": has_alpha,
            "alpha_content_bbox": alpha_bbox,
            "transparency_ratio": transparency_ratio,
            "mean_rgb": list(mean),
            "mean_hex": "#%02X%02X%02X" % mean,
        }
        return metadata, image.copy()
    except Exception as exc:  # Pillow raises format-specific errors.
        return {"inspection_error": str(exc)}, None


def parse_fraction(value: str | None) -> float | None:
    if not value or value in {"0/0", "N/A"}:
        return None
    try:
        return round(float(Fraction(value)), 4)
    except (ValueError, ZeroDivisionError):
        return None


def video_metadata(path: Path) -> dict[str, Any]:
    ffprobe = shutil.which("ffprobe")
    if not ffprobe:
        return {"inspection_error": "ffprobe is not available"}
    command = [
        ffprobe,
        "-v",
        "error",
        "-print_format",
        "json",
        "-show_format",
        "-show_streams",
        str(path),
    ]
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=30, check=False)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"inspection_error": str(exc)}
    if result.returncode != 0:
        return {"inspection_error": result.stderr.strip() or "ffprobe failed"}
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        return {"inspection_error": f"Invalid ffprobe JSON: {exc}"}
    streams = payload.get("streams", [])
    video = next((item for item in streams if item.get("codec_type") == "video"), {})
    audio = next((item for item in streams if item.get("codec_type") == "audio"), {})
    width, height = video.get("width"), video.get("height")
    aspect = round(width / height, 4) if isinstance(width, int) and isinstance(height, int) and height else None
    duration = payload.get("format", {}).get("duration") or video.get("duration")
    try:
        duration_value = round(float(duration), 3) if duration is not None else None
    except ValueError:
        duration_value = None
    return {
        "format": payload.get("format", {}).get("format_name"),
        "width": width,
        "height": height,
        "aspect": aspect,
        "orientation": orientation(aspect),
        "duration_seconds": duration_value,
        "frame_rate": parse_fraction(video.get("avg_frame_rate") or video.get("r_frame_rate")),
        "video_codec": video.get("codec_name"),
        "audio_codec": audio.get("codec_name"),
        "has_audio": bool(audio),
        "bit_rate": payload.get("format", {}).get("bit_rate"),
    }


def extract_keyframes(path: Path, asset_id: str, metadata: dict[str, Any], directory: Path, report_base: Path) -> list[str]:
    ffmpeg = shutil.which("ffmpeg")
    duration = metadata.get("duration_seconds")
    if not ffmpeg or not isinstance(duration, (int, float)) or duration <= 0:
        return []
    directory.mkdir(parents=True, exist_ok=True)
    times = [
        ("start", min(1.0, max(0.05, duration * 0.05))),
        ("middle", duration * 0.5),
        ("end", max(0.05, min(duration - 0.05, duration * 0.95))),
    ]
    output_paths: list[str] = []
    for label, second in times:
        output = directory / f"{asset_id}-{label}.jpg"
        if not output.exists():
            command = [
                ffmpeg,
                "-hide_banner",
                "-loglevel",
                "error",
                "-ss",
                f"{second:.3f}",
                "-i",
                str(path),
                "-frames:v",
                "1",
                "-vf",
                "scale=1280:-2:force_original_aspect_ratio=decrease",
                "-q:v",
                "2",
                "-n",
                str(output),
            ]
            result = subprocess.run(command, capture_output=True, text=True, timeout=60, check=False)
            if result.returncode != 0:
                continue
        output_paths.append(Path(os.path.relpath(output, report_base)).as_posix())
    return output_paths


def semantic_skeleton() -> dict[str, Any]:
    return {
        "review_status": "pending",
        "role": "unclassified",
        "subject": "",
        "context": "",
        "message": "",
        "focal_point": "",
        "directionality": "",
        "text_safe_regions": [],
        "protected_regions": [],
        "crop_tolerance": "unknown",
        "quality": "unreviewed",
        "rights": "unknown",
        "attribution": "",
        "sensitivity": "unknown",
        "alt_text": "",
    }


def placement_skeleton() -> dict[str, Any]:
    return {
        "recommended": "",
        "avoid": [],
        "journey_phases": [],
        "slide_candidates": [],
    }


def create_contact_sheet(items: list[tuple[str, str, Any]], output: Path) -> None:
    try:
        from PIL import Image, ImageDraw, ImageOps
    except ImportError:
        return
    if not items:
        return
    columns, cell_w, cell_h, gap = 4, 320, 240, 20
    rows = math.ceil(len(items) / columns)
    sheet = Image.new("RGB", (gap + columns * (cell_w + gap), gap + rows * (cell_h + gap)), "#ECECEC")
    draw = ImageDraw.Draw(sheet)
    for index, (asset_id, label, image) in enumerate(items):
        row, col = divmod(index, columns)
        x, y = gap + col * (cell_w + gap), gap + row * (cell_h + gap)
        canvas = Image.new("RGB", (cell_w, cell_h - 34), "white")
        try:
            thumb = ImageOps.contain(image.convert("RGBA"), (cell_w - 12, cell_h - 46))
            if thumb.mode == "RGBA":
                canvas.paste(thumb, ((cell_w - thumb.width) // 2, (canvas.height - thumb.height) // 2), thumb)
            else:
                canvas.paste(thumb, ((cell_w - thumb.width) // 2, (canvas.height - thumb.height) // 2))
        except Exception:
            pass
        sheet.paste(canvas, (x, y))
        safe_label = label if len(label) <= 42 else label[:39] + "..."
        draw.text((x, y + cell_h - 30), f"{asset_id}  {safe_label}", fill="black")
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", help="Directory containing attached media")
    parser.add_argument("--output", required=True, help="asset-manifest.json path")
    parser.add_argument("--contact-sheet", help="Optional PNG review sheet")
    parser.add_argument("--keyframes-dir", help="Optional directory for three video keyframes per file")
    parser.add_argument("--no-recursive", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    if not root.is_dir():
        raise SystemExit(f"Asset root is not a directory: {root}")
    output = Path(args.output).expanduser().resolve()
    contact_sheet = Path(args.contact_sheet).expanduser().resolve() if args.contact_sheet else None
    keyframes_dir = Path(args.keyframes_dir).expanduser().resolve() if args.keyframes_dir else None
    excluded = {output}
    if contact_sheet:
        excluded.add(contact_sheet)

    previous_by_path: dict[Path, dict[str, Any]] = {}
    previous_by_hash: dict[str, list[dict[str, Any]]] = {}
    next_asset_number = 1
    if output.exists():
        try:
            previous = json.loads(output.read_text(encoding="utf-8"))
            for item in previous.get("assets", []):
                if not isinstance(item, dict):
                    continue
                item_id = item.get("id")
                if isinstance(item_id, str) and re.fullmatch(r"A\d{2,}", item_id):
                    next_asset_number = max(next_asset_number, int(item_id[1:]) + 1)
                old_path = item.get("path")
                if isinstance(old_path, str):
                    candidate = Path(old_path)
                    if not candidate.is_absolute():
                        candidate = output.parent / candidate
                    previous_by_path[candidate.resolve()] = item
                old_hash = item.get("sha256")
                if isinstance(old_hash, str):
                    previous_by_hash.setdefault(old_hash, []).append(item)
        except (OSError, json.JSONDecodeError):
            pass

    candidates = root.glob("*") if args.no_recursive else root.rglob("*")
    files = sorted(
        path for path in candidates
        if path.is_file()
        and path.resolve() not in excluded
        and path.suffix.lower() in IMAGE_EXTENSIONS | VIDEO_EXTENSIONS
    )
    assets: list[dict[str, Any]] = []
    review_images: list[tuple[str, str, Any]] = []
    first_by_hash: dict[str, str] = {}
    used_previous_ids: set[str] = set()
    kind_counts: dict[str, int] = {"image": 0, "video": 0}

    for path in files:
        kind = "video" if path.suffix.lower() in VIDEO_EXTENSIONS else "image"
        kind_counts[kind] += 1
        digest = sha256(path)
        previous_item = previous_by_path.get(path.resolve())
        if previous_item is None:
            previous_item = next(
                (
                    item
                    for item in previous_by_hash.get(digest, [])
                    if isinstance(item.get("id"), str) and item["id"] not in used_previous_ids
                ),
                None,
            )
        previous_id = previous_item.get("id") if isinstance(previous_item, dict) else None
        if isinstance(previous_id, str) and previous_id not in used_previous_ids:
            asset_id = previous_id
            used_previous_ids.add(asset_id)
        else:
            while f"A{next_asset_number:02d}" in used_previous_ids:
                next_asset_number += 1
            asset_id = f"A{next_asset_number:02d}"
            used_previous_ids.add(asset_id)
            next_asset_number += 1
        duplicate_of = first_by_hash.get(digest)
        first_by_hash.setdefault(digest, asset_id)
        if kind == "image":
            technical, preview = image_metadata(path)
            if preview is not None:
                review_images.append((asset_id, path.name, preview))
        else:
            technical = video_metadata(path)
            if keyframes_dir:
                keyframes = extract_keyframes(path, asset_id, technical, keyframes_dir, output.parent)
                technical["keyframes"] = keyframes
                for keyframe in keyframes:
                    try:
                        from PIL import Image
                        frame_path = (output.parent / keyframe).resolve()
                        review_images.append((asset_id, f"{path.name} / {Path(keyframe).stem}", Image.open(frame_path).copy()))
                    except Exception:
                        pass
        previous_semantic = previous_item.get("semantic") if isinstance(previous_item, dict) else None
        previous_placement = previous_item.get("placement") if isinstance(previous_item, dict) else None
        assets.append(
            {
                "id": asset_id,
                "path": Path(os.path.relpath(path, output.parent)).as_posix(),
                "kind": kind,
                "sha256": digest,
                "bytes": path.stat().st_size,
                "duplicate_of": duplicate_of,
                "filename_hint": filename_hint(path, kind),
                "technical": technical,
                "semantic": previous_semantic if isinstance(previous_semantic, dict) else semantic_skeleton(),
                "placement": previous_placement if isinstance(previous_placement, dict) else placement_skeleton(),
            }
        )

    assets.sort(key=lambda item: int(str(item["id"])[1:]))

    manifest = {
        "schema_version": "1.0",
        "root": str(root),
        "assets": assets,
        "summary": {
            "total": len(assets),
            "images": kind_counts["image"],
            "videos": kind_counts["video"],
            "duplicates": sum(bool(item["duplicate_of"]) for item in assets),
            "pending_semantic_review": sum(
                item.get("semantic", {}).get("review_status") == "pending" for item in assets
            ),
        },
        "review_instruction": (
            "View every asset or representative video keyframe, then replace pending/unclassified "
            "semantic fields and complete placement guidance before using the asset in a deck plan. "
            "Re-running this script preserves prior semantic/placement review by path or SHA-256."
        ),
    }
    write_json(output, manifest)
    if contact_sheet:
        create_contact_sheet(review_images, contact_sheet)
    print(f"Asset manifest: {output}")
    print(f"Assets: {len(assets)} ({kind_counts['image']} images, {kind_counts['video']} videos)")
    print(f"Duplicates: {manifest['summary']['duplicates']}")
    if contact_sheet:
        print(f"Contact sheet: {contact_sheet if contact_sheet.exists() else 'not created'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
