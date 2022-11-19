USE `p21`;
SELECT * FROM `student`;

-- INSERT INTO `p21`.`student`
--    (`id`, `name`, `sname`, `age`, `birthday`, `active`)
-- VALUES ('4', 'Mykola', 'Korsikov', '39', '1983-04-14', 1);

SELECT * FROM `student` WHERE age > 20;

SELECT  * FROM  `student` ORDER BY age;

SELECT * FROM `student` WHERE name NOT IN ('Mykola');

INSERT INTO `p21`.`student`
   (`id`,
    `name`,
    `sname`,
    `age`,
    `birthday`,
    `active`)
VALUES (
        7,
        'Valeriia',
        'Kiparenko',
        '37',
        '1994-02-08',
        1);

UPDATE `student` SET `name` = 'Lera' WHERE `id` = 7;

DELETE FROM `student` WHERE id = 3;


CREATE DATABASE `p22`;