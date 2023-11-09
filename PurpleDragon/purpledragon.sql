-- phpMyAdmin SQL Dump
-- version 5.1.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 09, 2023 at 02:15 PM
-- Server version: 5.7.24
-- PHP Version: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `purpledragon`
--

-- --------------------------------------------------------

--
-- Table structure for table `compte`
--

CREATE TABLE `compte` (
  `etu_num` int(11) NOT NULL,
  `opr_date` datetime NOT NULL,
  `opr_montant` decimal(15,2) DEFAULT '0.00',
  `opr_libelle` varchar(50) DEFAULT NULL,
  `type_opeartion` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `compte`
--

INSERT INTO `compte` (`etu_num`, `opr_date`, `opr_montant`, `opr_libelle`, `type_opeartion`) VALUES
(1, '2023-03-09 09:15:34', '1.00', 'Initial', 'Bonus'),
(1, '2023-05-15 15:18:44', '-0.20', 'Cafe', 'Dépense'),
(1, '2023-07-11 11:14:05', '-0.20', 'Chocolat', 'Dépense'),
(1, '2023-07-24 15:20:20', '-0.20', 'Café', 'Dépense'),
(2, '2023-05-09 11:18:32', '1.00', 'Atelier Avec Dupont', 'Bonus'),
(2, '2023-05-16 08:23:32', '1.00', 'Inital', 'Bonus'),
(2, '2023-07-04 15:24:35', '1.00', 'Projet avec Pr Tournesol', 'Bonus'),
(2, '2023-07-06 15:24:35', '-0.20', 'Thé', 'Dépense'),
(2, '2023-07-26 15:23:32', '1.00', 'Chanson opéra pour Haddock', 'Bonus'),
(3, '2023-05-18 15:26:38', '1.00', 'initial', 'Bonus'),
(4, '2023-07-13 15:27:04', '1.00', 'intiial', 'Bonus'),
(4, '2023-07-21 13:10:40', '-0.20', 'Café', 'Dépense');

-- --------------------------------------------------------

--
-- Table structure for table `etudiant`
--

CREATE TABLE `etudiant` (
  `etu_num` int(11) NOT NULL,
  `etu_nom` varchar(255) DEFAULT NULL,
  `etu_prenom` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `etudiant`
--

INSERT INTO `etudiant` (`etu_num`, `etu_nom`, `etu_prenom`) VALUES
(1, 'Thompson', 'Allan'),
(2, 'Castafiore', 'Bianca'),
(3, 'Lampion', 'Séraphin'),
(4, 'Da Figueira', 'Oliveira');

-- --------------------------------------------------------

--
-- Table structure for table `type`
--

CREATE TABLE `type` (
  `type_opeartion` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `type`
--

INSERT INTO `type` (`type_opeartion`) VALUES
('Bonus'),
('Bonus transféré'),
('Dépense'),
('Recharge');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `compte`
--
ALTER TABLE `compte`
  ADD PRIMARY KEY (`etu_num`,`opr_date`),
  ADD KEY `type_opeartion` (`type_opeartion`);

--
-- Indexes for table `etudiant`
--
ALTER TABLE `etudiant`
  ADD PRIMARY KEY (`etu_num`);

--
-- Indexes for table `type`
--
ALTER TABLE `type`
  ADD PRIMARY KEY (`type_opeartion`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `etudiant`
--
ALTER TABLE `etudiant`
  MODIFY `etu_num` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `compte`
--
ALTER TABLE `compte`
  ADD CONSTRAINT `compte_ibfk_1` FOREIGN KEY (`etu_num`) REFERENCES `etudiant` (`etu_num`),
  ADD CONSTRAINT `compte_ibfk_2` FOREIGN KEY (`type_opeartion`) REFERENCES `type` (`type_opeartion`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
