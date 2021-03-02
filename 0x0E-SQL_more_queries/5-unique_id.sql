-- creates the table unique_id
-- unique_id description: id INT default 1 must be unique name VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id (id INTEGER UNIQUE DEFAULT 1, name VARCHAR(256))
