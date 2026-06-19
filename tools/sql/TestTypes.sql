use dvld;


INSERT INTO TestTypes (TestTypeID, TestTypeTitle, TestTypeDescription, TestTypeFees) VALUES
(1, N'Vision Test', N'This assesses the applicant''s visual acuity to ensure they have sufficient vision to drive safely.', 10.0000),
(2, N'Written (Theory) Test', N'This test assesses the applicant''s knowledge of traffic rules, road signs, and driving regulations. It typically consists of multiple-choice questions, and the applicant must select the correct answer(s). The written test aims to ensure that the applicant understands the rules of the road and can apply them in various driving scenarios.', 20.0000),
(3, N'Practical (Street) Test', N'This test evaluates the applicant''s driving skills and ability to operate a motor vehicle safely on public roads. A licensed examiner accompanies the applicant in the vehicle and observes their driving performance.', 30.0000);


select * from testtypes;