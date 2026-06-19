# Draw.io Layout Improvement Report

Generated: 2026-06-18T20:45:19

## Files Improved

- `docs/UML/database/dvld-erd.drawio`
- `docs/UML/database/physical-erd.drawio`
- `docs/UML/database/logical-erd.drawio`
- `docs/UML/database/database-schema.drawio`
- `docs/UML/database/chen-notation-erd.drawio`

## Additional Readable Diagrams Created

- `docs/UML/database/chen-notation-erd-readable.drawio`
- `docs/UML/database/chen-notation-erd-readable.png`

Split table diagrams were not created because the wider four-domain full diagrams are readable enough without removing full-context relationships.

## Layout Strategy

- Grouped table diagrams into four aligned domain columns: Identity / Reference, Application Processing, Licensing, and Testing.
- Standardized table widths, header styling, row heights, font sizes, PK/FK field styling, and page dimensions.
- Used orthogonal Draw.io connectors with ER one-to-many arrow styling and route waypoints.
- Kept `Users` in the Identity / Reference column while preserving all audit-created relationships.
- Expanded the Chen canvas and added a simplified readable Chen view with PK/FK attributes only.

## PNG Exports Regenerated

- `docs/UML/database/dvld-erd.png`
- `docs/UML/database/physical-erd.png`
- `docs/UML/database/logical-erd.png`
- `docs/UML/database/database-schema.png`
- `docs/UML/database/chen-notation-erd.png`
- `docs/UML/database/chen-notation-erd-readable.png`

## Validation

- `dvld-erd.drawio`: editable=True, vertices=107, edges=26, embedded_image=False, missing_tables=[], missing_relationships=[]
- `physical-erd.drawio`: editable=True, vertices=107, edges=26, embedded_image=False, missing_tables=[], missing_relationships=[]
- `logical-erd.drawio`: editable=True, vertices=107, edges=26, embedded_image=False, missing_tables=[], missing_relationships=[]
- `database-schema.drawio`: editable=True, vertices=107, edges=26, embedded_image=False, missing_tables=[], missing_relationships=[]
- `chen-notation-erd.drawio`: editable=True, vertices=129, edges=140, embedded_image=False, missing_tables=[], missing_relationships=[]
- `chen-notation-erd-readable.drawio`: editable=True, vertices=81, edges=92, embedded_image=False, missing_tables=[], missing_relationships=[]

## Schema Content Confirmation

- `script.sql` was not modified.
- Tables preserved: 14
- Columns preserved: 88
- FK relationships preserved: 26
- Table names, column names, SQL Server data types, PK/FK markers, nullability labels, identity labels, and relationships were generated from the same SQL-derived schema model.

## Remaining Visual Limitations

- The full Chen notation diagram remains dense because it includes all attributes and all relationships for the complete schema.
- Audit relationships from `Users` are inherently numerous; routing is improved but still visually busy in the full diagrams.
- Draw.io may reroute connectors slightly when opened interactively, but all shapes and connectors remain editable.
