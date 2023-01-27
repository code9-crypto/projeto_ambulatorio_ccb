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
-- Table structure for table `tb_fichas_de_atendimentos`
--

DROP TABLE IF EXISTS `tb_fichas_de_atendimentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tb_fichas_de_atendimentos` (
  `idatendimentos` int NOT NULL AUTO_INCREMENT,
  `evento` varchar(50) DEFAULT NULL,
  `nome_atendido` varchar(30) NOT NULL,
  `data` varchar(10) NOT NULL,
  `hora` varchar(5) NOT NULL,
  `alojamento` varchar(20) DEFAULT NULL,
  `clinica` varchar(20) DEFAULT NULL,
  `has` tinyint(1) DEFAULT NULL,
  `dm` tinyint(1) DEFAULT NULL,
  `dac` tinyint(1) DEFAULT NULL,
  `cirurgia_recente` tinyint(1) DEFAULT NULL,
  `alergia` varchar(15) DEFAULT NULL,
  `medicamentos_em_uso` varchar(1000) DEFAULT NULL,
  `pa` varchar(7) DEFAULT NULL,
  `pulso` varchar(7) DEFAULT NULL,
  `temperatura` varchar(5) DEFAULT NULL,
  `glicemia` varchar(2) DEFAULT NULL,
  `peso` varchar(5) DEFAULT NULL,
  `altura` varchar(6) DEFAULT NULL,
  `historico` varchar(1000) DEFAULT NULL,
  `medicacao` varchar(1000) DEFAULT NULL,
  `prescricao` varchar(1000) DEFAULT NULL,
  `retorno` varchar(1000) DEFAULT NULL,
  `hd` varchar(45) DEFAULT NULL,
  `cid` varchar(25) DEFAULT NULL,
  `tb_pacientes_fkpacientes_atendimento` int DEFAULT NULL,
  `tb_profissionais_fk_atendimento` int DEFAULT NULL,
  `identificacao_profissional` varchar(500) NOT NULL,
  `saturacao` varchar(7) DEFAULT NULL,
  `reavaliacao` char(3) NOT NULL,
  PRIMARY KEY (`idatendimentos`),
  KEY `tb_fichas_de_atendimentos_ibfk_1` (`tb_pacientes_fkpacientes_atendimento`),
  KEY `tb_fichas_de_atendimentos_ibfk_2` (`tb_profissionais_fk_atendimento`),
  CONSTRAINT `tb_fichas_de_atendimentos_ibfk_1` FOREIGN KEY (`tb_pacientes_fkpacientes_atendimento`) REFERENCES `tb_pacientes` (`fkpacientes_atendimento`),
  CONSTRAINT `tb_fichas_de_atendimentos_ibfk_2` FOREIGN KEY (`tb_profissionais_fk_atendimento`) REFERENCES `tb_profissionais` (`fk_atendimento`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_fichas_de_atendimentos`
--

LOCK TABLES `tb_fichas_de_atendimentos` WRITE;
/*!40000 ALTER TABLE `tb_fichas_de_atendimentos` DISABLE KEYS */;
INSERT INTO `tb_fichas_de_atendimentos` VALUES (1,'Reunião geral ministerial','William Caetano de Souza','01/12/2022','16:53','','',1,1,1,0,'Cimegripe','Nimesulida','95','613','46','87','456','57','tresdfgh','cvnxcb','sdfjbjh','bnm,bnm,yuop','','',3,NULL,'ADRIANO GARCEZ CRM:234567','31','SIM'),(2,'Reunião de Aconselhamento Ministerial','Eli Rosa França','02/12/2022','11:56','sdfg','sdfgsdfg',1,1,1,1,'zcvavasd','xcvzvx','645','321','687','12','687','321','sdgd','sxcvb','','','','',1,NULL,'ADRIANO SALDANHA CRM:567891','65','SIM');
/*!40000 ALTER TABLE `tb_fichas_de_atendimentos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-05 10:43:31
