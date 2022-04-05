CREATE TABLE `emp` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(16) DEFAULT NULL,
  `address` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `emp`
  ADD PRIMARY KEY (`id`);
  
ALTER TABLE `emp`
 MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;