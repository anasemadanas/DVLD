from __future__ import annotations

import base64
import html
import re
import zlib
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from xml.etree import ElementTree as ET


REPO_ROOT = Path(__file__).resolve().parents[2]
UML_ROOT = REPO_ROOT / "docs" / "UML"
REPORT_PATH = UML_ROOT / "drawio-validation-report.md"


@dataclass
class DrawioValidation:
    path: Path
    parse_ok: bool
    embedded_xml_exists: bool
    vertex_count: int
    edge_count: int
    image_cell_count: int
    embedded_image_markers: int
    mxcell_count: int
    status: str
    notes: list[str]


def decode_diagram_payload(payload: str) -> str | None:
    payload = payload.strip()
    if not payload or payload.startswith("<mxGraphModel"):
        return payload or None
    try:
        raw = base64.b64decode(payload)
        try:
            return zlib.decompress(raw, -15).decode("utf-8")
        except zlib.error:
            return raw.decode("utf-8")
    except Exception:
        return None


def collect_xml_text(path: Path) -> tuple[bool, str, list[str]]:
    notes: list[str] = []
    raw = path.read_text(encoding="utf-8", errors="ignore")
    xml_parts = [raw]
    try:
        root = ET.fromstring(raw)
        for diagram in root.findall(".//diagram"):
            if diagram.text and diagram.text.strip() and "<mxGraphModel" not in raw:
                decoded = decode_diagram_payload(html.unescape(diagram.text))
                if decoded:
                    xml_parts.append(decoded)
                    notes.append("Decoded compressed diagram XML payload.")
        return True, "\n".join(xml_parts), notes
    except ET.ParseError as exc:
        return False, raw, [f"XML parse error: {exc}"]


def validate_drawio(path: Path) -> DrawioValidation:
    parse_ok, text, notes = collect_xml_text(path)
    mxcell_count = len(re.findall(r"<mxCell\b", text))
    vertex_count = len(re.findall(r'\bvertex="1"', text))
    edge_count = len(re.findall(r'\bedge="1"', text))
    image_cell_count = len(re.findall(r"shape=image|image=", text))
    embedded_image_markers = len(re.findall(r"data:image|image/png|image/jpeg|base64,", text, re.IGNORECASE))
    embedded_xml_exists = "<mxfile" in text and "<mxGraphModel" in text and mxcell_count > 0

    if not parse_ok:
        status = "FAIL"
    elif embedded_image_markers:
        status = "FAIL"
        notes.append("Embedded image/base64 marker found.")
    elif not embedded_xml_exists:
        status = "FAIL"
        notes.append("Embedded Draw.io XML/mxGraphModel content was not found.")
    elif vertex_count == 0:
        status = "FAIL"
        notes.append("No editable vertex shapes found.")
    elif mxcell_count <= image_cell_count + 2:
        status = "FAIL"
        notes.append("Diagram appears to contain only image cells or root cells.")
    elif edge_count == 0:
        status = "WARN"
        notes.append("No editable connectors found; acceptable only for diagrams with no relationships/flows.")
    else:
        status = "PASS"

    return DrawioValidation(
        path=path,
        parse_ok=parse_ok,
        embedded_xml_exists=embedded_xml_exists,
        vertex_count=vertex_count,
        edge_count=edge_count,
        image_cell_count=image_cell_count,
        embedded_image_markers=embedded_image_markers,
        mxcell_count=mxcell_count,
        status=status,
        notes=notes,
    )


def write_report(results: list[DrawioValidation]) -> None:
    pass_count = sum(1 for r in results if r.status == "PASS")
    warn_count = sum(1 for r in results if r.status == "WARN")
    fail_count = sum(1 for r in results if r.status == "FAIL")
    total_vertices = sum(r.vertex_count for r in results)
    total_edges = sum(r.edge_count for r in results)

    lines = [
        "# Draw.io Editability Validation Report",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "## Scope",
        "",
        "- All `.drawio` files under `docs/UML`.",
        "",
        "## Validation Checks",
        "",
        "- Embedded Draw.io XML / `mxGraphModel` exists.",
        "- Editable vertex shapes exist.",
        "- Editable connector edges exist where expected.",
        "- Diagram is not a flat embedded image export.",
        "- No `data:image`, `image/png`, `image/jpeg`, or `base64,` image markers are present.",
        "",
        "## Summary",
        "",
        f"- Draw.io files checked: {len(results)}",
        f"- Passed: {pass_count}",
        f"- Warnings: {warn_count}",
        f"- Failed: {fail_count}",
        f"- Total editable shape vertices: {total_vertices}",
        f"- Total editable connector edges: {total_edges}",
        "",
        "## Results",
        "",
        "| File | Status | mxCells | Vertices | Edges | Image Cells | Embedded Image Markers | Notes |",
        "|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for result in results:
        rel = result.path.relative_to(REPO_ROOT)
        notes = "; ".join(result.notes) if result.notes else ""
        lines.append(
            f"| `{rel}` | {result.status} | {result.mxcell_count} | {result.vertex_count} | {result.edge_count} | "
            f"{result.image_cell_count} | {result.embedded_image_markers} | {notes} |"
        )

    failures = [r for r in results if r.status == "FAIL"]
    warnings = [r for r in results if r.status == "WARN"]
    lines.extend(["", "## Failures", ""])
    if failures:
        for result in failures:
            lines.append(f"- `{result.path.relative_to(REPO_ROOT)}`: {'; '.join(result.notes)}")
    else:
        lines.append("- None.")

    lines.extend(["", "## Warnings", ""])
    if warnings:
        for result in warnings:
            lines.append(f"- `{result.path.relative_to(REPO_ROOT)}`: {'; '.join(result.notes)}")
    else:
        lines.append("- None.")

    lines.extend(
        [
            "",
            "## Conclusion",
            "",
            "- Files marked `PASS` contain native editable Draw.io XML with editable shapes and connectors.",
            "- No passing file is an image-only wrapper.",
            "- Connectors remain editable where edge cells are present.",
        ]
    )
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    files = sorted(UML_ROOT.rglob("*.drawio"))
    results = [validate_drawio(path) for path in files]
    write_report(results)
    print(f"drawio_files={len(results)}")
    print(f"passed={sum(1 for r in results if r.status == 'PASS')}")
    print(f"warnings={sum(1 for r in results if r.status == 'WARN')}")
    print(f"failed={sum(1 for r in results if r.status == 'FAIL')}")
    print(f"report={REPORT_PATH}")


if __name__ == "__main__":
    main()
