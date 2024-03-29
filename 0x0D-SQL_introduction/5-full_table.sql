-- Prints the full description of a table
SELECT
    column_name,
    data_type,
    character_maximum_length,
    is_nullable,
    column_default
FROM
    information_schema.columns
WHERE
    table_schema = 'hbtn_0c_0'
    AND table_name = 'first_table';