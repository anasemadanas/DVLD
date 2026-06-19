use dvld;

INSERT INTO tests (TestID, TestAppointmentID, TestResult, Notes, CreatedByUserID)
VALUES
(29, 65, 1, NULL, 1),
(30, 66, 1, NULL, 1),
(31, 67, 1, NULL, 1),
(32, 68, 1, 'with Glasses', 1),
(33, 69, 0, NULL, 1),
(34, 70, 1, NULL, 1),
(35, 71, 1, NULL, 1);

select * from tests;