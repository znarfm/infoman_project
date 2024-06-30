CREATE DATABASE  IF NOT EXISTS `project` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `project`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: project
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `dependent`
--

DROP TABLE IF EXISTS `dependent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dependent` (
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dependent`
--

LOCK TABLES `dependent` WRITE;
/*!40000 ALTER TABLE `dependent` DISABLE KEYS */;
INSERT INTO `dependent` VALUES (1,1,'One Dela Cruz',1,1,'Teacher',40000,'1993-12-07'),(2,1,'Two Dela Cruz',0,1,'Cashier',30000,'1997-01-17'),(3,1,'Three Dela Cruz',0,0,NULL,NULL,'2000-07-18'),(4,2,'Moka Pinaglabanan',1,1,'Call Center Agent',25000,'1982-02-27'),(5,2,'Ubeka Pinaglabanan',0,1,'Accountant',45000,'1986-08-14'),(6,3,'Ana Santos',1,1,'Nurse',35000,'1960-04-12'),(7,4,'Roberto Rivera',1,1,'Engineer',50000,'1965-08-09'),(8,5,'Elena Guzman',1,0,NULL,NULL,'1970-05-25'),(9,6,'Carmen Reyes',1,1,'Teacher',40000,'1962-11-10'),(10,7,'Luis Dizon',1,1,'Architect',55000,'1975-03-17'),(11,8,'Juan Garcia',1,1,'Doctor',70000,'1970-08-15'),(12,8,'Marta Garcia',1,0,NULL,NULL,'1975-11-22'),(13,9,'Josefina Santos',1,1,'Lawyer',80000,'1968-03-14'),(14,10,'Luis Reyes',1,1,'Engineer',60000,'1972-12-10'),(15,11,'Celia Cruz',1,0,NULL,NULL,'1977-09-05');
/*!40000 ALTER TABLE `dependent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `education`
--

DROP TABLE IF EXISTS `education`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `education` (
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `education`
--

LOCK TABLES `education` WRITE;
/*!40000 ALTER TABLE `education` DISABLE KEYS */;
INSERT INTO `education` VALUES (1,1,123456,'Elementary',1947,1953),(2,1,567890,'High School',1953,1957),(3,1,123123,'College',1957,1961),(4,2,333444,'Elementary',1959,1966),(5,2,567890,'High School',1967,1971),(6,3,567891,'Elementary',1941,1947),(7,3,567892,'High School',1947,1951),(8,3,567893,'College',1951,1955),(9,4,567894,'Elementary',1948,1954),(10,4,567895,'High School',1954,1958),(11,5,567896,'Elementary',1955,1961),(12,5,567897,'High School',1961,1965),(13,6,567898,'Elementary',1944,1950),(14,6,567899,'High School',1950,1954),(15,7,567900,'Elementary',1957,1963),(16,7,567891,'High School',1963,1967),(17,8,567901,'Elementary',1947,1953),(18,8,567911,'High School',1953,1957),(19,9,567902,'Elementary',1949,1955),(20,9,567912,'High School',1955,1959),(21,10,567903,'Elementary',1954,1960),(22,10,567913,'High School',1960,1964),(23,11,567904,'Elementary',1958,1964),(24,11,567914,'High School',1964,1968),(25,12,567905,'Elementary',1952,1958),(26,12,567915,'High School',1958,1962);
/*!40000 ALTER TABLE `education` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `healthconcern`
--

DROP TABLE IF EXISTS `healthconcern`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `healthconcern` (
  `ConcernID` int NOT NULL AUTO_INCREMENT,
  `ReferenceCode` int NOT NULL,
  `ConcernType` enum('Medical','Dental','Vision','Hearing','Social') NOT NULL,
  `ConcernDetails` varchar(100) NOT NULL,
  PRIMARY KEY (`ConcernID`),
  KEY `fk_healthconcern_senior_idx` (`ReferenceCode`),
  CONSTRAINT `fk_healthconcern_senior` FOREIGN KEY (`ReferenceCode`) REFERENCES `senior` (`ReferenceCode`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `healthconcern`
--

LOCK TABLES `healthconcern` WRITE;
/*!40000 ALTER TABLE `healthconcern` DISABLE KEYS */;
INSERT INTO `healthconcern` VALUES (1,1,'Vision','Astigmatism'),(2,1,'Hearing','Hearing Loss'),(3,2,'Medical','High Blood Pressure'),(4,3,'Medical','Diabetes'),(5,3,'Dental','Gum Disease'),(6,4,'Vision','Cataracts'),(7,4,'Hearing','Tinnitus'),(8,5,'Medical','Hypertension'),(9,5,'Social','Depression'),(10,6,'Dental','Tooth Sensitivity'),(11,6,'Vision','Glaucoma'),(12,7,'Medical','Arthritis'),(13,7,'Hearing','Presbycusis'),(14,8,'Medical','Arthritis'),(15,9,'Vision','Glaucoma'),(16,10,'Hearing','Tinnitus'),(17,11,'Dental','Tooth Sensitivity'),(18,12,'Medical','Hypertension');
/*!40000 ALTER TABLE `healthconcern` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `income`
--

DROP TABLE IF EXISTS `income`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `income` (
  `IncomeID` int NOT NULL AUTO_INCREMENT,
  `ReferenceCode` int NOT NULL,
  `SourceOfIncome` enum('Salary','Pension','Business','Insurance','Savings','Stocks') NOT NULL,
  `Occupation` varchar(100) DEFAULT NULL,
  `MonthlyIncome` float NOT NULL DEFAULT '0',
  PRIMARY KEY (`IncomeID`),
  KEY `fk_income_senior_idx` (`ReferenceCode`),
  CONSTRAINT `fk_income_senior` FOREIGN KEY (`ReferenceCode`) REFERENCES `senior` (`ReferenceCode`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `income`
--

LOCK TABLES `income` WRITE;
/*!40000 ALTER TABLE `income` DISABLE KEYS */;
INSERT INTO `income` VALUES (1,1,'Pension',NULL,10000),(2,1,'Savings',NULL,15000),(3,2,'Pension','Self-Employed',10000),(4,2,'Business','Self-Employed',20000),(5,3,'Pension',NULL,12000),(6,3,'Savings',NULL,15000),(7,4,'Pension','Retired Engineer',13000),(8,4,'Business','Owner',25000),(9,5,'Pension',NULL,11000),(10,5,'Stocks',NULL,20000),(11,6,'Pension','Retired Teacher',14000),(12,6,'Savings',NULL,18000),(13,7,'Pension','Retired Architect',15000),(14,7,'Business','Owner',30000),(15,8,'Pension',NULL,12000),(16,9,'Savings',NULL,10000),(17,9,'Business','Owner',30000),(18,10,'Pension',NULL,14000),(19,11,'Stocks',NULL,20000),(20,12,'Pension',NULL,16000);
/*!40000 ALTER TABLE `income` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `school`
--

DROP TABLE IF EXISTS `school`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `school` (
  `SchoolID` int NOT NULL AUTO_INCREMENT,
  `SchoolName` varchar(100) NOT NULL,
  `SchoolAddress` varchar(150) NOT NULL,
  PRIMARY KEY (`SchoolID`)
) ENGINE=InnoDB AUTO_INCREMENT=567921 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `school`
--

LOCK TABLES `school` WRITE;
/*!40000 ALTER TABLE `school` DISABLE KEYS */;
INSERT INTO `school` VALUES (123123,'Polytechnic University of the Philippines','Manila City'),(123456,'Ewan Elementary School','Ewan City'),(333444,'Sucat Elementary School','Muntinlupa City'),(567890,'Basta National High School','Basta City'),(567891,'University of the Philippines','Quezon City'),(567892,'Ateneo de Manila University','Quezon City'),(567893,'De La Salle University','Manila City'),(567894,'University of Santo Tomas','Manila City'),(567895,'University of San Carlos','Cebu City'),(567896,'Silliman University','Dumaguete City'),(567897,'Mindanao State University','Marawi City'),(567898,'University of Mindanao','Davao City'),(567899,'Baguio Central University','Baguio City'),(567900,'West Visayas State University','Iloilo City'),(567901,'Makati Elementary School','Makati City'),(567902,'Quezon Elementary School','Quezon City'),(567903,'Taguig Elementary School','Taguig City'),(567904,'Pasig Elementary School','Pasig City'),(567905,'Caloocan Elementary School','Caloocan City'),(567906,'Mandaluyong Elementary School','Mandaluyong City'),(567907,'Las Piñas Elementary School','Las Piñas City'),(567908,'Marikina Elementary School','Marikina City'),(567909,'San Juan Elementary School','San Juan City'),(567910,'Valenzuela Elementary School','Valenzuela City'),(567911,'Makati High School','Makati City'),(567912,'Quezon High School','Quezon City'),(567913,'Taguig High School','Taguig City'),(567914,'Pasig High School','Pasig City'),(567915,'Caloocan High School','Caloocan City'),(567916,'Mandaluyong High School','Mandaluyong City'),(567917,'Las Piñas High School','Las Piñas City'),(567918,'Marikina High School','Marikina City'),(567919,'San Juan High School','San Juan City'),(567920,'Valenzuela High School','Valenzuela City');
/*!40000 ALTER TABLE `school` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `senior`
--

DROP TABLE IF EXISTS `senior`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `senior` (
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `senior`
--

LOCK TABLES `senior` WRITE;
/*!40000 ALTER TABLE `senior` DISABLE KEYS */;
INSERT INTO `senior` VALUES (1,'Juan Dela Cruz','Antipolo','1940-05-25','Antipolo','M','M','A-','09121234123','juandelacruz@gmail.com','Roman Catholic','Maria Dela Cruz','Juanito Dela Cruz','Juanita Middle'),(2,'Princess Sakura Pinaglabanan','Muntinlupa City','1951-03-19','Angeles City, Pampanga','W','F','B+','09999888765',NULL,'Iglesia ni Cristo','Anton Pinaglabanan','King Pinaglabanan','Jennifer Delos Reyes'),(3,'Carlos Santos','Quezon City','1935-11-20','Quezon City','M','M','O+','09175551234','carlos.santos@gmail.com','Evangelical','Lucia Santos','Pedro Santos','Maria Lopez'),(4,'Maria Rivera','Cebu City','1942-06-15','Cebu City','W','F','A+','09231231234','maria.rivera@gmail.com','Roman Catholic',NULL,'Jose Rivera','Clara Tan'),(5,'Miguel Guzman','Davao City','1949-09-30','Davao City','S','M','B-','09333334444','miguel.guzman@gmail.com','Baptist',NULL,'Ramon Guzman','Teresa Lim'),(6,'Luisa Reyes','Baguio City','1938-03-22','Baguio City','M','F','AB+','09444445555','luisa.reyes@gmail.com','Jehovah\'s Witnesses','Pedro Reyes','Carlos Reyes','Juanita Cruz'),(7,'Fernando Dizon','Iloilo City','1950-12-12','Iloilo City','SE','M','O-','09555556666','fernando.dizon@gmail.com','Islam',NULL,'Rafael Dizon','Angela Perez'),(8,'Jose Garcia','Manila City','1941-02-14','Manila City','M','M','A+','09178889999','jose.garcia@gmail.com','Roman Catholic','Maria Garcia','Pedro Garcia','Ana Ramos'),(9,'Rosario Santos','Cavite City','1943-05-21','Cavite City','W','F','B+','09179990000','rosario.santos@gmail.com','Evangelical',NULL,'Juan Santos','Luisa Hernandez'),(10,'Pedro Reyes','Pasig City','1948-09-10','Pasig City','S','M','O-','09171112222','pedro.reyes@gmail.com','Baptist',NULL,'Miguel Reyes','Carmen Diaz'),(11,'Dolores Cruz','Caloocan City','1952-03-30','Caloocan City','M','F','AB-','09172223333','dolores.cruz@gmail.com','Jehovah\'s Witnesses','Carlos Cruz','Rafael Cruz','Maria Santos'),(12,'Manuel Lopez','Makati City','1945-07-07','Makati City','SE','M','B-','09173334444','manuel.lopez@gmail.com','Islam',NULL,'Ramon Lopez','Teresa Aquino');
/*!40000 ALTER TABLE `senior` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-29 17:23:11
