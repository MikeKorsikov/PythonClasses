-- create database
CREATE SCHEMA `Academy`;

-- create tables
USE Academy;
CREATE TABLE `Academy`.`Teachers`
(
    `Id`             INT          NOT NULL AUTO_INCREMENT,
    `EmploymentDate` DATE         NOT NULL CHECK ( `EmploymentDate` > '1990-01-01' ),
    `IsAssistant`    BIT          NOT NULL                          DEFAULT 0,
    `IsProfessor`    BIT          NOT NULL                          DEFAULT 0,
    `Name`           VARCHAR(100) NOT NULL,
    `Position`       VARCHAR(100) NOT NULL,
    `Premium`        INT          NOT NULL CHECK ( `Premium` >= 0 ) DEFAULT 0,
    `Salary`         INT          NOT NULL CHECK ( `Salary` > 0),
    `Surname`        VARCHAR(100) NOT NULL,
    PRIMARY KEY (`Id`),
    UNIQUE INDEX `id_UNIQUE` (`Id` ASC) VISIBLE
);

CREATE TABLE `Academy`.`Departments`
(
    `Id`        INT          NOT NULL AUTO_INCREMENT,
    `Financing` INT          NOT NULL DEFAULT 0,
    `Name`      VARCHAR(100) NOT NULL UNIQUE,
    PRIMARY KEY (`Id`),
    UNIQUE INDEX `id_UNIQUE` (`Id` ASC) VISIBLE
);

CREATE TABLE `Academy`.`Faculties`
(
    `Id`   INT          NOT NULL AUTO_INCREMENT,
    `Dean` VARCHAR(100) NOT NULL,
    `Name` VARCHAR(100) NOT NULL UNIQUE,
    PRIMARY KEY (`Id`),
    UNIQUE INDEX `id_UNIQUE` (`Id` ASC) VISIBLE
);

CREATE TABLE `Academy`.`Groups`
(
    `Id`     INT         NOT NULL AUTO_INCREMENT,
    `Name`   VARCHAR(10) NOT NULL UNIQUE,
    `Rating` INT         NOT NULL CHECK ( `Rating` >= 0 AND `Rating` <= 5),
    `Year`   INT         NOT NULL CHECK ( `Year` >= 1 AND `Year` <= 5),
    PRIMARY KEY (`Id`),
    UNIQUE INDEX `id_UNIQUE` (`Id` ASC) VISIBLE
);

-- add content
INSERT INTO `Academy`.`Teachers` (`Id`, `EmploymentDate`, `IsAssistant`, `IsProfessor`, `Name`, `Position`, `Premium`,
                                  `Salary`, `Surname`)
VALUES ('1', 19910201, 0, 1, 'Max', 'Lecturer', 0, 12000, 'Pane');
INSERT INTO `Academy`.`Teachers` (`EmploymentDate`, `IsAssistant`, `IsProfessor`, `Name`, `Position`, `Premium`,
                                  `Salary`, `Surname`)
VALUES (19950123, 1, 0, 'Bruce', 'Backup lecturer', 1000, 15000, 'Wane');
INSERT INTO `Academy`.`Teachers` (`EmploymentDate`, `IsAssistant`, `IsProfessor`, `Name`, `Position`, `Premium`,
                                  `Salary`, `Surname`)
VALUES (20000102, 0, 1, 'Tom', 'Lecturer', 5000, 20000, 'Hardy');
INSERT INTO `Academy`.`Teachers` (`EmploymentDate`, `IsAssistant`, `IsProfessor`, `Name`, `Position`, `Premium`,
                                  `Salary`, `Surname`)
VALUES (19900102, 1, 0, 'Jessica', 'Lecturer', 8000, 7000, 'Hitchcock');
INSERT INTO `Academy`.`Teachers` (`EmploymentDate`, `IsAssistant`, `IsProfessor`, `Name`, `Position`, `Premium`,
                                  `Salary`, `Surname`)
VALUES (20210101, 1, 0, 'Mike', '3rd grade Lecturer', 100, 500, 'Lucky');
