--Write a script that creates a table second_table

--second_table description:
--id INT
--name VARCHAR(256)
--score INT
--The database name will be passed as an argument to the mysql command
--If the table second_table already exists, your script should not fail
--id = 1, , score = 10
--id = 2, , score = 3
--id = 3, , score = 14
-- id = 4, , score = 8Georgename = Bobname = Alexname = Johnname = 
CREATE TABLE IF NOT EXISTS second_table(id INT, name VARCHAR(256), score INT);
INSERT INTO second_table(id, name, score) VALUES (1, 'John', 10);
INSERT INTO second_table(id, name, score) VALUES (2, 'Alex', 3);
INSERT INTO second_table(id, name, score) VALUES (3, 'Bob', 14);
INSERT INTO second_table(id, name, score) VALUES (4, 'George', 8);
