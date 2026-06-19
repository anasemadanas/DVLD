create database DVLD;
go

use dvld;
go 

CREATE TABLE applications 
(applicationid int NOT NULL, applicantpersonid int NOT NULL, applicationdate datetime NOT NULL, applicationtypeid int NOT NULL, applicationstatus smallint NOT NULL DEFAULT 1, laststatusdate datetime NOT NULL, paidfees decimal(10,4) NOT NULL, createdbyuserid int NOT NULL, PRIMARY KEY (applicationid) );

CREATE TABLE applicationtypes (     applicationtypeid int NOT NULL,     applicationtypetitle varchar(150) NOT NULL,     applicationfees decimal(10,4) NOT NULL DEFAULT 0,     PRIMARY KEY (applicationtypeid) );

CREATE TABLE countries (     countryid int NOT NULL,     countryname varchar(50) NOT NULL,     PRIMARY KEY (countryid) );

CREATE TABLE detainedlicenses (     detainid int NOT NULL,     licenseid int NOT NULL,     detaindate datetime NOT NULL,     finefees decimal(10,4) NOT NULL,     createdbyuserid int NOT NULL,     isreleased bit NOT NULL DEFAULT 0,     releasedate datetime,     releasedbyuserid int,     releaseapplicationid int,     PRIMARY KEY (detainid) );

CREATE TABLE drivers (     driverid int NOT NULL,     personid int NOT NULL,     createdbyuserid int NOT NULL,     createddate datetime NOT NULL,     PRIMARY KEY (driverid) );

CREATE TABLE internationallicenses (     internationallicenseid int NOT NULL,     applicationid int NOT NULL,     driverid int NOT NULL,     issuedusinglocallicenseid int NOT NULL,     issuedate datetime NOT NULL,     expirationdate datetime NOT NULL,     isactive bit NOT NULL,     createdbyuserid int NOT NULL,     PRIMARY KEY (internationallicenseid) );

CREATE TABLE licenseclasses (     licenseclassid int NOT NULL,     classname varchar(50) NOT NULL,     classdescription varchar(500) NOT NULL,     minimumallowedage smallint NOT NULL DEFAULT 18,     defaultvaliditylength smallint NOT NULL DEFAULT 1,     classfees decimal(10,4) NOT NULL DEFAULT 0,     PRIMARY KEY (licenseclassid) );

CREATE TABLE licenses (     licenseid int NOT NULL,     applicationid int NOT NULL,     driverid int NOT NULL,     licenseclass int NOT NULL,     issuedate datetime NOT NULL,     expirationdate datetime NOT NULL,     notes varchar(500),     paidfees decimal(10,4) NOT NULL,     isactive bit NOT NULL DEFAULT 1,     issuereason smallint NOT NULL DEFAULT 1,     createdbyuserid int NOT NULL,     PRIMARY KEY (licenseid) );

CREATE TABLE localdrivinglicenseapplications (     localdrivinglicenseapplicationid int NOT NULL,     applicationid int NOT NULL,     licenseclassid int NOT NULL,     PRIMARY KEY (localdrivinglicenseapplicationid) );

CREATE TABLE people (     personid int NOT NULL,     nationalno varchar(20) NOT NULL,     firstname varchar(20) NOT NULL,     secondname varchar(20) NOT NULL,     thirdname varchar(20),     lastname varchar(20) NOT NULL,     dateofbirth datetime NOT NULL,     gendor smallint NOT NULL DEFAULT 0,     address varchar(500) NOT NULL,     phone varchar(20) NOT NULL,     email varchar(50),     nationalitycountryid int NOT NULL,     imagepath varchar(250),     PRIMARY KEY (personid) );

CREATE TABLE testappointments (     testappointmentid int NOT NULL,     testtypeid int NOT NULL,     localdrivinglicenseapplicationid int NOT NULL,     appointmentdate datetime NOT NULL,     paidfees decimal(10,4) NOT NULL,     createdbyuserid int NOT NULL,     islocked bit NOT NULL DEFAULT 0,     retaketestapplicationid int,     PRIMARY KEY (testappointmentid) );

CREATE TABLE tests (     testid int NOT NULL,     testappointmentid int NOT NULL,     testresult bit NOT NULL,     notes varchar(500),     createdbyuserid int NOT NULL,     PRIMARY KEY (testid) );


CREATE TABLE testtypes (     testtypeid int NOT NULL,     testtypetitle varchar(100) NOT NULL,     testtypedescription varchar(500) NOT NULL,     testtypefees decimal(10,4) NOT NULL,     PRIMARY KEY (testtypeid) );

CREATE TABLE users (     userid int NOT NULL,     personid int NOT NULL,     username varchar(20) NOT NULL,     password varchar(20) NOT NULL,     isactive bit NOT NULL,     PRIMARY KEY (userid) );