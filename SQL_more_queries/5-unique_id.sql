-- CREATE TABLE unique_id WITH UNIQUE id DEFAULT 1
-- Creates table unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256)); does not fail if it exists
CREATE TABLE IF NOT EXISTS unique_id (
  id INT DEFAULT 1 UNIQUE,
  name VARCHAR(256)
);
