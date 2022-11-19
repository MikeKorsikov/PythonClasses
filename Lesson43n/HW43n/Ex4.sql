-- creating database
CREATE SCHEMA VegiesAndFruits;

-- creating table
CREATE TABLE `VegiesAndFruits`.`TableVF` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NOT NULL,
  `Color` VARCHAR(45) NOT NULL,
  `Calories` INT NOT NULL,
  `Description` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE);

-- adding column with two options
ALTER TABLE `VegiesAndFruits`.`TableVF`
ADD COLUMN `Type` ENUM('V', 'F') NULL DEFAULT 'V' AFTER `Name`;

-- add content to table
INSERT INTO `vegiesandfruits`.`TableVF` (`Name`, `Type`, `Color`, `Calories`, `Description`)
VALUES ('Tomatos', 'V', 'Black', '50', 'Very expensive');
INSERT INTO `vegiesandfruits`.`TableVF` (`Name`, `Type`, `Color`, `Calories`, `Description`)
VALUES ('Orange', 'F', 'Orange', '200', 'From Spain');

-- showing content of table
SELECT * FROM VegiesAndFruits.TableVF;