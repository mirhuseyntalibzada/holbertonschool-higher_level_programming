-- LIST ALL CITIES WITH THEIR STATES
-- Outputs: cities.id - cities.name - states.name, ordered by cities.id ASC (single SELECT)
SELECT
  cities.id,
  cities.name,
  states.name
FROM cities
INNER JOIN states
  ON cities.state_id = states.id
ORDER BY cities.id ASC;
