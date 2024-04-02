-- lists all Comedy shows in the database
select
    tv_shows.title as 'title'
from
    tv_shows
    inner join tv_show_genres on tv_show_genres.show_id = tv_shows.id
    inner join tv_genres on tv_genres.id = tv_show_genres.genre_id
where
    tv_genres.id = 5
order by
    tv_shows.title ASC
