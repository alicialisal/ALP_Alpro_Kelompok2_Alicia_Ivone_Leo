-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 30, 2024 at 04:23 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `foodwaste`
--

-- --------------------------------------------------------

--
-- Table structure for table `keranjangplg`
--

CREATE TABLE `keranjangplg` (
  `UserPlg` varchar(25) NOT NULL,
  `KodeResto` varchar(5) NOT NULL,
  `KodeMenu` varchar(5) NOT NULL,
  `Harga` int(11) NOT NULL,
  `Jumlah` int(11) NOT NULL,
  `NoAuto` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `mkategori`
--

CREATE TABLE `mkategori` (
  `Kode` int(11) NOT NULL,
  `Kategori` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `mkategori`
--

INSERT INTO `mkategori` (`Kode`, `Kategori`) VALUES
(1, 'Minuman'),
(2, 'Camilan'),
(3, 'Manisan'),
(4, 'Nasi'),
(5, 'Ayam & Bebek'),
(6, 'Cepat Saji'),
(7, 'Roti & Kue'),
(8, 'Japanese'),
(9, 'Bakso & Soto'),
(10, 'Mie'),
(11, 'Korean'),
(12, 'Kopi'),
(13, 'Martabak'),
(14, 'Pizza & Pasta'),
(15, 'Chinese'),
(16, 'Sate'),
(17, 'Western'),
(18, 'Sari Laut'),
(19, 'Thailand');

-- --------------------------------------------------------

--
-- Table structure for table `mmenu`
--

CREATE TABLE `mmenu` (
  `KodeMenu` varchar(5) NOT NULL,
  `NamaMenu` varchar(100) NOT NULL,
  `Stok` int(11) NOT NULL,
  `HargaMenu` int(11) NOT NULL,
  `KodeResto` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `mmenu`
--

INSERT INTO `mmenu` (`KodeMenu`, `NamaMenu`, `Stok`, `HargaMenu`, `KodeResto`) VALUES
('A01', 'roti', 0, 7000, '1'),
('A01', 'nasi', 3, 3000, 'R0001'),
('A02', 'test', 0, 0, '1'),
('A02', 'roti', 5, 5000, 'R0001'),
('A03', 'air', 4, 1000, 'R0001'),
('A04', 'sayur', 2, 3500, 'R0001'),
('A05', 'daging', 0, 10000, 'R0001');

-- --------------------------------------------------------

--
-- Table structure for table `mpelanggan`
--

CREATE TABLE `mpelanggan` (
  `KodePlg` varchar(5) NOT NULL,
  `Nama` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `NoTelp` varchar(14) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `mpelanggan`
--

INSERT INTO `mpelanggan` (`KodePlg`, `Nama`, `Email`, `NoTelp`) VALUES
('P0001', 'Alicia', 'ajuanita@student.ciputra.ac.id', '08990080560');

-- --------------------------------------------------------

--
-- Table structure for table `mresto`
--

CREATE TABLE `mresto` (
  `KodeResto` varchar(5) NOT NULL,
  `Nama` varchar(100) NOT NULL,
  `Alamat` varchar(255) NOT NULL,
  `Kategori` varchar(255) NOT NULL,
  `JamTutup` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `mresto`
--

INSERT INTO `mresto` (`KodeResto`, `Nama`, `Alamat`, `Kategori`, `JamTutup`) VALUES
('R0001', 'Warung AW', 'UC Makassar', 'Minuman, Nasi', '00:00:00'),
('R0002', 'Baba The', 'Business Park CPI', 'Nasi, Ayam & Bebek', '22:00:00'),
('R0003', 'jaya', 'jalan latimojong', 'Camilan', '19:50:50');

-- --------------------------------------------------------

--
-- Table structure for table `muser`
--

CREATE TABLE `muser` (
  `Nama` varchar(25) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `Restoran` tinyint(1) NOT NULL,
  `KodeRestoPlg` varchar(5) NOT NULL,
  `Login` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `muser`
--

INSERT INTO `muser` (`Nama`, `Password`, `Restoran`, `KodeRestoPlg`, `Login`) VALUES
('alicia', '$2b$12$cZKmfx.v0UopWl8RBLcxdeOrzVcCkLdbv7GzJNO4k9K.FXBkiCNOC', 1, '', 0),
('andrey', '$2b$12$VH5TvkaJZwDWb3SSGG.MfOEkPXOFjCNUu3zPhBtXrHyVuqFiSWJUq', 1, 'R0003', 1),
('babathe', '$2b$12$IFunt.BuHsh32LTc0tzugewHSkOLwRMjKgRX4koEriRrVYRXpFAB6', 1, 'R0002', 0),
('plg', '$2b$12$IP1iIMqPNDN7PVCvQGg.ieXpakc3YnERN8oSf3w.n3oP2zUgum.QO', 0, '', 0),
('plg1', '$2b$12$IYAo7Q75JLujb6/HE.Dkf.u8KFAXoX6B2gGAYmtjkdM0lTR3nxueW', 0, 'P0001', 0),
('resto', '$2b$12$szcZtHH6RehY2XbyibE3luRc5F4DBkOk7pmq15LdZOj3VkdXDmbeW', 1, 'R0001', 0),
('test', '$2b$12$zT3Cm5u5r.3r9jag9xDelOx8GMVFNb7WRuyuyZdaAbqRYsc.naptm', 0, '', 0);

-- --------------------------------------------------------

--
-- Table structure for table `pesanan`
--

CREATE TABLE `pesanan` (
  `NoPesanan` varchar(13) NOT NULL,
  `Tgl` date NOT NULL,
  `Plg` varchar(50) NOT NULL,
  `KodeResto` varchar(5) NOT NULL,
  `Status` tinyint(1) NOT NULL,
  `NoUrutPesan` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pesanan`
--

INSERT INTO `pesanan` (`NoPesanan`, `Tgl`, `Plg`, `KodeResto`, `Status`, `NoUrutPesan`) VALUES
('PSN1101240001', '2024-01-11', 'plg', 'R0001', 0, 0),
('PSN1101241240', '2024-01-11', 'plg', 'R0001', 0, 0),
('PSN1701240001', '2024-01-17', 'plg', 'R0001', 1, 1),
('PSN1801240001', '2024-01-18', 'plg', 'R0001', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `pesanandet`
--

CREATE TABLE `pesanandet` (
  `NoPesanan` varchar(13) NOT NULL,
  `Kode` varchar(5) NOT NULL,
  `Jumlah` int(11) NOT NULL,
  `Harga` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pesanandet`
--

INSERT INTO `pesanandet` (`NoPesanan`, `Kode`, `Jumlah`, `Harga`) VALUES
('PSN1101240001', 'A01', 1, 7000),
('PSN1101241240', 'A02', 1, 5000),
('PSN1701240001', 'A02', 2, 5000),
('PSN1701240001', 'A02', 2, 5000),
('PSN1801240001', 'A03', 2, 1000),
('PSN1801240001', 'A01', 1, 3000);

-- --------------------------------------------------------

--
-- Table structure for table `tambahstok`
--

CREATE TABLE `tambahstok` (
  `NoTambah` varchar(10) NOT NULL,
  `Tgl` date NOT NULL,
  `Opr` varchar(30) NOT NULL,
  `KodeResto` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tambahstok`
--

INSERT INTO `tambahstok` (`NoTambah`, `Tgl`, `Opr`, `KodeResto`) VALUES
('0801240001', '2024-01-08', '', ''),
('1001240001', '2024-01-10', '', ''),
('1001240002', '2024-01-10', '', ''),
('1001240003', '2024-01-10', '', ''),
('1001240004', '2024-01-10', '', ''),
('1001240005', '2024-01-10', '', ''),
('1001240006', '2024-01-10', '', ''),
('1101240001', '2024-01-11', 'resto', 'R0001'),
('1101240002', '2024-01-11', 'resto', 'R0001'),
('1501240001', '2024-01-15', 'resto', 'R0001'),
('1501240002', '2024-01-15', 'resto', 'R0001'),
('1501240003', '2024-01-15', 'resto', 'R0001'),
('1501240004', '2024-01-15', 'resto', 'R0001'),
('1601240001', '2024-01-16', 'resto', 'R0001'),
('1701240001', '2024-01-17', 'resto', 'R0001'),
('1801240001', '2024-01-18', 'resto', 'R0001'),
('1801240002', '2024-01-18', 'resto', 'R0001'),
('1801240003', '2024-01-18', 'resto', 'R0001'),
('2101240001', '2024-01-21', 'resto', 'R0001'),
('2501240001', '2024-01-25', 'resto', 'R0001'),
('2501240002', '2024-01-25', 'resto', 'R0001');

-- --------------------------------------------------------

--
-- Table structure for table `tambahstokdet`
--

CREATE TABLE `tambahstokdet` (
  `NoTambah` varchar(10) NOT NULL,
  `KodeMenu` varchar(5) NOT NULL,
  `Jumlah` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tambahstokdet`
--

INSERT INTO `tambahstokdet` (`NoTambah`, `KodeMenu`, `Jumlah`) VALUES
('0801240001', 'A01', 3),
('1001240001', 'A01', 2),
('1001240002', 'A01', 2),
('1001240003', 'A01', 2),
('1001240004', 'A01', 2),
('1001240005', 'A01', 1),
('1001240006', 'A01', 1),
('1101240001', 'A01', 2),
('1101240002', 'A02', 2),
('1501240003', 'A01', 2),
('1501240004', 'A03', 3),
('1501240004', 'A02', 1),
('1601240001', 'A04', 2),
('1701240001', 'A01', 3),
('1701240001', 'A02', 2),
('1701240001', 'A03', 4),
('1701240001', 'A04', 1),
('1801240001', 'A04', 5),
('1801240001', 'A02', 3),
('1801240002', 'A01', 1),
('1801240003', 'A03', 2),
('2101240001', 'A06', 3),
('2501240001', 'A03', 4),
('2501240001', 'A01', 3),
('2501240002', 'A02', 5),
('2501240002', 'A04', 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `keranjangplg`
--
ALTER TABLE `keranjangplg`
  ADD PRIMARY KEY (`NoAuto`);

--
-- Indexes for table `mkategori`
--
ALTER TABLE `mkategori`
  ADD PRIMARY KEY (`Kode`);

--
-- Indexes for table `mmenu`
--
ALTER TABLE `mmenu`
  ADD UNIQUE KEY `KodeMenu` (`KodeMenu`,`KodeResto`);

--
-- Indexes for table `mpelanggan`
--
ALTER TABLE `mpelanggan`
  ADD PRIMARY KEY (`KodePlg`);

--
-- Indexes for table `mresto`
--
ALTER TABLE `mresto`
  ADD PRIMARY KEY (`KodeResto`);

--
-- Indexes for table `muser`
--
ALTER TABLE `muser`
  ADD PRIMARY KEY (`Nama`);

--
-- Indexes for table `pesanan`
--
ALTER TABLE `pesanan`
  ADD PRIMARY KEY (`NoPesanan`);

--
-- Indexes for table `tambahstok`
--
ALTER TABLE `tambahstok`
  ADD PRIMARY KEY (`NoTambah`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `keranjangplg`
--
ALTER TABLE `keranjangplg`
  MODIFY `NoAuto` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `mkategori`
--
ALTER TABLE `mkategori`
  MODIFY `Kode` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
