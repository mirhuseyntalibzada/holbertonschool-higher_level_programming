-- LIST RECORDS WITH NON-EMPTY NAME, SORTED BY SCORE DESC
-- Displays score then name; excludes NULL and empty/whitespace-only names
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
  AND TRIM(name) != ''
ORDER BY score DESC;
