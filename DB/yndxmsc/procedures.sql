DELIMITER //

DROP PROCEDURE IF EXISTS followers//

CREATE PROCEDURE followers
begin
	SELECT COUNT (*) FROM follows
	WHERE target_id = 1;
END//

DROP PROCEDURE IF EXISTS popular_genres//	
	
CREATE PROCEDURE popular_genres
begin
	SELECT genre, listens FROM media m
	GROUP BY m.genre
	ORDER BY m.listens DESC;
END//
	
DELIMITER ;