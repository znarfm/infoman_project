import sqlite3
import pandas as pd

def make_connection():
    return sqlite3.connect("projectdb.db")


# def create_tables(conn):
#     conn.execute(
#         """
#         CREATE TABLE IF NOT EXISTS `senior` (
#         `ReferenceCode` int NOT NULL AUTO_INCREMENT,
#         `Name` varchar(100) NOT NULL,
#         `Address` varchar(150) NOT NULL,
#         `BirthDate` date NOT NULL,
#         `BirthPlace` varchar(150) NOT NULL,
#         `CivilStatus` enum('S','M','W','SE') NOT NULL,
#         `SexAtBirth` enum('M','F') NOT NULL,
#         `BloodType` enum('A+','A-','B+','B-','AB+','AB-','O+','O-') NOT NULL,
#         `PrimaryContactNum` varchar(13) DEFAULT NULL,
#         `ActiveEmailAddress` varchar(150) DEFAULT NULL,
#         `Religion` enum('Roman Catholic','Islam','Iglesia ni Cristo','Jehovah''s Witnesses','Evangelical','Baptist','Mormon','Buddhist','Hindu','Others') NOT NULL,
#         `SpouseName` varchar(100) DEFAULT NULL,
#         `FatherName` varchar(100) NOT NULL,
#         `MotherName` varchar(100) NOT NULL,
#         PRIMARY KEY (`ReferenceCode`)
#         ) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

#         CREATE TABLE IF NOT EXISTS `dependent` (
#         `DepID` int NOT NULL AUTO_INCREMENT,
#         `ReferenceCode` int NOT NULL,
#         `DepName` varchar(100) NOT NULL,
#         `DepIsChild` tinyint NOT NULL,
#         `DepIsWorking` tinyint NOT NULL,
#         `DepOccupation` varchar(50) DEFAULT NULL,
#         `DepIncome` float DEFAULT NULL,
#         `DepBirthdate` date NOT NULL,
#         PRIMARY KEY (`DepID`,`ReferenceCode`),
#         KEY `refe_idx` (`ReferenceCode`),
#         CONSTRAINT `fk_dependent_senior` FOREIGN KEY (`ReferenceCode`) REFERENCES `senior` (`ReferenceCode`)
#         ) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

#         CREATE TABLE IF NOT EXISTS `education` (
#         `EducID` int NOT NULL AUTO_INCREMENT,
#         `ReferenceCode` int NOT NULL,
#         `SchoolID` int NOT NULL,
#         `EducationStage` text NOT NULL,
#         `YearStarted` year NOT NULL,
#         `GraduationYear` year NOT NULL,
#         PRIMARY KEY (`EducID`),
#         KEY `fk_education_senior_idx` (`ReferenceCode`),
#         KEY `fk_education_school_idx` (`SchoolID`),
#         CONSTRAINT `fk_education_school` FOREIGN KEY (`SchoolID`) REFERENCES `school` (`SchoolID`),
#         CONSTRAINT `fk_education_senior` FOREIGN KEY (`ReferenceCode`) REFERENCES `senior` (`ReferenceCode`)
#         ) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

#         CREATE TABLE IF NOT EXISTS `healthconcern` (
#         `ConcernID` int NOT NULL AUTO_INCREMENT,
#         `ReferenceCode` int NOT NULL,
#         `ConcernType` enum('Medical','Dental','Vision','Hearing','Social') NOT NULL,
#         `ConcernDetails` varchar(100) NOT NULL,
#         PRIMARY KEY (`ConcernID`),
#         KEY `fk_healthconcern_senior_idx` (`ReferenceCode`),
#         CONSTRAINT `fk_healthconcern_senior` FOREIGN KEY (`ReferenceCode`) REFERENCES `senior` (`ReferenceCode`)
#         ) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
#         /*!40101 SET character_set_client = @saved_cs_client */;

#         CREATE TABLE IF NOT EXISTS `income` (
#         `IncomeID` int NOT NULL AUTO_INCREMENT,
#         `ReferenceCode` int NOT NULL,
#         `SourceOfIncome` enum('Salary','Pension','Business','Insurance','Savings','Stocks') NOT NULL,
#         `Occupation` varchar(100) DEFAULT NULL,
#         `MonthlyIncome` float NOT NULL DEFAULT '0',
#         PRIMARY KEY (`IncomeID`),
#         KEY `fk_income_senior_idx` (`ReferenceCode`),
#         CONSTRAINT `fk_income_senior` FOREIGN KEY (`ReferenceCode`) REFERENCES `senior` (`ReferenceCode`)
#         ) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

#         CREATE TABLE IF NOT EXISTS `school` (
#         `SchoolID` int NOT NULL AUTO_INCREMENT,
#         `SchoolName` varchar(100) NOT NULL,
#         `SchoolAddress` varchar(150) NOT NULL,
#         PRIMARY KEY (`SchoolID`)
#         ) ENGINE=InnoDB AUTO_INCREMENT=567921 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
#         """
#     )

# INSERT statements
def insert_senior(senior_data):
    with make_connection() as conn:
        cursor = conn.cursor()
        insert_query = """
        INSERT INTO senior (name, address, birthdate, birthplace, civilstatus, sexatbirth, bloodtype, religion, primarycontactnum, activeemailaddress, fathername, mothername, spousename)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(insert_query, (
            senior_data["name"],
            senior_data["address"],
            senior_data["birthdate"],
            senior_data["birthplace"],
            senior_data["status"],
            senior_data["sex"],
            senior_data["blood_type"],
            senior_data["religion"],
            senior_data["contact_number"],
            senior_data["email"],
            senior_data["father"],
            senior_data["mother"],
            senior_data["spouse"]
        ))
        conn.commit()
        lastrowid = cursor.lastrowid
        return lastrowid

def insert_dependent(dependent_data):
    with make_connection() as conn:
        cursor = conn.cursor()
        insert_query = """
        INSERT INTO dependent (referencecode, depname, depischild, depisworking, depoccupation, depincome, depbirthdate)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(insert_query, (
            dependent_data["reference_code"],
            dependent_data["Name"],
            dependent_data["Is Child"],
            dependent_data["Is Working"],
            dependent_data["Occupation"],
            dependent_data["Income"],
            dependent_data["Birthdate"]
        ))
        conn.commit()

def insert_income(income_data):
    with make_connection() as conn:
        cursor = conn.cursor()
        insert_query = """
        INSERT INTO income (referencecode, sourceofincome, occupation, monthlyincome)
        VALUES (?, ?, ?, ?)
        """
        cursor.execute(insert_query, (
            income_data["reference_code"],
            income_data["Source"],
            income_data["Occupation"],
            income_data["Amount"]
        ))
        conn.commit()

def insert_health_concern(concern_data):
    with make_connection() as conn:
        cursor = conn.cursor()
        insert_query = """
        INSERT INTO healthconcern (referencecode, concerntype, concerndetails)
        VALUES (?, ?, ?)
        """
        cursor.execute(insert_query, (
            concern_data["reference_code"],
            concern_data["Type"],
            concern_data["Details"]
        ))
        conn.commit()

def insert_education(education_data):
    with make_connection() as conn:
        cursor = conn.cursor()
        insert_query = """
        INSERT INTO education (referencecode, schoolid, educationstage, yearstarted, graduationyear)
        VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(insert_query, (
            education_data["reference_code"],
            education_data["SchoolID"],
            education_data["Education Level"],
            education_data["Year Started"],
            education_data["Year Completed"]
        ))
        conn.commit()

# UPDATE statements
# TODO

# DELETE statements
def delete_senior(reference_code):
    with make_connection() as conn:
        cursor = conn.cursor()
        delete_query = "DELETE FROM senior WHERE ReferenceCode = ?"
        cursor.execute(delete_query, (int(reference_code),))
        conn.commit()
        