-- Use the database hbtn_0d_usa
USE hbtn_0d_usa;

-- Select cities with their corresponding state names using a subquery
SELECT 
    cities.id,
    cities.name AS city_name,
    (SELECT states.name FROM states WHERE states.id = cities.state_id) AS state_name
FROM cities
ORDER BY cities.id ASC;
