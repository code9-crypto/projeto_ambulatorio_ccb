-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: ambulatorio
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Table structure for table `tb_pacientes`
--

DROP TABLE IF EXISTS `tb_pacientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_pacientes` (
  `idpacientes` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(30) NOT NULL,
  `idade` int DEFAULT NULL,
  `sexo` char(1) NOT NULL,
  `telefone` varchar(15) NOT NULL,
  `comum_congregacao` varchar(19) NOT NULL,
  `ministerio` varchar(40) DEFAULT NULL,
  `cidade` varchar(25) NOT NULL,
  `estado` varchar(25) NOT NULL,
  `pais` varchar(15) NOT NULL,
  `fkpacientes_atendimento` int DEFAULT NULL,
  PRIMARY KEY (`idpacientes`),
  UNIQUE KEY `idpacientes_UNIQUE` (`idpacientes`),
  UNIQUE KEY `nome_UNIQUE` (`nome`),
  UNIQUE KEY `fkpacientes_atendimento` (`fkpacientes_atendimento`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_pacientes`
--

LOCK TABLES `tb_pacientes` WRITE;
/*!40000 ALTER TABLE `tb_pacientes` DISABLE KEYS */;
INSERT INTO `tb_pacientes` VALUES (1,'Eli Rosa França',62,'M','(13)986543216','Ilha do Sambaiatuba','Cooperador do Ofício','São Vicente','São Paulo','Brasil',1),(2,'Elizeu Rosa França',62,'M','(13)98465321','Ilha do Sambaiatuba','Encarregado','São Vicente','São Paulo','Brasil',2);
/*!40000 ALTER TABLE `tb_pacientes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-14 12:15:35
