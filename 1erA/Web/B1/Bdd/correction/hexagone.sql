-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : ven. 21 mars 2025 à 15:31
-- Version du serveur : 10.4.32-MariaDB
-- Version de PHP : 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `hexagone`
--

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE `users` (
  `id_user` int(11) NOT NULL,
  `firstname` varchar(255) NOT NULL,
  `lastname` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`id_user`, `firstname`, `lastname`, `email`, `password`, `created_at`, `updated_at`) VALUES
(9, 'Noah', 'Sillaire', 'noahsillaire@gmail.com', '0', '2025-03-21 09:27:56', '0000-00-00 00:00:00'),
(10, 'no', 'zdqz', 'qedeq', '0', '2025-03-21 09:32:01', '0000-00-00 00:00:00'),
(11, 'dzqdz', 'def', 'fsvcxvfb', '0', '2025-03-21 09:59:34', '0000-00-00 00:00:00'),
(12, 'vivien', 'antoine', 'jdheuge@gmail.com', '0', '2025-03-21 13:34:13', '0000-00-00 00:00:00'),
(13, 'vivien', 'antoine', 'antoine@gmail.com', '$2y$10$mToLRHH.n3csFjxu77L5CeFoUeb4uz5PH6ijiksfC7MwUE8rgjFua', '2025-03-21 13:37:41', '2025-03-21 13:37:41'),
(14, 'vivien', 'antoine', 'aaa@gmail.com', '$2y$10$YNofhdS866/sB5CXQDOfq.hYVzaNQvDKZ8rDGgweT.dRJRDCoas3y', '2025-03-21 14:03:11', '2025-03-21 14:03:11');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id_user`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `users`
--
ALTER TABLE `users`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
