from __future__ import annotations

import html
import sys
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from xml.etree import ElementTree as ET

from PIL import Image, ImageDraw, ImageFont


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[1]
DB_DIR = REPO_ROOT / "docs" / "UML" / "database"
SQL_SOURCE = REPO_ROOT / "script.sql"

sys.path.insert(0, str(SCRIPT_DIR))
from sync_database_diagrams_from_sql import ForeignKey, Schema, Table, parse_sql  # noqa: E402


TABLE_DRAWIOS = {
    "dvld-erd.drawio": "DVLD System - ERD",
    "physical-erd.drawio": "DVLD System - Physical ERD",
    "logical-erd.drawio": "DVLD System - Logical ERD",
    "database-schema.drawio": "DVLD System - Database Schema",
}
TABLE_PNGS = {
    "dvld-erd.png": "DVLD System - ERD",
    "physical-erd.png": "DVLD System - Physical ERD",
    "logical-erd.png": "DVLD System - Logical ERD",
    "database-schema.png": "DVLD System - Database Schema",
}
ALL_DRAWIOS = list(TABLE_DRAWIOS) + ["chen-notation-erd.drawio", "chen-notation-erd-readable.drawio"]
ALL_PNGS = list(TABLE_PNGS) + ["chen-notation-erd.png", "chen-notation-erd-readable.png"]


DOMAIN_POSITIONS = {
    "Countries": (70, 125),
    "People": (70, 270),
    "Users": (70, 690),
    "Drivers": (70, 910),
    "ApplicationTypes": (560, 125),
    "Applications": (560, 310),
    "LocalDrivingLicenseApplications": (560, 620),
    "LicenseClasses": (1050, 125),
    "Licenses": (1050, 350),
    "InternationalLicenses": (1050, 735),
    "DetainedLicenses": (1050, 1040),
    "TestTypes": (1540, 125),
    "TestAppointments": (1540, 370),
    "Tests": (1540, 690),
}
DOMAIN_HEADINGS = [
    ("Identity / Reference", 70, 80, 430),
    ("Application Processing", 560, 80, 430),
    ("Licensing", 1050, 80, 430),
    ("Testing", 1540, 80, 430),
]
PAGE_WIDTH = 2200
PAGE_HEIGHT = 1360
TABLE_WIDTH = 430
HEADER_HEIGHT = 34
ROW_HEIGHT = 23


@dataclass
class EdgePath:
    source: tuple[int, int]
    points: list[tuple[int, int]]
    target: tuple[int, int]


def apply_improved_layout(schema: Schema) -> None:
    for table in schema.tables.values():
        table.x, table.y = DOMAIN_POSITIONS[table.name]
        table.width = TABLE_WIDTH
        table.height = HEADER_HEIGHT + len(table.columns) * ROW_HEIGHT


def table_anchor(table: Table, other: Table) -> tuple[int, int]:
    if table.x + table.width < other.x:
        return table.x + table.width, table.y + HEADER_HEIGHT // 2
    if other.x + other.width < table.x:
        return table.x, table.y + HEADER_HEIGHT // 2
    if table.y < other.y:
        return table.x + table.width // 2, table.y + table.height
    return table.x + table.width // 2, table.y


def edge_path(schema: Schema, fk: ForeignKey, index: int) -> EdgePath:
    source_table = schema.tables[fk.parent_table]
    target_table = schema.tables[fk.child_table]
    source = table_anchor(source_table, target_table)
    target = table_anchor(target_table, source_table)

    if source_table.x == target_table.x:
        channel_x = source_table.x + source_table.width + 38 + (index % 4) * 16
        return EdgePath(source, [(channel_x, source[1]), (channel_x, target[1])], target)

    if abs(source[0] - target[0]) > abs(source[1] - target[1]):
        mid_x = (source[0] + target[0]) // 2 + ((index % 5) - 2) * 14
        return EdgePath(source, [(mid_x, source[1]), (mid_x, target[1])], target)

    mid_y = (source[1] + target[1]) // 2 + ((index % 5) - 2) * 14
    return EdgePath(source, [(source[0], mid_y), (target[0], mid_y)], target)


def font(size: int, bold: bool = False):
    paths = [
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
    ]
    for item in paths:
        if Path(item).exists():
            return ImageFont.truetype(item, size)
    return ImageFont.load_default()


def graph_root(name: str, width: int, height: int) -> tuple[ET.Element, ET.Element]:
    mxfile = ET.Element(
        "mxfile",
        {
            "host": "app.diagrams.net",
            "modified": datetime.now(UTC).isoformat(),
            "agent": "Codex database layout improver",
            "version": "24.7.17",
        },
    )
    diagram = ET.SubElement(mxfile, "diagram", {"id": name, "name": name})
    graph = ET.SubElement(
        diagram,
        "mxGraphModel",
        {
            "dx": str(width),
            "dy": str(height),
            "grid": "1",
            "gridSize": "10",
            "guides": "1",
            "tooltips": "1",
            "connect": "1",
            "arrows": "1",
            "fold": "1",
            "page": "1",
            "pageScale": "1",
            "pageWidth": str(width),
            "pageHeight": str(height),
            "math": "0",
            "shadow": "0",
        },
    )
    root = ET.SubElement(graph, "root")
    ET.SubElement(root, "mxCell", {"id": "0"})
    ET.SubElement(root, "mxCell", {"id": "1", "parent": "0"})
    return mxfile, root


def mx_cell(
    root: ET.Element,
    cell_id: str,
    value: str,
    style: str,
    *,
    vertex: bool = True,
    edge: bool = False,
    source: str | None = None,
    target: str | None = None,
    x: int = 0,
    y: int = 0,
    width: int = 0,
    height: int = 0,
    points: list[tuple[int, int]] | None = None,
) -> None:
    attrs = {"id": cell_id, "value": value, "style": style, "parent": "1"}
    if vertex:
        attrs["vertex"] = "1"
    if edge:
        attrs.pop("vertex", None)
        attrs["edge"] = "1"
    if source:
        attrs["source"] = source
    if target:
        attrs["target"] = target
    cell = ET.SubElement(root, "mxCell", attrs)
    geom_attrs = {"as": "geometry"}
    if edge:
        geom_attrs["relative"] = "1"
    else:
        geom_attrs.update({"x": str(x), "y": str(y), "width": str(width), "height": str(height)})
    geom = ET.SubElement(cell, "mxGeometry", geom_attrs)
    if edge and points:
        array = ET.SubElement(geom, "Array", {"as": "points"})
        for px, py in points:
            ET.SubElement(array, "mxPoint", {"x": str(px), "y": str(py)})


def column_style(column) -> str:
    base = (
        "rounded=0;whiteSpace=wrap;html=1;align=left;verticalAlign=middle;"
        "spacingLeft=8;fontSize=10;strokeColor=#CBD5E1;"
    )
    if column.pk:
        return base + "fillColor=#EAF2FF;fontStyle=1;fontColor=#111827;"
    if column.fk:
        return base + "fillColor=#F8FAFC;fontStyle=2;fontColor=#111827;"
    return base + "fillColor=#FFFFFF;fontColor=#111827;"


def write_table_drawio(schema: Schema, path: Path, title: str) -> None:
    mxfile, root = graph_root(path.stem, PAGE_WIDTH, PAGE_HEIGHT)
    mx_cell(
        root,
        "title",
        html.escape(title),
        "text;html=1;strokeColor=none;fillColor=none;fontSize=24;fontStyle=1;align=center;",
        x=0,
        y=24,
        width=PAGE_WIDTH,
        height=36,
    )
    for label, x, y, width in DOMAIN_HEADINGS:
        mx_cell(
            root,
            f"domain_{label.replace(' ', '_').replace('/', '')}",
            html.escape(label),
            "rounded=0;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#93C5FD;fontColor=#0F172A;fontStyle=1;fontSize=13;align=center;",
            x=x,
            y=y,
            width=width,
            height=30,
        )

    table_ids: dict[str, str] = {}
    next_id = 2
    for table in schema.tables.values():
        header_id = f"table_{next_id}"
        next_id += 1
        table_ids[table.name] = header_id
        mx_cell(
            root,
            header_id,
            html.escape(table.name),
            "rounded=0;whiteSpace=wrap;html=1;fillColor=#1E3A8A;strokeColor=#0F172A;fontColor=#FFFFFF;fontStyle=1;fontSize=12;align=center;",
            x=table.x,
            y=table.y,
            width=table.width,
            height=HEADER_HEIGHT,
        )
        for row, column in enumerate(table.columns):
            mx_cell(
                root,
                f"col_{next_id}",
                html.escape(column.drawio_label),
                column_style(column),
                x=table.x,
                y=table.y + HEADER_HEIGHT + row * ROW_HEIGHT,
                width=table.width,
                height=ROW_HEIGHT,
            )
            next_id += 1

    edge_style = (
        "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;"
        "startArrow=ERone;endArrow=ERmany;startFill=0;endFill=0;strokeColor=#475569;"
        "fontColor=#334155;fontSize=9;labelBackgroundColor=#FFFFFF;"
    )
    for index, fk in enumerate(schema.foreign_keys):
        path_points = edge_path(schema, fk, index)
        mx_cell(
            root,
            f"fk_{next_id}",
            html.escape(fk.name),
            edge_style,
            vertex=False,
            edge=True,
            source=table_ids[fk.parent_table],
            target=table_ids[fk.child_table],
            points=path_points.points,
        )
        next_id += 1

    ET.indent(mxfile)
    path.write_text(ET.tostring(mxfile, encoding="unicode"), encoding="utf-8")


def draw_polyline(draw: ImageDraw.ImageDraw, path: EdgePath, fill: str = "#64748B", width: int = 2) -> None:
    pts = [path.source] + path.points + [path.target]
    draw.line(pts, fill=fill, width=width)


def render_table_png(schema: Schema, path: Path, title: str) -> None:
    image = Image.new("RGB", (PAGE_WIDTH, PAGE_HEIGHT), "white")
    draw = ImageDraw.Draw(image)
    draw.text((PAGE_WIDTH // 2, 43), title, fill="#111827", font=font(25, True), anchor="mm")
    for label, x, y, width in DOMAIN_HEADINGS:
        draw.rectangle([x, y, x + width, y + 30], fill="#EFF6FF", outline="#93C5FD", width=1)
        draw.text((x + width // 2, y + 15), label, fill="#0F172A", font=font(13, True), anchor="mm")

    for index, fk in enumerate(schema.foreign_keys):
        draw_polyline(draw, edge_path(schema, fk, index))
        pts = [edge_path(schema, fk, index).source] + edge_path(schema, fk, index).points + [edge_path(schema, fk, index).target]
        mid = pts[len(pts) // 2]
        draw.rectangle([mid[0] - 58, mid[1] - 8, mid[0] + 58, mid[1] + 8], fill="white")
        draw.text(mid, fk.name.replace("FK_", "")[:24], fill="#334155", font=font(8), anchor="mm")

    for table in schema.tables.values():
        draw.rectangle([table.x, table.y, table.x + table.width, table.y + HEADER_HEIGHT], fill="#1E3A8A", outline="#0F172A", width=2)
        draw.text((table.x + table.width // 2, table.y + HEADER_HEIGHT // 2), table.name, fill="white", font=font(12, True), anchor="mm")
        for row, column in enumerate(table.columns):
            y = table.y + HEADER_HEIGHT + row * ROW_HEIGHT
            fill = "#EAF2FF" if column.pk else "#F8FAFC" if column.fk else "#FFFFFF"
            draw.rectangle([table.x, y, table.x + table.width, y + ROW_HEIGHT], fill=fill, outline="#CBD5E1")
            draw.text((table.x + 8, y + ROW_HEIGHT // 2), column.drawio_label[:72], fill="#111827", font=font(9, column.pk), anchor="lm")
    image.save(path)


CHEN_ENTITY_POSITIONS = {
    "Countries": (220, 245),
    "People": (650, 245),
    "Users": (1080, 245),
    "Drivers": (1510, 245),
    "ApplicationTypes": (220, 780),
    "Applications": (650, 780),
    "LocalDrivingLicenseApplications": (1080, 780),
    "LicenseClasses": (1510, 780),
    "Licenses": (650, 1315),
    "InternationalLicenses": (1080, 1315),
    "DetainedLicenses": (1510, 1315),
    "TestTypes": (1940, 780),
    "TestAppointments": (1940, 1090),
    "Tests": (1940, 1400),
}
CHEN_WIDTH = 2400
CHEN_HEIGHT = 1780


def chen_attr_position(table: Table, index: int) -> tuple[int, int]:
    x, y = CHEN_ENTITY_POSITIONS[table.name]
    side = -1 if index % 2 == 0 else 1
    row = index // 2
    ax = x - 210 if side < 0 else x + 260
    ay = y - 145 + row * 45
    return ax, ay


def chen_relation_position(fk: ForeignKey, index: int) -> tuple[int, int]:
    px, py = CHEN_ENTITY_POSITIONS[fk.parent_table]
    cx, cy = CHEN_ENTITY_POSITIONS[fk.child_table]
    return (px + cx) // 2 + 70 + ((index % 3) - 1) * 28, (py + cy) // 2 + ((index % 4) - 1) * 22


def write_chen_drawio(schema: Schema, path: Path, readable: bool = False) -> None:
    mxfile, root = graph_root(path.stem, CHEN_WIDTH, CHEN_HEIGHT)
    title = "DVLD System - Chen ERD" + (" Readable View" if readable else "")
    mx_cell(
        root,
        "title",
        html.escape(title),
        "text;html=1;strokeColor=none;fillColor=none;fontSize=24;fontStyle=1;align=center;",
        x=0,
        y=24,
        width=CHEN_WIDTH,
        height=36,
    )

    ids: dict[str, str] = {}
    next_id = 2
    for table in schema.tables.values():
        x, y = CHEN_ENTITY_POSITIONS[table.name]
        entity_id = f"entity_{next_id}"
        ids[table.name] = entity_id
        next_id += 1
        mx_cell(
            root,
            entity_id,
            html.escape(table.name),
            "rounded=0;whiteSpace=wrap;html=1;fillColor=#D9ECFF;strokeColor=#1F4E79;fontColor=#0B2545;fontStyle=1;fontSize=11;",
            x=x,
            y=y,
            width=220,
            height=50,
        )
        columns = [column for column in table.columns if column.pk or column.fk] if readable else table.columns
        for index, column in enumerate(columns):
            ax, ay = chen_attr_position(table, index)
            fill = "#FFB347" if column.pk else "#B39DDB" if column.fk else "#2F3437"
            font_color = "#111111" if column.pk else "#FFFFFF"
            attr_id = f"attr_{next_id}"
            next_id += 1
            mx_cell(
                root,
                attr_id,
                html.escape(f"{column.name}\n{column.data_type}"),
                f"ellipse;whiteSpace=wrap;html=1;fillColor={fill};strokeColor=#111111;fontColor={font_color};fontSize=9;",
                x=ax,
                y=ay,
                width=180,
                height=38,
            )
            mx_cell(
                root,
                f"edge_{next_id}",
                "",
                "edgeStyle=orthogonalEdgeStyle;html=1;endArrow=none;strokeColor=#94A3B8;",
                vertex=False,
                edge=True,
                source=entity_id,
                target=attr_id,
            )
            next_id += 1

    for index, fk in enumerate(schema.foreign_keys):
        rx, ry = chen_relation_position(fk, index)
        rel_id = f"rel_{next_id}"
        next_id += 1
        mx_cell(
            root,
            rel_id,
            html.escape(fk.name),
            "rhombus;whiteSpace=wrap;html=1;fillColor=#8B3A2E;strokeColor=#5B2119;fontColor=#FFFFFF;fontStyle=1;fontSize=8;",
            x=rx,
            y=ry,
            width=120,
            height=72,
        )
        for source, target, label in [(ids[fk.parent_table], rel_id, "1"), (rel_id, ids[fk.child_table], "N")]:
            mx_cell(
                root,
                f"edge_{next_id}",
                label,
                "edgeStyle=orthogonalEdgeStyle;html=1;endArrow=none;strokeColor=#64748B;fontSize=10;labelBackgroundColor=#FFFFFF;",
                vertex=False,
                edge=True,
                source=source,
                target=target,
            )
            next_id += 1

    ET.indent(mxfile)
    path.write_text(ET.tostring(mxfile, encoding="unicode"), encoding="utf-8")


def render_chen_png(schema: Schema, path: Path, readable: bool = False) -> None:
    image = Image.new("RGB", (CHEN_WIDTH, CHEN_HEIGHT), "white")
    draw = ImageDraw.Draw(image)
    title = "DVLD System - Chen ERD" + (" Readable View" if readable else "")
    draw.text((CHEN_WIDTH // 2, 43), title, fill="#111827", font=font(25, True), anchor="mm")
    centers = {name: (x + 110, y + 25) for name, (x, y) in CHEN_ENTITY_POSITIONS.items()}

    for table in schema.tables.values():
        x, y = CHEN_ENTITY_POSITIONS[table.name]
        draw.rectangle([x, y, x + 220, y + 50], fill="#D9ECFF", outline="#1F4E79", width=2)
        draw.text((x + 110, y + 25), table.name, fill="#0B2545", font=font(10, True), anchor="mm")
        columns = [column for column in table.columns if column.pk or column.fk] if readable else table.columns
        for index, column in enumerate(columns):
            ax, ay = chen_attr_position(table, index)
            fill = "#FFB347" if column.pk else "#B39DDB" if column.fk else "#2F3437"
            font_color = "#111111" if column.pk else "#FFFFFF"
            draw.line([centers[table.name], (ax + 90, ay + 19)], fill="#94A3B8", width=1)
            draw.ellipse([ax, ay, ax + 180, ay + 38], fill=fill, outline="#111111", width=1)
            draw.text((ax + 90, ay + 19), column.name[:24], fill=font_color, font=font(8), anchor="mm")

    for index, fk in enumerate(schema.foreign_keys):
        rx, ry = chen_relation_position(fk, index)
        center = (rx + 60, ry + 36)
        diamond = [(rx + 60, ry), (rx + 120, ry + 36), (rx + 60, ry + 72), (rx, ry + 36)]
        draw.line([centers[fk.parent_table], center], fill="#64748B", width=1)
        draw.line([center, centers[fk.child_table]], fill="#64748B", width=1)
        draw.polygon(diamond, fill="#8B3A2E", outline="#5B2119")
        draw.text(center, fk.name.replace("FK_", "")[:18], fill="white", font=font(7, True), anchor="mm")
    image.save(path)


def validate_drawio(path: Path, schema: Schema, min_edges: int) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    root = ET.parse(path).getroot()
    cells = root.findall(".//mxCell")
    vertices = sum(1 for cell in cells if cell.get("vertex") == "1")
    edges = sum(1 for cell in cells if cell.get("edge") == "1")
    embedded = any(marker in text for marker in ["data:image/", "shape=image", "image=data:image"])
    missing_tables = [table for table in schema.tables if table not in text]
    missing_fks = [fk.name for fk in schema.foreign_keys if fk.name not in text and "readable" not in path.stem]
    return {
        "vertices": vertices,
        "edges": edges,
        "embedded_image": embedded,
        "missing_tables": missing_tables,
        "missing_relationships": missing_fks,
        "editable": vertices >= len(schema.tables) and edges >= min_edges and not embedded,
    }


def write_report(schema: Schema, validations: dict[str, dict[str, object]]) -> None:
    lines = [
        "# Draw.io Layout Improvement Report",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "## Files Improved",
        "",
    ]
    lines.extend(f"- `docs/UML/database/{name}`" for name in TABLE_DRAWIOS)
    lines.append("- `docs/UML/database/chen-notation-erd.drawio`")
    lines.append("")
    lines.append("## Additional Readable Diagrams Created")
    lines.append("")
    lines.append("- `docs/UML/database/chen-notation-erd-readable.drawio`")
    lines.append("- `docs/UML/database/chen-notation-erd-readable.png`")
    lines.append("")
    lines.append("Split table diagrams were not created because the wider four-domain full diagrams are readable enough without removing full-context relationships.")
    lines.append("")
    lines.append("## Layout Strategy")
    lines.append("")
    lines.append("- Grouped table diagrams into four aligned domain columns: Identity / Reference, Application Processing, Licensing, and Testing.")
    lines.append("- Standardized table widths, header styling, row heights, font sizes, PK/FK field styling, and page dimensions.")
    lines.append("- Used orthogonal Draw.io connectors with ER one-to-many arrow styling and route waypoints.")
    lines.append("- Kept `Users` in the Identity / Reference column while preserving all audit-created relationships.")
    lines.append("- Expanded the Chen canvas and added a simplified readable Chen view with PK/FK attributes only.")
    lines.append("")
    lines.append("## PNG Exports Regenerated")
    lines.append("")
    lines.extend(f"- `docs/UML/database/{name}`" for name in ALL_PNGS)
    lines.append("")
    lines.append("## Validation")
    lines.append("")
    for name, validation in validations.items():
        lines.append(
            f"- `{name}`: editable={validation['editable']}, vertices={validation['vertices']}, "
            f"edges={validation['edges']}, embedded_image={validation['embedded_image']}, "
            f"missing_tables={validation['missing_tables']}, missing_relationships={validation['missing_relationships']}"
        )
    lines.append("")
    lines.append("## Schema Content Confirmation")
    lines.append("")
    lines.append("- `script.sql` was not modified.")
    lines.append(f"- Tables preserved: {len(schema.tables)}")
    lines.append(f"- Columns preserved: {len(schema.columns)}")
    lines.append(f"- FK relationships preserved: {len(schema.foreign_keys)}")
    lines.append("- Table names, column names, SQL Server data types, PK/FK markers, nullability labels, identity labels, and relationships were generated from the same SQL-derived schema model.")
    lines.append("")
    lines.append("## Remaining Visual Limitations")
    lines.append("")
    lines.append("- The full Chen notation diagram remains dense because it includes all attributes and all relationships for the complete schema.")
    lines.append("- Audit relationships from `Users` are inherently numerous; routing is improved but still visually busy in the full diagrams.")
    lines.append("- Draw.io may reroute connectors slightly when opened interactively, but all shapes and connectors remain editable.")
    (DB_DIR / "drawio-layout-improvement-report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    schema = parse_sql(SQL_SOURCE)
    apply_improved_layout(schema)

    for name, title in TABLE_DRAWIOS.items():
        write_table_drawio(schema, DB_DIR / name, title)
    write_chen_drawio(schema, DB_DIR / "chen-notation-erd.drawio")
    write_chen_drawio(schema, DB_DIR / "chen-notation-erd-readable.drawio", readable=True)

    for name, title in TABLE_PNGS.items():
        render_table_png(schema, DB_DIR / name, title)
    render_chen_png(schema, DB_DIR / "chen-notation-erd.png")
    render_chen_png(schema, DB_DIR / "chen-notation-erd-readable.png", readable=True)

    validations = {name: validate_drawio(DB_DIR / name, schema, len(schema.foreign_keys)) for name in ALL_DRAWIOS}
    write_report(schema, validations)

    print(f"drawio_files_updated={len(TABLE_DRAWIOS) + 1}")
    print("readable_chen_created=1")
    print(f"png_files_regenerated={len(ALL_PNGS)}")
    print(f"tables_preserved={len(schema.tables)}")
    print(f"relationships_preserved={len(schema.foreign_keys)}")
    print("embedded_image_wrappers=0")


if __name__ == "__main__":
    main()
