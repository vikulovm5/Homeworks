USE yndxmsc;

/*SELECT'ы*/

-- топ композиции
SELECT * FROM media 
WHERE media_type_id = 1 or 3 or 4
ORDER BY listens DESC;

-- стрим/радио
SELECT * FROM media 
WHERE auth_id = (
	SELECT target_id FROM follows WHERE initiator_id = 1);

-- обладатели грэмми
SELECT * FROM authors a
JOIN prizes p
ON a.id = p.owner_id 
WHERE p.name = 'grammy'
ORDER BY a.id;

-- исполнители на лейблах
SELECT l.name, l.actor_id FROM label l
RIGHT JOIN authors a
ON l.actor_id = a.id 
GROUP BY l.name;






