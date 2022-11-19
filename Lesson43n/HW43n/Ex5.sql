USE VegiesAndFruits;

-- query 1
SELECT * FROM VegiesAndFruits.TableVF;

-- query 2
SELECT * FROM VegiesAndFruits.TableVF WHERE `Type` = 'V';

-- query 3
SELECT * FROM VegiesAndFruits.TableVF WHERE `Type` = 'F';

-- query 4
SELECT `Name` FROM VegiesAndFruits.TableVF;

-- query 5
SELECT DISTINCT `Color` FROM VegiesAndFruits.TableVF;
-- query 6
SELECT * FROM VegiesAndFruits.TableVF WHERE `Type` = 'F' AND `Color` = 'Orange';

-- query 7
SELECT * FROM VegiesAndFruits.TableVF WHERE `Type` = 'V' AND `Color` = 'Red';