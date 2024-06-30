import streamlit as st


def make_connection(name, type):
    return st.connection(name=name, type=type, ttl=600)


def create_tables(conn):
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS `senior` (
        `ReferenceCode` int NOT NULL AUTO_INCREMENT,
        `Name` varchar(100) NOT NULL,
        `Address` varchar(150) NOT NULL,
        `BirthDate` date NOT NULL,
        `BirthPlace` varchar(150) NOT NULL,
        `CivilStatus` enum('S','M','W','SE') NOT NULL,
        `SexAtBirth` enum('M','F') NOT NULL,
        `BloodType` enum('A+','A-','B+','B-','AB+','AB-','O+','O-') NOT NULL,
        `PrimaryContactNum` varchar(13) DEFAULT NULL,
        `ActiveEmailAddress` varchar(150) DEFAULT NULL,
        `Religion` enum('Roman Catholic','Islam','Iglesia ni Cristo','Jehovah''s Witnesses','Evangelical','Baptist','Mormon','Buddhist','Hindu','Others') NOT NULL,
        `SpouseName` varchar(100) DEFAULT NULL,
        `FatherName` varchar(100) NOT NULL,
        `MotherName` varchar(100) NOT NULL,
        PRIMARY KEY (`ReferenceCode`)
        ) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

        CREATE TABLE IF NOT EXISTS `dependent` (
        `DepID` int NOT NULL AUTO_INCREMENT,
        `ReferenceCode` int NOT NULL,
        `DepName` varchar(100) NOT NULL,
        `DepIsChild` tinyint NOT NULL,
        `DepIsWorking` tinyint NOT NULL,
        `DepOccupation` varchar(50) DEFAULT NULL,
        `DepIncome` float DEFAULT NULL,
        `DepBirthdate` date NOT NULL,
        PRIMARY KEY (`DepID`,`ReferenceCode`),
        KEY `refe_idx` (`ReferenceCode`),
        CONSTRAINT `fk_dependent_senior` FOREIGN KEY (`ReferenceCode`) REFERENCES `senior` (`ReferenceCode`)
        ) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

        CREATE TABLE IF NOT EXISTS `education` (
        `EducID` int NOT NULL AUTO_INCREMENT,
        `ReferenceCode` int NOT NULL,
        `SchoolID` int NOT NULL,
        `EducationStage` text NOT NULL,
        `YearStarted` year NOT NULL,
        `GraduationYear` year NOT NULL,
        PRIMARY KEY (`EducID`),
        KEY `fk_education_senior_idx` (`ReferenceCode`),
        KEY `fk_education_school_idx` (`SchoolID`),
        CONSTRAINT `fk_education_school` FOREIGN KEY (`SchoolID`) REFERENCES `school` (`SchoolID`),
        CONSTRAINT `fk_education_senior` FOREIGN KEY (`ReferenceCode`) REFERENCES `senior` (`ReferenceCode`)
        ) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

        CREATE TABLE IF NOT EXISTS `healthconcern` (
        `ConcernID` int NOT NULL AUTO_INCREMENT,
        `ReferenceCode` int NOT NULL,
        `ConcernType` enum('Medical','Dental','Vision','Hearing','Social') NOT NULL,
        `ConcernDetails` varchar(100) NOT NULL,
        PRIMARY KEY (`ConcernID`),
        KEY `fk_healthconcern_senior_idx` (`ReferenceCode`),
        CONSTRAINT `fk_healthconcern_senior` FOREIGN KEY (`ReferenceCode`) REFERENCES `senior` (`ReferenceCode`)
        ) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        /*!40101 SET character_set_client = @saved_cs_client */;

        CREATE TABLE IF NOT EXISTS `income` (
        `IncomeID` int NOT NULL AUTO_INCREMENT,
        `ReferenceCode` int NOT NULL,
        `SourceOfIncome` enum('Salary','Pension','Business','Insurance','Savings','Stocks') NOT NULL,
        `Occupation` varchar(100) DEFAULT NULL,
        `MonthlyIncome` float NOT NULL DEFAULT '0',
        PRIMARY KEY (`IncomeID`),
        KEY `fk_income_senior_idx` (`ReferenceCode`),
        CONSTRAINT `fk_income_senior` FOREIGN KEY (`ReferenceCode`) REFERENCES `senior` (`ReferenceCode`)
        ) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

        CREATE TABLE IF NOT EXISTS `school` (
        `SchoolID` int NOT NULL AUTO_INCREMENT,
        `SchoolName` varchar(100) NOT NULL,
        `SchoolAddress` varchar(150) NOT NULL,
        PRIMARY KEY (`SchoolID`)
        ) ENGINE=InnoDB AUTO_INCREMENT=567921 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        """
    )


# used for viewing all columns from a specific table
def show_table(conn, table_name):
    return conn.query(
        f"""SELECT * 
            FROM {table_name};""",
        ttl=600,
    )

def get_senior_name_and_code(conn):
    return conn.query(
        """SELECT Name, ReferenceCode 
            FROM Senior;""",
        ttl=600,
    )

def get_schools(conn):
    return conn.query(
        """SELECT SchoolID, SchoolName
            FROM school
            ORDER BY SchoolName;""",
        ttl=600,
    )

def filter_reference_code(conn, table_name, reference_code):
    return conn.query(
        f"""SELECT * 
            FROM {table_name} 
            WHERE ReferenceCode = '{reference_code}';""",
        ttl=600,
    )
