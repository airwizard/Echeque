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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$30000$OzwSG1lMihnV$jdUAeX9rz5S8SlJAIPW6TfmI5ruKLblVgQPJ1AjuAHA=','2017-03-24 16:07:19.379896',0,'amy','','','amy@gmail.com',0,1,'2017-02-23 13:52:51.444269'),(2,'pbkdf2_sha256$30000$DliqPty0iV2q$WUc3whHapGUGd+350Cy4WuTYoVArjh+IJxlpyuYAHKo=',NULL,0,'bob','','','bob@gmail.com',0,1,'2017-02-23 14:44:08.416066'),(3,'pbkdf2_sha256$30000$4tEfiLS9Iu5N$8Z2O6HH0W94+pThDFFsSMTF8wbXyVCK/7ktEtYiZQ6M=',NULL,0,'ace','','','ace@gmail.com',0,1,'2017-02-23 14:44:34.503863'),(4,'pbkdf2_sha256$30000$FUyieYlJ3tia$EqFzVvj7ajS3ZmGyukObzWyzSlWscxSgYp0fVOOmLqE=',NULL,0,'ted','','','ted@gmail.com',0,1,'2017-02-23 14:45:02.253811'),(5,'pbkdf2_sha256$30000$gBweCywGgKYO$1pcHPvPZp+RnagCnzqhQ5m7WkJLb8DKxon5470ut5HA=',NULL,0,'gingko','','','gingko@gmail.com',0,1,'2017-02-23 14:45:27.446248'),(6,'pbkdf2_sha256$30000$hmp5mRPX0Oaj$DCtKT9SmKbSG/qergM04x2sQJel7Z+Ca/XrbMsRyLUM=',NULL,0,'emma','','','emma@gmail.com',0,1,'2017-03-01 17:29:11.809153'),(7,'pbkdf2_sha256$30000$uMoiMRxOEKvL$aJd3d/NkiQHelNkRcwXg0TvzbnriDXQkY0FMJAKwzVw=','2017-03-24 16:07:37.940241',0,'test','','','test@gmail.com',0,1,'2017-03-23 12:53:18.992642');
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

-- Dump completed on 2017-03-24 11:42:15
