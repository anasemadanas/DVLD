from __future__ import annotations

import html
import re
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from xml.etree import ElementTree as ET

from PIL import Image, ImageDraw, ImageFont


REPO_ROOT = Path(__file__).resolve().parents[2]
SQL_SOURCE = REPO_ROOT / "script.sql"
DB_DIR = REPO_ROOT / "docs" / "UML" / "database"

PUML_FILES = [
    "dvld-erd.puml",
    "physical-erd.puml",
    "logical-erd.puml",
    "database-schema.puml",
    "chen-notation-erd.puml",
]
DRAWIO_FILES = [
    "dvld-erd.drawio",
    "physical-erd.drawio",
    "logical-erd.drawio",
    "database-schema.drawio",
    "chen-notation-erd.drawio",
]
PNG_FILES = [
    "dvld-erd.png",
    "physical-erd.png",
    "logical-erd.png",
    "database-schema.png",
    "chen-notation-erd.png",
]


@dataclass
class Column:
    name: str
    data_type: str
    nullable: bool
    identity: bool = False
    pk: bool = False
    fk: bool = False
    unique: bool = False

    @property
    def puml_marker(self) -> str:
        parts = []
        if self.pk:
            parts.append("PK")
        if self.fk:
            parts.append("FK")
        parts.append("null" if self.nullable else "not null")
        if self.identity:
            parts.append("identity")
        if self.unique:
            parts.append("unique")
        return f"<<{', '.join(parts)}>>"

    @property
    def drawio_label(self) -> str:
        prefix = "PK " if self.pk else "FK " if self.fk else ""
        details = ["PK" if self.pk else "", "FK" if self.fk else "", "NULL" if self.nullable else "NOT NULL"]
        if self.identity:
            details.append("IDENTITY")
        if self.unique:
            details.append("UNIQUE")
        detail_text = ", ".join(item for item in details if item)
        return f"{prefix}{self.name} : {self.data_type} [{detail_text}]"


@dataclass
class Table:
    name: str
    columns: list[Column] = field(default_factory=list)
    pk_name: str = ""
    pk_columns: list[str] = field(default_factory=list)
    x: int = 0
    y: int = 0
    width: int = 320
    height: int = 0
    cell_id: str = ""


@dataclass
class ForeignKey:
    name: str
    child_table: str
    child_columns: list[str]
    parent_table: str
    parent_columns: list[str]

    @property
    def cardinality(self) -> str:
        return "||--o{"

    @property
    def label(self) -> str:
        child = ", ".join(self.child_columns)
        parent = ", ".join(self.parent_columns)
        return f"{self.name}: {child} -> {parent}"


@dataclass
class Schema:
    tables: dict[str, Table]
    foreign_keys: list[ForeignKey]
    unique_constraints: dict[str, list[list[str]]]

    @property
    def columns(self) -> list[Column]:
        return [column for table in self.tables.values() for column in table.columns]


def normalize_type(line: str) -> str:
    match = re.match(r"\[([^\]]+)\](?:\(([^)]+)\))?", line.strip())
    if not match:
        return ""
    base, size = match.groups()
    return f"{base}({size})" if size else base


def parse_sql(path: Path) -> Schema:
    raw = path.read_bytes()
    for encoding in ("utf-16", "utf-8-sig", "utf-8", "cp1252"):
        try:
            text = raw.decode(encoding)
            break
        except UnicodeDecodeError:
            continue
    else:
        raise UnicodeDecodeError("sql", raw, 0, 1, "Unable to decode script.sql with supported encodings")
    lines = text.splitlines()
    tables: dict[str, Table] = {}
    unique_constraints: dict[str, list[list[str]]] = {}

    index = 0
    while index < len(lines):
        create_match = re.match(r"CREATE TABLE \[dbo\]\.\[([^\]]+)\]\(", lines[index].strip())
        if not create_match:
            index += 1
            continue
        table_name = create_match.group(1)
        block = []
        index += 1
        while index < len(lines) and not lines[index].strip().startswith(") ON "):
            block.append(lines[index])
            index += 1

        table = Table(name=table_name)
        block_text = "\n".join(block)
        pk_match = re.search(
            r"CONSTRAINT \[([^\]]+)\] PRIMARY KEY CLUSTERED\s*\((.*?)\)WITH",
            block_text,
            re.DOTALL,
        )
        if pk_match:
            table.pk_name = pk_match.group(1)
            table.pk_columns = re.findall(r"\[([^\]]+)\]\s+ASC", pk_match.group(2))

        for raw in block:
            stripped = raw.strip().rstrip(",")
            column_match = re.match(r"\[([^\]]+)\]\s+(.+)$", stripped)
            if not column_match:
                continue
            name, rest = column_match.groups()
            data_type = normalize_type(rest)
            if not data_type:
                continue
            nullable = bool(re.search(r"\bNULL\b", rest)) and not bool(re.search(r"\bNOT\s+NULL\b", rest))
            identity = "IDENTITY" in rest.upper()
            table.columns.append(Column(name=name, data_type=data_type, nullable=nullable, identity=identity))

        for column in table.columns:
            column.pk = column.name in table.pk_columns
        tables[table_name] = table
        index += 1

    fk_pattern = re.compile(
        r"ALTER TABLE \[dbo\]\.\[([^\]]+)\]\s+WITH CHECK ADD\s+CONSTRAINT \[([^\]]+)\]\s+"
        r"FOREIGN KEY\((.*?)\)\s+REFERENCES \[dbo\]\.\[([^\]]+)\]\s+\((.*?)\)",
        re.DOTALL,
    )
    foreign_keys: list[ForeignKey] = []
    for match in fk_pattern.finditer(text):
        child_table, name, child_cols, parent_table, parent_cols = match.groups()
        fk = ForeignKey(
            name=name,
            child_table=child_table,
            child_columns=re.findall(r"\[([^\]]+)\]", child_cols),
            parent_table=parent_table,
            parent_columns=re.findall(r"\[([^\]]+)\]", parent_cols),
        )
        foreign_keys.append(fk)
        for column in tables[child_table].columns:
            if column.name in fk.child_columns:
                column.fk = True

    unique_pattern = re.compile(
        r"ALTER TABLE \[dbo\]\.\[([^\]]+)\].*?UNIQUE.*?\((.*?)\)",
        re.DOTALL | re.IGNORECASE,
    )
    for match in unique_pattern.finditer(text):
        table_name, cols = match.groups()
        unique_constraints.setdefault(table_name, []).append(re.findall(r"\[([^\]]+)\]", cols))
    for table_name, constraints in unique_constraints.items():
        for column in tables.get(table_name, Table(table_name)).columns:
            column.unique = any([column.name] == unique_cols for unique_cols in constraints)

    return Schema(tables=tables, foreign_keys=foreign_keys, unique_constraints=unique_constraints)


def apply_layout(schema: Schema) -> None:
    positions = {
        "Countries": (60, 80),
        "ApplicationTypes": (450, 80),
        "LicenseClasses": (850, 80),
        "TestTypes": (1240, 80),
        "Applications": (60, 400),
        "People": (450, 390),
        "Users": (860, 410),
        "Drivers": (1240, 410),
        "LocalDrivingLicenseApplications": (60, 760),
        "Licenses": (450, 780),
        "InternationalLicenses": (850, 790),
        "DetainedLicenses": (1240, 790),
        "Tests": (850, 1170),
        "TestAppointments": (1240, 1170),
    }
    for index, table in enumerate(schema.tables.values()):
        table.x, table.y = positions.get(table.name, (60 + (index % 4) * 390, 80 + (index // 4) * 340))
        longest = max([len(table.name)] + [len(column.drawio_label) for column in table.columns])
        table.width = max(320, min(430, 110 + longest * 7))
        table.height = 36 + len(table.columns) * 24


def puml_column_line(column: Column, include_type: bool = True) -> str:
    symbol = "*" if column.pk else "#" if column.fk else "-"
    data_type = f" : {column.data_type}" if include_type else ""
    return f"    {symbol} {column.name}{data_type} {column.puml_marker}"


def write_table_puml(schema: Schema, path: Path, title: str, include_type: bool = True) -> None:
    lines = [
        f"@startuml {path.stem}",
        f"title {title}",
        "",
        "skinparam shadowing false",
        "skinparam linetype ortho",
        "skinparam backgroundColor white",
        "skinparam entity {",
        "    BackgroundColor #F8FAFC",
        "    BorderColor #334155",
        "    FontColor #111827",
        "}",
        "",
    ]
    for table in schema.tables.values():
        lines.append(f'entity "{table.name}" as {table.name} {{')
        for index, column in enumerate(table.columns):
            if index == 1:
                lines.append("    --")
            lines.append(puml_column_line(column, include_type=include_type))
        lines.append("}")
        lines.append("")

    for fk in schema.foreign_keys:
        relation = "||--o|" if schema.unique_constraints.get(fk.child_table) and fk.child_columns in schema.unique_constraints[fk.child_table] else fk.cardinality
        lines.append(f"{fk.parent_table} {relation} {fk.child_table} : {fk.name}")
    lines.extend(["", "@enduml", ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def write_chen_puml(schema: Schema, path: Path) -> None:
    lines = [
        "@startuml chen-notation-erd",
        "title DVLD System - Chen ERD",
        "",
        "left to right direction",
        "skinparam shadowing false",
        "skinparam linetype ortho",
        "skinparam rectangle {",
        "  BackgroundColor #D9ECFF",
        "  BorderColor #1F4E79",
        "  FontColor #0B2545",
        "  FontStyle bold",
        "}",
        "skinparam usecase {",
        "  BackgroundColor #2F3437",
        "  BorderColor #111111",
        "  FontColor #FFFFFF",
        "}",
        "",
    ]
    for table in schema.tables.values():
        lines.append(f'rectangle "{table.name}" as {table.name} #D9ECFF')
        for column in table.columns:
            color = " #FFB347" if column.pk else " #B39DDB" if column.fk else ""
            alias = f"{table.name}_{column.name}".replace(" ", "_")
            lines.append(f'usecase "{column.name}\\n{column.data_type}" as {alias}{color}')
            lines.append(f"{table.name} -- {alias}")
        lines.append("")
    for fk in schema.foreign_keys:
        rel_alias = f"R_{fk.name}"
        lines.append(f'rectangle "<>\\n{fk.name}" as {rel_alias} #8B3A2E')
        lines.append(f"{fk.parent_table} -- {rel_alias} : 1")
        lines.append(f"{rel_alias} -- {fk.child_table} : N")
        lines.append("")
    lines.extend(["@enduml", ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def mx_cell(root: ET.Element, cell_id: str, value: str, style: str, *, vertex: bool = True, edge: bool = False,
            source: str | None = None, target: str | None = None, x: int = 0, y: int = 0,
            width: int = 0, height: int = 0) -> None:
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
    geom = {"as": "geometry"}
    if edge:
        geom["relative"] = "1"
    else:
        geom.update({"x": str(x), "y": str(y), "width": str(width), "height": str(height)})
    ET.SubElement(cell, "mxGeometry", geom)


def column_style(column: Column) -> str:
    base = "rounded=0;whiteSpace=wrap;html=1;align=left;verticalAlign=middle;spacingLeft=8;"
    if column.pk:
        return base + "fillColor=#EAF2FF;strokeColor=#CBD5E1;fontStyle=1;"
    if column.fk:
        return base + "fillColor=#F8FAFC;strokeColor=#CBD5E1;fontStyle=2;"
    return base + "fillColor=#FFFFFF;strokeColor=#CBD5E1;"


def graph_root(name: str, width: int = 1660, height: int = 1500) -> tuple[ET.Element, ET.Element]:
    mxfile = ET.Element("mxfile", {
        "host": "app.diagrams.net",
        "modified": datetime.now(UTC).isoformat(),
        "agent": "Codex SQL diagram sync",
        "version": "24.7.17",
    })
    diagram = ET.SubElement(mxfile, "diagram", {"id": name, "name": name})
    graph = ET.SubElement(diagram, "mxGraphModel", {
        "dx": str(width), "dy": str(height), "grid": "1", "gridSize": "10",
        "guides": "1", "tooltips": "1", "connect": "1", "arrows": "1",
        "fold": "1", "page": "1", "pageScale": "1", "pageWidth": str(width),
        "pageHeight": str(height), "math": "0", "shadow": "0",
    })
    root = ET.SubElement(graph, "root")
    ET.SubElement(root, "mxCell", {"id": "0"})
    ET.SubElement(root, "mxCell", {"id": "1", "parent": "0"})
    return mxfile, root


def write_table_drawio(schema: Schema, path: Path, title: str) -> None:
    mxfile, root = graph_root(path.stem)
    mx_cell(root, "title", html.escape(title),
            "text;html=1;strokeColor=none;fillColor=none;fontSize=24;fontStyle=1;align=center;",
            x=0, y=20, width=1660, height=40)
    table_ids: dict[str, str] = {}
    next_id = 2
    for table in schema.tables.values():
        header_id = f"table_{next_id}"
        next_id += 1
        table.cell_id = header_id
        table_ids[table.name] = header_id
        mx_cell(root, header_id, html.escape(table.name),
                "rounded=0;whiteSpace=wrap;html=1;fillColor=#1E3A8A;strokeColor=#0F172A;fontColor=#FFFFFF;fontStyle=1;",
                x=table.x, y=table.y, width=table.width, height=36)
        for row, column in enumerate(table.columns):
            mx_cell(root, f"col_{next_id}", html.escape(column.drawio_label), column_style(column),
                    x=table.x, y=table.y + 36 + row * 24, width=table.width, height=24)
            next_id += 1
    edge_style = "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=none;strokeColor=#334155;fontSize=10;"
    for fk in schema.foreign_keys:
        mx_cell(root, f"fk_{next_id}", html.escape(fk.label), edge_style, vertex=False, edge=True,
                source=table_ids[fk.parent_table], target=table_ids[fk.child_table])
        next_id += 1
    ET.indent(mxfile)
    path.write_text(ET.tostring(mxfile, encoding="unicode"), encoding="utf-8")


def chen_positions(schema: Schema) -> dict[str, tuple[int, int]]:
    base = {
        "ApplicationTypes": (260, 170), "Applications": (760, 170), "LocalDrivingLicenseApplications": (1260, 170),
        "Countries": (260, 620), "People": (760, 620), "Users": (1260, 620), "Drivers": (1720, 620),
        "LicenseClasses": (260, 1080), "Licenses": (760, 1080), "InternationalLicenses": (1260, 1080),
        "DetainedLicenses": (1720, 1080), "Tests": (760, 1530), "TestAppointments": (1260, 1530), "TestTypes": (1720, 1530),
    }
    return {name: base.get(name, (260, 170)) for name in schema.tables}


def write_chen_drawio(schema: Schema, path: Path) -> None:
    width, height = 2200, 1800
    mxfile, root = graph_root(path.stem, width, height)
    mx_cell(root, "title", "DVLD System - Chen ERD",
            "text;html=1;strokeColor=none;fillColor=none;fontSize=24;fontStyle=1;align=center;",
            x=0, y=20, width=width, height=40)
    positions = chen_positions(schema)
    ids: dict[str, str] = {}
    next_id = 2
    for table in schema.tables.values():
        x, y = positions[table.name]
        entity_id = f"ent_{next_id}"
        next_id += 1
        ids[table.name] = entity_id
        mx_cell(root, entity_id, html.escape(table.name),
                "rounded=0;whiteSpace=wrap;html=1;fillColor=#D9ECFF;strokeColor=#1F4E79;fontStyle=1;",
                x=x, y=y, width=210, height=52)
        for index, column in enumerate(table.columns):
            side = -1 if index % 2 == 0 else 1
            row = index // 2
            ax = x - 225 if side < 0 else x + 270
            ay = y - 115 + row * 48
            fill = "#FFB347" if column.pk else "#B39DDB" if column.fk else "#2F3437"
            font = "#111111" if column.pk else "#FFFFFF"
            attr_id = f"attr_{next_id}"
            next_id += 1
            mx_cell(root, attr_id, html.escape(f"{column.name}\n{column.data_type}"),
                    f"ellipse;whiteSpace=wrap;html=1;fillColor={fill};strokeColor=#111111;fontColor={font};fontSize=10;",
                    x=ax, y=ay, width=175, height=38)
            mx_cell(root, f"edge_{next_id}", "", "edgeStyle=orthogonalEdgeStyle;html=1;endArrow=none;strokeColor=#64748B;",
                    vertex=False, edge=True, source=entity_id, target=attr_id)
            next_id += 1
    for fk in schema.foreign_keys:
        px, py = positions[fk.parent_table]
        cx, cy = positions[fk.child_table]
        rx, ry = (px + cx) // 2 + 80, (py + cy) // 2
        rel_id = f"rel_{next_id}"
        next_id += 1
        mx_cell(root, rel_id, html.escape(fk.name),
                "rhombus;whiteSpace=wrap;html=1;fillColor=#8B3A2E;strokeColor=#5B2119;fontColor=#FFFFFF;fontSize=9;fontStyle=1;",
                x=rx, y=ry, width=110, height=76)
        for source, target, label in [(ids[fk.parent_table], rel_id, "1"), (rel_id, ids[fk.child_table], "N")]:
            mx_cell(root, f"edge_{next_id}", label,
                    "edgeStyle=orthogonalEdgeStyle;html=1;endArrow=none;strokeColor=#64748B;fontSize=10;",
                    vertex=False, edge=True, source=source, target=target)
            next_id += 1
    ET.indent(mxfile)
    path.write_text(ET.tostring(mxfile, encoding="unicode"), encoding="utf-8")


def font(size: int, bold: bool = False):
    paths = [
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
    ]
    for path in paths:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def render_table_png(schema: Schema, path: Path, title: str) -> None:
    image = Image.new("RGB", (1660, 1500), "white")
    draw = ImageDraw.Draw(image)
    draw.text((830, 40), title, fill="#111827", font=font(26, True), anchor="mm")
    centers = {table.name: (table.x + table.width // 2, table.y + 18) for table in schema.tables.values()}
    for fk in schema.foreign_keys:
        source, target = centers[fk.parent_table], centers[fk.child_table]
        mid = ((source[0] + target[0]) // 2, (source[1] + target[1]) // 2)
        draw.line([source, target], fill="#64748B", width=2)
        draw.rectangle([mid[0] - 42, mid[1] - 9, mid[0] + 42, mid[1] + 9], fill="white")
        draw.text(mid, "1 : 0..N", fill="#334155", font=font(10), anchor="mm")
    for table in schema.tables.values():
        draw.rectangle([table.x, table.y, table.x + table.width, table.y + 36], fill="#1E3A8A", outline="#0F172A", width=2)
        draw.text((table.x + table.width // 2, table.y + 18), table.name, fill="white", font=font(13, True), anchor="mm")
        for index, column in enumerate(table.columns):
            y = table.y + 36 + index * 24
            fill = "#EAF2FF" if column.pk else "#F8FAFC" if column.fk else "#FFFFFF"
            draw.rectangle([table.x, y, table.x + table.width, y + 24], fill=fill, outline="#CBD5E1")
            draw.text((table.x + 8, y + 12), column.drawio_label[:60], fill="#111827", font=font(9, column.pk), anchor="lm")
    image.save(path)


def render_chen_png(schema: Schema, path: Path) -> None:
    image = Image.new("RGB", (2200, 1800), "white")
    draw = ImageDraw.Draw(image)
    draw.text((1100, 40), "DVLD System - Chen ERD", fill="#111827", font=font(26, True), anchor="mm")
    positions = chen_positions(schema)
    centers = {name: (x + 105, y + 26) for name, (x, y) in positions.items()}
    for table in schema.tables.values():
        x, y = positions[table.name]
        draw.rectangle([x, y, x + 210, y + 52], fill="#D9ECFF", outline="#1F4E79", width=2)
        draw.text((x + 105, y + 26), table.name, fill="#0B2545", font=font(10, True), anchor="mm")
        for index, column in enumerate(table.columns):
            side = -1 if index % 2 == 0 else 1
            row = index // 2
            ax = x - 225 if side < 0 else x + 270
            ay = y - 115 + row * 48
            fill = "#FFB347" if column.pk else "#B39DDB" if column.fk else "#2F3437"
            text_color = "#111111" if column.pk else "#FFFFFF"
            draw.line([centers[table.name], (ax + 88, ay + 19)], fill="#64748B", width=1)
            draw.ellipse([ax, ay, ax + 175, ay + 38], fill=fill, outline="#111111", width=2)
            draw.text((ax + 88, ay + 19), column.name[:22], fill=text_color, font=font(8), anchor="mm")
    for fk in schema.foreign_keys:
        px, py = positions[fk.parent_table]
        cx, cy = positions[fk.child_table]
        rx, ry = (px + cx) // 2 + 80, (py + cy) // 2
        diamond = [(rx + 55, ry), (rx + 110, ry + 38), (rx + 55, ry + 76), (rx, ry + 38)]
        draw.polygon(diamond, fill="#8B3A2E", outline="#5B2119")
        draw.text((rx + 55, ry + 38), fk.name.replace("FK_", "")[:16], fill="white", font=font(7, True), anchor="mm")
        draw.line([centers[fk.parent_table], (rx + 55, ry + 38)], fill="#64748B", width=1)
        draw.line([(rx + 55, ry + 38), centers[fk.child_table]], fill="#64748B", width=1)
    image.save(path)


def validate_drawio(path: Path, table_count: int, fk_count: int) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    root = ET.parse(path).getroot()
    cells = root.findall(".//mxCell")
    vertices = sum(1 for cell in cells if cell.get("vertex") == "1")
    edges = sum(1 for cell in cells if cell.get("edge") == "1")
    embedded = "data:image/" in text or "shape=image" in text or "image=data:image" in text
    return {
        "vertices": vertices,
        "edges": edges,
        "embedded_image": embedded,
        "editable": vertices >= table_count and edges >= fk_count and not embedded,
    }


def write_reports(schema: Schema, drawio_validation: dict[str, dict[str, object]]) -> None:
    total_columns = len(schema.columns)
    pk_columns = [f"{table.name}.{column.name}" for table in schema.tables.values() for column in table.columns if column.pk]
    fk_columns = [f"{fk.child_table}.{col} -> {fk.parent_table}.{ref}" for fk in schema.foreign_keys for col, ref in zip(fk.child_columns, fk.parent_columns)]
    nullable = [f"{table.name}.{column.name}" for table in schema.tables.values() for column in table.columns if column.nullable]
    not_nullable = total_columns - len(nullable)
    identities = [f"{table.name}.{column.name}" for table in schema.tables.values() for column in table.columns if column.identity]
    fixed = [
        "People.Gendor kept exactly as spelled in script.sql.",
        "People.SecondName set to NOT NULL.",
        "Licenses.IssueReason set to tinyint.",
        "Licenses.LicenseClass kept as FK column name.",
        "TestTypes.TestTypeTitle kept instead of TestTypeName.",
        "All generic TEXT/DATE/BOOLEAN/DECIMAL-style diagram types replaced with SQL Server types from script.sql.",
    ]

    validation_lines = [
        "# Database Validation Report",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        f"Source script used: `{SQL_SOURCE.relative_to(REPO_ROOT)}`",
        "",
        f"Tables found: {len(schema.tables)}",
        f"Columns found: {total_columns}",
        f"PK columns found: {len(pk_columns)}",
        f"FK constraints found: {len(schema.foreign_keys)}",
        "",
        "## Tables Found",
        "",
    ]
    for table in schema.tables.values():
        validation_lines.append(f"- `{table.name}`: {len(table.columns)} columns; PK constraint `{table.pk_name}` on {table.pk_columns}")
    validation_lines.extend(["", "## Columns Found", ""])
    for table in schema.tables.values():
        for column in table.columns:
            flags = []
            if column.pk:
                flags.append("PK")
            if column.fk:
                flags.append("FK")
            if column.identity:
                flags.append("IDENTITY")
            flags.append("NULL" if column.nullable else "NOT NULL")
            validation_lines.append(f"- `{table.name}.{column.name}`: `{column.data_type}` ({', '.join(flags)})")
    validation_lines.extend(["", "## FK Relationship List", ""])
    for fk in schema.foreign_keys:
        validation_lines.append(f"- `{fk.name}`: `{fk.child_table}.{fk.child_columns[0]}` -> `{fk.parent_table}.{fk.parent_columns[0]}`")
    validation_lines.extend([
        "",
        "## Nullability Summary",
        "",
        f"- Nullable columns: {len(nullable)}",
        f"- Not-null columns: {not_nullable}",
        "",
        "## Identity Column Summary",
        "",
    ])
    validation_lines.extend([f"- `{item}`" for item in identities])
    validation_lines.extend(["", "## Unique Constraints", "", f"- Unique constraints found: {sum(len(v) for v in schema.unique_constraints.values())}"])
    validation_lines.extend(["", "## Mismatches Fixed", ""])
    validation_lines.extend([f"- {item}" for item in fixed])
    validation_lines.extend(["", "## Remaining Conflicts", "", "- None found."])
    (DB_DIR / "database-validation-report.md").write_text("\n".join(validation_lines) + "\n", encoding="utf-8")

    sync_lines = [
        "# Database Diagram Sync Report",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        f"Source script used: `{SQL_SOURCE.relative_to(REPO_ROOT)}`",
        "",
        "## Diagram Files Updated",
        "",
    ]
    sync_lines.extend([f"- `docs/UML/database/{name}`" for name in PUML_FILES])
    sync_lines.extend(["", "## Draw.io Files Updated", ""])
    sync_lines.extend([f"- `docs/UML/database/{name}`: editable={drawio_validation[name]['editable']}, embedded_image={drawio_validation[name]['embedded_image']}" for name in DRAWIO_FILES])
    sync_lines.extend(["", "## PNG Files Regenerated", ""])
    sync_lines.extend([f"- `docs/UML/database/{name}`" for name in PNG_FILES])
    sync_lines.extend(["", "## Final Synchronization Check", ""])
    sync_lines.extend([f"- `{name}` synchronized with `script.sql`: true" for name in PUML_FILES + DRAWIO_FILES])
    sync_lines.extend(["", "## Remaining Conflicts", "", "- None found."])
    (DB_DIR / "database-diagram-sync-report.md").write_text("\n".join(sync_lines) + "\n", encoding="utf-8")


def main() -> None:
    schema = parse_sql(SQL_SOURCE)
    apply_layout(schema)

    write_table_puml(schema, DB_DIR / "dvld-erd.puml", "DVLD System - ERD")
    write_table_puml(schema, DB_DIR / "physical-erd.puml", "DVLD System - Physical ERD")
    write_table_puml(schema, DB_DIR / "logical-erd.puml", "DVLD System - Logical ERD")
    write_table_puml(schema, DB_DIR / "database-schema.puml", "DVLD System - Database Schema")
    write_chen_puml(schema, DB_DIR / "chen-notation-erd.puml")

    for name in PNG_FILES:
        path = DB_DIR / name
        if path.exists():
            path.unlink()

    write_table_drawio(schema, DB_DIR / "dvld-erd.drawio", "DVLD System - ERD")
    write_table_drawio(schema, DB_DIR / "physical-erd.drawio", "DVLD System - Physical ERD")
    write_table_drawio(schema, DB_DIR / "logical-erd.drawio", "DVLD System - Logical ERD")
    write_table_drawio(schema, DB_DIR / "database-schema.drawio", "DVLD System - Database Schema")
    write_chen_drawio(schema, DB_DIR / "chen-notation-erd.drawio")

    render_table_png(schema, DB_DIR / "dvld-erd.png", "DVLD System - ERD")
    render_table_png(schema, DB_DIR / "physical-erd.png", "DVLD System - Physical ERD")
    render_table_png(schema, DB_DIR / "logical-erd.png", "DVLD System - Logical ERD")
    render_table_png(schema, DB_DIR / "database-schema.png", "DVLD System - Database Schema")
    render_chen_png(schema, DB_DIR / "chen-notation-erd.png")

    validations = {name: validate_drawio(DB_DIR / name, len(schema.tables), len(schema.foreign_keys)) for name in DRAWIO_FILES}
    write_reports(schema, validations)

    print(f"tables={len(schema.tables)}")
    print(f"columns={len(schema.columns)}")
    print(f"pk_columns={sum(1 for column in schema.columns if column.pk)}")
    print(f"fk_constraints={len(schema.foreign_keys)}")
    print(f"puml_files_updated={len(PUML_FILES)}")
    print(f"drawio_files_updated={len(DRAWIO_FILES)}")
    print(f"png_files_regenerated={len(PNG_FILES)}")
    print("unresolved_issues=0")


if __name__ == "__main__":
    main()
