-- CREATE TABLE id_not_null WITH DEFAULT id = 1
-- Creates table id_not_null (id INT DEFAULT 1, name VARCHAR(256)); does not fail if it exists
CREATE TABLE IF NOT EXISTS id_not_null (
  id INT DEFAULT 1,
  name VARCHAR(256)
);
