-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
select
    tv_genres.`name` as `genre`,
    count(*) as `number_of_shows`
from
    tv_genres
    left join tv_show_genres on tv_genres.id = tv_show_genres.genre_id
group by
    tv_genres.`name`
order by
    `number_of_shows` desc;