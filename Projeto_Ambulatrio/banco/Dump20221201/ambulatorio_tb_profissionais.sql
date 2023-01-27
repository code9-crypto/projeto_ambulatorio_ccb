-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: localhost    Database: ambulatorio
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tb_profissionais`
--

DROP TABLE IF EXISTS `tb_profissionais`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tb_profissionais` (
  `idprofissionais` int NOT NULL AUTO_INCREMENT,
  `nome_completo` varchar(45) NOT NULL,
  `profissao` varchar(10) NOT NULL,
  `fkcontas` int DEFAULT NULL,
  `fk_atendimento` int DEFAULT NULL,
  `crm` varchar(6) NOT NULL,
  PRIMARY KEY (`idprofissionais`),
  UNIQUE KEY `nome_completo` (`nome_completo`),
  UNIQUE KEY `fk_atendimento` (`fk_atendimento`),
  KEY `fkcontas` (`fkcontas`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_profissionais`
--

LOCK TABLES `tb_profissionais` WRITE;
/*!40000 ALTER TABLE `tb_profissionais` DISABLE KEYS */;
INSERT INTO `tb_profissionais` VALUES (1,'William caetano de souza','enfermeiro',NULL,NULL,'123456'),(2,'Adriano Garcez','médico',NULL,NULL,'234567'),(3,'Rafael barbosa','médico',NULL,NULL,'345678'),(4,'João Carlos','médico',NULL,NULL,'456789'),(5,'Adriano saldanha','médico',NULL,NULL,'567891');
/*!40000 ALTER TABLE `tb_profissionais` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-01 14:02:11