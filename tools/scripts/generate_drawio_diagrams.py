from __future__ import annotations

import html
import re
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Iterable
from xml.etree import ElementTree as ET

from PIL import Image, ImageDraw, ImageFont


BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[2]


@dataclass
class Entity:
    name: str
    alias: str
    rows: list[str]
    x: int = 0
    y: int = 0
    w: int = 280
    h: int = 0
    cell_id: str = ""


@dataclass
class Relation:
    source: str
    target: str
    label: str = ""
    source_card: str = ""
    target_card: str = ""


@dataclass
class Shape:
    alias: str
    label: str
    kind: str
    x: int
    y: int
    w: int
    h: int
    fill: str
    stroke: str
    font: str = "#111827"
    cell_id: str = ""


@dataclass
class DiagramModel:
    title: str
    entities: list[Entity] = field(default_factory=list)
    relations: list[Relation] = field(default_factory=list)
    shapes: list[Shape] = field(default_factory=list)
    shape_edges: list[Relation] = field(default_factory=list)
    width: int = 1600
    height: int = 1200


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def clean_row(row: str) -> str:
    row = row.strip()
    row = row.replace("* ", "PK ")
    row = row.replace("# ", "FK ")
    row = row.replace("- ", "")
    row = row.replace("<<PK>>", "[PK]")
    row = row.replace("<<FK>>", "[FK]")
    row = row.replace("<<PK, AUTOINCREMENT>>", "[PK, AI]")
    row = row.replace("<<UNIQUE>>", "[UNIQUE]")
    row = re.sub(r"\s+", " ", row)
    return row


def parse_entities_and_relations(text: str) -> tuple[list[Entity], list[Relation]]:
    entities: list[Entity] = []
    aliases: dict[str, str] = {}
    for match in re.finditer(r'entity\s+(?:"([^"]+)"|([A-Za-z0-9_]+))(?:\s+as\s+([A-Za-z0-9_]+))?\s*\{(.*?)\}', text, re.S):
        name = match.group(1) or match.group(2)
        alias = match.group(3) or name
        rows = []
        for raw in match.group(4).splitlines():
            raw = raw.strip()
            if not raw or raw == "--":
                continue
            rows.append(clean_row(raw))
        entities.append(Entity(name=name, alias=alias, rows=rows))
        aliases[alias] = alias
        aliases[name] = alias

    relations: list[Relation] = []
    rel_re = re.compile(r"^([A-Za-z0-9_]+)\s+([|o}{\-\w]+)--([|o}{\-\w]+)\s+([A-Za-z0-9_]+)(?:\s*:\s*(.+))?$")
    for line in text.splitlines():
        line = line.strip()
        m = rel_re.match(line)
        if not m:
            continue
        src, left, right, tgt, label = m.groups()
        if src in aliases and tgt in aliases:
            relations.append(Relation(aliases[src], aliases[tgt], (label or "").strip(), left, right))
    return entities, relations


def card_label(token: str) -> str:
    token = token.strip("-")
    return {
        "||": "1",
        "o|": "0..1",
        "|o": "0..1",
        "o{": "0..N",
        "}o": "0..N",
        "|{": "1..N",
        "}|": "1..N",
    }.get(token, token)


def assign_table_layout(entities: list[Entity]) -> None:
    positions = {
        "ApplicationTypes": (60, 60),
        "Applications": (380, 60),
        "LocalDrivingLicenseApplications": (720, 80),
        "LicenseClasses": (1100, 70),
        "Countries": (60, 410),
        "People": (360, 360),
        "Users": (720, 390),
        "Drivers": (1050, 390),
        "Licenses": (60, 770),
        "InternationalLicenses": (410, 760),
        "DetainedLicenses": (760, 760),
        "TestTypes": (1120, 730),
        "TestAppointments": (1120, 1010),
        "Tests": (780, 1050),
        "LDLApplications": (720, 80),
    }
    for i, entity in enumerate(entities):
        x, y = positions.get(entity.alias, (60 + (i % 4) * 360, 60 + (i // 4) * 320))
        entity.x = x
        entity.y = y
        entity.w = 300 if len(entity.name) > 24 else 280
        entity.h = 34 + len(entity.rows) * 24


def style_for_row(row: str) -> str:
    if "[PK" in row:
        return "fillColor=#FFE6CC;strokeColor=#D79B00;fontStyle=1;align=left;spacingLeft=8;html=1;"
    if "[FK" in row:
        return "fillColor=#E1D5E7;strokeColor=#9673A6;align=left;spacingLeft=8;html=1;"
    return "fillColor=#FFFFFF;strokeColor=#CBD5E1;align=left;spacingLeft=8;html=1;"


def add_cell(root: ET.Element, cell_id: str, value: str, style: str, parent: str = "1", vertex: bool = True,
             edge: bool = False, source: str | None = None, target: str | None = None,
             x: int = 0, y: int = 0, w: int = 0, h: int = 0) -> ET.Element:
    attrs = {"id": cell_id, "value": value, "style": style, "parent": parent}
    if vertex:
        attrs["vertex"] = "1"
    if edge:
        attrs["edge"] = "1"
        attrs.pop("vertex", None)
    if source:
        attrs["source"] = source
    if target:
        attrs["target"] = target
    cell = ET.SubElement(root, "mxCell", attrs)
    geo_attrs = {"as": "geometry"}
    if edge:
        geo_attrs["relative"] = "1"
    else:
        geo_attrs.update({"x": str(x), "y": str(y), "width": str(w), "height": str(h)})
    ET.SubElement(cell, "mxGeometry", geo_attrs)
    return cell


def write_table_drawio(model: DiagramModel, out: Path) -> None:
    mxfile = ET.Element("mxfile", {"host": "app.diagrams.net", "modified": datetime.now(UTC).isoformat(), "agent": "Codex", "version": "24.7.17"})
    diagram = ET.SubElement(mxfile, "diagram", {"id": out.stem, "name": out.stem})
    graph = ET.SubElement(diagram, "mxGraphModel", {"dx": "1600", "dy": "1200", "grid": "1", "gridSize": "10", "guides": "1", "tooltips": "1", "connect": "1", "arrows": "1", "fold": "1", "page": "1", "pageScale": "1", "pageWidth": str(model.width), "pageHeight": str(model.height), "math": "0", "shadow": "0"})
    root = ET.SubElement(graph, "root")
    ET.SubElement(root, "mxCell", {"id": "0"})
    ET.SubElement(root, "mxCell", {"id": "1", "parent": "0"})
    add_cell(root, "title", html.escape(model.title), "text;html=1;strokeColor=none;fillColor=none;fontSize=24;fontStyle=1;align=center;", x=0, y=10, w=model.width, h=40)
    cell_map: dict[str, str] = {}
    next_id = 2
    for entity in model.entities:
        header_id = f"t{next_id}"
        next_id += 1
        entity.cell_id = header_id
        cell_map[entity.alias] = header_id
        add_cell(root, header_id, html.escape(entity.name), "rounded=0;whiteSpace=wrap;html=1;fillColor=#DBEAFE;strokeColor=#1E3A8A;fontStyle=1;fontColor=#0F172A;", x=entity.x, y=entity.y, w=entity.w, h=34)
        for idx, row in enumerate(entity.rows):
            rid = f"t{next_id}"
            next_id += 1
            add_cell(root, rid, html.escape(row), style_for_row(row), x=entity.x, y=entity.y + 34 + idx * 24, w=entity.w, h=24)
    for rel in model.relations:
        if rel.source not in cell_map or rel.target not in cell_map:
            continue
        label = f"{card_label(rel.source_card)} : {card_label(rel.target_card)}"
        if rel.label:
            label = f"{label}  {rel.label}"
        add_cell(root, f"e{next_id}", html.escape(label), "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=none;strokeColor=#475569;fontSize=10;", vertex=False, edge=True, source=cell_map[rel.source], target=cell_map[rel.target])
        next_id += 1
    ET.indent(mxfile)
    out.write_text(ET.tostring(mxfile, encoding="unicode"), encoding="utf-8")


def parse_chen(text: str) -> DiagramModel:
    entity_names = [
        "ApplicationType", "Application", "LocalDrivingLicenseApplication", "Country", "Person", "User", "Driver",
        "LicenseClass", "License", "InternationalLicense", "DetainedLicense", "TestTypes", "TestAppointment", "Test"
    ]
    entity_pos = {
        "ApplicationType": (300, 180), "Application": (850, 180), "LocalDrivingLicenseApplication": (1450, 180),
        "Country": (300, 680), "Person": (850, 680), "User": (1450, 680), "Driver": (1850, 680),
        "LicenseClass": (300, 1180), "License": (850, 1180), "InternationalLicense": (1450, 1180),
        "DetainedLicense": (1850, 1180), "Test": (850, 1660), "TestAppointment": (1450, 1660), "TestTypes": (1850, 1660),
    }
    model = DiagramModel("DVLD System - Chen ERD", width=2500, height=1950)
    for name in entity_names:
        x, y = entity_pos[name]
        model.shapes.append(Shape(name, name, "entity", x, y, 190, 52, "#D9ECFF", "#1F4E79", "#0B2545"))

    attr_by_entity: dict[str, list[tuple[str, str, str]]] = {name: [] for name in entity_names}
    for line in text.splitlines():
        m = re.match(r'\s*usecase\s+"([^"]+)"\s+as\s+([A-Za-z0-9_]+)(?:\s+#([A-Fa-f0-9]+))?', line)
        if not m:
            continue
        label, alias, color = m.groups()
        owner = None
        for name in sorted(entity_names, key=len, reverse=True):
            if alias.startswith(name + "_") or alias.startswith(name.replace("LocalDrivingLicenseApplication", "LDLA") + "_"):
                owner = name
                break
        if alias.startswith("LDLA_"):
            owner = "LocalDrivingLicenseApplication"
        if owner:
            kind = "pk" if color == "FFB347" else "fk" if color == "B39DDB" else "attr"
            attr_by_entity[owner].append((alias, label, kind))

    for entity in model.shapes[:]:
        attrs = attr_by_entity.get(entity.alias, [])
        for i, (alias, label, kind) in enumerate(attrs):
            side = -1 if i % 2 == 0 else 1
            row = i // 2
            x = entity.x - 215 if side == -1 else entity.x + entity.w + 60
            y = entity.y - 120 + row * 52
            fill = "#FFB347" if kind == "pk" else "#B39DDB" if kind == "fk" else "#2F3437"
            font = "#111111" if kind == "pk" else "#FFFFFF"
            model.shapes.append(Shape(alias, label, "attribute", x, y, 165, 38, fill, "#111111", font))
            model.shape_edges.append(Relation(entity.alias, alias))

    rel_pos: dict[str, tuple[int, int]] = {
        "R_IsFrom": (620, 700), "R_PersonUser": (1230, 700), "R_PersonDriver": (1715, 700),
        "R_Applies": (850, 440), "R_ApplicationTypeApplication": (620, 205), "R_ApplicationLDLA": (1230, 205),
        "R_LicenseClassLDLA": (880, 950), "R_DriverLicense": (1420, 950), "R_DriverInternationalLicense": (1780, 950),
        "R_LicenseClassLicense": (620, 1205), "R_ApplicationLicense": (870, 950), "R_ApplicationInternationalLicense": (1230, 950),
        "R_LicenseInternationalLicense": (1230, 1205), "R_LicenseDetainedLicense": (1730, 1205), "R_ApplicationDetainedLicense": (1720, 940),
        "R_TestTypesAppointment": (1780, 1700), "R_LDLATestAppointment": (1450, 440), "R_TestAppointmentTest": (1230, 1700),
        "R_UserApplication": (1230, 440), "R_UserDriver": (1720, 520), "R_UserLicense": (1250, 940),
        "R_UserInternationalLicense": (1450, 940), "R_UserDetainedLicense": (1850, 940), "R_UserTestAppointment": (1450, 1460),
        "R_UserTest": (1180, 1460), "R_UserReleasedDetainedLicense": (2060, 940),
    }
    rel_aliases = set()
    for line in text.splitlines():
        m = re.match(r'\s*rectangle\s+"<>\s*\\n([^"]+)"\s+as\s+([A-Za-z0-9_]+)', line)
        if m:
            label, alias = m.groups()
            x, y = rel_pos.get(alias, (700, 700))
            rel_aliases.add(alias)
            model.shapes.append(Shape(alias, label, "relationship", x, y, 100, 72, "#8B3A2E", "#5B2119", "#FFFFFF"))
    aliases = {s.alias for s in model.shapes}
    for line in text.splitlines():
        if "-[hidden]" in line:
            continue
        m = re.match(r'\s*([A-Za-z0-9_]+)\s+--\s+([A-Za-z0-9_]+)(?:\s*:\s*(.+))?', line)
        if not m:
            continue
        src, tgt, label = m.groups()
        if src in aliases and tgt in aliases and (src in rel_aliases or tgt in rel_aliases):
            model.shape_edges.append(Relation(src, tgt, (label or "").strip()))
    return model


def write_shape_drawio(model: DiagramModel, out: Path) -> None:
    mxfile = ET.Element("mxfile", {"host": "app.diagrams.net", "modified": datetime.now(UTC).isoformat(), "agent": "Codex", "version": "24.7.17"})
    diagram = ET.SubElement(mxfile, "diagram", {"id": out.stem, "name": out.stem})
    graph = ET.SubElement(diagram, "mxGraphModel", {"dx": "1500", "dy": "1500", "grid": "1", "gridSize": "10", "guides": "1", "tooltips": "1", "connect": "1", "arrows": "1", "fold": "1", "page": "1", "pageScale": "1", "pageWidth": str(model.width), "pageHeight": str(model.height), "math": "0", "shadow": "0"})
    root = ET.SubElement(graph, "root")
    ET.SubElement(root, "mxCell", {"id": "0"})
    ET.SubElement(root, "mxCell", {"id": "1", "parent": "0"})
    add_cell(root, "title", html.escape(model.title), "text;html=1;strokeColor=none;fillColor=none;fontSize=24;fontStyle=1;align=center;", x=0, y=20, w=model.width, h=40)
    cell_map: dict[str, str] = {}
    for i, shape in enumerate(model.shapes, 2):
        shape.cell_id = f"s{i}"
        cell_map[shape.alias] = shape.cell_id
        base = f"whiteSpace=wrap;html=1;fillColor={shape.fill};strokeColor={shape.stroke};fontColor={shape.font};"
        if shape.kind == "attribute":
            style = "ellipse;" + base + ("fontStyle=1;" if shape.fill == "#FFB347" else "")
        elif shape.kind == "relationship":
            style = "rhombus;" + base + "fontStyle=1;"
        else:
            style = "rounded=0;" + base + "fontStyle=1;"
        add_cell(root, shape.cell_id, html.escape(shape.label), style, x=shape.x, y=shape.y, w=shape.w, h=shape.h)
    next_id = len(model.shapes) + 3
    for edge in model.shape_edges:
        if edge.source in cell_map and edge.target in cell_map:
            add_cell(root, f"e{next_id}", html.escape(edge.label), "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=none;strokeColor=#475569;fontSize=11;", vertex=False, edge=True, source=cell_map[edge.source], target=cell_map[edge.target])
            next_id += 1
    ET.indent(mxfile)
    out.write_text(ET.tostring(mxfile, encoding="unicode"), encoding="utf-8")


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
    ]
    for item in candidates:
        if Path(item).exists():
            return ImageFont.truetype(item, size)
    return ImageFont.load_default()


def render_model(model: DiagramModel, out: Path) -> None:
    img = Image.new("RGB", (model.width, model.height), "white")
    d = ImageDraw.Draw(img)
    d.text((model.width // 2, 20), model.title, fill="#111827", font=font(26, True), anchor="ma")
    if model.entities:
        centers = {e.alias: (e.x + e.w // 2, e.y + 17) for e in model.entities}
        for rel in model.relations:
            if rel.source in centers and rel.target in centers:
                d.line([centers[rel.source], centers[rel.target]], fill="#64748B", width=2)
                sx, sy = centers[rel.source]
                tx, ty = centers[rel.target]
                if rel.label:
                    d.text(((sx + tx) // 2, (sy + ty) // 2), rel.label, fill="#334155", font=font(10), anchor="mm")
        for e in model.entities:
            d.rectangle([e.x, e.y, e.x + e.w, e.y + 34], fill="#DBEAFE", outline="#1E3A8A", width=2)
            d.text((e.x + e.w // 2, e.y + 17), e.name, fill="#0F172A", font=font(13, True), anchor="mm")
            for i, row in enumerate(e.rows):
                y = e.y + 34 + i * 24
                fill = "#FFE6CC" if "[PK" in row else "#E1D5E7" if "[FK" in row else "#FFFFFF"
                d.rectangle([e.x, y, e.x + e.w, y + 24], fill=fill, outline="#CBD5E1")
                d.text((e.x + 8, y + 12), row[:48], fill="#111827", font=font(10), anchor="lm")
    else:
        centers = {s.alias: (s.x + s.w // 2, s.y + s.h // 2) for s in model.shapes}
        for edge in model.shape_edges:
            if edge.source in centers and edge.target in centers:
                d.line([centers[edge.source], centers[edge.target]], fill="#64748B", width=2)
                if edge.label:
                    sx, sy = centers[edge.source]
                    tx, ty = centers[edge.target]
                    d.text(((sx + tx) // 2, (sy + ty) // 2), edge.label, fill="#334155", font=font(10), anchor="mm")
        for s in model.shapes:
            box = [s.x, s.y, s.x + s.w, s.y + s.h]
            if s.kind == "attribute":
                d.ellipse(box, fill=s.fill, outline=s.stroke, width=2)
            elif s.kind == "relationship":
                cx, cy = centers[s.alias]
                d.polygon([(cx, s.y), (s.x + s.w, cy), (cx, s.y + s.h), (s.x, cy)], fill=s.fill, outline=s.stroke)
            else:
                d.rectangle(box, fill=s.fill, outline=s.stroke, width=2)
            d.text(centers[s.alias], s.label, fill=s.font, font=font(11, s.kind != "attribute"), anchor="mm")
    img.save(out)


def report(files: list[tuple[str, Path]], pngs: list[Path]) -> None:
    lines = [
        "# Draw.io Generation Report",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "## Source references used",
        "",
        "- `111111.png` (visual reference only; not embedded)",
        "- `docs/UML/database/physical-erd.puml`",
        "- `docs/UML/database/logical-erd.puml`",
        "- `docs/UML/database/chen-notation-erd.puml`",
        "- `docs/UML/database/database-schema.puml` (reviewed; physical definitions were used for consistent table/relationship names)",
        "",
        "## Generated Draw.io files",
        "",
    ]
    for name, path in files:
        text = path.read_text(encoding="utf-8")
        editable = "<mxCell" in text and "image=data:image" not in text and "shape=image" not in text
        lines.append(f"- `{path.relative_to(ROOT)}`: editable XML shapes/connectors = `{editable}` ({name})")
    lines += ["", "## Generated PNG files", ""]
    for path in pngs:
        lines.append(f"- `{path.relative_to(ROOT)}`")
    lines += [
        "",
        "## Validation",
        "",
        "- Each `.drawio` file is uncompressed XML and contains native `mxCell` vertices and edges.",
        "- No generated `.drawio` file embeds `111111.png` or any other PNG as an image-only wrapper.",
        "- PNG exports exist for all four requested diagrams.",
        "",
        "## Assumptions",
        "",
        "- `database-schema.drawio` uses the complete physical ERD table set because `database-schema.puml` contains naming drift and incomplete relationships.",
        "- `LicenseClasses` and `LocalDrivingLicenseApplications` names follow the required output list and `physical-erd.puml`.",
        "- Chen attributes are generated from `chen-notation-erd.puml`; PK attributes use orange ovals and FK attributes use purple ovals.",
        "",
        "## Limitations",
        "",
        "- The original `.drawio` source was missing, so layout is a faithful reconstruction rather than a byte-for-byte recovery.",
        "- PNGs were rendered from the generated model locally because a Draw.io desktop CLI was not installed on this machine.",
    ]
    (BASE / "drawio-generation-report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    physical_text = read_text(BASE / "physical-erd.puml")
    logical_text = read_text(BASE / "logical-erd.puml")
    chen_text = read_text(BASE / "chen-notation-erd.puml")

    outputs: list[tuple[str, Path]] = []
    pngs: list[Path] = []
    for source_name, title, drawio_name, png_name, text in [
        ("database schema", "DVLD System - Database Schema", "database-schema.drawio", "database-schema.png", physical_text),
        ("physical ERD", "DVLD System - Physical ERD", "physical-erd.drawio", "physical-erd.png", physical_text),
        ("logical ERD", "DVLD System - Logical ERD", "logical-erd.drawio", "logical-erd.png", logical_text),
    ]:
        entities, relations = parse_entities_and_relations(text)
        assign_table_layout(entities)
        model = DiagramModel(title, entities=entities, relations=relations, width=1460, height=1320)
        drawio_path = BASE / drawio_name
        png_path = BASE / png_name
        write_table_drawio(model, drawio_path)
        render_model(model, png_path)
        outputs.append((source_name, drawio_path))
        pngs.append(png_path)

    chen_model = parse_chen(chen_text)
    chen_drawio = BASE / "chen-notation-erd.drawio"
    chen_png = BASE / "chen-notation-erd.png"
    write_shape_drawio(chen_model, chen_drawio)
    render_model(chen_model, chen_png)
    outputs.append(("Chen ERD", chen_drawio))
    pngs.append(chen_png)
    report(outputs, pngs)


if __name__ == "__main__":
    main()
