-- changeset: 1
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(16) NOT NULL,
    `password` TEXT NOT NULL,
    UNIQUE (username)
);
INSERT INTO users (username, password)
    SELECT 'admin', 'admin'
    WHERE NOT EXISTS (SELECT 1 FROM users WHERE username = 'admin');


-- changeset: 2
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    job_title TEXT NOT NULL,
    job_location TEXT,
    job_link TEXT,
    job_status_id INTEGER DEFAULT 1,
    user_id INTEGER NOT NULL DEFAULT 0
);


-- changeset: 3
-- commented because was executed, but not controlled by liquibase yet
-- ALTER TABLE users ADD COLUMN active BOOLEAN DEFAULT TRUE;
