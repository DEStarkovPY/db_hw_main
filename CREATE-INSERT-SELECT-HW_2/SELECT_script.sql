--Домашнее задание №2
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




-- Домашнее задание №3
--Пункт №1
SELECT genre_id, COUNT(singer_id) FROM genresinger
GROUP BY genre_id
ORDER BY COUNT(singer_id);

--Пункт №2
SELECT year_of_release, COUNT(*) FROM track t
LEFT JOIN album a ON t.album_id = a.id
GROUP BY year_of_release
HAVING year_of_release BETWEEN 2019 AND 2020;

--Пункт №3
SELECT a.title, AVG(duration) FROM track t
LEFT JOIN album a ON t.album_id = a.id 
GROUP BY  a.title;

SELECT * FROM singeralbum s;
--Пункт №4
SELECT s.name, a.year_of_release  FROM singer s
LEFT JOIN singeralbum s2 ON s.id = s2.singer_id
LEFT JOIN album a ON a.id = s2.album_id
WHERE a.year_of_release != 2020;


--Пункт №5
SELECT c.title, s2.name  FROM collection c
LEFT JOIN trackcollection t ON c.id = t.collection_id
LEFT JOIN track t2 ON t.track_id = t2.id
LEFT JOIN album a ON t2.album_id = a.id
LEFT JOIN singeralbum s ON a.id = s.album_id
LEFT JOIN singer s2 ON s.singer_id = s2.id
WHERE name LIKE '%Den'
GROUP BY c.title, s2.name;

--Пункт №6
SELECT a.title, COUNT(DISTINCT g2.title) FROM album a
LEFT JOIN singeralbum s ON a.id = s.album_id
LEFT JOIN singer s2 ON s2.id = s.singer_id
LEFT JOIN genresinger g ON s2.id = g.singer_id
LEFT JOIN genre g2 ON g2.id = g.genre_id
GROUP BY a.title
HAVING COUNT(DISTINCT g2.title) >1;

--Пункт №7
SELECT title, track_id, collection_id FROM track t
LEFT JOIN trackcollection t2 ON t.id = t2.track_id
GROUP BY title, track_id, collection_id
HAVING track_id IS NULL
ORDER BY  track_id DESC;

--Пункт №8
SELECT s.name, t.duration FROM singer s
JOIN singeralbum s2 ON s.id = s2.singer_id
JOIN album a ON s2.album_id = a.id
JOIN track t ON a.id = t.album_id
WHERE t.duration = (
SELECT MIN(t.duration) FROM track t
);

--Пункт №9
SELECT a.title, COUNT(t.title) from album a
JOIN track t ON a.id = t.album_id
GROUP BY a.title
HAVING COUNT(t.title) = (
	SELECT MIN(count) FROM (
		SELECT a.title, COUNT(t.title) from album a
		JOIN track t ON a.id = t.album_id
		GROUP BY a.title) AS foo);









