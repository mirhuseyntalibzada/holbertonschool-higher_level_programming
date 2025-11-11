-- CREATE TABLE force_name WITH NON-NULL name
-- Creates table force_name (id INT, name VARCHAR(256) NOT NULL); does not fail if it exists
CREATE TABLE IF NOT EXISTS force_name (
  id INT,
  name VARCHAR(256) NOT NULL
);
