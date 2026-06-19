# DVLD Driving License Management System

## Project Overview

The DVLD Driving License Management System is a desktop-based business
application for managing driver and vehicle licensing operations. It supports
the end-to-end lifecycle of people records, license applications, tests, local
licenses, international licenses, renewals, replacements, detentions, releases,
search, reporting, and administration.

The repository contains the application source, formal documentation, UML
diagrams, database design artifacts, reusable tooling, and persistent generated
outputs required to maintain the project in a reproducible enterprise workflow.

Main services include:

- User authentication and user administration
- Person and driver record management
- Local driving license application processing
- Vision, written, and practical test scheduling
- Test result recording
- Driving license issuance, renewal, and replacement
- International license issuance
- License detention and release
- Search, filtering, reporting, and audit support

## Repository Structure

```text
.
├── docs/                 Documentation, DOCX deliverables, and UML sources
│   └── UML/
│       ├── database/     ERD, EERD, schema, physical, logical, and overview diagrams
│       ├── design/       Architecture, deployment, UI flow, and system diagrams
│       └── diagram/      Use case, class, sequence, and activity diagrams
└── DVLD-Project/         Application source code and Visual Studio project files
```

Persistent tools, caches, generated outputs, and export logs live outside the
repository in `C:\Users\Public\DVLD-Workspace`.

## Documentation Structure

The project documentation set is maintained under `docs/`:

- `Driving_License_Management_SRS_1.0.docx` - Software Requirements Specification
- `Functional_Requirements_Specification.docx` - detailed functional requirements
- `System_Design_Document.docx` - system architecture and design documentation
- `Database_Design_Document.docx` - database design, relationships, constraints, and data dictionary
- `User_Guide.docx` - practical guide for DVLD employees
- `User_Stories.docx` - business user stories and stakeholder goals
- `DVLD - Project 1 - Requirements v1.docx` - original project requirements reference

Source DOCX files must be preserved. Temporary Word lock files such as
`~$*.docx` are not part of the documentation set and should be removed.

## UML Structure

UML sources live under `docs/UML` and are exported to matching PNG files.

- Architecture: layered architecture, component architecture, system interaction, and system overview
- ERD/EERD: conceptual, logical, physical, crow's foot, Chen notation, and enhanced ERD views
- Sequence diagrams: business workflow and service interaction scenarios
- Activity diagrams: operational process flows
- UI flow: navigation and screen-flow documentation
- Deployment: workstation, runtime, database, and support environment
- Database schema: SQL Server-oriented physical data model and overview

Each `.puml` file must have a matching `.png` export with the same basename.
Malformed export names such as `*.puml.png` should not be used.

## Tools and Technologies

- PlantUML for UML source rendering
- SQL Server for enterprise persistent storage
- Java runtime for PlantUML execution
- Python for DOCX automation and repository utility scripts
- LibreOffice or `soffice` for DOCX to PDF conversion and render verification
- Graphviz for PlantUML graph layout and direct DOT rendering
- Visual Studio / VS Code for development and documentation maintenance
- Markdown for repository-level documentation
- DOCX for formal deliverables

## Diagram Export Instructions

PlantUML is cached in the shared Windows workspace at:

```text
C:\Users\Public\DVLD-Workspace\tools\plantuml\plantuml.jar
```

Verify PlantUML without downloading again:

```powershell
java -jar C:\Users\Public\DVLD-Workspace\tools\plantuml\plantuml.jar -version
```

Render a single diagram:

```powershell
java -jar C:\Users\Public\DVLD-Workspace\tools\plantuml\plantuml.jar docs\UML\database\database-overview.puml
```

Render through the shared reusable helper:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass `
  -File C:\Users\Public\DVLD-Workspace\tools\bin\render-plantuml.ps1 `
  -InputFiles docs\UML\database\database-overview.puml
```

For full UML regeneration, delete stale PNG exports, validate all `.puml`
files, and render all sources with the cached project-local PlantUML jar.

## Workspace and Tool Persistence

Reusable tools and generated outputs are stored in a permanent shared Windows
workspace:

```text
C:\Users\Public\DVLD-Workspace
```

Primary persistent paths:

- `C:\Users\Public\DVLD-Workspace\tools\bin`
- `C:\Users\Public\DVLD-Workspace\tools\scripts`
- `C:\Users\Public\DVLD-Workspace\tools\plantuml\plantuml.jar`
- `C:\Users\Public\DVLD-Workspace\tools\java`
- `C:\Users\Public\DVLD-Workspace\tools\python`
- `C:\Users\Public\DVLD-Workspace\tools\libreoffice`
- `C:\Users\Public\DVLD-Workspace\tools\graphviz`
- `C:\Users\Public\DVLD-Workspace\tools\cache`
- `C:\Users\Public\DVLD-Workspace\generated`
- `C:\Users\Public\DVLD-Workspace\png`
- `C:\Users\Public\DVLD-Workspace\exports`
- `C:\Users\Public\DVLD-Workspace\logs`

The shared public workspace is the long-lived source of reusable tools, caches,
exports, and logs. Do not store reusable dependencies in repo-local temporary
folders, session-only cache paths, or operating-system runtime scratch
locations.

The repository root also contains `workspace-config.json`, which records the
current shared workspace root, tool paths, cache paths, export paths, and
generated output paths used by the helper scripts.

## Naming Conventions

- PlantUML sources use lowercase kebab-case where possible, for example
  `database-overview.puml` and `issue-driving-license-sequence.puml`.
- PNG exports use the same basename as the source, for example
  `database-overview.png`.
- Avoid malformed generated names such as `diagram.puml.png`.
- DOCX deliverables use descriptive PascalCase or title-style names with clear
  document purpose, such as `Database_Design_Document.docx`.
- Workspace exports preserve relative UML folders to avoid filename collisions.

## Future Enhancements

Planned enterprise evolution areas include:

- Web API layer for integration and service-based deployment
- Mobile application for applicant-facing services and notifications
- Cloud synchronization and centralized backup strategy
- Advanced reporting dashboards and operational analytics
- AI-assisted insights for test outcomes, renewal risk, and workload planning

## Validation Checklist

Before delivery or release:

- All `.puml` files compile successfully.
- Every `.puml` has a matching `.png`.
- No `*.puml.png` malformed exports remain.
- No temporary Word lock files remain.
- Source DOCX files are preserved.
- Generated outputs are preserved in `C:\Users\Public\DVLD-Workspace`.
- Tool dependencies are reused from `C:\Users\Public\DVLD-Workspace\tools`.

## License

This project is licensed under the MIT License.
