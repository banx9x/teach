-- MySQL không hỗ trợ FULL JOIN
-- Cách mô phỏng phương pháp FULL JOIN
SELECT * FROM t1
LEFT JOIN t2 ON t1.column = t2.column
UNION
SELECT * FROM t1
RIGHT JOIN t2 ON t1.column = t2.column
