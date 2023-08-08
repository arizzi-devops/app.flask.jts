--liquibase formatted sql
--changeset arizzi:1
CREATE TABLE IF NOT EXISTS user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    login VARCHAR(12) NOT NULL UNIQUE,
    password VARCHAR(32) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);
INSERT INTO user (name,login,password)
	VALUES ('Admin','admin','admin');

--changeset arizzi:2
CREATE TABLE IF NOT EXISTS job (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL,
    url VARCHAR(200) NOT NULL,
    status_id INT NOT NULL
);
