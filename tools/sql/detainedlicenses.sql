use dvld;

INSERT INTO detainedlicenses(DetainID, LicenseID, DetainDate, FineFees, CreatedByUserID, IsReleased, ReleaseDate, ReleasedByUserID, ReleaseApplicationID)
VALUES
(5, 14, '2023-09-25T08:53:00', 56.0000, 1, 0, NULL, NULL, NULL),
(6, 15, '2023-09-25T08:54:00', 60.0000, 1, 0, NULL, NULL, NULL);

select * from detainedlicenses;