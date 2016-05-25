-- MySQL dump 10.13  Distrib 5.7.9, for osx10.9 (x86_64)
--
-- Host: 127.0.0.1    Database: mydb
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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (6,'again testuser2','2016-05-15 18:55:03','2016-05-15 18:55:03',1,12),(7,'asdfa','2016-05-15 18:59:01','2016-05-15 18:59:01',1,12),(9,'works?','2016-05-15 18:59:29','2016-05-15 18:59:29',1,10),(11,'for kiyoung tack only','2016-05-15 19:00:12','2016-05-15 19:00:12',1,13),(14,'cmt del','2016-05-15 19:01:22','2016-05-15 19:01:22',2,14),(17,'my comment','2016-05-15 19:01:55','2016-05-15 19:01:55',2,15),(18,'ha','2016-05-15 19:02:18','2016-05-15 19:02:18',2,16),(19,'hi','2016-05-15 19:02:21','2016-05-15 19:02:21',2,16),(20,'is it?','2016-05-15 19:02:26','2016-05-15 19:02:26',2,12);
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
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
  PRIMARY KEY (`id`),
  KEY `fk_messages_users_idx` (`user_id`),
  CONSTRAINT `fk_messages_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (3,'aklsdjfklsa','2016-05-15 02:14:04','2016-05-15 02:14:04',2,1),(4,'ksjalkfja;kljsfaklf','2016-05-15 02:20:23','2016-05-15 02:20:23',2,2),(6,'this is msg for taco taki','2016-05-15 18:18:18','2016-05-15 18:18:18',1,3),(7,'lala','2016-05-15 18:19:25','2016-05-15 18:19:25',1,1),(8,'kljaklf','2016-05-15 18:22:33','2016-05-15 18:22:33',1,2),(9,'does it work?','2016-05-15 18:36:36','2016-05-15 18:36:36',1,2),(10,'does it work','2016-05-15 18:36:40','2016-05-15 18:36:40',1,1),(11,'this is for test user','2016-05-15 18:39:37','2016-05-15 18:39:37',1,3),(12,'TESTUSER ONLY MSG','2016-05-15 18:52:10','2016-05-15 18:52:10',1,3),(13,'for kiyoung tack only','2016-05-15 19:00:05','2016-05-15 19:00:05',1,1),(14,'i wrote sth for u','2016-05-15 19:01:15','2016-05-15 19:01:15',2,1),(15,'eh?','2016-05-15 19:01:41','2016-05-15 19:01:41',2,2),(16,'dude','2016-05-15 19:02:16','2016-05-15 19:02:16',2,3);
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'kiyoung','tack','caca@ca.com','$2b$12$bsdltbR7Er9/kopqSholK.mYK2RFYmTsoRMxLVpqI3JNWxecRlK.e',9,'2016-05-14 23:54:24','2016-05-14 23:54:24'),(2,'taco','taki','jkjk@jk.com','$2b$12$g2GZ64UTqmRTo2ULKVVru.Sf7IXBEA22pCbFRWp8714wYGbO7bqaK',1,'2016-05-15 00:45:15','2016-05-15 00:45:15'),(3,'test','user','1@1.com','$2b$12$Keb9sSWGHCpMZQ5GAzkkuetuBgWhJ5Q4yjhleYliLqckQ7H9WmDye',1,'2016-05-15 02:49:57','2016-05-15 02:49:57');
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

-- Dump completed on 2016-05-15 19:13:20
