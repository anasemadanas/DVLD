use DVLD;


INSERT INTO LicenseClasses (LicenseClassID, ClassName, ClassDescription, MinimumAllowedAge, DefaultValidityLength, ClassFees) VALUES
(1, N'Class 1 - Small Motorcycle', N'It allows the driver to drive small motorcycles, It is suitable for motorcycles with small capacity and limited power.', 18, 5, 15.0000),
(2, N'Class 2 - Heavy Motorcycle License', N'Heavy Motorcycle License (Large Motorcycle License)', 21, 5, 30.0000),
(3, N'Class 3 - Ordinary driving license', N'Ordinary driving license (car licence)', 18, 10, 20.0000),
(4, N'Class 4 - Commercial', N'Commercial driving license (taxi/limousine)', 21, 10, 200.0000),
(5, N'Class 5 - Agricultural', N'Agricultural and work vehicles used in farming or construction, (tractors / tillage machinery)', 21, 10, 50.0000),
(6, N'Class 6 - Small and medium bus', N'Small and medium bus license', 21, 10, 250.0000),
(7, N'Class 7 - Truck and heavy vehicle', N'Truck and heavy vehicle license', 21, 10, 300.0000);


select * from licenseclasses;