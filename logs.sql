-- MySQL dump 10.13  Distrib 5.7.28, for Linux (x86_64)
--
-- Host: localhost    Database: logs
-- ------------------------------------------------------
-- Server version	5.7.28-0ubuntu0.16.04.2

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
-- Table structure for table `o_error_nginx`
--

DROP TABLE IF EXISTS `o_error_nginx`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `o_error_nginx` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `level` char(10) NOT NULL,
  `msg` text NOT NULL,
  `day` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `day_level` (`day`,`level`)
) ENGINE=InnoDB AUTO_INCREMENT=27014 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `o_error_php`
--

DROP TABLE IF EXISTS `o_error_php`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `o_error_php` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `request` text NOT NULL,
  `day` date NOT NULL,
  `trace` text NOT NULL,
  `post` text NOT NULL,
  PRIMARY KEY (`id`),
  KEY `day` (`day`)
) ENGINE=InnoDB AUTO_INCREMENT=107 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `o_error_yii2`
--

DROP TABLE IF EXISTS `o_error_yii2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `o_error_yii2` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `code` char(6) NOT NULL,
  `msg` text NOT NULL,
  `day` date NOT NULL,
  `trace` text NOT NULL,
  `stack` mediumtext NOT NULL,
  `type` enum('error-fatal-api','error-fatal-game','error-fatal-system','error-game','error-api') NOT NULL,
  PRIMARY KEY (`id`),
  KEY `day` (`day`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `o_slow_php`
--

DROP TABLE IF EXISTS `o_slow_php`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `o_slow_php` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `hash` char(32) NOT NULL,
  `stack` text NOT NULL,
  `cnt` smallint(5) NOT NULL,
  `day` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `day` (`day`)
) ENGINE=InnoDB AUTO_INCREMENT=4632 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `s_error_nginx`
--

DROP TABLE IF EXISTS `s_error_nginx`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `s_error_nginx` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `level` char(10) NOT NULL,
  `msg` text NOT NULL,
  `day` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `day_level` (`day`,`level`)
) ENGINE=InnoDB AUTO_INCREMENT=20891 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `s_error_php`
--

DROP TABLE IF EXISTS `s_error_php`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `s_error_php` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `request` text NOT NULL,
  `day` date NOT NULL,
  `trace` text NOT NULL,
  `post` text NOT NULL,
  PRIMARY KEY (`id`),
  KEY `day` (`day`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `s_error_yii2`
--

DROP TABLE IF EXISTS `s_error_yii2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `s_error_yii2` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `code` char(6) NOT NULL,
  `msg` text NOT NULL,
  `day` date NOT NULL,
  `trace` text NOT NULL,
  `stack` mediumtext NOT NULL,
  `type` enum('error-fatal-api','error-fatal-game','error-fatal-system','error-game','error-api') NOT NULL,
  PRIMARY KEY (`id`),
  KEY `day` (`day`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `s_slow_php`
--

DROP TABLE IF EXISTS `s_slow_php`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `s_slow_php` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `hash` char(32) NOT NULL,
  `stack` text NOT NULL,
  `cnt` smallint(5) NOT NULL,
  `day` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `day` (`day`)
) ENGINE=InnoDB AUTO_INCREMENT=4387 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-23 15:00:56
