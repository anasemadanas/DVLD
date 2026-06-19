# DVLD UML Catalog

This catalog explains the UML library used by the DVLD documentation set. It helps readers understand which diagram to open, why it exists, who should use it, and which business area it supports.

## Architecture Diagrams

| File Name | Purpose | Audience | Related Module |
|---|---|---|---|
| `design/architecture.puml` | Presents the enterprise layered architecture with presentation, business, data access, and database layers. | Architects, developers, reviewers | System-wide architecture |
| `design/component_architecture.puml` | Shows major services, repositories, and supporting components at component level. | Developers, architects | Service layer and component structure |
| `design/system-architecture.puml` | Summarizes system architecture and major runtime relationships. | Architects, onboarding engineers | System-wide architecture |
| `design/system-diagram.puml` | Shows high-level system interaction across users, application layers, and persistence. | Stakeholders, developers | System overview |
| `design/module-interaction.puml` | Explains how major business modules interact with one another. | Developers, analysts | Cross-module interaction |
| `design/deployment.puml` | Documents deployment and runtime hosting relationships. | Architects, infrastructure reviewers | Deployment and runtime topology |

## Sequence Diagrams

| File Name | Purpose | Audience | Related Module |
|---|---|---|---|
| `diagram/general-sequence-diagram.puml` | Provides a generic request-response interaction pattern for the DVLD application. | Developers, students, reviewers | General application flow |
| `diagram/issue-driving-license-sequence.puml` | Captures the real business workflow for issuing a first driving license with eligibility and test validation branches. | Developers, QA, business reviewers | License issuance |
| `diagram/sequence-license-issuance.puml` | Shows the broader license issuance workflow at sequence level. | Developers, QA | License issuance |
| `diagram/sequence-license-renewal.puml` | Describes the renewal service interaction flow. | Developers, QA | License renewal |
| `diagram/sequence-license-release.puml` | Describes release of a detained license after payment and validation. | Developers, QA | License release |
| `diagram/sequence-license-detention.puml` | Shows the detention workflow interaction between UI, services, and persistence. | Developers, QA | License detention |
| `diagram/sequence-lost-license-replacement.puml` | Documents the lost-license replacement business flow. | Developers, QA | Lost license replacement |
| `diagram/sequence-damaged-license-replacement.puml` | Documents the damaged-license replacement business flow. | Developers, QA | Damaged license replacement |
| `diagram/sequence-retake-test.puml` | Shows the retake test workflow and supporting checks. | Developers, QA | Retake test service |
| `diagram/service-seq/sequence-first-time-license-issuance.puml` | Shows first-time license issuance with service-level interaction detail. | Developers, architects | License issuance services |
| `diagram/service-seq/sequence-general-operation.puml` | Shows a general service orchestration pattern for common operations. | Developers, onboarding engineers | Shared service interaction |
| `diagram/service-seq/sequence-international-license.puml` | Shows the service-level flow for international license issuance. | Developers, QA | International licenses |
| `diagram/service-seq/sequence-license-detention-release.puml` | Shows end-to-end detention and release interactions at service level. | Developers, QA | Detention and release |
| `diagram/service-seq/sequence-license-renewal.puml` | Shows renewal behavior at service orchestration level. | Developers, QA | License renewal |
| `diagram/service-seq/sequence-test-management.puml` | Shows scheduling, result recording, and test sequencing logic. | Developers, QA | Test management |
| `sequence/login-auth-sequence.puml` | Shows login authentication, password verification, active-user checks, audit logging, and database-error handling. | Developers, QA, security reviewers | Authentication and user access |

## Activity Diagrams

| File Name | Purpose | Audience | Related Module |
|---|---|---|---|
| `diagram/general-activity-diagram.puml` | Shows a general activity pattern for DVLD business workflows. | Analysts, developers | General workflow reference |
| `diagram/license-issuance-activity.puml` | Documents the real business activity flow for license issuance including rejection paths. | QA, developers, business reviewers | License issuance |
| `diagram/activity-license-issuance.puml` | Shows the main issuance activity flow from validation through confirmation. | Developers, QA | License issuance |
| `diagram/activity-license-renewal.puml` | Shows renewal decision points and processing sequence. | Developers, QA | License renewal |
| `diagram/activity-license-detention-release.puml` | Covers detention and release decision flow. | Developers, QA | Detention and release |
| `diagram/activity-international-license.puml` | Shows international license issuance activity logic. | Developers, QA | International licenses |
| `diagram/activity-lost-license-replacement.puml` | Shows lost-license replacement flow and validation points. | Developers, QA | Lost license replacement |
| `diagram/activity-damaged-license-replacement.puml` | Shows damaged-license replacement flow and validation points. | Developers, QA | Damaged license replacement |
| `diagram/activity-retake-test.puml` | Shows retake test eligibility and execution flow. | Developers, QA | Test management |

## ERD / EERD Diagrams

| File Name | Purpose | Audience | Related Module |
|---|---|---|---|
| `database/conceptual-erd.puml` | Presents the conceptual data model at business entity level. | Analysts, architects | Database conceptual model |
| `database/chen-notation-erd.puml` | Presents conceptual entities and relationships using Chen notation. | Analysts, database reviewers | Database conceptual model |
| `database/crows-foot-erd.puml` | Presents cardinality-focused ERD using crow's foot notation. | DBAs, developers | Database logical relationships |
| `database/logical-erd.puml` | Shows the logical database design and key table relationships. | Developers, DBAs | Database logical design |
| `database/physical-erd.puml` | Shows the physical implementation-oriented ERD. | DBAs, developers | Database physical design |
| `database/eerd.puml` | Shows enhanced entity relationships for inheritance and extended business structure. | Architects, DBAs | Enhanced database model |
| `database/dvld-erd.puml` | Provides a DVLD-specific ERD view for the overall data model. | Developers, reviewers | Core database model |

## Database Diagrams

| File Name | Purpose | Audience | Related Module |
|---|---|---|---|
| `database/database-overview.puml` | Provides a presentation-friendly overview of the main DVLD entities and high-level relationships. | Stakeholders, architects, onboarding engineers | Database overview |
| `database/database-schema.puml` | Shows the schema-oriented database view used alongside the database design document. | Developers, DBAs | Database schema |

## Deployment Diagram

| File Name | Purpose | Audience | Related Module |
|---|---|---|---|
| `design/deployment.puml` | Documents deployment nodes, application placement, and SQL Server persistence environment. | Architects, infrastructure reviewers | Deployment and environment |

## UI Flow Diagrams

| File Name | Purpose | Audience | Related Module |
|---|---|---|---|
| `design/ui-flow-navigation.puml` | Shows user navigation between primary screens and modules. | UX reviewers, developers, testers | UI navigation |
| `design/screen-flow.puml` | Shows screen-to-screen workflow progression. | Developers, QA, onboarding users | Screen flow |
| `design/system-inputs.puml` | Documents major system inputs and user-driven entry points. | Analysts, developers | Input flow |
| `design/state_user_session.puml` | Shows the session state lifecycle from sign-in through logout. | Developers, QA | User session management |

## State Diagrams

| File Name | Purpose | Audience | Related Module |
|---|---|---|---|
| `state/application-state-diagram.puml` | Shows application lifecycle states from submission through validation, processing, completion, cancellation, or rejection. | Analysts, developers, QA | Application processing |
| `state/license-state-diagram.puml` | Shows license lifecycle states including active, expired, renewed, replaced, detained, released, and inactive. | Analysts, developers, QA | License lifecycle |

## Use Case and Class Diagrams

| File Name | Purpose | Audience | Related Module |
|---|---|---|---|
| `diagram/use-case-diagram.puml` | Shows the complete use case landscape for DVLD business actors. | Stakeholders, analysts, developers | System use cases |
| `diagram/use-case-diagram-base.puml` | Provides a simplified or baseline use case view for documentation support. | Analysts, onboarding readers | Use case baseline |
| `diagram/class-diagram.puml` | Shows object model structure and key domain classes. | Developers, reviewers | Domain model |

## How To Use This Catalog

Open architecture diagrams first when you need system context, then move to sequence and activity diagrams for business workflows, and finally use the ERD and schema views when you need data-model detail. For QA and business validation work, start with the use case, sequence, and activity sections before drilling into service-level diagrams.
