--liquibase formatted sql
--changeset arizzi:1
CREATE TABLE IF NOT EXISTS user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    login VARCHAR(12) NOT NULL UNIQUE,
    password VARCHAR(128) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);
INSERT INTO user (name,login,password)
	VALUES ('Admin','admin','pbkdf2:sha256:600000$ntbWuWyrvJ4L0zsv$923a15ec48a163ab4c009eb827e254c13e2630333745ba62aef3553cd0b1b236');

--changeset arizzi:2
CREATE TABLE IF NOT EXISTS job (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL,
    url VARCHAR(200) NOT NULL,
    status_id INT NOT NULL
);

--changeset arizzi:3
CREATE TABLE IF NOT EXISTS job_status (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(32) NOT NULL
);
INSERT INTO job_status (name)
	VALUES ('Applied'), ('H.R.'), ('Tech'), ('Done');
