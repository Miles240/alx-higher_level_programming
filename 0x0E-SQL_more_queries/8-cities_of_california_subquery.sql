-- ists all the cities of California that can be found in the database hbtn_0d_usa
SELECT
    cities.id,
    cities.name
FROM
    cities,
    states
WHERE
    cities.state_id = 1
    AND states.name = 'California' ORDER BY cities.id ASC;