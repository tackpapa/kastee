-- MySQL dump 10.13  Distrib 5.7.9, for osx10.9 (x86_64)
--
-- Host: 127.0.0.1    Database: newschema
-- ------------------------------------------------------
-- Server version	5.5.42

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
-- Table structure for table `announcements`
--

DROP TABLE IF EXISTS `announcements`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `announcements` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` varchar(45) DEFAULT NULL,
  `content` varchar(45) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `apt` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id_idx` (`user_id`),
  CONSTRAINT `user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `announcements`
--

LOCK TABLES `announcements` WRITE;
/*!40000 ALTER TABLE `announcements` DISABLE KEYS */;
INSERT INTO `announcements` VALUES (1,'2015.2.22','Potluck Party in Saturday 1pm in main hall',1,'fountain'),(8,'2016-05-24 18:36:36','barbecue party next friday!',7,'archstone'),(9,'2016-05-24 18:37:45','lala',7,'archstone'),(10,'2016-05-24 19:22:37','rent due tomorrow',1,'fountain'),(13,'2016-05-26 11:13:47','yo',9,'eddy');
/*!40000 ALTER TABLE `announcements` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comment` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `message_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_comments_messages1_idx` (`message_id`,`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (6,'again testuser2','2016-05-15 18:55:03','2016-05-15 18:55:03',1,12),(7,'asdfa','2016-05-15 18:59:01','2016-05-15 18:59:01',1,12),(11,'for kiyoung tack only','2016-05-15 19:00:12','2016-05-15 19:00:12',1,13),(14,'cmt del','2016-05-15 19:01:22','2016-05-15 19:01:22',2,14),(17,'my comment','2016-05-15 19:01:55','2016-05-15 19:01:55',2,15),(21,'a yo','2016-05-23 22:19:44','2016-05-23 22:19:44',1,16),(22,'write your comments heresdafaf\r\n','2016-05-23 23:44:08','2016-05-23 23:44:08',1,14),(23,'yesssss','2016-05-24 03:58:34','2016-05-24 03:58:34',1,18),(24,'wtf','2016-05-24 04:53:52','2016-05-24 04:53:52',4,18),(25,'ok','2016-05-24 04:54:14','2016-05-24 04:54:14',1,19),(26,'write your comments here','2016-05-24 12:44:17','2016-05-24 12:44:17',1,20),(27,'same thing','2016-05-24 12:51:27','2016-05-24 12:51:27',1,20),(28,'im down iwill bring beer ','2016-05-24 14:20:00','2016-05-24 14:20:00',1,21),(29,'yaay','2016-05-24 17:29:05','2016-05-24 17:29:05',2,23),(30,'really?','2016-05-24 18:35:20','2016-05-24 18:35:20',8,24),(31,'me 2','2016-05-26 11:00:33','2016-05-26 11:00:33',4,23),(32,'so what','2016-05-26 11:14:49','2016-05-26 11:14:49',10,26);
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dmcomments`
--

DROP TABLE IF EXISTS `dmcomments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dmcomments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `dm_id` int(11) DEFAULT NULL,
  `dmcomment` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `dm_id_idx` (`dm_id`),
  KEY `user_id_idx` (`user_id`),
  CONSTRAINT `dm_id` FOREIGN KEY (`dm_id`) REFERENCES `dms` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dmcomments`
--

LOCK TABLES `dmcomments` WRITE;
/*!40000 ALTER TABLE `dmcomments` DISABLE KEYS */;
INSERT INTO `dmcomments` VALUES (4,1,12,'no im not hi\r\n','2016-05-24 13:04:25'),(6,2,8,'is it working?','2016-05-24 17:30:21'),(7,2,6,'no','2016-05-24 17:38:16'),(8,2,8,'hey man','2016-05-24 17:38:33'),(9,2,8,'whatsup','2016-05-24 17:45:21'),(10,1,11,'what','2016-05-26 10:11:52');
/*!40000 ALTER TABLE `dmcomments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dms`
--

DROP TABLE IF EXISTS `dms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dms` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dm` varchar(255) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `friend_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id_idx` (`user_id`),
  KEY `friend_id_idx` (`friend_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dms`
--

LOCK TABLES `dms` WRITE;
/*!40000 ALTER TABLE `dms` DISABLE KEYS */;
INSERT INTO `dms` VALUES (1,'yo man whats up',0,0,'2016-05-24 03:46:31'),(2,'yo man',1,2,'2016-05-24 03:49:16'),(3,'yo dude',1,2,'2016-05-24 03:59:59'),(4,'second attempt\r\n',1,2,'2016-05-24 04:16:20'),(5,'lalal',1,2,'2016-05-24 04:19:49'),(6,'thirdddd',1,2,'2016-05-24 04:20:33'),(7,'fourth',1,2,'2016-05-24 04:20:50'),(8,'fifth',1,2,'2016-05-24 04:21:37'),(9,'yo man',1,4,'2016-05-24 04:54:50'),(10,'this is direct msg',1,1,'2016-05-24 12:44:29'),(11,'lalalal',2,1,'2016-05-24 13:03:20'),(12,'hi frank',2,1,'2016-05-24 13:03:25'),(13,'my sink is broken',1,4,'2016-05-24 14:19:40'),(14,'yo whatsup',1,2,'2016-05-24 18:39:27'),(15,'test',1,2,'2016-05-24 19:00:39'),(16,'shut up',1,4,'2016-05-24 19:23:21');
/*!40000 ALTER TABLE `dms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `friend_id` int(11) NOT NULL,
  `apt` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_messages_users_idx` (`user_id`),
  CONSTRAINT `fk_messages_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (11,'this is for test user','2016-05-15 18:39:37','2016-05-15 18:39:37',1,3,'fountain'),(12,'TESTUSER ONLY MSG','2016-05-15 18:52:10','2016-05-15 18:52:10',1,3,'fountain'),(13,'for kiyoung tack only','2016-05-15 19:00:05','2016-05-15 19:00:05',1,1,'fountain'),(18,'nooooo','2016-05-24 03:58:22','2016-05-24 03:58:22',2,1,'fountain'),(20,'so what','2016-05-24 12:44:14','2016-05-24 12:44:14',1,1,'fountain'),(21,'i want barbecue','2016-05-24 14:19:51','2016-05-24 14:19:51',1,1,'fountain'),(22,'lalala i wanna play basketball','2016-05-24 17:27:35','2016-05-24 17:27:35',2,0,'fountain'),(23,'i wanna play pingpong','2016-05-24 17:28:58','2016-05-24 17:28:58',2,0,'fountain'),(24,'I\'m the first one to Post','2016-05-24 18:33:26','2016-05-24 18:33:26',7,0,'archstone'),(25,'Im the first one in this apartment ','2016-05-26 11:13:37','2016-05-26 11:13:37',9,0,'eddy'),(26,'hi im new','2016-05-26 11:14:43','2016-05-26 11:14:43',10,0,'eddy');
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first` varchar(45) DEFAULT NULL,
  `last` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `pw` varchar(255) DEFAULT NULL,
  `level` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `apt` varchar(45) DEFAULT NULL,
  `car` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'kiyoung','101','caca@ca.com','$2b$12$bsdltbR7Er9/kopqSholK.mYK2RFYmTsoRMxLVpqI3JNWxecRlK.e',9,'2016-05-14 23:54:24','2016-05-14 23:54:24','fountain',NULL),(2,'redbull','102','jkjk@jk.com','$2b$12$g9x5o31XvVQ6IWWh64XY5uO7nu4ZYHRMMr3mB7pZ5m.A1IYEdYPqy',7,'2016-05-15 00:45:15','2016-05-15 00:45:15','fountain',NULL),(5,'kkangpe','105','kk@kk.com','$2b$12$VcKmaHcUHldDZnhB3hZOteZMcD.Rz3bDQpCaDO2JcXczyLMbJIZRq',6,'2016-05-24 16:14:34','2016-05-24 16:14:34','fountain',NULL),(6,'mango','202','mm@mm.com','$2b$12$qx4fUjBTTtcbq7hHbZkfBuyhsyK9bSicsDnch3TXfTBmPG3QnTG2e',1,'2016-05-24 16:20:25','2016-05-24 16:20:25','fountain',NULL),(7,'chuck norris','501','rr@rr.com','$2b$12$8ifTpStd34q3e6TUSbpy3.uT3lwC4QRzdD.w6N1dnj0jYd5dUbBAi',6,'2016-05-24 18:31:58','2016-05-24 18:31:58','archstone',NULL),(8,'connor tack','502','ee@ee.com','$2b$12$EhveklabwNity/uC5dcbUOHH41ZxW8igOk1uIAIU8AQQXOMGqfwwO',1,'2016-05-24 18:34:02','2016-05-24 18:34:02','archstone',NULL),(9,'Eddy Norris','302','jj@jj.com','$2b$12$ps2cqUrjFEewdEt/asU3AO33v5o3TRSpAPADmUwfw3exSiyrXYL2K',6,'2016-05-26 11:13:20','2016-05-26 11:13:20','eddy','6Xgy341'),(10,'Eddys daughter','102','yy@yy.com','$2b$12$VtCOvc8iOYkc7Tatb6lrTumBWv70SRHnEi3QbQR4DX7pQaIChgOXi',1,'2016-05-26 11:14:29','2016-05-26 11:14:29','eddy','ksdknf');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-05-26 13:04:42
