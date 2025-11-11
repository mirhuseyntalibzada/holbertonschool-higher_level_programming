-- CREATE DATABASE hbtn_0d_2 AND READ-ONLY USER user_0d_2
-- Ensures DB exists, creates the user with password, and grants SELECT on that DB only

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
