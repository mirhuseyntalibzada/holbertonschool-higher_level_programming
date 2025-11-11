-- LIST ALL SHOWS WITH THEIR GENRE IDS (INCLUDING SHOWS WITHOUT GENRES)
-- Outputs: tv_shows.title - tv_show_genres.genre_id (NULL if no genre)
-- Sorted by title ASC, then genre_id ASC (single SELECT)
SELECT
  tv_shows.title AS title,
  tv_show_genres.genre_id AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
  ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
