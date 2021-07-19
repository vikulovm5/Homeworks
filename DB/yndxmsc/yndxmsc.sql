DROP DATABASE IF EXISTS yndxmsc;
CREATE DATABASE yndxmsc;
USE yndxmsc;

-- пользователи
DROP TABLE IF EXISTS users;
CREATE TABLE users(
	id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	firstname VARCHAR(50),
	lastname VARCHAR(50),
	email VARCHAR(100) UNIQUE,
	password_hash VARCHAR(256),
	phone BIGINT UNSIGNED UNIQUE,
	
	INDEX idx_users_username(firstname, lastname)
);

-- жанры
DROP TABLE IF EXISTS genres;
CREATE TABLE genres(
	id SERIAL,
	name VARCHAR(255)
	
);
-- авторы

DROP TABLE IF EXISTS authors;
CREATE TABLE authors(
	id BIGINT UNSIGNED NOT NULL UNIQUE,
	user_id BIGINT UNSIGNED NOT NULL,
	name VARCHAR(50),
	country VARCHAR(50),
	
	FOREIGN KEY (user_id) REFERENCES users(id)
);	
	

-- медиа
DROP TABLE IF EXISTS media_types;
CREATE TABLE media_types(
	id SERIAL,
	name VARCHAR(255) #('song', 'podcast', 'remix', 'live', 'lection', 'book')
    
);

DROP TABLE IF EXISTS media;
CREATE TABLE media(
	id BIGINT UNSIGNED NOT NULL PRIMARY KEY,
	auth_id BIGINT UNSIGNED NOT NULL,
	media_name VARCHAR(50),
	media_type_id BIGINT UNSIGNED NOT NULL,
	genre BIGINT UNSIGNED NOT NULL,
	listens BIGINT,
	released_at DATETIME DEFAULT current_timestamp(),	
	
	FOREIGN KEY (auth_id) REFERENCES authors(id),
	FOREIGN KEY (media_type_id) REFERENCES media_types(id),
	FOREIGN KEY (genre) REFERENCES genres(id),
	INDEX idx_trackname(auth_id, id)
	
);

-- списки воспроизведения

DROP TABLE IF EXISTS playlists;
CREATE TABLE playlists(
	id BIGINT UNSIGNED NOT NULL,
	name VARCHAR(50),
	creator BIGINT UNSIGNED NOT NULL,
	media_id BIGINT UNSIGNED NOT NULL,
	
	FOREIGN KEY (creator) REFERENCES users(id),
	FOREIGN KEY (media_id) REFERENCES media(id)
);

-- подписки

DROP TABLE IF EXISTS follows;
CREATE TABLE follows(
	id SERIAL,
	initiator_id BIGINT UNSIGNED NOT NULL,
	target_id BIGINT UNSIGNED NOT NULL,
	
	PRIMARY KEY (initiator_id, target_id),
	FOREIGN KEY (initiator_id) REFERENCES users(id),
    FOREIGN KEY (target_id) REFERENCES users(id),
    CHECK (initiator_id <> target_id)
);

-- лайки
DROP TABLE IF EXISTS likes;
CREATE TABLE likes(
	id SERIAL,
    user_id BIGINT UNSIGNED NOT NULL,
    media_id BIGINT UNSIGNED NOT NULL,
    created_at DATETIME DEFAULT NOW(),


    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (media_id) REFERENCES media(id)
);

-- лейбл
DROP TABLE IF EXISTS label;
CREATE TABLE label(
	id SERIAL,
	name VARCHAR(50),
    actor_id BIGINT UNSIGNED NOT NULL,
    owner_id BIGINT UNSIGNED NOT NULL,
    country VARCHAR(50),
    
    FOREIGN KEY (actor_id) REFERENCES authors(id),
    FOREIGN KEY (owner_id) REFERENCES users(id)
);


-- премии
DROP TABLE IF EXISTS prizes;
CREATE TABLE prizes(
	id SERIAL,
	name VARCHAR(50),
    owner_id BIGINT UNSIGNED NOT NULL,
    
    FOREIGN KEY (owner_id) REFERENCES authors(id)
);





