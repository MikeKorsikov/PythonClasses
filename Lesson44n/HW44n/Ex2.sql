USE Academy;

-- query 1
SELECT `Name`
FROM `Departments`
ORDER BY `Name` DESC;

-- query 2
SELECT `Name`, `Rating`
FROM `Groups`;

-- query 3
SELECT `Surname`, (`Salary` / (`Salary` + `Premium`)) AS 'salary as % of total income'
FROM Teachers;

-- query 4
SELECT CONCAT('The dean of faculty ', `Name`, ' is ', `Dean`, '.') AS "Result"
FROM `Faculties`;

-- query 5
SELECT `Surname`
FROM `Teachers`
WHERE `IsProfessor` = 1
  AND `Salary` > 1050;

-- query 6
SELECT `Name`
FROM `Departments`
WHERE `Financing` < 11000
   OR `Financing` > 25000;

-- query 7
SELECT `Name`
FROM `Faculties`
WHERE `Name` != 'Computer Science';

-- query 8
SELECT `Surname`, `Position`
FROM Teachers
WHERE IsProfessor = 0;

-- query 9
SELECT `Surname`, `Position`, `Salary`, `Premium`
FROM Teachers
WHERE `IsAssistant` = 1
  AND `Premium` >= 160
  AND `Premium` <= 550;

-- query 10
SELECT `Surname`, `Salary`
FROM `Teachers`
WHERE `IsAssistant` = 1;

-- query 11
SELECT `Surname`, `Position`
FROM `Teachers`
WHERE `EmploymentDate` >= 20000101;

-- query 12
SELECT `Name` AS 'Name of Department'
FROM Departments
WHERE LEFT(`Name`, 4) <= 'Soft'
ORDER BY `Name`;

-- query 13
SELECT `Surname`
FROM Teachers
WHERE IsAssistant = 1
  AND (`Salary` + `Premium`) <= 1200;

-- query 14
SELECT `Name`
FROM `Groups`
WHERE `Year` = 5
  AND (`Rating` >= 2 AND `Rating` <= 4);

-- query 15
SELECT `Surname`
FROM `Teachers`
WHERE `IsAssistant` = 1
  AND `Salary` < 550
  AND `Premium` < 200;