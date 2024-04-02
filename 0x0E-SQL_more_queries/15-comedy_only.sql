-- lists all Comedy shows in the database
SELECT
    tv_shows.title AS 'title'
FROM
    tv_shows
    INNER JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
    INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE
    tv_genres.id = 5
ORDER BY
    tv_shows.title ASC