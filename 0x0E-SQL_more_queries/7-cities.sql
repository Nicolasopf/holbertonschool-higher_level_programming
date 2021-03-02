-- creates the database hbtn_0d_usa and the table cities
-- state_id INT, t be null and must be a FOREIGN KEY
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id INT NOT NULL PRIMARY KAY AUTO_INCREMENT, state_id INT NOT NULL, name varchar(256) NOT NULL, FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id))
