--
-- File generated with SQLiteStudio v3.4.4 on Mon Jul 8 23:51:02 2024
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: dependent
CREATE TABLE IF NOT EXISTS dependent (
    DepID         INTEGER PRIMARY KEY AUTOINCREMENT,
    ReferenceCode INTEGER NOT NULL,
    DepName       TEXT    NOT NULL,
    DepIsChild    INTEGER CHECK (DepIsChild IN (0, 1) ) 
                          NOT NULL,
    DepIsWorking  INTEGER CHECK (DepIsWorking IN (0, 1) ) 
                          NOT NULL,
    DepOccupation TEXT,
    DepIncome     REAL,
    DepBirthdate  DATE    NOT NULL,
    FOREIGN KEY (
        ReferenceCode
    )
    REFERENCES senior (ReferenceCode) 
);


-- Table: education
CREATE TABLE IF NOT EXISTS education (
    EducID         INTEGER PRIMARY KEY AUTOINCREMENT,
    ReferenceCode  INTEGER NOT NULL,
    SchoolID       TEXT    NOT NULL,
    EducationStage TEXT    CHECK (EducationStage IN ('Primary', 'Secondary', 'Tertiary') ) 
                           NOT NULL,
    YearStarted    TEXT    NOT NULL,
    GraduationYear TEXT    NOT NULL,
    FOREIGN KEY (
        ReferenceCode
    )
    REFERENCES senior (ReferenceCode),
    FOREIGN KEY (
        SchoolID
    )
    REFERENCES school (SchoolID) 
);


-- Table: healthconcern
CREATE TABLE IF NOT EXISTS healthconcern (
    ConcernID      INTEGER PRIMARY KEY AUTOINCREMENT,
    ReferenceCode  INTEGER NOT NULL,
    ConcernType    TEXT    CHECK (ConcernType IN ('Medical', 'Dental', 'Vision', 'Hearing', 'Social') ) 
                           NOT NULL,
    ConcernDetails TEXT    NOT NULL,
    FOREIGN KEY (
        ReferenceCode
    )
    REFERENCES senior (ReferenceCode) 
);


-- Table: income
CREATE TABLE IF NOT EXISTS income (
    IncomeID       INTEGER PRIMARY KEY AUTOINCREMENT,
    ReferenceCode  INTEGER NOT NULL,
    SourceOfIncome TEXT    CHECK (SourceOfIncome IN ('Salary', 'Pension', 'Business', 'Insurance', 'Savings', 'Stocks') ) 
                           NOT NULL,
    Occupation     TEXT,
    MonthlyIncome  REAL    NOT NULL
                           DEFAULT 0,
    FOREIGN KEY (
        ReferenceCode
    )
    REFERENCES senior (ReferenceCode) 
);


-- Table: school
CREATE TABLE IF NOT EXISTS school (
    SchoolID      INTEGER PRIMARY KEY AUTOINCREMENT,
    SchoolName    TEXT    NOT NULL,
    SchoolAddress TEXT    NOT NULL
);


-- Table: senior
CREATE TABLE IF NOT EXISTS senior (
    ReferenceCode      INTEGER,
    Name               TEXT    NOT NULL,
    Address            TEXT    NOT NULL,
    BirthDate          DATE    NOT NULL,
    BirthPlace         TEXT    NOT NULL,
    CivilStatus        TEXT    NOT NULL
                               CHECK (CivilStatus IN ('Single', 'Married', 'Widowed', 'Separated') ),
    SexAtBirth         TEXT    NOT NULL
                               CHECK (SexAtBirth IN ('Male', 'Female') ),
    BloodType          TEXT    NOT NULL
                               CHECK (BloodType IN ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-', 'Unknown') ),
    PrimaryContactNum  TEXT,
    ActiveEmailAddress TEXT,
    Religion           TEXT    NOT NULL
                               CHECK (Religion IN ('Roman Catholic', 'Islam', 'Iglesia ni Cristo', 'Jehovah''s Witnesses', 'Evangelical', 'Baptist', 'Mormon', 'Buddhist', 'Hindu', 'Others') ),
    SpouseName         TEXT,
    FatherName         TEXT    NOT NULL,
    MotherName         TEXT    NOT NULL,
    PRIMARY KEY (
        ReferenceCode AUTOINCREMENT
    )
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
