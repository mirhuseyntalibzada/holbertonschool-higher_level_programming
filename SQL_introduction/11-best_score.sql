-- LIST RECORDS WITH SCORE >= 10 ORDERED BY SCORE DESC
-- Displays score then name for rows where score >= 10
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
