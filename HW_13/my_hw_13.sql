-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: my_hw_13
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `class_7b`
--

DROP TABLE IF EXISTS `class_7b`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `class_7b` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  `age` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class_7b`
--

LOCK TABLES `class_7b` WRITE;
/*!40000 ALTER TABLE `class_7b` DISABLE KEYS */;
INSERT INTO `class_7b` VALUES (1,'Ivanov Ivan',7),(2,'Petrov Petr',9),(3,'Sidorova Alena',11),(4,'Kola Yula',NULL),(5,'Midlov Serhey',15);
/*!40000 ALTER TABLE `class_7b` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `more_info`
--

DROP TABLE IF EXISTS `more_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `more_info` (
  `id` int NOT NULL AUTO_INCREMENT,
  `gender` varchar(40) DEFAULT NULL,
  `color_of_dress` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `more_info`
--

LOCK TABLES `more_info` WRITE;
/*!40000 ALTER TABLE `more_info` DISABLE KEYS */;
INSERT INTO `more_info` VALUES (1,'male','blue'),(2,NULL,'black'),(3,'female','pink'),(4,'male',NULL),(5,'male','green');
/*!40000 ALTER TABLE `more_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `school_79`
--

DROP TABLE IF EXISTS `school_79`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `school_79` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  `age` int DEFAULT NULL,
  `class` int DEFAULT NULL,
  `avg_grade` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `school_79`
--

LOCK TABLES `school_79` WRITE;
/*!40000 ALTER TABLE `school_79` DISABLE KEYS */;
INSERT INTO `school_79` VALUES (1,'Ivanov Ivan',7,1,8.7),(2,'Petrov Petr',8,2,8.8),(3,'Sidorova Alena',9,3,8.9),(4,'Midlov Serhey',10,4,6.7),(5,'Lipova Oksana',11,5,5.4),(6,'Buharevich Igor',12,6,9.4),(7,'Dayrova Elena',13,7,8),(8,'Pochepov Vladimir',14,8,7),(9,'Fursov Nikita',15,9,8.1),(10,'Pestraya Irina',16,10,9.1),(11,'Botanov Mihail',17,11,9.9);
/*!40000 ALTER TABLE `school_79` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `school_80`
--

DROP TABLE IF EXISTS `school_80`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `school_80` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  `age` int DEFAULT NULL,
  `class` int DEFAULT NULL,
  `avg_grade` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `school_80`
--

LOCK TABLES `school_80` WRITE;
/*!40000 ALTER TABLE `school_80` DISABLE KEYS */;
INSERT INTO `school_80` VALUES (1,'Delphi Oleg',7,1,5.6),(2,'Oracle Denis ',8,2,4.2),(3,'Python Dimitar',9,3,7.9),(4,'Tarantul Anna',10,4,5.7),(5,'Java Yana',11,5,9.3),(6,'Povidlov John',12,6,7.4),(7,'Reader Nina',13,7,8.2),(8,'Joinov Petr',14,8,7.3),(9,'Printova Lesya',15,9,6.1),(10,'Prostov Ivan',16,10,4.2),(11,'Kikimorova Nika',17,11,9.8);
/*!40000 ALTER TABLE `school_80` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-25 22:41:29
