-- CREATE second_table AND INSERT MULTIPLE ROWS
-- Creates table second_table (id INT, name VARCHAR(256), score INT) if it doesn't exist, then inserts 4 rows
CREATE TABLE IF NOT EXISTS second_table (
  id INT,
  name VARCHAR(256),
  score INT
);

-- INSERT INITIAL DATA
-- Adds the required records
INSERT INTO second_table (id, name, score) VALUES
  (1, 'John', 10),
  (2, 'Alex', 3),
  (3, 'Bob', 14),
  (4, 'George', 8);
