-- COUNT SHOWS PER GENRE (ONLY GENRES WITH AT LEAST ONE SHOW)
-- Outputs: genre - number_of_shows, sorted by number_of_shows DESC (single SELECT)
SELECT
  tv_genres.name AS genre,
  COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres
  ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
