DELIMITER //

DROP TRIGGER IF EXISTS de_listen //
CREATE TRIGGER de_listen BEFORE INSERT ON media
	BEGIN
		SET listens = 0 
	END//


DROP TRIGGER IF EXISTS rating //
CREATE TRIGGER rating AFTER UPDATE ON media
	BEGIN
		listens / (SELECT COUNT(*) FROM users)
	END//
	
DELIMITER ;