-- Task: List all tables in a specific database

-- Set the database name (replace `dbname` with your actual database name)
SET @dbname = 'dbname';

-- Query to list tables
SELECT table_name
FROM information_schema.tables
WHERE table_schema = DATABASE();
