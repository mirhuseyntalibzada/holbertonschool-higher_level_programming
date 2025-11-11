-- LIST ALL GENRES FOR THE SHOW 'Dexter'
-- Outputs tv_genres.name for the single show titled 'Dexter', sorted alphabetically
SELECT
  tv_genres.name AS name
FROM tv_genres
INNER JOIN tv_show_genres
  ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
  ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
