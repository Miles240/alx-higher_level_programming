-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
select
    tv_genres.name as 'name'
from
    tv_genres
    join tv_show_genres on tv_show_genres.genre_id = tv_genres.id
    join tv_shows on tv_shows.id = tv_show_genres.show_id
where
    tv_shows.id = 8
order by
    tv_genres.name desc;