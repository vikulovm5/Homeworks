USE yndxmsc;

/*представления*/

-- 
DROP VIEW IF EXISTS label_owners;
CREATE VIEW label_owners AS
SELECT name, owner_id
FROM label;

#SELECT * FROM label_owners;

--
DROP VIEW IF EXISTS uganda_music;
CREATE VIEW uganda_music AS
SELECT name, user_id
FROM authors a
WHERE a.country = 'Uganda';

#SELECT * FROM uganda_music;
