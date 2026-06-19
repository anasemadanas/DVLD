use DVLD;

INSERT INTO ApplicationTypes (ApplicationTypeID, ApplicationTypeTitle, ApplicationFees) VALUES
(1, N'New Local Driving License Service', 15.0000),
(2, N'Renew Driving License Service', 5.0000),
(3, N'Replacement for a Lost Driving License', 10.0000),
(4, N'Replacement for a Damaged Driving License', 5.0000),
(5, N'Release Detained Driving Licsense', 15.0000),
(6, N'New International License', 50.0000);

select * from applicationtypes;