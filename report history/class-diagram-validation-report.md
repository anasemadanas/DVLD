# Class Diagram Validation Report

Generated: 2026-06-18

## Source Files Reviewed

- `docs/UML/diagram/class-diagram.puml`
- `script.sql`

## Validation Summary

The current class diagram is best treated as a conceptual domain model, not an implementation-oriented database model. It communicates the main DVLD business objects, but it does not exactly mirror SQL table names, SQL Server data types, database columns, nullable fields, identity columns, FK constraints, or SQL-enforced cardinalities.

The diagram was updated only to clarify this intent:

- Title changed to `DVLD System - Conceptual Domain Model`.
- A note was added inside the PlantUML diagram explaining that it is not the physical database model and that `script.sql` plus `docs/UML/database/*-erd.puml` are authoritative for SQL-backed structure.

## Classes That Map Directly To SQL Tables

| Class | SQL Table | Mapping Quality | Notes |
|---|---|---|---|
| `Person` | `People` | Partial | Concept name differs from plural SQL table. Several attributes use business-friendly names. |
| `User` | `Users` | Partial | Core identity fields exist, but `UserName` casing and password storage semantics differ. |
| `Driver` | `Drivers` | Good | Main identifiers align conceptually. |
| `Application` | `Applications` | Partial | SQL has `ApplicantPersonID`, `ApplicationTypeID`, `CreatedByUserID`, and status/date fields. |
| `License` | `Licenses` | Partial | SQL has `LicenseClass`, `PaidFees`, and SQL Server data types not shown in the conceptual class. |
| `LicenseClass` | `LicenseClasses` | Good | Conceptual attributes broadly align. |
| `TestAppointment` | `TestAppointments` | Partial | SQL table includes `TestTypeID`, `LocalDrivingLicenseApplicationID`, `CreatedByUserID`, and `IsLocked`. |
| `TestType` | `TestTypes` | Partial | SQL uses `TestTypeTitle`, `TestTypeDescription`, and `TestTypeFees`. |
| `DetainedLicense` | `DetainedLicenses` | Partial | SQL has release user/application FKs and `IsReleased`; conceptual class includes `Reason`, which is not in SQL. |
| `InternationalLicense` | `InternationalLicenses` | Partial | SQL has `ApplicationID`, `DriverID`, `IssuedUsingLocalLicenseID`, and `CreatedByUserID`. |

## Conceptual-Only Classes

| Class | Reason |
|---|---|
| `AuditLog` | No matching SQL table exists in `script.sql`. Audit logging is a conceptual/system-design concern unless a future audit table is added. |
| `TestResult` | No separate SQL table exists. SQL stores test result data in the `Tests` table. |

## SQL Tables Missing From The Class Diagram

| SQL Table | Recommendation |
|---|---|
| `Countries` | Add to an implementation-oriented class model if the class diagram is ever synchronized to SQL. |
| `ApplicationTypes` | Add to implementation-oriented model or keep implicit in conceptual diagram. |
| `LocalDrivingLicenseApplications` | Add if modeling the database/application aggregate boundary. |
| `Tests` | Add if replacing conceptual `TestResult` with SQL-backed entities. |

## Attribute Naming Mismatches

| Class Attribute | SQL Equivalent | Notes |
|---|---|---|
| `Person.NationalNumber` | `People.NationalNo` | Conceptual naming differs. |
| `Person.PhoneNumber` | `People.Phone` | Conceptual naming differs. |
| `Person.Nationality` | `People.NationalityCountryID` plus `Countries` | Concept hides FK relationship. |
| `Person.PersonalPhoto` | `People.ImagePath` | Conceptual naming differs. |
| `Application.ApplicationType` | `Applications.ApplicationTypeID` plus `ApplicationTypes` | Concept hides FK relationship. |
| `Application.Status` | `Applications.ApplicationStatus` | Conceptual naming differs. |
| `License.ExpiryDate` | `Licenses.ExpirationDate` | Conceptual naming differs. |
| `License.LicenseNumber` | None | No direct SQL column exists in `Licenses`. |
| `License.IssueReason` | `Licenses.IssueReason` | SQL type is `tinyint`, not string. |
| `LicenseClass.ValidityLength` | `LicenseClasses.DefaultValidityLength` | Conceptual naming differs. |
| `TestAppointment.AppointmentID` | `TestAppointments.TestAppointmentID` | Conceptual naming differs. |
| `TestType.TestTypeName` | `TestTypes.TestTypeTitle` | SQL naming differs. |
| `TestType.Fees` | `TestTypes.TestTypeFees` | Conceptual naming differs. |
| `DetainedLicense.DetentionID` | `DetainedLicenses.DetainID` | Conceptual naming differs. |
| `DetainedLicense.DetentionDate` | `DetainedLicenses.DetainDate` | Conceptual naming differs. |
| `DetainedLicense.FineAmount` | `DetainedLicenses.FineFees` | Conceptual naming differs. |
| `DetainedLicense.Reason` | None | No direct SQL column exists. |
| `InternationalLicense.ExpiryDate` | `InternationalLicenses.ExpirationDate` | Conceptual naming differs. |

## Relationship And Cardinality Mismatches

| Diagram Relationship | SQL-Backed Finding | Recommendation |
|---|---|---|
| `Person "1" -- "0..1" User` | `Users.PersonID` is an FK to `People.PersonID`, but no UNIQUE constraint exists in `script.sql`. | Treat as business optional one-to-one, technically one-to-many unless UNIQUE is added. |
| `Person "1" -- "0..1" Driver` | `Drivers.PersonID` is an FK to `People.PersonID`, but no UNIQUE constraint exists in `script.sql`. | Treat as business optional one-to-one, technically one-to-many unless UNIQUE is added. |
| `Application "1" -- "0..*" TestAppointment` | SQL links `TestAppointments` to `LocalDrivingLicenseApplications`, not directly to `Applications`. | Keep conceptual or route through `LocalDrivingLicenseApplications` in implementation model. |
| `TestAppointment "1" -- "0..1" TestResult` | SQL has `Tests.TestAppointmentID` FK with no UNIQUE constraint. | Technically one-to-many unless business logic enforces one test result per appointment. |
| `User "1" -- "0..*" AuditLog` | No `AuditLog` SQL table exists. | Keep as conceptual service/audit concern or add an audit table in a future schema change. |

## Recommendation

Do not force this class diagram to become the physical database model. Keep it as a conceptual domain model for business and design discussion. Use the synchronized database diagrams and `script.sql` for implementation-level table, column, type, PK/FK, and cardinality validation.

If an implementation-oriented class diagram is required later, create a separate diagram instead of overwriting this conceptual view.

