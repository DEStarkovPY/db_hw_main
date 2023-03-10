--Пункт №1
SELECT title, year_of_release FROM Album
WHERE year_of_release = 2018;

--Пункт №2
SELECT title, duration FROM Track
ORDER BY duration DESC
LIMIT 1;

--Пункт №3
SELECT title FROM Track 
WHERE duration >= 3.5;

--Пункт №4
SELECT title FROM Collection
WHERE year_of_release BETWEEN 2018 AND 2020;

--Пункт №5
SELECT name FROM Singer
WHERE name NOT LIKE '% %';

--Пункт №6
SELECT title FROM Track
WHERE title LIKE '%My%' OR title LIKE '%my%' OR title LIKE '%Мой%' OR title LIKE '%мой%';

