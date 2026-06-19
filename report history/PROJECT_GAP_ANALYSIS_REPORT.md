# DVLD Project Gap Analysis Report

Generated: 2026-06-18

## Executive Summary

The DVLD project has a strong documentation foundation: formal DOCX documents exist for requirements, design, database design, user guidance, user stories, traceability, and QA; the UML library is broad; and the database diagrams have recently been synchronized from `script.sql` as the authoritative implementation source.

The main enterprise gaps are not a lack of diagrams or documents. The remaining issues are traceability depth, consistency between document names and current files, measurable non-functional requirements, class/domain model alignment with the SQL-backed vocabulary, and stronger QA coverage for negative, security, concurrency, recovery, and operational scenarios.

Overall readiness is good for portfolio or internal handoff, but still below strict enterprise handoff quality until traceability, NFR testability, security/operations detail, and class/design consistency are tightened.

## Review Scope And Evidence

Reviewed document set:

- `docs/Driving_License_Management_SRS_1.0.docx`
- `docs/Functional_Requirements_Specification_FRS.docx`
- `docs/System_Design_Document_SDD.docx`
- `docs/Database_Design_Document.docx`
- `docs/User_Guide.docx`
- `docs/User_Stories.docx`
- `docs/Requirements_Traceability_Matrix.docx`
- `docs/QA_Test_Plan.docx`

Name/version drift found:

- Requested `docs/Functional_Requirements_Specification.docx` is not present in the current worktree; `docs/Functional_Requirements_Specification_FRS.docx` is present and was reviewed.
- Requested `docs/System_Design_Document.docx` is not present in the current worktree; `docs/System_Design_Document_SDD.docx` is present and was reviewed.

Reviewed UML and database sources:

- Use case, class, sequence, activity, service sequence, architecture, deployment, UI flow, and database PlantUML files under `docs/UML`.
- `script.sql`
- SQL-synchronized database PUML and Draw.io files under `docs/UML/database`.

Current database synchronization evidence:

- Tables parsed from `script.sql`: 14
- Columns parsed: 88
- PK columns parsed: 14
- FK constraints parsed: 26
- Unique constraints found in SQL: 0
- Database Draw.io files contain native editable XML shapes/connectors and no embedded image wrappers.

## Strengths

- The project has an unusually complete documentation set for a desktop application: SRS, FRS, SDD, database design, user guide, user stories, RTM, and QA plan all exist in usable form.
- The database diagrams are now grounded in `script.sql`, including SQL Server data types, nullability, identity columns, PKs, FKs, and real FK constraint names.
- UML coverage is broad: architecture, deployment, use case, class, activity, sequence, service sequence, UI flow, and several ERD styles are present.
- Critical business workflows already have sequence or activity coverage, including license issuance, renewal, replacement, detention/release, international license issuance, retake testing, and test management.
- The user guide is practical and workflow-oriented, with six screenshot placeholders already present.
- The Requirements Traceability Matrix exists and maps user stories to FR IDs, use cases, services, tables, UML diagrams, and test cases.
- The QA test plan includes 20 sample test cases and covers functional, validation, security, usability, integration, regression, database, and error-handling test types.

## Weaknesses

- Traceability is incomplete. The SRS contains `FR-01` through `FR-17` and `NFR-01` through `NFR-17`, while the FRS, user stories, RTM, and QA plan do not consistently cover all of those IDs.
- The current RTM maps 15 user stories and `TC-01` through `TC-15`, while the QA plan contains `TC-01` through `TC-20`; `TC-16` through `TC-20` are not fully represented in the RTM.
- The class diagram uses a simplified domain vocabulary that does not fully align with `script.sql`: examples include `NationalNumber` instead of `NationalNo`, `TestResult` as a class rather than the SQL `Tests` table, `AuditLog` without a matching SQL table, and one-to-one person/user/driver cardinalities that are not enforced by unique constraints in the database.
- Non-functional requirements exist in the SRS, but they are not consistently measurable, traced, or tested.
- Several enterprise operational concerns are thin: backup/restore, retention, audit retention, role-permission matrix depth, encryption, deployment configuration, exception logging, monitoring, migration/versioning, and recovery procedures.
- The use case diagram covers major actor interactions but does not show `include`/`extend` relationships for validation, payment, audit logging, test prerequisites, or duplicate checks.
- Some UML diagrams overlap in purpose, especially general sequence/activity diagrams versus business-specific and service-level diagrams. The UML catalog helps, but diagram-level traceability could be stronger.

## Missing Requirements

Critical missing or incomplete requirement areas:

- Full traceability for every SRS `FR-*`, `NFR-*`, and `BR-*` item into user stories, use cases, design elements, database tables, and QA tests.
- Measurable NFR acceptance criteria, including performance targets, availability expectations, backup/recovery objectives, security requirements, audit retention, maintainability, usability, and accessibility.
- Explicit role-permission matrix for each module and operation, including read/create/update/delete, approval, issuance, detention, release, and administrative configuration.
- Data retention and audit policy for applications, tests, licenses, user actions, detention records, and images.
- Security requirements for password storage, authentication failure behavior, inactive users, session timeout, least privilege, database credential handling, and sensitive data exposure.
- Error handling requirements for failed database writes, duplicate applications, locked appointments, detained licenses, inactive users, and partial workflow failures.

Recommended requirement improvements:

- Add requirement priority, source, owner, status, and verification method columns where practical.
- Split broad requirements such as license services into separately testable sub-requirements with stable IDs.
- Add preconditions and postconditions for core workflows: issue license, renew license, replace license, detain license, release license, schedule tests, and record results.
- Add explicit business rules for fees, application status transitions, test ordering, retake eligibility, active license rules, and international license constraints.

Optional requirement improvements:

- Add glossary terms for local license, international license, detained license, release application, license class, test appointment, retake, and active/inactive license.
- Add out-of-scope and future-scope sections so API/cloud/mobile roadmap ideas do not look like current implementation commitments.

## Missing UML

Critical UML gaps:

- Update or qualify the class diagram so it aligns with the SQL-backed domain vocabulary and documented business entities. Current class names/properties are useful conceptually, but not implementation-accurate.
- Add traceability labels or references from major use cases and workflow diagrams back to `FR`, `US`, and `TC` IDs.
- Add a permission/role access diagram or matrix view if role-based access is expected to be reviewed as enterprise documentation.

Recommended UML improvements:

- Add a state machine diagram for application lifecycle: New, Cancelled, Completed, and any blocked/failed states.
- Add a state machine diagram for license lifecycle: Active, Inactive, Expired, Detained, Released, Replaced, Renewed.
- Add a state machine diagram for test appointment lifecycle: Scheduled, Locked, Passed, Failed, Retake Required, Cancelled if supported.
- Add or refine sequence diagrams for payment/fee handling, login/authentication, user administration, person registration, and search/reporting.
- Add `include`/`extend` relationships in the use case diagram for validation, fee payment, audit logging, duplicate checks, and eligibility checks.
- Add package/component diagrams that distinguish current desktop layers from any future API concepts.

Optional UML improvements:

- Add a data flow diagram for applicant data, images, tests, license records, and reports.
- Add a report/search flow diagram if reporting becomes a formal business capability.
- Add a diagram purpose banner or note inside high-overlap diagrams to reduce reader confusion.

## Sequence Diagram Review

Validated existing sequence coverage:

- General sequence diagram exists.
- Issue driving license sequence diagram exists and includes eligibility, tests, driver creation, and license persistence.
- License renewal sequence diagram exists.
- International license issuance sequence diagram exists.
- License detention/release sequence diagram exists.
- Test management sequence diagram exists.
- Lost/damaged replacement and retake test sequence diagrams exist.

Recommended additional or refined sequence diagrams:

- Critical: Authentication and authorization sequence, including inactive user and invalid credential branches.
- Critical: Payment/fee recording sequence, because fee status gates several workflows.
- Recommended: Person registration/update sequence, including NationalNo uniqueness and country reference validation.
- Recommended: Application status transition sequence, showing application creation, validation, cancellation, completion, and last status date updates.
- Recommended: Search/reporting sequence, especially if reporting is part of formal user expectations.
- Optional: Admin reference-data maintenance sequence for application types, license classes, and test types.

## Activity Diagram Review

Validated existing activity coverage:

- General activity diagram exists.
- License issuance activity diagram exists.
- Renewal, international license, detention/release, replacement, and retake activity diagrams exist.

Recommended additional or refined activity diagrams:

- Critical: Application lifecycle activity from applicant selection through application completion/cancellation.
- Recommended: Authentication/session activity including lockout or inactive user behavior if supported.
- Recommended: Fee payment and receipt workflow.
- Recommended: Test scheduling and result locking workflow with retake path.
- Optional: Admin maintenance workflow for users, application types, test types, and license classes.

## System Design Review

Strengths:

- Layered architecture is clear: presentation, business, data access, and SQL Server database.
- Services are named for core business concerns: authentication, user, application, license, test, validation, and audit.
- Deployment diagram correctly reflects a desktop application talking to a SQL Server database.
- Error handling, logging, security, services, design patterns, and role matrix concepts are present in the System Design Document.

Gaps:

- Repository coverage should be explicit for every SQL table or aggregate: People, Countries, Users, Drivers, Applications, ApplicationTypes, LicenseClasses, Licenses, InternationalLicenses, DetainedLicenses, TestTypes, TestAppointments, and Tests.
- Transaction boundaries are not concrete enough for multi-step workflows such as license issuance, release after fine payment, international license issuance, and test result locking.
- Logging and audit design needs clearer distinction between application logs, audit records, database constraints, and user-visible errors.
- Deployment documentation should include environment configuration, connection strings, backup/restore, database permissions, and workstation setup.
- Security design needs stronger treatment of password storage, session timeout, database credentials, least privilege, and sensitive image/file path handling.

## Database Design Review

Strengths:

- `script.sql` is now the database source of truth.
- Current database diagrams reflect 14 tables, 88 columns, 14 PK columns, and 26 FK constraints.
- SQL Server types are preserved exactly in the synchronized diagrams.
- No SQL unique constraints are present, so one-to-one claims should not be treated as technically enforced.

Gaps:

- Business uniqueness rules should be documented separately from SQL-enforced uniqueness. For example, duplicate active application prevention or active international license prevention may be business rules unless enforced by constraints/indexes.
- Database Design Document should be rechecked against `script.sql` after the recent database diagram sync.
- Indexing strategy is not enterprise-ready. FK indexes, search indexes, and status/date indexes should be documented if expected.
- Delete/update behavior for all FKs should be explicitly documented.
- Migration/versioning strategy is missing.
- Backup/restore and data retention are not detailed enough for enterprise operations.

## User Guide Review

Strengths:

- Covers major employee workflows.
- Includes troubleshooting and support guidance.
- Includes screenshot placeholders.
- Uses step/action/expected-result style in several areas.

Gaps:

- Screenshots are placeholders rather than final images.
- Role-specific quick paths should be stronger for Administrator, Licensing Employee, and Test Officer.
- Operational guidance for failed transactions, duplicate records, blocked applications, locked appointments, and database/server connectivity is thin.
- There is limited guidance for data correction versus technical escalation.
- There is no dedicated section for common business-rule errors and what staff should do next.

## User Stories Review

Strengths:

- 15 user stories exist.
- Each story has business area, role, acceptance criteria, priority, and related FR ID.
- Main business workflows are represented.

Gaps:

- Stories do not cover all SRS `FR-*` and `NFR-*` IDs.
- Acceptance criteria are present but mostly high-level; several need Given/When/Then or testable rule detail.
- Edge-case stories are underrepresented: inactive user, invalid permissions, duplicate active application, duplicate active license, detained license restrictions, failed payment, failed database save, and retake restrictions.
- Dependencies between stories are not documented.
- There is no release/sprint grouping or status field.

## Missing Test Coverage

Critical missing or under-traced test coverage:

- NFR verification tests for performance, security, availability, backup/restore, audit retention, usability, and maintainability.
- Permission/role negative tests for each restricted workflow.
- Transaction rollback tests for multi-step license issuance, detention/release, renewal, and international license issuance.
- Database constraint tests for every FK relationship and nullability rule.
- Data migration/restore validation tests.

Recommended test improvements:

- Extend RTM so all 20 QA test cases are mapped.
- Add negative tests for duplicate applications, duplicate appointments, invalid status transitions, detained licenses, inactive users, and missing payment.
- Add report/search tests for filters, invalid criteria, empty results, and large result sets.
- Add regression suites grouped by critical workflow.

Optional test improvements:

- Add exploratory test charters for employee usability.
- Add screenshot-based user guide verification.
- Add SQL smoke tests for schema drift detection.

## Enterprise Readiness Scores

| Area | Score | Rationale |
|---|---:|---|
| SRS | 7.0 / 10 | Broad FR/NFR/BR coverage exists, but traceability and measurable acceptance criteria need work. |
| Functional Requirements | 7.2 / 10 | Good module coverage and acceptance criteria additions, but not aligned with all SRS IDs. |
| System Design | 7.4 / 10 | Strong layered direction, but transaction, security, deployment, and repository specifics need more rigor. |
| Database Design | 8.0 / 10 | SQL-backed diagrams are now strong; remaining gaps are indexes, migration, retention, and enforced-vs-business uniqueness. |
| UML | 7.8 / 10 | Broad diagram library with many workflow diagrams; class diagram and traceability need improvement. |
| User Guide | 7.4 / 10 | Practical workflow guidance; final screenshots and deeper troubleshooting are still needed. |
| User Stories | 7.0 / 10 | Good story structure; coverage, edge cases, and dependency/status tracking need improvement. |
| QA Plan | 7.2 / 10 | Useful 20-case baseline; needs full RTM linkage, NFR tests, negative tests, and rollback tests. |

Overall enterprise readiness: 7.4 / 10.

## Prioritized Recommendations

### A. Critical Missing Items

- Complete traceability across SRS `FR-*`, `NFR-*`, `BR-*`, FRS IDs, user stories, use cases, UML diagrams, services, database tables, and QA tests.
- Reconcile requested document filenames with current repository filenames, especially `Functional_Requirements_Specification_FRS.docx` and `System_Design_Document_SDD.docx`.
- Update or explicitly label the class diagram as conceptual, because it does not currently match the SQL-backed data model closely enough for implementation review.
- Add measurable NFR acceptance criteria and NFR test cases.
- Add authentication/authorization and payment/fee sequence coverage or strengthen existing diagrams to include those critical branches.
- Extend the RTM to include all QA test cases, especially `TC-16` through `TC-20`.

### B. Recommended Improvements

- Add state diagrams for application, license, and test appointment lifecycles.
- Add stronger transaction and rollback design for multi-step operations.
- Document role-permission coverage per module and operation.
- Document backup, restore, retention, migration, and deployment configuration.
- Add database index strategy and clarify which uniqueness rules are SQL-enforced versus business-enforced.
- Add Given/When/Then style acceptance criteria for high-priority user stories.
- Add negative and edge-case user stories for blocked, duplicate, inactive, detained, failed, and retake scenarios.
- Add final screenshots to the User Guide.

### C. Optional Improvements

- Add data flow diagrams for images, applications, test results, licenses, and reports.
- Add glossary and acronym sections across the document set.
- Add document status/owner/reviewer metadata to every formal DOCX.
- Add diagram purpose notes inside overlapping diagrams.
- Add a recurring documentation review checklist under `docs/reviews`.

### D. Do Not Change

- Do not redesign the database schema unless a real inconsistency is found against `script.sql`.
- Do not remove the multiple ERD views; they are useful as different stakeholder views now that the implementation diagrams are synchronized.
- Do not remove the existing workflow sequence/activity diagrams; improve traceability and labels instead.
- Do not rewrite the DOCX set from scratch. The current documents are a solid base and should be improved incrementally.
- Do not remove generated PNG exports or Draw.io files that correspond to the synchronized database diagrams.

## Final Gap Analysis

The DVLD project is in good shape as a documentation-heavy desktop application project. It has enough materials to explain the system to developers, QA, and business reviewers. The highest-value next step is a traceability and verification pass: every requirement should connect to a user story, use case, design component, UML diagram, database object where relevant, and QA test.

The second-highest-value step is design consistency. The database diagrams now follow `script.sql`, but the class diagram and some business/design documents still need to be checked against the same vocabulary and relationship rules. In particular, any optional one-to-one business interpretation should be documented as business-level unless a SQL unique constraint enforces it.

The third-highest-value step is enterprise operational depth. Security, logging, backup/restore, retention, deployment configuration, transaction boundaries, and recovery behavior are the areas that most clearly separate a strong academic/portfolio package from a strict enterprise handoff package.

