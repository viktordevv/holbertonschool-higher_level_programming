-- lists all Comedy shows in the database hbtn_0d_tvshows.


SELECT title FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_genres.name = "Comedy"
GROUP BY title
ORDER BY title ASC;
