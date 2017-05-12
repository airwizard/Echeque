-- MySQL dump 10.13  Distrib 5.7.17, for Linux (x86_64)
--
-- Host: localhost    Database: Echeque
-- ------------------------------------------------------
-- Server version	5.7.17

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$30000$uy9FPa6wFt8v$tpqCI68buQ7GaEKGab35o9WEdmqcYp+/QoE67UTyqdM=','2017-03-27 07:56:09.685621',0,'HSBC','','','hsbc@gmail.com',0,1,'2017-03-27 02:57:33.550946'),(2,'pbkdf2_sha256$30000$7eH85PMHhAHK$pv4YAQfdepcSJUL/q+PyeOuwqzR7zt1qu29E21DYAKs=',NULL,0,'BOC','','','boc@gmail.com',0,1,'2017-03-27 04:01:11.488535'),(3,'pbkdf2_sha256$30000$75lSPaVjtn4T$XtizqLEJ69a59Pnirvx7DZbOe866vdKpOxv1QmDDWtQ=',NULL,0,'HangSeng','','','hangseng@gmail.com',0,1,'2017-03-27 04:02:23.149062'),(4,'pbkdf2_sha256$30000$DpwoT40UehsX$klqjQNUqMhGQSY3e+ku1WspnXKpnjEB1i1582J5E3kA=','2017-03-30 10:19:57.493623',0,'Gingko','','','gingko@gmail.com',0,1,'2017-03-27 04:03:37.928595'),(5,'pbkdf2_sha256$30000$dC58a1onjvxG$PRsX2+jSAgf6z7IfN5UIe8kc4mdw0Y/X6broSmkxuBg=','2017-04-07 03:28:24.683064',0,'Lyu','','','lyufujie@outlook.com',0,1,'2017-03-27 04:04:23.520909'),(6,'pbkdf2_sha256$30000$o3ghFFk6Xqfd$Vq/eSqTsJZqbFRySk++WD8ZAWy/IPo+X+gpn+XONdLs=',NULL,0,'Jolin','','','jolin@gmail.com',0,1,'2017-03-30 10:19:42.906705'),(7,'pbkdf2_sha256$30000$LjejoCqmdFK5$9a/RcEqiP/RUK40JhxRskNy6o9YZrDKBvywfgDdqb9o=',NULL,0,'Amy','','','amy@gmail.com',0,1,'2017-04-07 03:27:26.731516'),(8,'pbkdf2_sha256$30000$iiwuvPydYu0R$69srZeY+1OUl6i8ef3brPCme9KkIpFbyZzaaz8fsfkk=',NULL,0,'Bob','','','bob@gmail.com',0,1,'2017-04-07 03:27:56.766929');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-04-06 20:38:50
