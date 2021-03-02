-- list num of records with the same score in the table second_table
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score DESC
