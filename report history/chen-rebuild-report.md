# Chen ERD Rebuild Report

## Rebuild Status

`chen-notation-erd.puml` was rebuilt from scratch. The previous simplified structure was deleted and replaced with a new PlantUML Chen-style ERD.

## Source Reference

`DVLD RS DB.drawio` and an exported Draw.io Chen ERD image were not found in the current repository or workspace during this rebuild. The diagram was rebuilt from the full entity, attribute, relationship, layout, and styling requirements provided in the request.

## Entities Included

- Person
- User
- Driver
- Application
- ApplicationType
- Country
- License
- LicenseClass
- LocalDrivingLicenseApplication
- InternationalLicense
- DetainedLicense
- TestAppointment
- Test
- TestTypes

## Counts

- Entities: 14
- Attributes: 89
- Relationships: 26

## Generated Files

- `docs/UML/database/chen-notation-erd.puml`
- `docs/UML/database/chen-notation-erd.png`

## PlantUML Limitations

- Standard PlantUML does not support Chen relationship diamonds as first-class nodes in this diagram syntax. Relationship nodes are rendered as red/brown PlantUML rectangles labeled with `<>` to visually distinguish them from entity rectangles.
- PlantUML automatic layout produces a taller, line-heavy diagram than the Draw.io canvas. Hidden layout links were added to keep the major groups close to the requested positions, but exact Draw.io placement cannot be guaranteed.
- Attribute ovals are represented using PlantUML `usecase` nodes, which is the closest built-in pure PlantUML oval shape.
