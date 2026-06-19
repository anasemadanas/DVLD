use dvld;

INSERT INTO People (PersonID, NationalNo, FirstName, SecondName, ThirdName, LastName, DateOfBirth, Gendor, Address, Phone, Email, NationalityCountryID, ImagePath) VALUES
(1, N'N1', N'Mohammed', N'Saqer', N'Mussa', N'Abu-Hadhoud', '1977-11-06 00:00:00', 0, N'Amman Jubaiha1', N'999876', N'Msaqer@gmail.com', 90, N'C:\DVLD-People-Images\93776d4e-f437-4b5c-a9eb-a831b42af6eb.png'),
(1023, N'N2', N'Omar', N'Mohammed', N'Saqer', N'Abu-Hadhoud', '2005-06-01 20:13:44', 0, N'Amman 20091-Street', N'07992992', N'Omar@g.com', 90, NULL),  --ImagePath is NULL here
(1024, N'N3', N'Hamzeh', N'Mohammed', N'Saqer', N'Abu-Hadhoud', '2005-09-23 21:05:06', 0, N'Amman', N'234566', N'H@H.com', 90, N'C:\DVLD-People-Images\c69c1ea5-2738-4f0b-baa5-b76810c5c9ee.png'),
(1025, N'n4', N'Khalid', N'ALi', N'Maher', N'hamed', '2005-09-24 13:32:14', 0, N'Amman - Uni street 8938', N'566543', N'Kh@k.com', 90, N'C:\DVLD-People-Images\eefc59c8-9471-43a5-b786-f476fe7843af.jpg');


select * from people;