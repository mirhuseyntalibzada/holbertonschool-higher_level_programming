-- LIST ALL CITIES OF CALIFORNIA (WITHOUT USING JOIN)
-- Outputs city id and name for rows whose state_id matches the id of 'California'
SELECT id, name
FROM cities
WHERE state_id = (
  SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;
