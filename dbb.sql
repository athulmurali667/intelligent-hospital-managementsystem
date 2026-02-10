/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.33 : Database - hospital_management
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`hospital_management` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `hospital_management`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add booking_table',7,'add_booking_table'),
(26,'Can change booking_table',7,'change_booking_table'),
(27,'Can delete booking_table',7,'delete_booking_table'),
(28,'Can view booking_table',7,'view_booking_table'),
(29,'Can add department_table',8,'add_department_table'),
(30,'Can change department_table',8,'change_department_table'),
(31,'Can delete department_table',8,'delete_department_table'),
(32,'Can view department_table',8,'view_department_table'),
(33,'Can add login_table',9,'add_login_table'),
(34,'Can change login_table',9,'change_login_table'),
(35,'Can delete login_table',9,'delete_login_table'),
(36,'Can view login_table',9,'view_login_table'),
(37,'Can add hospital_table',10,'add_hospital_table'),
(38,'Can change hospital_table',10,'change_hospital_table'),
(39,'Can delete hospital_table',10,'delete_hospital_table'),
(40,'Can view hospital_table',10,'view_hospital_table'),
(41,'Can add doctor_table',11,'add_doctor_table'),
(42,'Can change doctor_table',11,'change_doctor_table'),
(43,'Can delete doctor_table',11,'delete_doctor_table'),
(44,'Can view doctor_table',11,'view_doctor_table'),
(45,'Can add prescription_table',12,'add_prescription_table'),
(46,'Can change prescription_table',12,'change_prescription_table'),
(47,'Can delete prescription_table',12,'delete_prescription_table'),
(48,'Can view prescription_table',12,'view_prescription_table'),
(49,'Can add schedule_table',13,'add_schedule_table'),
(50,'Can change schedule_table',13,'change_schedule_table'),
(51,'Can delete schedule_table',13,'delete_schedule_table'),
(52,'Can view schedule_table',13,'view_schedule_table'),
(53,'Can add user_table',14,'add_user_table'),
(54,'Can change user_table',14,'change_user_table'),
(55,'Can delete user_table',14,'delete_user_table'),
(56,'Can view user_table',14,'view_user_table'),
(57,'Can add rating_table',15,'add_rating_table'),
(58,'Can change rating_table',15,'change_rating_table'),
(59,'Can delete rating_table',15,'delete_rating_table'),
(60,'Can view rating_table',15,'view_rating_table'),
(61,'Can add complaint_table',16,'add_complaint_table'),
(62,'Can change complaint_table',16,'change_complaint_table'),
(63,'Can delete complaint_table',16,'delete_complaint_table'),
(64,'Can view complaint_table',16,'view_complaint_table');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(7,'myapp','booking_table'),
(16,'myapp','complaint_table'),
(8,'myapp','department_table'),
(11,'myapp','doctor_table'),
(10,'myapp','hospital_table'),
(9,'myapp','login_table'),
(12,'myapp','prescription_table'),
(15,'myapp','rating_table'),
(13,'myapp','schedule_table'),
(14,'myapp','user_table'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2024-09-22 05:51:45.377751'),
(2,'auth','0001_initial','2024-09-22 05:51:46.628669'),
(3,'admin','0001_initial','2024-09-22 05:51:47.175486'),
(4,'admin','0002_logentry_remove_auto_add','2024-09-22 05:51:47.206734'),
(5,'admin','0003_logentry_add_action_flag_choices','2024-09-22 05:51:47.237983'),
(6,'contenttypes','0002_remove_content_type_name','2024-09-22 05:51:47.472344'),
(7,'auth','0002_alter_permission_name_max_length','2024-09-22 05:51:47.597332'),
(8,'auth','0003_alter_user_email_max_length','2024-09-22 05:51:47.644210'),
(9,'auth','0004_alter_user_username_opts','2024-09-22 05:51:47.675454'),
(10,'auth','0005_alter_user_last_login_null','2024-09-22 05:51:47.831691'),
(11,'auth','0006_require_contenttypes_0002','2024-09-22 05:51:47.847317'),
(12,'auth','0007_alter_validators_add_error_messages','2024-09-22 05:51:47.862941'),
(13,'auth','0008_alter_user_username_max_length','2024-09-22 05:51:48.041361'),
(14,'auth','0009_alter_user_last_name_max_length','2024-09-22 05:51:48.166355'),
(15,'auth','0010_alter_group_name_max_length','2024-09-22 05:51:48.275720'),
(16,'auth','0011_update_proxy_permissions','2024-09-22 05:51:48.330937'),
(17,'auth','0012_alter_user_first_name_max_length','2024-09-22 05:51:48.549673'),
(18,'myapp','0001_initial','2024-09-22 05:51:50.674525'),
(19,'sessions','0001_initial','2024-09-22 05:51:50.783895'),
(20,'myapp','0002_alter_doctor_table_age','2024-09-22 11:36:52.869090');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('drailnj7zie9jqmsepcghxlyy78o2f1l','eyJsaWQiOjd9:1ssKXZ:BixaFFeFIaG5Uhl91KMiJR79NMyfAbMszlHcPRe3VfI','2024-10-06 11:14:09.422277'),
('im1epw8r7udszaz2c1bs1bk9daahs5d1','eyJsaWQiOjF9:1ssIbL:xqOleHMV3tgQQ3D5W17nOPTZ0iVp3DQBFbbJWYaFhOQ','2024-10-06 09:09:55.276119'),
('rxinzaapmcvxnpcg4ra7y1lwt9lttl0z','eyJsaWQiOjExfQ:1ssKvy:TfWULFn0yN4q-9NJnJJcYvFWbW7DNeoZ8DjEAaCFAH4','2024-10-06 11:39:22.748504'),
('wphqy3cdrvy1yw57worno8xihhs484mc','eyJsaWQiOjV9:1ssGU6:5_6h1a66VRAccDZhaju9OvdZds3cBpNJl7EiilFY2CE','2024-10-06 06:54:18.385660');

/*Table structure for table `myapp_booking_table` */

DROP TABLE IF EXISTS `myapp_booking_table`;

CREATE TABLE `myapp_booking_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `status` varchar(100) NOT NULL,
  `SCHEDULE_id` bigint NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_booking_table_SCHEDULE_id_a5990019_fk_myapp_sch` (`SCHEDULE_id`),
  KEY `myapp_booking_table_USER_id_00b8e12a_fk_myapp_user_table_id` (`USER_id`),
  CONSTRAINT `myapp_booking_table_SCHEDULE_id_a5990019_fk_myapp_sch` FOREIGN KEY (`SCHEDULE_id`) REFERENCES `myapp_schedule_table` (`id`),
  CONSTRAINT `myapp_booking_table_USER_id_00b8e12a_fk_myapp_user_table_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_booking_table` */

/*Table structure for table `myapp_complaint_table` */

DROP TABLE IF EXISTS `myapp_complaint_table`;

CREATE TABLE `myapp_complaint_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `complaint` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `reply` varchar(100) NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_complaint_table_USER_id_fc088c0e_fk_myapp_user_table_id` (`USER_id`),
  CONSTRAINT `myapp_complaint_table_USER_id_fc088c0e_fk_myapp_user_table_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_complaint_table` */

/*Table structure for table `myapp_department_table` */

DROP TABLE IF EXISTS `myapp_department_table`;

CREATE TABLE `myapp_department_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `department` varchar(100) NOT NULL,
  `details` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_department_table` */

insert  into `myapp_department_table`(`id`,`department`,`details`) values 
(1,'eye','eye care');

/*Table structure for table `myapp_doctor_table` */

DROP TABLE IF EXISTS `myapp_doctor_table`;

CREATE TABLE `myapp_doctor_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `age` date NOT NULL,
  `gender` varchar(100) NOT NULL,
  `qualifiction` varchar(100) NOT NULL,
  `specialization` varchar(100) NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `DEPARTMENT_id` bigint NOT NULL,
  `HOSPITAL_id` bigint NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_doctor_table_DEPARTMENT_id_43d69e28_fk_myapp_dep` (`DEPARTMENT_id`),
  KEY `myapp_doctor_table_HOSPITAL_id_21a4f52f_fk_myapp_hos` (`HOSPITAL_id`),
  KEY `myapp_doctor_table_LOGIN_id_2bf8efd4_fk_myapp_login_table_id` (`LOGIN_id`),
  CONSTRAINT `myapp_doctor_table_DEPARTMENT_id_43d69e28_fk_myapp_dep` FOREIGN KEY (`DEPARTMENT_id`) REFERENCES `myapp_department_table` (`id`),
  CONSTRAINT `myapp_doctor_table_HOSPITAL_id_21a4f52f_fk_myapp_hos` FOREIGN KEY (`HOSPITAL_id`) REFERENCES `myapp_hospital_table` (`id`),
  CONSTRAINT `myapp_doctor_table_LOGIN_id_2bf8efd4_fk_myapp_login_table_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `myapp_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_doctor_table` */

insert  into `myapp_doctor_table`(`id`,`name`,`age`,`gender`,`qualifiction`,`specialization`,`phone`,`email`,`photo`,`DEPARTMENT_id`,`HOSPITAL_id`,`LOGIN_id`) values 
(1,'anil','2024-09-04','male','MBBS','EYE',23456789,'anil777@gmail.com','images_5CVjmnY.jfif',1,1,11);

/*Table structure for table `myapp_hospital_table` */

DROP TABLE IF EXISTS `myapp_hospital_table`;

CREATE TABLE `myapp_hospital_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  `latitude` double NOT NULL,
  `longitude` double NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_hospital_table_LOGIN_id_cf107bdf_fk_myapp_login_table_id` (`LOGIN_id`),
  CONSTRAINT `myapp_hospital_table_LOGIN_id_cf107bdf_fk_myapp_login_table_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `myapp_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_hospital_table` */

insert  into `myapp_hospital_table`(`id`,`name`,`place`,`post`,`phone`,`email`,`latitude`,`longitude`,`LOGIN_id`) values 
(1,'BMH','kozhikode','kozhikode',2345674567,' hospital@gmail.com',33333,345,5),
(2,'happy','kozhikode','kozhikode',2345674567,'happy@gmail.com',33333,345,7);

/*Table structure for table `myapp_login_table` */

DROP TABLE IF EXISTS `myapp_login_table`;

CREATE TABLE `myapp_login_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL,
  `type` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_login_table` */

insert  into `myapp_login_table`(`id`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(5,'hospital','hospital','hospital'),
(6,'user','user','user'),
(7,'happy','happy','hospital'),
(11,'doctor','doctor','doctor');

/*Table structure for table `myapp_prescription_table` */

DROP TABLE IF EXISTS `myapp_prescription_table`;

CREATE TABLE `myapp_prescription_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `prescription` varchar(500) NOT NULL,
  `report` varchar(1000) NOT NULL,
  `files` varchar(100) NOT NULL,
  `BOOK_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_prescription_t_BOOK_id_b817cb7a_fk_myapp_boo` (`BOOK_id`),
  CONSTRAINT `myapp_prescription_t_BOOK_id_b817cb7a_fk_myapp_boo` FOREIGN KEY (`BOOK_id`) REFERENCES `myapp_booking_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_prescription_table` */

/*Table structure for table `myapp_rating_table` */

DROP TABLE IF EXISTS `myapp_rating_table`;

CREATE TABLE `myapp_rating_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rating` double NOT NULL,
  `review` varchar(1000) NOT NULL,
  `date` date NOT NULL,
  `DOCTOR_id` bigint NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_rating_table_DOCTOR_id_539e50f8_fk_myapp_doctor_table_id` (`DOCTOR_id`),
  KEY `myapp_rating_table_USER_id_e76d06f2_fk_myapp_user_table_id` (`USER_id`),
  CONSTRAINT `myapp_rating_table_DOCTOR_id_539e50f8_fk_myapp_doctor_table_id` FOREIGN KEY (`DOCTOR_id`) REFERENCES `myapp_doctor_table` (`id`),
  CONSTRAINT `myapp_rating_table_USER_id_e76d06f2_fk_myapp_user_table_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_rating_table` */

/*Table structure for table `myapp_schedule_table` */

DROP TABLE IF EXISTS `myapp_schedule_table`;

CREATE TABLE `myapp_schedule_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fromtime` time(6) NOT NULL,
  `totime` time(6) NOT NULL,
  `date` date NOT NULL,
  `DOCTOR_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_schedule_table_DOCTOR_id_fbda35d5_fk_myapp_doctor_table_id` (`DOCTOR_id`),
  CONSTRAINT `myapp_schedule_table_DOCTOR_id_fbda35d5_fk_myapp_doctor_table_id` FOREIGN KEY (`DOCTOR_id`) REFERENCES `myapp_doctor_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_schedule_table` */

/*Table structure for table `myapp_user_table` */

DROP TABLE IF EXISTS `myapp_user_table`;

CREATE TABLE `myapp_user_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `age` int NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_user_table_LOGIN_id_76a60eb1_fk_myapp_login_table_id` (`LOGIN_id`),
  CONSTRAINT `myapp_user_table_LOGIN_id_76a60eb1_fk_myapp_login_table_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `myapp_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_user_table` */

insert  into `myapp_user_table`(`id`,`name`,`gender`,`age`,`place`,`post`,`phone`,`email`,`photo`,`LOGIN_id`) values 
(1,'user','male',23,'kozhikode','kozhikode',345678,'user@gmail.com','',6);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
