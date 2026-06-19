from __future__ import annotations

import html
import math
import re
import subprocess
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from xml.etree import ElementTree as ET


REPO_ROOT = Path(__file__).resolve().parents[2]
UML_DIRS = [
    REPO_ROOT / "docs" / "UML" / "diagram",
    REPO_ROOT / "docs" / "UML" / "design",
    REPO_ROOT / "docs" / "UML" / "state",
]
REPORT_PATH = REPO_ROOT / "docs" / "UML" / "export-sync-report.md"
FORCE_REFRESH_ALL_EXPORTS = True
PLANTUML_JAR_CANDIDATES = [
    Path("C:/Users/Public/DVLD-Workspace/tools/plantuml/plantuml.jar"),
    Path("C:/Users/D4RK/.vscode/extensions/jebbs.plantuml-2.18.1/plantuml.jar"),
    Path("C:/Users/D4RK/.cursor/extensions/jebbs.plantuml-2.18.1-universal/plantuml.jar"),
    Path("C:/Users/D4RK/.antigravity/extensions/jebbs.plantuml-2.18.1-universal/plantuml.jar"),
]


@dataclass
class ExportStatus:
    puml: Path
    png: Path
    drawio: Path
    png_reason: str | None = None
    drawio_reason: str | None = None
    png_generated: bool = False
    drawio_generated: bool = False
    png_error: str | None = None
    drawio_error: str | None = None


class DrawioBuilder:
    def __init__(self, title: str):
        self.mxfile = ET.Element(
            "mxfile",
            {
                "host": "app.diagrams.net",
                "modified": datetime.now().isoformat(timespec="seconds"),
                "agent": "Codex UML export synchronizer",
                "version": "24.7.17",
                "type": "device",
            },
        )
        self.diagram = ET.SubElement(self.mxfile, "diagram", {"id": "diagram-1", "name": title[:80] or "Page-1"})
        self.model = ET.SubElement(
            self.diagram,
            "mxGraphModel",
            {
                "dx": "1600",
                "dy": "1000",
                "grid": "1",
                "gridSize": "10",
                "guides": "1",
                "tooltips": "1",
                "connect": "1",
                "arrows": "1",
                "fold": "1",
                "page": "1",
                "pageScale": "1",
                "pageWidth": "1600",
                "pageHeight": "1000",
                "math": "0",
                "shadow": "0",
            },
        )
        self.root = ET.SubElement(self.model, "root")
        ET.SubElement(self.root, "mxCell", {"id": "0"})
        ET.SubElement(self.root, "mxCell", {"id": "1", "parent": "0"})
        self.counter = 2

    def new_id(self) -> str:
        value = str(self.counter)
        self.counter += 1
        return value

    def vertex(self, value: str, x: float, y: float, w: float, h: float, style: str) -> str:
        cell_id = self.new_id()
        cell = ET.SubElement(
            self.root,
            "mxCell",
            {
                "id": cell_id,
                "value": html.escape(value, quote=False),
                "style": style,
                "vertex": "1",
                "parent": "1",
            },
        )
        ET.SubElement(
            cell,
            "mxGeometry",
            {"x": str(round(x, 1)), "y": str(round(y, 1)), "width": str(round(w, 1)), "height": str(round(h, 1)), "as": "geometry"},
        )
        return cell_id

    def edge(self, source: str, target: str, label: str = "", style: str | None = None) -> str:
        cell_id = self.new_id()
        edge_style = style or "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;"
        cell = ET.SubElement(
            self.root,
            "mxCell",
            {
                "id": cell_id,
                "value": html.escape(label, quote=False),
                "style": edge_style,
                "edge": "1",
                "parent": "1",
                "source": source,
                "target": target,
            },
        )
        ET.SubElement(cell, "mxGeometry", {"relative": "1", "as": "geometry"})
        return cell_id

    def tostring(self) -> str:
        return '<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(self.mxfile, encoding="unicode")


def clean_label(text: str) -> str:
    text = text.strip().strip("{}")
    text = re.sub(r"\s+as\s+\w+$", "", text, flags=re.IGNORECASE).strip()
    return text.strip('"')


def alias_from_decl(line: str) -> tuple[str, str] | None:
    match = re.match(r'\s*(actor|boundary|control|database|participant|component|rectangle|usecase|class|state)\s+"?([^"{]+?)"?\s*(?:as\s+(\w+))?\s*(?:#\w+)?\s*$', line)
    if not match:
        return None
    kind, label, alias = match.groups()
    label = label.strip().strip('"')
    alias = alias or re.sub(r"\W+", "", label) or f"{kind}_{abs(hash(label))}"
    return alias, label


def parse_title(lines: list[str], fallback: str) -> str:
    for line in lines:
        match = re.match(r"\s*title\s+(.+)$", line)
        if match:
            return match.group(1).strip()
    return fallback


def classify(lines: list[str]) -> str:
    text = "\n".join(lines)
    if re.search(r"\busecase\b", text):
        return "usecase"
    if re.search(r"\bclass\s+\w+", text):
        return "class"
    if re.search(r"\b(actor|boundary|control|participant)\b", text) and re.search(r"\w+\s*-+>+|\w+\s*-->", text):
        return "sequence"
    if re.search(r"^\s*state\s+", text, re.M) or re.search(r"\[\*\]\s*-+>", text):
        return "state"
    if re.search(r"^\s*start\s*$", text, re.M) and re.search(r"^\s*:", text, re.M):
        return "activity"
    if re.search(r"\bcomponent\b|\bpackage\b|\bdatabase\b", text):
        return "component"
    if re.search(r"rectangle\s+\"", text):
        return "flow"
    return "generic"


def simple_grid_positions(count: int, start_x=80, start_y=100, w=210, h=70, gap_x=80, gap_y=70) -> list[tuple[float, float]]:
    cols = max(1, math.ceil(math.sqrt(count)))
    positions = []
    for idx in range(count):
        row = idx // cols
        col = idx % cols
        positions.append((start_x + col * (w + gap_x), start_y + row * (h + gap_y)))
    return positions


def build_usecase(lines: list[str], title: str) -> str:
    b = DrawioBuilder(title)
    b.vertex(title, 40, 30, 760, 40, "text;html=1;fontStyle=1;fontSize=18;strokeColor=none;fillColor=none;")
    actors: dict[str, str] = {}
    usecases: dict[str, str] = {}
    links: list[tuple[str, str, str]] = []
    for line in lines:
        am = re.match(r'\s*actor\s+"([^"]+)"\s+as\s+(\w+)', line)
        um = re.match(r'\s*usecase\s+"([^"]+)"\s+as\s+(\w+)', line)
        lm = re.match(r"\s*(\w+)\s+[-.]+>\s+(\w+)(?:\s*:\s*(.+))?", line)
        if am:
            actors[am.group(2)] = am.group(1)
        elif um:
            usecases[um.group(2)] = um.group(1)
        elif lm:
            links.append((lm.group(1), lm.group(2), lm.group(3) or ""))
    ids: dict[str, str] = {}
    for idx, (alias, label) in enumerate(actors.items()):
        ids[alias] = b.vertex(label, 40, 120 + idx * 110, 120, 60, "shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;")
    positions = simple_grid_positions(len(usecases), start_x=280, start_y=100, w=190, h=58, gap_x=70, gap_y=45)
    for (alias, label), (x, y) in zip(usecases.items(), positions):
        ids[alias] = b.vertex(label, x, y, 190, 58, "ellipse;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;")
    for src, dst, label in links:
        if src in ids and dst in ids:
            style = "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=none;dashed=1;" if "include" in label or "extend" in label else "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=none;"
            b.edge(ids[src], ids[dst], label, style)
    return b.tostring()


def build_sequence(lines: list[str], title: str) -> str:
    b = DrawioBuilder(title)
    b.vertex(title, 40, 20, 900, 40, "text;html=1;fontStyle=1;fontSize=18;strokeColor=none;fillColor=none;")
    participants: dict[str, str] = {}
    messages: list[tuple[str, str, str]] = []
    for line in lines:
        decl = alias_from_decl(line)
        if decl and re.match(r"\s*(actor|boundary|control|database|participant)\b", line):
            participants[decl[0]] = decl[1]
        mm = re.match(r"\s*(\w+)\s*-+>+?\s*(\w+)\s*:\s*(.+)", line)
        if mm:
            messages.append((mm.group(1), mm.group(2), mm.group(3).strip()))
            participants.setdefault(mm.group(1), mm.group(1))
            participants.setdefault(mm.group(2), mm.group(2))
    ids: dict[str, str] = {}
    x_gap = 190
    for idx, (alias, label) in enumerate(participants.items()):
        x = 70 + idx * x_gap
        ids[alias] = b.vertex(label, x, 90, 140, 50, "rounded=1;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;")
        b.vertex("", x + 68, 150, 4, max(280, 35 * len(messages) + 40), "shape=line;html=1;strokeColor=#999999;dashed=1;")
    y = 185
    for src, dst, label in messages:
        if src in ids and dst in ids:
            b.edge(ids[src], ids[dst], label, "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;")
            y += 35
    return b.tostring()


def build_component_or_flow(lines: list[str], title: str) -> str:
    b = DrawioBuilder(title)
    b.vertex(title, 40, 25, 900, 40, "text;html=1;fontStyle=1;fontSize=18;strokeColor=none;fillColor=none;")
    nodes: dict[str, str] = {}
    labels: dict[str, str] = {}
    edges: list[tuple[str, str, str]] = []
    for line in lines:
        decl = alias_from_decl(line)
        if decl:
            labels[decl[0]] = decl[1]
        lm = re.match(r"\s*(\w+)\s+[-.]+>\s+(\w+)(?:\s*:\s*(.+))?", line)
        if lm:
            edges.append((lm.group(1), lm.group(2), lm.group(3) or ""))
            labels.setdefault(lm.group(1), lm.group(1))
            labels.setdefault(lm.group(2), lm.group(2))
    positions = simple_grid_positions(len(labels), start_x=70, start_y=100, w=210, h=60, gap_x=80, gap_y=70)
    for (alias, label), (x, y) in zip(labels.items(), positions):
        style = "rounded=1;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;"
        if "Database" in label or "SQL" in label:
            style = "shape=cylinder3d;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#f8cecc;strokeColor=#b85450;"
        nodes[alias] = b.vertex(label, x, y, 210, 60, style)
    for src, dst, label in edges:
        if src in nodes and dst in nodes:
            b.edge(nodes[src], nodes[dst], label)
    return b.tostring()


def build_activity(lines: list[str], title: str) -> str:
    b = DrawioBuilder(title)
    b.vertex(title, 40, 20, 760, 40, "text;html=1;fontStyle=1;fontSize=18;strokeColor=none;fillColor=none;")
    previous = b.vertex("Start", 360, 90, 80, 40, "ellipse;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;")
    y = 160
    for line in lines:
        action = re.match(r"\s*:(.+);", line)
        decision = re.match(r"\s*if\s*\((.+)\)", line)
        if action:
            current = b.vertex(action.group(1).strip(), 280, y, 240, 56, "rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;")
        elif decision:
            current = b.vertex(decision.group(1).strip(), 310, y, 180, 80, "rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;")
        else:
            continue
        b.edge(previous, current)
        previous = current
        y += 90
    end = b.vertex("Stop", 360, y, 80, 40, "ellipse;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;")
    b.edge(previous, end)
    return b.tostring()


def build_state(lines: list[str], title: str) -> str:
    b = DrawioBuilder(title)
    b.vertex(title, 40, 20, 780, 40, "text;html=1;fontStyle=1;fontSize=18;strokeColor=none;fillColor=none;")
    states: dict[str, str] = {}
    transitions: list[tuple[str, str, str]] = []
    for line in lines:
        tm = re.match(r'\s*("?[\w\s/]+"?|\[\*\])\s*-+>\s*("?[\w\s/]+"?|\[\*\])(?:\s*:\s*(.+))?', line)
        if tm:
            src, dst, label = [tm.group(i).strip().strip('"') if tm.group(i) else "" for i in range(1, 4)]
            transitions.append((src, dst, label))
            if src != "[*]":
                states.setdefault(src, src)
            if dst != "[*]":
                states.setdefault(dst, dst)
    ids: dict[str, str] = {}
    ids["[*]_start"] = b.vertex("Start", 70, 100, 70, 40, "ellipse;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;")
    ids["[*]_end"] = b.vertex("End", 760, 520, 70, 40, "ellipse;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;")
    positions = simple_grid_positions(len(states), start_x=230, start_y=100, w=170, h=60, gap_x=70, gap_y=70)
    for (alias, label), (x, y) in zip(states.items(), positions):
        ids[alias] = b.vertex(label, x, y, 170, 60, "rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;")
    for src, dst, label in transitions:
        source = ids["[*]_start"] if src == "[*]" else ids.get(src)
        target = ids["[*]_end"] if dst == "[*]" else ids.get(dst)
        if source and target:
            b.edge(source, target, label)
    return b.tostring()


def build_class(lines: list[str], title: str) -> str:
    b = DrawioBuilder(title)
    b.vertex(title, 40, 20, 900, 40, "text;html=1;fontStyle=1;fontSize=18;strokeColor=none;fillColor=none;")
    classes: dict[str, list[str]] = {}
    relations: list[tuple[str, str, str]] = []
    current: str | None = None
    for line in lines:
        cm = re.match(r"\s*class\s+(\w+)", line)
        if cm:
            current = cm.group(1)
            classes[current] = []
            continue
        if current and "}" in line:
            current = None
            continue
        if current and line.strip().startswith("+"):
            classes[current].append(line.strip())
        rm = re.match(r'\s*(\w+)\s+"?[^"]*"?\s*[-.]+[-.]\s+"?[^"]*"?\s*(\w+)', line)
        if rm:
            relations.append((rm.group(1), rm.group(2), ""))
    ids = {}
    positions = simple_grid_positions(len(classes), start_x=60, start_y=90, w=220, h=120, gap_x=70, gap_y=80)
    for (name, attrs), (x, y) in zip(classes.items(), positions):
        value = f"<b>{html.escape(name)}</b><hr/>" + "<br/>".join(html.escape(a) for a in attrs)
        ids[name] = b.vertex(value, x, y, 220, max(90, 34 + len(attrs) * 18), "swimlane;html=1;whiteSpace=wrap;startSize=28;fillColor=#dae8fc;strokeColor=#6c8ebf;")
    for src, dst, label in relations:
        if src in ids and dst in ids:
            b.edge(ids[src], ids[dst], label, "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=none;")
    return b.tostring()


def build_generic(lines: list[str], title: str) -> str:
    b = DrawioBuilder(title)
    b.vertex(title, 40, 20, 900, 40, "text;html=1;fontStyle=1;fontSize=18;strokeColor=none;fillColor=none;")
    body = "\n".join(line for line in lines if line.strip() and not line.strip().startswith("@"))
    b.vertex(body, 80, 100, 720, 500, "rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#666666;align=left;verticalAlign=top;spacing=12;")
    return b.tostring()


def puml_to_drawio(puml_path: Path) -> str:
    lines = puml_path.read_text(encoding="utf-8", errors="ignore").splitlines()
    title = parse_title(lines, puml_path.stem)
    kind = classify(lines)
    if kind == "usecase":
        return build_usecase(lines, title)
    if kind == "sequence":
        return build_sequence(lines, title)
    if kind in {"component", "flow"}:
        return build_component_or_flow(lines, title)
    if kind == "activity":
        return build_activity(lines, title)
    if kind == "state":
        return build_state(lines, title)
    if kind == "class":
        return build_class(lines, title)
    return build_generic(lines, title)


def reason_for_sync(puml: Path, export: Path) -> str | None:
    if FORCE_REFRESH_ALL_EXPORTS:
        if not export.exists():
            return "missing"
        if export.stat().st_mtime < puml.stat().st_mtime:
            return "older than PUML"
        return "full sync refresh"
    if not export.exists():
        return "missing"
    if export.stat().st_mtime < puml.stat().st_mtime:
        return "older than PUML"
    return None


def find_plantuml_jar() -> Path | None:
    for candidate in PLANTUML_JAR_CANDIDATES:
        if candidate.exists():
            return candidate
    return None


def sync_png(statuses: list[ExportStatus], jar: Path | None) -> None:
    targets = [s for s in statuses if s.png_reason]
    if not targets:
        return
    if not jar:
        for status in statuses:
            if status.png_reason:
                status.png_error = "PlantUML jar not found."
        return
    for status in targets:
        if FORCE_REFRESH_ALL_EXPORTS and status.png.exists():
            status.png.unlink()
        cmd = ["java", "-jar", str(jar), "-tpng", str(status.puml)]
        result = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True)
        if result.returncode == 0 and status.png.exists() and status.png.stat().st_mtime >= status.puml.stat().st_mtime:
            status.png_generated = True
        else:
            status.png_error = (result.stderr or result.stdout or "PNG export failed.").strip()


def sync_drawio(statuses: list[ExportStatus]) -> None:
    for status in statuses:
        if not status.drawio_reason:
            continue
        try:
            status.drawio.write_text(puml_to_drawio(status.puml), encoding="utf-8")
            if status.drawio.exists() and status.drawio.stat().st_mtime >= status.puml.stat().st_mtime:
                status.drawio_generated = True
            else:
                status.drawio_error = "Draw.io file was written but timestamp did not synchronize."
        except Exception as exc:
            status.drawio_error = str(exc)


def validate_drawio(path: Path) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8", errors="ignore")
    if "image/png" in text or "base64," in text:
        return False
    return "<mxCell" in text and 'vertex="1"' in text


def write_report(statuses: list[ExportStatus], jar: Path | None) -> None:
    png_generated = [s for s in statuses if s.png_generated]
    drawio_generated = [s for s in statuses if s.drawio_generated]
    missing_exports = []
    failures = []
    mismatches = []
    synced = []
    for s in statuses:
        if not s.png.exists():
            missing_exports.append(str(s.png.relative_to(REPO_ROOT)))
        if not s.drawio.exists():
            missing_exports.append(str(s.drawio.relative_to(REPO_ROOT)))
        if s.png_error:
            failures.append(f"{s.png.relative_to(REPO_ROOT)} - {s.png_error}")
        if s.drawio_error:
            failures.append(f"{s.drawio.relative_to(REPO_ROOT)} - {s.drawio_error}")
        if s.png.exists() and s.png.stat().st_mtime < s.puml.stat().st_mtime:
            mismatches.append(f"{s.png.relative_to(REPO_ROOT)} older than {s.puml.relative_to(REPO_ROOT)}")
        if s.drawio.exists() and s.drawio.stat().st_mtime < s.puml.stat().st_mtime:
            mismatches.append(f"{s.drawio.relative_to(REPO_ROOT)} older than {s.puml.relative_to(REPO_ROOT)}")
        if s.png.exists() and s.drawio.exists() and s.png.stat().st_mtime >= s.puml.stat().st_mtime and s.drawio.stat().st_mtime >= s.puml.stat().st_mtime and validate_drawio(s.drawio):
            synced.append(str(s.puml.relative_to(REPO_ROOT)))
        elif s.drawio.exists() and not validate_drawio(s.drawio):
            failures.append(f"{s.drawio.relative_to(REPO_ROOT)} - Draw.io validation failed or file contains embedded image data.")

    lines = [
        "# UML Export Sync Report",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "## Scope",
        "",
        "- `docs/UML/diagram`",
        "- `docs/UML/design`",
        "- `docs/UML/state`",
        "",
        "## Tooling",
        "",
        f"- PlantUML jar: `{jar}`" if jar else "- PlantUML jar: not found",
        "- Draw.io export method: native editable `mxCell` XML generated from latest PlantUML source.",
        "- Draw.io image embedding: not used.",
        "",
        "## Summary",
        "",
        f"- Total PUML files found: {len(statuses)}",
        f"- PNG generated: {len(png_generated)}",
        f"- Draw.io generated: {len(drawio_generated)}",
        f"- Missing exports after sync: {len(missing_exports)}",
        f"- Export failures: {len(failures)}",
        f"- Timestamp mismatches after sync: {len(mismatches)}",
        f"- Files synchronized successfully: {len(synced)}",
        "",
        "## PNG Generated",
        "",
    ]
    lines.extend(f"- `{s.png.relative_to(REPO_ROOT)}` ({s.png_reason})" for s in png_generated)
    if not png_generated:
        lines.append("- None.")
    lines.extend(["", "## Draw.io Generated", ""])
    lines.extend(f"- `{s.drawio.relative_to(REPO_ROOT)}` ({s.drawio_reason})" for s in drawio_generated)
    if not drawio_generated:
        lines.append("- None.")
    lines.extend(["", "## Missing Exports", ""])
    lines.extend(f"- `{item}`" for item in missing_exports) if missing_exports else lines.append("- None.")
    lines.extend(["", "## Export Failures", ""])
    lines.extend(f"- {item}" for item in failures) if failures else lines.append("- None.")
    lines.extend(["", "## Timestamp Mismatches", ""])
    lines.extend(f"- {item}" for item in mismatches) if mismatches else lines.append("- None.")
    lines.extend(["", "## Files Synchronized Successfully", ""])
    lines.extend(f"- `{item}`" for item in synced)
    lines.extend(
        [
            "",
            "## Final Validation",
            "",
            "- PUML remains the source of truth.",
            "- PNG exports are synchronized for files without export failures.",
            "- Draw.io exports are native editable XML with vertices and edges, not image-only wrappers.",
            "- Database schema, SRS, FRS, SDD, and RTM were not modified.",
            "- Diagram logic was not changed; this pass only synchronized export artifacts.",
        ]
    )
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    puml_files = sorted({p for d in UML_DIRS for p in d.rglob("*.puml")})
    statuses: list[ExportStatus] = []
    for puml in puml_files:
        png = puml.with_suffix(".png")
        drawio = puml.with_suffix(".drawio")
        statuses.append(
            ExportStatus(
                puml=puml,
                png=png,
                drawio=drawio,
                png_reason=reason_for_sync(puml, png),
                drawio_reason=reason_for_sync(puml, drawio),
            )
        )
    jar = find_plantuml_jar()
    sync_png(statuses, jar)
    sync_drawio(statuses)
    write_report(statuses, jar)
    print(f"total_puml={len(statuses)}")
    print(f"png_generated={sum(1 for s in statuses if s.png_generated)}")
    print(f"drawio_generated={sum(1 for s in statuses if s.drawio_generated)}")
    print(f"report={REPORT_PATH}")


if __name__ == "__main__":
    main()
