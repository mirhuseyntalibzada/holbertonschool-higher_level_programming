-- COUNT RECORDS PER SCORE, SORTED BY COUNT DESC
-- Displays: score and number (count of rows with that score)
SELECT
  score,
  COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
