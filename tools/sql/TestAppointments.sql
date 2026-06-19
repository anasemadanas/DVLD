use DVLD;


INSERT INTO TestAppointments (TestAppointmentID, TestTypeID, LocalDrivingLicenseApplicationID, AppointmentDate, PaidFees, CreatedByUserID, IsLocked) VALUES
(65, 1, 30, '2023-09-24 03:25:00', 10.0000, 1, 1),
(66, 2, 30, '2023-09-24 03:25:00', 20.0000, 1, 1),
(67, 3, 30, '2023-09-24 03:25:00', 30.0000, 1, 1),
(68, 1, 31, '2023-09-24 13:49:00', 10.0000, 1, 1),
(69, 2, 31, '2023-09-24 13:50:00', 20.0000, 1, 1),
(70, 2, 31, '2023-09-25 13:51:00', 20.0000, 1, 1),
(71, 3, 31, '2023-09-28 13:52:00', 30.0000, 1, 1);

select * from testappointments;