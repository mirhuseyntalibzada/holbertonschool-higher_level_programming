-- LIST SHOWS WITH AT LEAST ONE GENRE
-- Outputs: tv_shows.title - tv_show_genres.genre_id
-- Sorted by title ASC, then genre_id ASC (single SELECT)
SELECT
  tv_shows.title AS title,
  tv_show_genres.genre_id AS genre_id
FROM tv_shows
INNER JOIN tv_show_genres
  ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
