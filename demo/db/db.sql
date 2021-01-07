
SELECT * 
FROM employees AS e
WHERE 


-- Lấy ra tất cả records trong bảng customers
? ? FROM customers;

-- Lấy ra cột city trong bảng customers
SELECT ?
? customers;

-- Lấy ra tất cả giá trị trong cột country (không trùng lặp)
-- từ bảng customers
SELECT ? ?
FROM customers;

-- Lấy ra tất cả customers có city = 'Hanoi'
SELECT *
FROM customers
? ?;

-- Lấy ra tất cả customers có city không = 'Hanoi'
SELECT *
FROM customers
? ?;

-- Lấy ra tất cả customers có city = 'Hanoi' và points > 2000
SELECT *
FROM customers
? ?;


-- Lấy ra tất cả customers có độ tuổi (age) trong khoảng 20 - 30
SELECT *
FROM customers 
? ?;


-- Lấy ra tất cả customers sắp xếp theo độ tuổi (age) tăng dần
SELECT *
FROM customers
? ?;


-- Lấy ra tất cả customers, sắp xếp theo city theo bảng alphabe
--  và age giảm dần
SELECT *
FROM customers
? ?;

-- Lấy  ra tất cả customes không có phone
SELECT *
FROM customers
? ?;


-- Lấy ra tất cả customers có tên bắt đầu bằng 'B'
-- và kết thúc bằng 'a' hoặc 'n'
SELECT *
FROM customers
? ?;

-- Lấy ra 3 customers có points cao nhất
SELECT *
FROM customers 
? ?;


-- Lấy ra tất cả customers, sắp xếp ngẫu nhiên
SELECT *
FROM customrers
? ?;

-- Lấy ra fullname (first_name, last_name) tất cả customers
SELECT ?
FROM customers;


-- Giả sử có bảng customers (id, name, phone, address)
-- Viết câu lệnh lấy ra tất cả customers
-- Nếu không có phone hoặc address thì in ra ""


-- Ví dụ có bảng parameters
-- A    B
-- 0    4
-- 5    1
-- ... ...
-- A, B là đối số phương trình bậc 1 ax + b = 0
-- Viết câu lệnh in ra nghiệm phương trình
-- với giá trị đối số tương ứng

SELECT
    A,
    B,
    CASE 
        WHEN a = 0 AND b = 0 THEN "Vô số nghiệm"
        WHEN a = 0 AND b <> 0 THEN "Vô nghiệm"
        ELSE - b / a
    END AS "Nghiệm"
FROM parameters;










