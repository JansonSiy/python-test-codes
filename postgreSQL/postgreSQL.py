# To choose a database, just open PostgreSQL and double-click. 
# If it fails, it will give a line of code that you can copy and paste in the terminal.

# TO VIEW LIST OF ALL DATABASES
\l

# QUIT
\q

# CREATE DATABASE
CREATE DATABASE name_of_database;

# CONNECT TO DATABASES
psql -h localhost -p 5432 -U jansonharoldsiy test
# note: host(-h) if you are not connected to any server use localhost, port(-p) by default is 5432, username(-U) has a default, 
    # type (psql --help) in terminal to see default username, then database name
\c name_of_database

# DELETING A DATABASE (permanent)
DROP DATABASE name_of_database;

# CREATE TABLE
# reference link: https://www.postgresql.org/docs/11/datatype.html
CREATE TABLE person (
    id int,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender VARCHAR(6),
    date_of_birth DATE);

# TO VIEW LIST OF TABLES
\d (d is for describe)

# TO VIEW CONTENT OF TABLE
\d person (list of relations)
\dt (just the table)

# CREATING TABLE WITH CONSTRAINTS
CREATE TABLE person (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender VARCHAR(6) NOT NULL,
    date_of_birth DATE NOT NULL);
# note: BIGSERIAL - auto increment
# PRIMARY KEY - telling postgreSQL that this is your primary key
# NOT NULL - should not be null

# DELETING A TABLE
DROP TABLE person

# INSERT RECORD INTO TABLES
INSERT INTO person (first_name, last_name, gender, date_of_birth, email)
VALUES ('Jan', 'Siy', 'MALE', DATE '1994-10-05', 'janson@email.com');

# TO VIEW COLUMNS AND ROWS OF A TABLE
SELECT # FROM person;
# all
SELECT first_name FROM person;
# one column
SELECT first_name, last_name FROM person;
# two or more column

# SHORTCUT TO CREATING THOUSAND ROWS
# reference link: https://www.mockaroo.com/
\i /Users/jansonharoldsiy/Downloads/person.sql
# note: \i go_to_file_path

# ORDER BY
SELECT # FROM person ORDER BY country_of_birth;
SELECT # FROM person ORDER BY country_of_birth ASC;
SELECT # FROM person ORDER BY country_of_birth DESC;

# DISTINCT (eliminates duplicate)
SELECT DISTINCT country_of_birth FROM person ORDER BY country_of_birth DESC;

# WHERE (filtering with conditions)
FROM person WHERE gender = 'Male';
SELECT # FROM person WHERE gender = 'Male' AND country_of_birth = 'Philippines';
SELECT # FROM person WHERE gender = 'Male' AND (country_of_birth = 'Philippines' OR country_of_birth = 'China');

# COMPARISON OPERATORS
SELECT 1 = 1; (returns boolean, t or f)
<
>
<=
>=
<> (not equal)

# LIMIT & FETCH & OFFSET
SELECT # FROM person LIMIT 5;
# limits return value
SELECT # FROM person OFFSET 5 LIMIT 5;
# offset = skip
SELECT # FROM person OFFSET 5 FETCH FIRST 5 ROW ONLY;
# fetch is the same as limit but a SQL standard
SELECT # FROM person OFFSET 5 FETCH FIRST ROW ONLY;

# IN
# selects all rows that has the following value after IN
SELECT # FROM person WHERE country_of_birth IN ('China', 'Philippines', 'France');

# BETWEEN
SELECT # FROM person WHERE date_of_birth BETWEEN DATE '2021-01-01' AND '2021-01-31';

# LIKE & ILIKE (case sensitive)
SELECT # FROM person WHERE email LIKE  '%google.com';
SELECT # FROM person WHERE email LIKE '%@google%';
# should contain the data from % to %
SELECT # FROM person WHERE country_of_birth LIKE 'p%';
# error because not in uppercase
SELECT # FROM person WHERE country_of_birth ILIKE 'p%';
# ignores case sensitive

# GROUP BY (groups and counts(count(# ))
SELECT country_of_birth, COUNT(# ) FROM person GROUP BY country_of_birth;

# GROUP BY HAVING
SELECT country_of_birth, COUNT(# ) FROM person GROUP BY country_of_birth HAVING COUNT(# ) < 5;

# MAX
SELECT MAX(price) FROM car;

# MIN
SELECT MIN(price) FROM car;
# example:
SELECT make, model, MIN(price) FROM car GROUP BY make, model;

# AVERAGE
SELECT AVG(price) FROM car;

# ROUND OFF
SELECT ROUND(AVG(price)) FROM car;

# SUM
SELECT SUM(price) FROM car;
# example:
SELECT make, SUM(price) FROM car GROUP BY make;

# BASICS OF ARITHMETIC OPERATORS
+
-
# 
/
^
SELECT5! (factorial)
SELECT 10 % 3 (modulos)

# ARITHMETIC OPERATORS WITH YOUR DATA WITH ALIAS
# note: display car
# adds a column that displays 10% of the price
# adds another column that displays the discounted price
# renames the columns using AS (ALIAS)
SELECT id, make, model, price AS original_price, ROUND(price #  .10, 2) AS ten_percent_value, ROUND(price - (price #  .10)) AS discount_after_ten_percent_value FROM car;

# COALESCE
# note: since other rows doesn't have email value, you can use COALESE. first parameter is the column and second is the replacement
SELECT COALESCE(email, 'email not provided') FROM person;

# NULLIF
# note: takes two arguments, if the first argument is equals to the second argument, it returns nullif
# if the first argument is not equals to the second argument it returns the first argument

# TIMESTAMPS & DATE
SELECT NOW();
SELECT NOW()::DATE;
SELECT NOW()::TIME;
SELECT NOW() - INTERVAL '1 YEAR';  
SELECT NOW() - INTERVAL '1 MONTH';
SELECT NOW() - INTERVAL '1 DAY';
SELECT NOW() + INTERVAL '1 YEAR';  
SELECT NOW() + INTERVAL '1 MONTH';
SELECT NOW() + INTERVAL '1 DAY';

# EXTRACTING FIELDS
SELECT EXTRACT(YEAR from NOW());
SELECT EXTRACT(MONTH from NOW());
SELECT EXTRACT(DAY from NOW());
SELECT EXTRACT(DOW from NOW());
SELECT EXTRACT(CENTURY from NOW());

# AGE FUNCTION
SELECT first_name, last_name, gender, country_of_birth, AGE(NOW(), date_of_birth) AS age FROM person;

# UNIQUE CONSTRAINT
# note: making email unique
# add constraint
ALTER TABLE person ADD CONSTRAINT unique_email_address UNIQUE (email);
# or
ALTER TABLE person ADD UNIQUE (email);

#removing constraint
ALTER TABLE person DROP CONSTRAINT unique_email_address;

# CHECK CONSTRAINT
ALTER TABLE person ADD CONSTRAINT gender_constraint CHECK (gender = 'Male' OR gender = 'Female');

# DELETING DATA
DELETE FROM person WHERE id = '1';
DELETE FROM person WHERE gender = 'Female' AND country_of_birth = 'Philippines';

# UPDATING DATA
UPDATE person SET first_name = 'test1', last_name='test2', email = 'test@email.com' WHERE id = 2;

# ON CONFLICT (how to handle conflicts)
ON CONFLICT (id) DO NOTHING; (if the id is the conflict)
ON CONFLICT (id) DO UPDATE SET email = EXCLUDED.email, first_name = EXCLUDED.first_name;
# allows to override existing data

# RELATIONSHIP BETWEEN TABLES (check person-car.sql)
UPDATE person SET car_id = 1 WHERE id = 1;
UPDATE person SET car_id = 2 WHERE id = 2;
SELECT # FROM person;
# for checking

# INNER JOINS (joining two tables)
SELECT # FROM person JOIN car ON person.car_id = car.id;
# another sample:
SELECT person.first_name, car.make, car.model, car.price FROM person JOIN car ON person.car_id = car.id;

# LEFT JOIN (joining two tables including those who doesn't have any relationship)
SELECT # FROM person LEFT JOIN car ON car.id = person.car_id;

# GENERATING CSV
\copy (SELECT # FROM person LEFT JOIN car on car.id = person.car_id) TO '/Users/jansonharoldsiy/Downloads/results.csv' DELIMITER ',' CSV HEADER;

# SEQUENCES
SELECT # FROM person_id_seq;
 last_value | log_cnt | is_called 
------------+---------+-----------
          3 |      30 | t
(1 row)
# note: last_value is the last id, log_cnt is how many times this was called, is called is a boolean if it's been called or not
# restart ALTER SEQUENCE person_id_seq RESTART WITH 0;

# EXTENTIONS (check extensions available)
SELECT # FROM pg_available_extensions;