--
-- File generated with SQLiteStudio v3.4.4 on Mon Jul 8 23:51:29 2024
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: dependent
DROP TABLE IF EXISTS dependent;
CREATE TABLE dependent (
    DepID INTEGER PRIMARY KEY AUTOINCREMENT, 
    ReferenceCode INTEGER NOT NULL, 
    DepName TEXT NOT NULL, 
    DepIsChild INTEGER CHECK(DepIsChild IN (0, 1)) NOT NULL, 
    DepIsWorking INTEGER CHECK(DepIsWorking IN (0, 1)) NOT NULL, 
    DepOccupation TEXT, 
    DepIncome REAL, 
    DepBirthdate DATE NOT NULL,
    FOREIGN KEY (ReferenceCode) REFERENCES senior (ReferenceCode)
);
INSERT INTO dependent (DepID, ReferenceCode, DepName, DepIsChild, DepIsWorking, DepOccupation, DepIncome, DepBirthdate) VALUES (1, 1, 'One Dela Cruz', 1, 1, 'Teacher', 40000.0, '1993-12-07');
INSERT INTO dependent (DepID, ReferenceCode, DepName, DepIsChild, DepIsWorking, DepOccupation, DepIncome, DepBirthdate) VALUES (2, 1, 'Two Dela Cruz', 0, 1, 'Cashier', 30000.0, '1997-01-17');
INSERT INTO dependent (DepID, ReferenceCode, DepName, DepIsChild, DepIsWorking, DepOccupation, DepIncome, DepBirthdate) VALUES (3, 1, 'Three Dela Cruz', 0, 0, NULL, NULL, '2000-07-18');
INSERT INTO dependent (DepID, ReferenceCode, DepName, DepIsChild, DepIsWorking, DepOccupation, DepIncome, DepBirthdate) VALUES (4, 2, 'Moka Pinaglabanan', 1, 1, 'Call Center Agent', 25000.0, '1982-02-27');
INSERT INTO dependent (DepID, ReferenceCode, DepName, DepIsChild, DepIsWorking, DepOccupation, DepIncome, DepBirthdate) VALUES (5, 2, 'Ubeka Pinaglabanan', 0, 1, 'Accountant', 45000.0, '1986-08-14');
INSERT INTO dependent (DepID, ReferenceCode, DepName, DepIsChild, DepIsWorking, DepOccupation, DepIncome, DepBirthdate) VALUES (6, 3, 'Ana Santos', 1, 1, 'Nurse', 35000.0, '1960-04-12');
INSERT INTO dependent (DepID, ReferenceCode, DepName, DepIsChild, DepIsWorking, DepOccupation, DepIncome, DepBirthdate) VALUES (7, 4, 'Roberto Rivera', 1, 1, 'Engineer', 50000.0, '1965-08-09');
INSERT INTO dependent (DepID, ReferenceCode, DepName, DepIsChild, DepIsWorking, DepOccupation, DepIncome, DepBirthdate) VALUES (8, 5, 'Elena Guzman', 1, 0, NULL, NULL, '1970-05-25');
INSERT INTO dependent (DepID, ReferenceCode, DepName, DepIsChild, DepIsWorking, DepOccupation, DepIncome, DepBirthdate) VALUES (9, 6, 'Carmen Reyes', 1, 1, 'Teacher', 40000.0, '1962-11-10');
INSERT INTO dependent (DepID, ReferenceCode, DepName, DepIsChild, DepIsWorking, DepOccupation, DepIncome, DepBirthdate) VALUES (10, 7, 'Luis Dizon', 1, 1, 'Architect', 55000.0, '1975-03-17');
INSERT INTO dependent (DepID, ReferenceCode, DepName, DepIsChild, DepIsWorking, DepOccupation, DepIncome, DepBirthdate) VALUES (11, 8, 'Juan Garcia', 1, 1, 'Doctor', 70000.0, '1970-08-15');
INSERT INTO dependent (DepID, ReferenceCode, DepName, DepIsChild, DepIsWorking, DepOccupation, DepIncome, DepBirthdate) VALUES (12, 8, 'Marta Garcia', 1, 0, NULL, NULL, '1975-11-22');
INSERT INTO dependent (DepID, ReferenceCode, DepName, DepIsChild, DepIsWorking, DepOccupation, DepIncome, DepBirthdate) VALUES (13, 9, 'Josefina Santos', 1, 1, 'Lawyer', 80000.0, '1968-03-14');
INSERT INTO dependent (DepID, ReferenceCode, DepName, DepIsChild, DepIsWorking, DepOccupation, DepIncome, DepBirthdate) VALUES (14, 10, 'Luis Reyes', 1, 1, 'Engineer', 60000.0, '1972-12-10');
INSERT INTO dependent (DepID, ReferenceCode, DepName, DepIsChild, DepIsWorking, DepOccupation, DepIncome, DepBirthdate) VALUES (15, 11, 'Celia Cruz', 1, 0, NULL, NULL, '1977-09-05');
INSERT INTO dependent (DepID, ReferenceCode, DepName, DepIsChild, DepIsWorking, DepOccupation, DepIncome, DepBirthdate) VALUES (16, 13, 'Michael Ventura', 1, 0, 'None', 0.0, '1980-08-24');
INSERT INTO dependent (DepID, ReferenceCode, DepName, DepIsChild, DepIsWorking, DepOccupation, DepIncome, DepBirthdate) VALUES (17, 13, 'Jobert Ventura', 1, 0, 'None', 0.0, '1982-07-10');
INSERT INTO dependent (DepID, ReferenceCode, DepName, DepIsChild, DepIsWorking, DepOccupation, DepIncome, DepBirthdate) VALUES (18, 13, 'Reymark Jovenal', 0, 0, 'None', 0.0, '1984-03-03');
INSERT INTO dependent (DepID, ReferenceCode, DepName, DepIsChild, DepIsWorking, DepOccupation, DepIncome, DepBirthdate) VALUES (19, 13, 'Donna Ventura', 1, 0, 'None', 0.0, '1986-04-04');
INSERT INTO dependent (DepID, ReferenceCode, DepName, DepIsChild, DepIsWorking, DepOccupation, DepIncome, DepBirthdate) VALUES (20, 14, 'Sheena Reyes', 1, 0, 'None', 0.0, '1978-04-27');
INSERT INTO dependent (DepID, ReferenceCode, DepName, DepIsChild, DepIsWorking, DepOccupation, DepIncome, DepBirthdate) VALUES (21, 15, 'Kapitan Malaya', 1, 0, 'Barangay Captain', 25000.0, '1990-05-23');
INSERT INTO dependent (DepID, ReferenceCode, DepName, DepIsChild, DepIsWorking, DepOccupation, DepIncome, DepBirthdate) VALUES (22, 15, 'Reyster Mendoza', 0, 0, 'None', 0.0, '2015-12-31');
INSERT INTO dependent (DepID, ReferenceCode, DepName, DepIsChild, DepIsWorking, DepOccupation, DepIncome, DepBirthdate) VALUES (23, 16, 'Jesusa Sining', 1, 0, 'Saleslady', 8000.0, '1987-12-25');
INSERT INTO dependent (DepID, ReferenceCode, DepName, DepIsChild, DepIsWorking, DepOccupation, DepIncome, DepBirthdate) VALUES (24, 18, 'Kyungmin Rivera', 1, 0, 'Manager', 42000.0, '1988-10-03');

-- Table: education
DROP TABLE IF EXISTS education;
CREATE TABLE education (
    EducID INTEGER PRIMARY KEY AUTOINCREMENT, 
    ReferenceCode INTEGER NOT NULL, 
    SchoolID TEXT NOT NULL, 
    EducationStage TEXT CHECK(EducationStage IN ('Primary', 'Secondary', 'Tertiary')) NOT NULL, 
    YearStarted TEXT NOT NULL, 
    GraduationYear TEXT NOT NULL,
    FOREIGN KEY (ReferenceCode) REFERENCES senior (ReferenceCode),
    FOREIGN KEY (SchoolID) REFERENCES school (SchoolID)
);
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (1, 1, '123456', 'Primary', '1947', '1953');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (2, 1, '567890', 'Secondary', '1953', '1957');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (3, 1, '123123', 'Tertiary', '1957', '1961');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (4, 2, '333444', 'Primary', '1959', '1966');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (5, 2, '567890', 'Secondary', '1967', '1971');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (6, 3, '567891', 'Primary', '1941', '1947');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (7, 3, '567892', 'Secondary', '1947', '1951');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (8, 3, '567893', 'Tertiary', '1951', '1955');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (9, 4, '567894', 'Primary', '1948', '1954');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (10, 4, '567895', 'Secondary', '1954', '1958');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (11, 5, '567896', 'Primary', '1955', '1961');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (12, 5, '567897', 'Secondary', '1961', '1965');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (13, 6, '567898', 'Primary', '1944', '1950');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (14, 6, '567899', 'Secondary', '1950', '1954');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (15, 7, '567900', 'Primary', '1957', '1963');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (16, 7, '567891', 'Secondary', '1963', '1967');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (17, 8, '567901', 'Primary', '1947', '1953');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (18, 8, '567911', 'Secondary', '1953', '1957');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (19, 9, '567902', 'Primary', '1949', '1955');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (20, 9, '567912', 'Secondary', '1955', '1959');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (21, 10, '567903', 'Primary', '1954', '1960');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (22, 10, '567913', 'Secondary', '1960', '1964');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (23, 11, '567904', 'Primary', '1958', '1964');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (24, 11, '567914', 'Secondary', '1964', '1968');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (25, 12, '567905', 'Primary', '1952', '1958');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (26, 12, '567915', 'Secondary', '1958', '1962');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (27, 13, '567890', 'Primary', '1957', '1963');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (28, 14, '567902', 'Primary', '1952', '1958');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (29, 14, '567912', 'Secondary', '1959', '1963');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (30, 15, '567905', 'Primary', '1967', '1973');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (31, 15, '567915', 'Secondary', '1973', '1977');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (32, 15, '123123', 'Tertiary', '1977', '1981');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (33, 16, '567896', 'Primary', '1964', '1970');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (34, 16, '567896', 'Secondary', '1970', '1974');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (35, 16, '567896', 'Tertiary', '1974', '1978');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (36, 18, '567892', 'Primary', '1970', '1976');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (37, 18, '567892', 'Secondary', '1976', '1980');
INSERT INTO education (EducID, ReferenceCode, SchoolID, EducationStage, YearStarted, GraduationYear) VALUES (38, 18, '567892', 'Tertiary', '1980', '1984');

-- Table: healthconcern
DROP TABLE IF EXISTS healthconcern;
CREATE TABLE healthconcern (
    ConcernID INTEGER PRIMARY KEY AUTOINCREMENT, 
    ReferenceCode INTEGER NOT NULL, 
    ConcernType TEXT CHECK(ConcernType IN ('Medical', 'Dental', 'Vision', 'Hearing', 'Social')) NOT NULL, 
    ConcernDetails TEXT NOT NULL,
    FOREIGN KEY (ReferenceCode) REFERENCES senior (ReferenceCode)
);
INSERT INTO healthconcern (ConcernID, ReferenceCode, ConcernType, ConcernDetails) VALUES (1, 1, 'Vision', 'Astigmatism');
INSERT INTO healthconcern (ConcernID, ReferenceCode, ConcernType, ConcernDetails) VALUES (2, 1, 'Hearing', 'Hearing Loss');
INSERT INTO healthconcern (ConcernID, ReferenceCode, ConcernType, ConcernDetails) VALUES (3, 2, 'Medical', 'High Blood Pressure');
INSERT INTO healthconcern (ConcernID, ReferenceCode, ConcernType, ConcernDetails) VALUES (4, 3, 'Medical', 'Diabetes');
INSERT INTO healthconcern (ConcernID, ReferenceCode, ConcernType, ConcernDetails) VALUES (5, 3, 'Dental', 'Gum Disease');
INSERT INTO healthconcern (ConcernID, ReferenceCode, ConcernType, ConcernDetails) VALUES (6, 4, 'Vision', 'Cataracts');
INSERT INTO healthconcern (ConcernID, ReferenceCode, ConcernType, ConcernDetails) VALUES (7, 4, 'Hearing', 'Tinnitus');
INSERT INTO healthconcern (ConcernID, ReferenceCode, ConcernType, ConcernDetails) VALUES (8, 5, 'Medical', 'Hypertension');
INSERT INTO healthconcern (ConcernID, ReferenceCode, ConcernType, ConcernDetails) VALUES (9, 5, 'Social', 'Depression');
INSERT INTO healthconcern (ConcernID, ReferenceCode, ConcernType, ConcernDetails) VALUES (10, 6, 'Dental', 'Tooth Sensitivity');
INSERT INTO healthconcern (ConcernID, ReferenceCode, ConcernType, ConcernDetails) VALUES (11, 6, 'Vision', 'Glaucoma');
INSERT INTO healthconcern (ConcernID, ReferenceCode, ConcernType, ConcernDetails) VALUES (12, 7, 'Medical', 'Arthritis');
INSERT INTO healthconcern (ConcernID, ReferenceCode, ConcernType, ConcernDetails) VALUES (13, 7, 'Hearing', 'Presbycusis');
INSERT INTO healthconcern (ConcernID, ReferenceCode, ConcernType, ConcernDetails) VALUES (14, 8, 'Medical', 'Arthritis');
INSERT INTO healthconcern (ConcernID, ReferenceCode, ConcernType, ConcernDetails) VALUES (15, 9, 'Vision', 'Glaucoma');
INSERT INTO healthconcern (ConcernID, ReferenceCode, ConcernType, ConcernDetails) VALUES (16, 10, 'Hearing', 'Tinnitus');
INSERT INTO healthconcern (ConcernID, ReferenceCode, ConcernType, ConcernDetails) VALUES (17, 11, 'Dental', 'Tooth Sensitivity');
INSERT INTO healthconcern (ConcernID, ReferenceCode, ConcernType, ConcernDetails) VALUES (18, 12, 'Medical', 'Hypertension');
INSERT INTO healthconcern (ConcernID, ReferenceCode, ConcernType, ConcernDetails) VALUES (19, 13, 'Dental', 'Teeth Erosion');
INSERT INTO healthconcern (ConcernID, ReferenceCode, ConcernType, ConcernDetails) VALUES (20, 13, 'Social', 'Depression');
INSERT INTO healthconcern (ConcernID, ReferenceCode, ConcernType, ConcernDetails) VALUES (21, 14, 'Vision', 'Glaucoma');
INSERT INTO healthconcern (ConcernID, ReferenceCode, ConcernType, ConcernDetails) VALUES (22, 15, 'Hearing', 'Otosclerosis ');
INSERT INTO healthconcern (ConcernID, ReferenceCode, ConcernType, ConcernDetails) VALUES (23, 16, 'Social', 'Anxiety');
INSERT INTO healthconcern (ConcernID, ReferenceCode, ConcernType, ConcernDetails) VALUES (24, 17, 'Medical', 'Prostate Cancer');

-- Table: income
DROP TABLE IF EXISTS income;
CREATE TABLE income (
    IncomeID INTEGER PRIMARY KEY AUTOINCREMENT, 
    ReferenceCode INTEGER NOT NULL, 
    SourceOfIncome TEXT CHECK(SourceOfIncome IN ('Salary', 'Pension', 'Business', 'Insurance', 'Savings', 'Stocks')) NOT NULL, 
    Occupation TEXT, 
    MonthlyIncome REAL NOT NULL DEFAULT 0,
    FOREIGN KEY (ReferenceCode) REFERENCES senior (ReferenceCode)
);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (1, 1, 'Pension', NULL, 10000.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (2, 1, 'Savings', NULL, 15000.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (3, 2, 'Pension', 'Self-Employed', 10000.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (4, 2, 'Business', 'Self-Employed', 20000.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (5, 3, 'Pension', NULL, 12000.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (6, 3, 'Savings', NULL, 15000.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (7, 4, 'Pension', 'Retired Engineer', 13000.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (8, 4, 'Business', 'Owner', 25000.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (9, 5, 'Pension', NULL, 11000.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (10, 5, 'Savings', NULL, 14000.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (11, 6, 'Pension', NULL, 11500.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (12, 6, 'Business', 'Consultant', 23000.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (13, 7, 'Pension', 'Retired Architect', 12000.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (14, 7, 'Business', 'Owner', 26000.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (15, 8, 'Pension', NULL, 12500.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (16, 8, 'Savings', NULL, 15000.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (17, 9, 'Pension', 'Retired Teacher', 11000.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (18, 9, 'Business', 'Owner', 24000.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (19, 10, 'Pension', NULL, 13000.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (20, 10, 'Savings', NULL, 15000.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (21, 11, 'Pension', NULL, 12500.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (22, 11, 'Business', 'Consultant', 22000.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (23, 12, 'Pension', NULL, 13500.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (24, 12, 'Savings', NULL, 14000.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (25, 13, 'Business', 'Entrepreneur', 50000.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (26, 13, 'Pension', 'Entrepreneur', 30000.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (27, 13, 'Stocks', 'Entrepreneur', 45000.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (28, 14, 'Pension', NULL, 10000.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (29, 14, 'Insurance', NULL, 40000.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (30, 14, 'Stocks', NULL, 60000.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (31, 15, 'Salary', 'Teacher', 50000.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (32, 15, 'Stocks', 'Teacher', 45000.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (33, 15, 'Insurance', 'Teacher', 10000.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (34, 16, 'Pension', NULL, 10000.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (35, 18, 'Salary', 'Architect', 70000.0);
INSERT INTO income (IncomeID, ReferenceCode, SourceOfIncome, Occupation, MonthlyIncome) VALUES (36, 18, 'Stocks', 'Architect', 80000.0);

-- Table: school
DROP TABLE IF EXISTS school;
CREATE TABLE school (
    SchoolID INTEGER PRIMARY KEY AUTOINCREMENT,
    SchoolName TEXT NOT NULL,
    SchoolAddress TEXT NOT NULL
);
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (123123, 'Polytechnic University of the Philippines', 'Manila City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (123456, 'Ewan Elementary School', 'Ewan City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (125487, 'Antipolo Dela Virgen School Inc.', 'Antipolo City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (156487, 'San Jose National High School', 'Antipolo City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (333444, 'Sucat Elementary School', 'Muntinlupa City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (567890, 'Basta National High School', 'Basta City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (567891, 'University of the Philippines', 'Quezon City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (567892, 'Ateneo de Manila University', 'Quezon City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (567893, 'De La Salle University', 'Manila City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (567894, 'University of Santo Tomas', 'Manila City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (567895, 'University of San Carlos', 'Cebu City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (567896, 'Silliman University', 'Dumaguete City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (567897, 'Mindanao State University', 'Marawi City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (567898, 'University of Mindanao', 'Davao City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (567899, 'Baguio Central University', 'Baguio City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (567900, 'West Visayas State University', 'Iloilo City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (567901, 'Makati Elementary School', 'Makati City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (567902, 'Quezon Elementary School', 'Quezon City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (567903, 'Taguig Elementary School', 'Taguig City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (567904, 'Pasig Elementary School', 'Pasig City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (567905, 'Caloocan Elementary School', 'Caloocan City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (567906, 'Mandaluyong Elementary School', 'Mandaluyong City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (567907, 'Las Piñas Elementary School', 'Las Piñas City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (567908, 'Marikina Elementary School', 'Marikina City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (567909, 'San Juan Elementary School', 'San Juan City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (567910, 'Valenzuela Elementary School', 'Valenzuela City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (567911, 'Makati High School', 'Makati City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (567912, 'Quezon High School', 'Quezon City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (567913, 'Taguig High School', 'Taguig City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (567914, 'Pasig High School', 'Pasig City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (567915, 'Caloocan High School', 'Caloocan City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (567916, 'Mandaluyong High School', 'Mandaluyong City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (567917, 'Las Piñas High School', 'Las Piñas City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (567918, 'Marikina High School', 'Marikina City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (567919, 'San Juan High School', 'San Juan City');
INSERT INTO school (SchoolID, SchoolName, SchoolAddress) VALUES (567920, 'Valenzuela High School', 'Valenzuela City');

-- Table: senior
DROP TABLE IF EXISTS senior;
CREATE TABLE senior (ReferenceCode INTEGER, Name TEXT NOT NULL, Address TEXT NOT NULL, BirthDate DATE NOT NULL, BirthPlace TEXT NOT NULL, CivilStatus TEXT NOT NULL CHECK (CivilStatus IN ('Single', 'Married', 'Widowed', 'Separated')), SexAtBirth TEXT NOT NULL CHECK (SexAtBirth IN ('Male', 'Female')), BloodType TEXT NOT NULL CHECK (BloodType IN ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-', 'Unknown')), PrimaryContactNum TEXT, ActiveEmailAddress TEXT, Religion TEXT NOT NULL CHECK (Religion IN ('Roman Catholic', 'Islam', 'Iglesia ni Cristo', 'Jehovah''s Witnesses', 'Evangelical', 'Baptist', 'Mormon', 'Buddhist', 'Hindu', 'Others')), SpouseName TEXT, FatherName TEXT NOT NULL, MotherName TEXT NOT NULL, PRIMARY KEY (ReferenceCode AUTOINCREMENT));
INSERT INTO senior (ReferenceCode, Name, Address, BirthDate, BirthPlace, CivilStatus, SexAtBirth, BloodType, PrimaryContactNum, ActiveEmailAddress, Religion, SpouseName, FatherName, MotherName) VALUES (1, 'Juan Dela Cruz', 'Antipolo', '1940-05-25', 'Antipolo', 'Married', 'Male', 'A-', '09121234123', 'juandelacruz@gmail.com', 'Roman Catholic', 'Maria Dela Cruz', 'Juanito Dela Cruz', 'Juanita Middle');
INSERT INTO senior (ReferenceCode, Name, Address, BirthDate, BirthPlace, CivilStatus, SexAtBirth, BloodType, PrimaryContactNum, ActiveEmailAddress, Religion, SpouseName, FatherName, MotherName) VALUES (2, 'Princess Sakura Pinaglabanan', 'Muntinlupa City', '1951-03-19', 'Angeles City, Pampanga', 'Widowed', 'Female', 'B+', '09999888765', NULL, 'Iglesia ni Cristo', 'Anton Pinaglabanan', 'King Pinaglabanan', 'Jennifer Delos Reyes');
INSERT INTO senior (ReferenceCode, Name, Address, BirthDate, BirthPlace, CivilStatus, SexAtBirth, BloodType, PrimaryContactNum, ActiveEmailAddress, Religion, SpouseName, FatherName, MotherName) VALUES (3, 'Carlos Santos', 'Quezon City', '1935-11-20', 'Quezon City', 'Married', 'Male', 'O+', '09175551234', 'carlos.santos@gmail.com', 'Evangelical', 'Lucia Santos', 'Pedro Santos', 'Maria Lopez');
INSERT INTO senior (ReferenceCode, Name, Address, BirthDate, BirthPlace, CivilStatus, SexAtBirth, BloodType, PrimaryContactNum, ActiveEmailAddress, Religion, SpouseName, FatherName, MotherName) VALUES (4, 'Maria Rivera', 'Cebu City', '1942-06-15', 'Cebu City', 'Widowed', 'Female', 'A+', '09231231234', 'maria.rivera@gmail.com', 'Roman Catholic', NULL, 'Jose Rivera', 'Clara Tan');
INSERT INTO senior (ReferenceCode, Name, Address, BirthDate, BirthPlace, CivilStatus, SexAtBirth, BloodType, PrimaryContactNum, ActiveEmailAddress, Religion, SpouseName, FatherName, MotherName) VALUES (5, 'Miguel Guzman', 'Davao City', '1949-09-30', 'Davao City', 'Single', 'Male', 'B-', '09333334444', 'miguel.guzman@gmail.com', 'Baptist', NULL, 'Ramon Guzman', 'Teresa Lim');
INSERT INTO senior (ReferenceCode, Name, Address, BirthDate, BirthPlace, CivilStatus, SexAtBirth, BloodType, PrimaryContactNum, ActiveEmailAddress, Religion, SpouseName, FatherName, MotherName) VALUES (6, 'Luisa Reyes', 'Baguio City', '1938-03-22', 'Baguio City', 'Married', 'Female', 'AB+', '09444445555', 'luisa.reyes@gmail.com', 'Jehovah''s Witnesses', 'Pedro Reyes', 'Carlos Reyes', 'Juanita Cruz');
INSERT INTO senior (ReferenceCode, Name, Address, BirthDate, BirthPlace, CivilStatus, SexAtBirth, BloodType, PrimaryContactNum, ActiveEmailAddress, Religion, SpouseName, FatherName, MotherName) VALUES (7, 'Fernando Dizon', 'Iloilo City', '1950-12-12', 'Iloilo City', 'Separated', 'Male', 'O-', '09555556666', 'fernando.dizon@gmail.com', 'Islam', NULL, 'Rafael Dizon', 'Angela Perez');
INSERT INTO senior (ReferenceCode, Name, Address, BirthDate, BirthPlace, CivilStatus, SexAtBirth, BloodType, PrimaryContactNum, ActiveEmailAddress, Religion, SpouseName, FatherName, MotherName) VALUES (8, 'Jose Garcia', 'Manila City', '1941-02-14', 'Manila City', 'Married', 'Male', 'A+', '09178889999', 'jose.garcia@gmail.com', 'Roman Catholic', 'Maria Garcia', 'Pedro Garcia', 'Ana Ramos');
INSERT INTO senior (ReferenceCode, Name, Address, BirthDate, BirthPlace, CivilStatus, SexAtBirth, BloodType, PrimaryContactNum, ActiveEmailAddress, Religion, SpouseName, FatherName, MotherName) VALUES (9, 'Rosario Santos', 'Cavite City', '1943-05-21', 'Cavite City', 'Widowed', 'Female', 'B+', '09179990000', 'rosario.santos@gmail.com', 'Evangelical', NULL, 'Juan Santos', 'Luisa Hernandez');
INSERT INTO senior (ReferenceCode, Name, Address, BirthDate, BirthPlace, CivilStatus, SexAtBirth, BloodType, PrimaryContactNum, ActiveEmailAddress, Religion, SpouseName, FatherName, MotherName) VALUES (10, 'Pedro Reyes', 'Pasig City', '1948-09-10', 'Pasig City', 'Single', 'Male', 'O-', '09171112222', 'pedro.reyes@gmail.com', 'Baptist', NULL, 'Miguel Reyes', 'Carmen Diaz');
INSERT INTO senior (ReferenceCode, Name, Address, BirthDate, BirthPlace, CivilStatus, SexAtBirth, BloodType, PrimaryContactNum, ActiveEmailAddress, Religion, SpouseName, FatherName, MotherName) VALUES (11, 'Dolores Cruz', 'Caloocan City', '1952-03-30', 'Caloocan City', 'Married', 'Female', 'AB-', '09172223333', 'dolores.cruz@gmail.com', 'Jehovah''s Witnesses', 'Carlos Cruz', 'Rafael Cruz', 'Maria Santos');
INSERT INTO senior (ReferenceCode, Name, Address, BirthDate, BirthPlace, CivilStatus, SexAtBirth, BloodType, PrimaryContactNum, ActiveEmailAddress, Religion, SpouseName, FatherName, MotherName) VALUES (12, 'Manuel Lopez', 'Makati City', '1945-07-07', 'Makati City', 'Separated', 'Male', 'B-', '09173334444', 'manuel.lopez@gmail.com', 'Islam', NULL, 'Ramon Lopez', 'Teresa Aquino');
INSERT INTO senior (ReferenceCode, Name, Address, BirthDate, BirthPlace, CivilStatus, SexAtBirth, BloodType, PrimaryContactNum, ActiveEmailAddress, Religion, SpouseName, FatherName, MotherName) VALUES (13, 'John Ventura', 'Palawan', '1950-01-08', 'Mindoro', 'Married', 'Male', 'O+', '09566639472', 'johnventura@gmail.com', 'Roman Catholic', 'Jane Ventura', 'Steven Ventura', 'Stephanie Ventura');
INSERT INTO senior (ReferenceCode, Name, Address, BirthDate, BirthPlace, CivilStatus, SexAtBirth, BloodType, PrimaryContactNum, ActiveEmailAddress, Religion, SpouseName, FatherName, MotherName) VALUES (14, 'Maloi Reyes', 'Quezon City', '1945-03-17', 'Quezon City', 'Widowed', 'Female', 'A+', '09237206518', 'binimaloi@gmail.com', 'Baptist', 'Diokno Reyes', 'Nikolas Reyes', 'Arrabella Reyes');
INSERT INTO senior (ReferenceCode, Name, Address, BirthDate, BirthPlace, CivilStatus, SexAtBirth, BloodType, PrimaryContactNum, ActiveEmailAddress, Religion, SpouseName, FatherName, MotherName) VALUES (15, 'Bayani Malaya', 'Zaragoza', '1960-07-30', 'Gapan City', 'Married', 'Male', 'B-', '09247409284', 'bayanifreedom@gmail.com', 'Mormon', 'Selena Malaya', 'Sungtsol Malaya', 'Soolgi Malaya');
INSERT INTO senior (ReferenceCode, Name, Address, BirthDate, BirthPlace, CivilStatus, SexAtBirth, BloodType, PrimaryContactNum, ActiveEmailAddress, Religion, SpouseName, FatherName, MotherName) VALUES (16, 'Diwata Alon', 'Pasay City', '1958-11-28', 'Iloilo City', 'Widowed', 'Female', 'A-', '09448823194', 'diwataoverload@gmail.com', 'Islam', 'Dyelo Alon', 'Chaolong Alon', 'Mamie Alon');
INSERT INTO senior (ReferenceCode, Name, Address, BirthDate, BirthPlace, CivilStatus, SexAtBirth, BloodType, PrimaryContactNum, ActiveEmailAddress, Religion, SpouseName, FatherName, MotherName) VALUES (17, 'Lakan Sining', 'Manila', '1955-04-08', 'Taguig City', 'Single', 'Male', 'O+', '09974583329', 'lakanarts@gmail.com', 'Roman Catholic', NULL, 'Matikas Sining', 'Magdalena Sining');
INSERT INTO senior (ReferenceCode, Name, Address, BirthDate, BirthPlace, CivilStatus, SexAtBirth, BloodType, PrimaryContactNum, ActiveEmailAddress, Religion, SpouseName, FatherName, MotherName) VALUES (18, 'Shinyu Rivera', 'Taguig CIty', '1963-11-07', 'Ilocos Norte', 'Married', 'Male', 'AB+', '09247110705', 'twsshinyu@gmail.com', 'Roman Catholic', 'Princess Rivera', 'Dohoon Rivera', 'Hanie Delos Santos');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
