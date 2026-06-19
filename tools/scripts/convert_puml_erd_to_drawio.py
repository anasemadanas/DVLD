from __future__ import annotations

import argparse
import html
import re
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from xml.etree import ElementTree as ET


try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:  # pragma: no cover - handled in the report.
    Image = None
    ImageDraw = None
    ImageFont = None


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SOURCE = REPO_ROOT / "docs" / "UML" / "database" / "dvld-erd.puml"
DEFAULT_DRAWIO = REPO_ROOT / "docs" / "UML" / "database" / "dvld-erd.drawio"
DEFAULT_PNG = REPO_ROOT / "docs" / "UML" / "database" / "dvld-erd.png"
DEFAULT_REPORT = REPO_ROOT / "docs" / "UML" / "database" / "dvld-erd-conversion-report.md"


@dataclass
class Column:
    name: str
    data_type: str
    is_pk: bool = False
    is_fk: bool = False

    @property
    def label(self) -> str:
        prefix = "PK " if self.is_pk else "FK " if self.is_fk else ""
        suffix = " [PK]" if self.is_pk else " [FK]" if self.is_fk else ""
        return f"{prefix}{self.name} : {self.data_type}{suffix}"


@dataclass
class Entity:
    name: str
    alias: str
    columns: list[Column]
    x: int = 0
    y: int = 0
    width: int = 310
    height: int = 0
    header_id: str = ""


@dataclass
class Relationship:
    source: str
    source_cardinality: str
    target_cardinality: str
    target: str
    label: str = ""

    @property
    def cardinality_label(self) -> str:
        left = cardinality_text(self.source_cardinality)
        right = cardinality_text(self.target_cardinality)
        base = f"{left} : {right}"
        return f"{base} {self.label}".strip()


def cardinality_text(token: str) -> str:
    cleaned = token.replace("-", "")
    return {
        "||": "1",
        "o|": "0..1",
        "|o": "0..1",
        "o{": "0..N",
        "}o": "0..N",
        "|{": "1..N",
        "}|": "1..N",
    }.get(cleaned, cleaned)


def parse_column(line: str) -> Column | None:
    raw = line.strip()
    if not raw or raw == "--" or raw.startswith("'"):
        return None

    is_pk = raw.startswith("*") or "<<PK>>" in raw or "<<PK" in raw
    is_fk = "<<FK>>" in raw or "<<FK" in raw
    raw = raw.lstrip("*").strip()
    raw = re.sub(r"<<[^>]+>>", "", raw).strip()

    match = re.match(r"([^:]+?)\s*:\s*(.+)$", raw)
    if not match:
        return Column(raw, "", is_pk=is_pk, is_fk=is_fk)

    return Column(
        name=match.group(1).strip(),
        data_type=match.group(2).strip(),
        is_pk=is_pk,
        is_fk=is_fk,
    )


def parse_puml(source: Path) -> tuple[str, list[Entity], list[Relationship]]:
    text = source.read_text(encoding="utf-8")
    title_match = re.search(r"^\s*title\s+(.+)$", text, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "PlantUML ERD"

    entities: list[Entity] = []
    alias_lookup: dict[str, str] = {}
    entity_pattern = re.compile(
        r'entity\s+(?:"([^"]+)"|([A-Za-z_][\w]*))(?:\s+as\s+([A-Za-z_][\w]*))?\s*\{(.*?)\}',
        re.DOTALL,
    )
    for match in entity_pattern.finditer(text):
        name = match.group(1) or match.group(2)
        alias = match.group(3) or name
        columns = [column for line in match.group(4).splitlines() if (column := parse_column(line))]
        entity = Entity(name=name, alias=alias, columns=columns)
        entity.height = 38 + len(columns) * 26
        entity.width = max(300, min(420, 130 + max((len(column.label) for column in columns), default=len(name)) * 7))
        entities.append(entity)
        alias_lookup[alias] = alias
        alias_lookup[name] = alias

    relationships: list[Relationship] = []
    relation_pattern = re.compile(
        r"^\s*([A-Za-z_][\w]*)\s+([|o}{]+)--([|o}{]+)\s+([A-Za-z_][\w]*)(?:\s*:\s*(.+?))?\s*$",
        re.MULTILINE,
    )
    for match in relation_pattern.finditer(text):
        source, source_cardinality, target_cardinality, target, label = match.groups()
        if source not in alias_lookup or target not in alias_lookup:
            continue
        relationships.append(
            Relationship(
                source=alias_lookup[source],
                source_cardinality=source_cardinality,
                target_cardinality=target_cardinality,
                target=alias_lookup[target],
                label=(label or "").strip(),
            )
        )

    return title, entities, relationships


def apply_layout(entities: list[Entity]) -> None:
    positions = {
        "Countries": (70, 80),
        "ApplicationTypes": (470, 80),
        "LicenseClasses": (870, 80),
        "People": (470, 390),
        "Users": (850, 410),
        "Drivers": (1230, 410),
        "Applications": (70, 390),
        "LDLApplications": (70, 720),
        "Licenses": (470, 760),
        "InternationalLicenses": (850, 760),
        "DetainedLicenses": (1230, 760),
        "TestTypes": (1230, 80),
        "TestAppointments": (1230, 1130),
        "Tests": (850, 1130),
    }
    for index, entity in enumerate(entities):
        entity.x, entity.y = positions.get(entity.alias, (70 + (index % 4) * 390, 80 + (index // 4) * 330))


def make_cell(
    root: ET.Element,
    cell_id: str,
    value: str,
    style: str,
    *,
    parent: str = "1",
    vertex: bool = True,
    edge: bool = False,
    source: str | None = None,
    target: str | None = None,
    x: int = 0,
    y: int = 0,
    width: int = 0,
    height: int = 0,
) -> ET.Element:
    attributes = {"id": cell_id, "value": value, "style": style, "parent": parent}
    if vertex:
        attributes["vertex"] = "1"
    if edge:
        attributes.pop("vertex", None)
        attributes["edge"] = "1"
    if source:
        attributes["source"] = source
    if target:
        attributes["target"] = target

    cell = ET.SubElement(root, "mxCell", attributes)
    geometry = {"as": "geometry"}
    if edge:
        geometry["relative"] = "1"
    else:
        geometry.update({"x": str(x), "y": str(y), "width": str(width), "height": str(height)})
    ET.SubElement(cell, "mxGeometry", geometry)
    return cell


def column_style(column: Column) -> str:
    base = "rounded=0;whiteSpace=wrap;html=1;align=left;verticalAlign=middle;spacingLeft=8;"
    if column.is_pk:
        return base + "fillColor=#EAF2FF;strokeColor=#CBD5E1;fontStyle=1;fontColor=#111827;"
    if column.is_fk:
        return base + "fillColor=#F8FAFC;strokeColor=#CBD5E1;fontStyle=2;fontColor=#111827;"
    return base + "fillColor=#FFFFFF;strokeColor=#CBD5E1;fontColor=#111827;"


def write_drawio(title: str, entities: list[Entity], relationships: list[Relationship], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    mxfile = ET.Element(
        "mxfile",
        {
            "host": "app.diagrams.net",
            "modified": datetime.now(UTC).isoformat(),
            "agent": "Codex PlantUML ERD converter",
            "version": "24.7.17",
        },
    )
    diagram = ET.SubElement(mxfile, "diagram", {"id": "dvld-erd", "name": "dvld-erd"})
    graph = ET.SubElement(
        diagram,
        "mxGraphModel",
        {
            "dx": "1600",
            "dy": "1400",
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
            "pageHeight": "1450",
            "math": "0",
            "shadow": "0",
        },
    )
    root = ET.SubElement(graph, "root")
    ET.SubElement(root, "mxCell", {"id": "0"})
    ET.SubElement(root, "mxCell", {"id": "1", "parent": "0"})
    make_cell(
        root,
        "title",
        html.escape(title),
        "text;html=1;strokeColor=none;fillColor=none;fontSize=24;fontStyle=1;align=center;verticalAlign=middle;",
        x=0,
        y=20,
        width=1600,
        height=40,
    )

    entity_ids: dict[str, str] = {}
    next_id = 2
    for entity in entities:
        header_id = f"entity_{next_id}"
        next_id += 1
        entity.header_id = header_id
        entity_ids[entity.alias] = header_id
        make_cell(
            root,
            header_id,
            html.escape(entity.name),
            "rounded=0;whiteSpace=wrap;html=1;fillColor=#1E3A8A;strokeColor=#0F172A;fontColor=#FFFFFF;fontStyle=1;align=center;verticalAlign=middle;",
            x=entity.x,
            y=entity.y,
            width=entity.width,
            height=38,
        )
        for row_index, column in enumerate(entity.columns):
            make_cell(
                root,
                f"column_{next_id}",
                html.escape(column.label),
                column_style(column),
                x=entity.x,
                y=entity.y + 38 + row_index * 26,
                width=entity.width,
                height=26,
            )
            next_id += 1

    edge_style = (
        "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;"
        "endArrow=none;strokeColor=#334155;fontColor=#334155;fontSize=10;"
    )
    for relationship in relationships:
        if relationship.source not in entity_ids or relationship.target not in entity_ids:
            continue
        make_cell(
            root,
            f"rel_{next_id}",
            html.escape(relationship.cardinality_label),
            edge_style,
            vertex=False,
            edge=True,
            source=entity_ids[relationship.source],
            target=entity_ids[relationship.target],
        )
        next_id += 1

    ET.indent(mxfile)
    output.write_text(ET.tostring(mxfile, encoding="unicode"), encoding="utf-8")


def font(size: int, bold: bool = False):
    if ImageFont is None:
        return None
    font_paths = [
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
    ]
    for font_path in font_paths:
        if Path(font_path).exists():
            return ImageFont.truetype(font_path, size)
    return ImageFont.load_default()


def render_png(title: str, entities: list[Entity], relationships: list[Relationship], output: Path) -> tuple[bool, str]:
    if Image is None or ImageDraw is None:
        return False, "Pillow is not installed; PNG rendering skipped."

    output.parent.mkdir(parents=True, exist_ok=True)
    image = Image.new("RGB", (1600, 1450), "white")
    draw = ImageDraw.Draw(image)
    draw.text((800, 40), title, fill="#111827", font=font(26, True), anchor="mm")

    centers = {entity.alias: (entity.x + entity.width // 2, entity.y + 19) for entity in entities}
    for relationship in relationships:
        if relationship.source not in centers or relationship.target not in centers:
            continue
        source = centers[relationship.source]
        target = centers[relationship.target]
        midpoint = ((source[0] + target[0]) // 2, (source[1] + target[1]) // 2)
        draw.line([source, target], fill="#64748B", width=2)
        draw.rectangle([midpoint[0] - 30, midpoint[1] - 9, midpoint[0] + 30, midpoint[1] + 9], fill="white")
        draw.text(midpoint, relationship.cardinality_label[:18], fill="#334155", font=font(10), anchor="mm")

    for entity in entities:
        draw.rectangle([entity.x, entity.y, entity.x + entity.width, entity.y + 38], fill="#1E3A8A", outline="#0F172A", width=2)
        draw.text((entity.x + entity.width // 2, entity.y + 19), entity.name, fill="white", font=font(13, True), anchor="mm")
        for index, column in enumerate(entity.columns):
            y = entity.y + 38 + index * 26
            fill = "#EAF2FF" if column.is_pk else "#F8FAFC" if column.is_fk else "#FFFFFF"
            draw.rectangle([entity.x, y, entity.x + entity.width, y + 26], fill=fill, outline="#CBD5E1")
            draw.text((entity.x + 8, y + 13), column.label[:58], fill="#111827", font=font(10, column.is_pk), anchor="lm")

    image.save(output)
    return True, "PNG generated with Pillow from the parsed editable diagram model."


def validate_drawio(drawio_path: Path, entities: list[Entity], relationships: list[Relationship]) -> dict[str, object]:
    text = drawio_path.read_text(encoding="utf-8") if drawio_path.exists() else ""
    parsed = ET.parse(drawio_path).getroot() if drawio_path.exists() else None
    cells = parsed.findall(".//mxCell") if parsed is not None else []
    vertices = sum(1 for cell in cells if cell.get("vertex") == "1")
    edges = sum(1 for cell in cells if cell.get("edge") == "1")
    missing_tables = [entity.name for entity in entities if html.escape(entity.name) not in text]
    embedded_image = "image=data:image" in text or "shape=image" in text or "data:image/" in text
    return {
        "exists": drawio_path.exists(),
        "vertices": vertices,
        "edges": edges,
        "embedded_image": embedded_image,
        "editable": drawio_path.exists() and vertices > 0 and edges >= len(relationships) and not embedded_image,
        "missing_tables": missing_tables,
    }


def write_report(
    source: Path,
    drawio: Path,
    png: Path,
    report: Path,
    entities: list[Entity],
    relationships: list[Relationship],
    validation: dict[str, object],
    png_success: bool,
    png_message: str,
) -> None:
    report.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# DVLD ERD Draw.io Conversion Report",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "## Source File Used",
        "",
        f"- `{source.relative_to(REPO_ROOT)}`",
        "",
        "## Generated Files",
        "",
        f"- `{drawio.relative_to(REPO_ROOT)}`",
        f"- `{png.relative_to(REPO_ROOT)}` ({'succeeded' if png_success else 'not generated'})",
        f"- `{report.relative_to(REPO_ROOT)}`",
        "",
        "## Tables Detected",
        "",
    ]
    for entity in entities:
        pk_count = sum(1 for column in entity.columns if column.is_pk)
        fk_count = sum(1 for column in entity.columns if column.is_fk)
        lines.append(f"- `{entity.name}` as `{entity.alias}`: {len(entity.columns)} columns, PK={pk_count}, FK={fk_count}")

    lines.extend(["", "## Relationships Detected", ""])
    for relationship in relationships:
        lines.append(
            f"- `{relationship.source}` {relationship.source_cardinality}--{relationship.target_cardinality} "
            f"`{relationship.target}` ({relationship.cardinality_label})"
        )

    lines.extend(
        [
            "",
            "## Validation",
            "",
            f"- Draw.io exists: `{validation['exists']}`",
            f"- Native editable vertices: `{validation['vertices']}`",
            f"- Native editable edges: `{validation['edges']}`",
            f"- Embedded base64/image wrapper found: `{validation['embedded_image']}`",
            f"- Editable Draw.io output: `{validation['editable']}`",
            f"- Missing tables from output: `{validation['missing_tables']}`",
            f"- PNG export/generation succeeded: `{png_success}`",
            f"- PNG note: {png_message}",
            "",
            "## Limitations Or Assumptions",
            "",
            "- `dvld-erd.puml` was treated as the only authoritative source.",
            "- The script generates uncompressed Draw.io XML using native `mxCell` shapes and connectors.",
            "- PNG output is generated from the parsed model with Pillow when available; it is a preview/export, not embedded in the Draw.io file.",
            "- Draw.io connector routing is left editable; diagrams.net may visually reroute lines when opened.",
        ]
    )
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")


def convert(source: Path, drawio: Path, png: Path, report: Path) -> int:
    title, entities, relationships = parse_puml(source)
    apply_layout(entities)
    write_drawio(title, entities, relationships, drawio)
    png_success, png_message = render_png(title, entities, relationships, png)
    validation = validate_drawio(drawio, entities, relationships)
    write_report(source, drawio, png, report, entities, relationships, validation, png_success, png_message)
    return 0 if validation["editable"] and not validation["missing_tables"] else 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert the DVLD PlantUML ERD to native editable Draw.io XML.")
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--drawio", type=Path, default=DEFAULT_DRAWIO)
    parser.add_argument("--png", type=Path, default=DEFAULT_PNG)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()
    return convert(args.source.resolve(), args.drawio.resolve(), args.png.resolve(), args.report.resolve())


if __name__ == "__main__":
    raise SystemExit(main())
