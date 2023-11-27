-- Adminer 4.8.1 MySQL 10.11.4-MariaDB-1~deb12u1 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `admin_id` int(11) NOT NULL AUTO_INCREMENT,
  `login` varchar(32) NOT NULL,
  `mot_de_passe` varchar(256) NOT NULL,
  PRIMARY KEY (`admin_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `admin` (`admin_id`, `login`, `mot_de_passe`) VALUES
(1,	'22106979',	'$2y$10$ZAYdbBBUH7z5MwySHjiOeeswuZaxxpFHr4tY7uU6Dxb3/K/rrXXFS');

DROP TABLE IF EXISTS `Compte`;
CREATE TABLE `Compte` (
  `etu_num` int(11) NOT NULL,
  `opr_date` datetime NOT NULL,
  `opr_montant` decimal(15,2) DEFAULT 0.00,
  `opr_libelle` varchar(50) DEFAULT NULL,
  `type_opeartion` varchar(255) NOT NULL,
  PRIMARY KEY (`etu_num`,`opr_date`),
  KEY `type_opeartion` (`type_opeartion`),
  CONSTRAINT `Compte_ibfk_1` FOREIGN KEY (`etu_num`) REFERENCES `Etudiant` (`etu_num`),
  CONSTRAINT `Compte_ibfk_2` FOREIGN KEY (`type_opeartion`) REFERENCES `Type` (`type_opeartion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `Compte` (`etu_num`, `opr_date`, `opr_montant`, `opr_libelle`, `type_opeartion`) VALUES
(1,	'2023-03-09 09:15:34',	1.00,	'Initial',	'Bonus'),
(1,	'2023-05-15 15:18:44',	-0.20,	'Cafe',	'Dépense'),
(1,	'2023-07-11 11:14:05',	-0.20,	'Chocolat',	'Dépense'),
(1,	'2023-07-24 15:20:20',	-0.20,	'Café',	'Dépense'),
(2,	'2023-05-09 11:18:32',	1.00,	'Atelier Avec Dupont',	'Bonus'),
(2,	'2023-05-16 08:23:32',	1.00,	'Inital',	'Bonus'),
(2,	'2023-07-04 15:24:35',	1.00,	'Projet avec Pr Tournesol',	'Bonus'),
(2,	'2023-07-06 15:24:35',	-0.20,	'Thé',	'Dépense'),
(2,	'2023-07-26 15:23:32',	1.00,	'Chanson opéra pour Haddock',	'Bonus'),
(3,	'2023-05-18 15:26:38',	1.00,	'initial',	'Bonus'),
(4,	'2023-07-13 15:27:04',	1.00,	'intiial',	'Bonus'),
(4,	'2023-07-21 13:10:40',	-0.20,	'Café',	'Dépense');

DROP TABLE IF EXISTS `Etudiant`;
CREATE TABLE `Etudiant` (
  `etu_num` int(11) NOT NULL AUTO_INCREMENT,
  `etu_nom` varchar(255) DEFAULT NULL,
  `etu_prenom` varchar(255) DEFAULT NULL,
  `etu_solde` decimal(15,2) DEFAULT 0.00,
  `etu_bonus` decimal(15,2) DEFAULT 0.00,
  PRIMARY KEY (`etu_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `Etudiant` (`etu_num`, `etu_nom`, `etu_prenom`, `etu_solde`, `etu_bonus`) VALUES
(1,	'Thompson',	'Allan',	0.00,	1.00),
(2,	'Castafiore',	'Bianca',	0.00,	0.00),
(3,	'Lampion',	'Séraphin',	0.00,	0.00),
(4,	'Da Figueira',	'Oliveira',	0.00,	0.00),
(6,	'Boucher',	'Adrien',	0.00,	1.00),
(9,	'machar',	'antoine',	0.00,	0.00),
(78,	'Lapute',	'adrien',	0.00,	0.00),
(89,	'dhdfhf',	'hiihihih',	0.00,	0.00),
(95,	'balltrou',	'nayar',	0.00,	1.00),
(22103436,	'Pauws',	'El Grande Nicolas',	0.00,	11.00),
(22104088,	'Fernandes',	'Mathias',	0.00,	0.00);

DROP TABLE IF EXISTS `Type`;
CREATE TABLE `Type` (
  `type_opeartion` varchar(255) NOT NULL,
  PRIMARY KEY (`type_opeartion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `Type` (`type_opeartion`) VALUES
('Bonus'),
('Bonus transféré'),
('Dépense'),
('Recharge');

-- 2023-11-27 22:05:36
