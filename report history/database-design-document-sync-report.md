# Database Design Document Sync Report

Generated: 2026-06-18T21:12:54

## Source Of Truth

- `script.sql`

## Sections Updated

- Section 5 - Relationships
- Section 5.2 - Audit Relationships
- Section 6 - Primary Keys & Foreign Keys
- Section 7 - Constraints
- Section 8 - Data Dictionary

## Mismatches Fixed

- Replaced older or generic SQL type descriptions with SQL Server types parsed from `script.sql`.
- Preserved implemented column names such as `Gendor`, `LicenseClass`, `ApplicantPersonID`, `NationalityCountryID`, and `TestTypeTitle`.
- Rebuilt the Data Dictionary from the current 14-table, 88-column SQL Server schema.

## Relationship Cardinality Fixes

- Documented every FK as Parent Table `1` to Child Table `Many` unless a SQL UNIQUE constraint exists.
- Documented `People -> Users` as technically One-to-Many and optional One-to-One only as a business rule.
- Documented `People -> Drivers` as technically One-to-Many and optional One-to-One only as a business rule.
- Documented `Applications -> LocalDrivingLicenseApplications` as technically One-to-Many and optional One-to-One only as a business rule if intended.
- Moved user-created operational relationships into Section 5.2 Audit Relationships.

## PK/FK Fixes

- `People.NationalityCountryID` now references `Countries.CountryID`.
- `Applications.ApplicantPersonID` now references `People.PersonID`.
- `Licenses.LicenseClass` now references `LicenseClasses.LicenseClassID`.
- `LocalDrivingLicenseApplications.LocalDrivingLicenseApplicationID` is documented as the PK.
- All 26 FK constraint names from `script.sql` are included.

## Data Type Fixes

- `People.SecondName` is `nvarchar(20) NOT NULL`.
- `People.ThirdName` is `nvarchar(20) NULL`.
- `Licenses.IssueReason` is `tinyint NOT NULL`.
- `Applications.ApplicationStatus` is `tinyint NOT NULL`.
- `Applications.PaidFees`, `ApplicationTypes.ApplicationFees`, `LicenseClasses.ClassFees`, and fee fields are `smallmoney`.
- `IssueDate`, `ExpirationDate`, `AppointmentDate`, `DetainDate`, and `ReleaseDate` use the exact `datetime` or `smalldatetime` types from SQL.
- `Tests.TestResult` is `bit NOT NULL`.

## Validation Summary

- Tables documented: 14
- Columns documented: 88
- FK constraints documented: 26
- Missing required text: []
- Generic disallowed type mentions: []
- Missing tables: []
- Missing FK constraints: []

## Remaining Conflicts

- None identified in Sections 5-8 after synchronization.

## Notes

- `script.sql` was not modified.
- Database diagrams, PlantUML, and Draw.io files were not modified.
- Visual DOCX render QA was not completed because the available renderer dependency stack is incomplete in this environment; structural validation was completed with `python-docx`.
