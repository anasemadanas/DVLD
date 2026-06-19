# Draw.io Editability Validation Report

Generated: 2026-06-18T22:14:58

## Scope

- All `.drawio` files under `docs/UML`.

## Validation Checks

- Embedded Draw.io XML / `mxGraphModel` exists.
- Editable vertex shapes exist.
- Editable connector edges exist where expected.
- Diagram is not a flat embedded image export.
- No `data:image`, `image/png`, `image/jpeg`, or `base64,` image markers are present.

## Summary

- Draw.io files checked: 45
- Passed: 41
- Warnings: 4
- Failed: 0
- Total editable shape vertices: 1124
- Total editable connector edges: 844

## Results

| File | Status | mxCells | Vertices | Edges | Image Cells | Embedded Image Markers | Notes |
|---|---:|---:|---:|---:|---:|---:|---|
| `docs\UML\database\chen-notation-erd-readable.drawio` | PASS | 175 | 81 | 92 | 0 | 0 |  |
| `docs\UML\database\chen-notation-erd.drawio` | PASS | 271 | 129 | 140 | 0 | 0 |  |
| `docs\UML\database\database-schema.drawio` | PASS | 135 | 107 | 26 | 0 | 0 |  |
| `docs\UML\database\dvld-erd.drawio` | PASS | 135 | 107 | 26 | 0 | 0 |  |
| `docs\UML\database\logical-erd.drawio` | PASS | 135 | 107 | 26 | 0 | 0 |  |
| `docs\UML\database\physical-erd.drawio` | PASS | 135 | 107 | 26 | 0 | 0 |  |
| `docs\UML\design\architecture.drawio` | WARN | 11 | 9 | 0 | 0 | 0 | No editable connectors found; acceptable only for diagrams with no relationships/flows. |
| `docs\UML\design\component_architecture.drawio` | PASS | 84 | 29 | 53 | 0 | 0 |  |
| `docs\UML\design\deployment.drawio` | PASS | 13 | 7 | 4 | 0 | 0 |  |
| `docs\UML\design\module-interaction.drawio` | PASS | 23 | 9 | 12 | 0 | 0 |  |
| `docs\UML\design\screen-flow.drawio` | PASS | 17 | 8 | 7 | 0 | 0 |  |
| `docs\UML\design\state_user_session.drawio` | PASS | 22 | 9 | 11 | 0 | 0 |  |
| `docs\UML\design\system-architecture.drawio` | WARN | 11 | 9 | 0 | 0 | 0 | No editable connectors found; acceptable only for diagrams with no relationships/flows. |
| `docs\UML\design\system-diagram.drawio` | PASS | 16 | 11 | 3 | 0 | 0 |  |
| `docs\UML\design\system-inputs.drawio` | PASS | 34 | 17 | 15 | 0 | 0 |  |
| `docs\UML\design\ui-flow-navigation.drawio` | PASS | 26 | 13 | 11 | 0 | 0 |  |
| `docs\UML\diagram\activity-damaged-license-replacement.drawio` | PASS | 24 | 12 | 10 | 0 | 0 |  |
| `docs\UML\diagram\activity-international-license.drawio` | PASS | 30 | 15 | 13 | 0 | 0 |  |
| `docs\UML\diagram\activity-license-detention-release.drawio` | PASS | 32 | 16 | 14 | 0 | 0 |  |
| `docs\UML\diagram\activity-license-issuance.drawio` | PASS | 44 | 22 | 20 | 0 | 0 |  |
| `docs\UML\diagram\activity-license-renewal.drawio` | PASS | 30 | 15 | 13 | 0 | 0 |  |
| `docs\UML\diagram\activity-lost-license-replacement.drawio` | PASS | 24 | 12 | 10 | 0 | 0 |  |
| `docs\UML\diagram\activity-retake-test.drawio` | PASS | 24 | 12 | 10 | 0 | 0 |  |
| `docs\UML\diagram\class-diagram.drawio` | PASS | 26 | 13 | 11 | 0 | 0 |  |
| `docs\UML\diagram\general-activity-diagram.drawio` | PASS | 32 | 16 | 14 | 0 | 0 |  |
| `docs\UML\diagram\general-sequence-diagram.drawio` | PASS | 22 | 11 | 9 | 0 | 0 |  |
| `docs\UML\diagram\issue-driving-license-sequence.drawio` | WARN | 3 | 1 | 0 | 0 | 0 | No editable connectors found; acceptable only for diagrams with no relationships/flows. |
| `docs\UML\diagram\license-issuance-activity.drawio` | PASS | 40 | 20 | 18 | 0 | 0 |  |
| `docs\UML\diagram\sequence-damaged-license-replacement.drawio` | PASS | 19 | 9 | 8 | 0 | 0 |  |
| `docs\UML\diagram\sequence-license-detention.drawio` | PASS | 18 | 9 | 7 | 0 | 0 |  |
| `docs\UML\diagram\sequence-license-issuance.drawio` | PASS | 29 | 13 | 14 | 0 | 0 |  |
| `docs\UML\diagram\sequence-license-release.drawio` | PASS | 19 | 9 | 8 | 0 | 0 |  |
| `docs\UML\diagram\sequence-license-renewal.drawio` | PASS | 24 | 11 | 11 | 0 | 0 |  |
| `docs\UML\diagram\sequence-lost-license-replacement.drawio` | PASS | 21 | 9 | 10 | 0 | 0 |  |
| `docs\UML\diagram\sequence-retake-test.drawio` | PASS | 24 | 11 | 11 | 0 | 0 |  |
| `docs\UML\diagram\service-seq\sequence-first-time-license-issuance.drawio` | WARN | 3 | 1 | 0 | 0 | 0 | No editable connectors found; acceptable only for diagrams with no relationships/flows. |
| `docs\UML\diagram\service-seq\sequence-general-operation.drawio` | PASS | 22 | 11 | 9 | 0 | 0 |  |
| `docs\UML\diagram\service-seq\sequence-international-license.drawio` | PASS | 33 | 13 | 18 | 0 | 0 |  |
| `docs\UML\diagram\service-seq\sequence-license-detention-release.drawio` | PASS | 34 | 11 | 21 | 0 | 0 |  |
| `docs\UML\diagram\service-seq\sequence-license-renewal.drawio` | PASS | 31 | 13 | 16 | 0 | 0 |  |
| `docs\UML\diagram\service-seq\sequence-test-management.drawio` | PASS | 37 | 13 | 22 | 0 | 0 |  |
| `docs\UML\diagram\use-case-diagram-base.drawio` | PASS | 61 | 24 | 35 | 0 | 0 |  |
| `docs\UML\diagram\use-case-diagram.drawio` | PASS | 64 | 25 | 37 | 0 | 0 |  |
| `docs\UML\state\application-state-diagram.drawio` | PASS | 20 | 8 | 10 | 0 | 0 |  |
| `docs\UML\state\license-state-diagram.drawio` | PASS | 25 | 10 | 13 | 0 | 0 |  |

## Failures

- None.

## Warnings

- `docs\UML\design\architecture.drawio`: No editable connectors found; acceptable only for diagrams with no relationships/flows.
- `docs\UML\design\system-architecture.drawio`: No editable connectors found; acceptable only for diagrams with no relationships/flows.
- `docs\UML\diagram\issue-driving-license-sequence.drawio`: No editable connectors found; acceptable only for diagrams with no relationships/flows.
- `docs\UML\diagram\service-seq\sequence-first-time-license-issuance.drawio`: No editable connectors found; acceptable only for diagrams with no relationships/flows.

## Conclusion

- Files marked `PASS` contain native editable Draw.io XML with editable shapes and connectors.
- No passing file is an image-only wrapper.
- Connectors remain editable where edge cells are present.
- Files marked `WARN` still contain native editable Draw.io XML and editable shapes, but no editable connector edge cells were found, so connector editability could not be confirmed for those files.
