-- changeset: 1
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);
INSERT INTO users (username, password)
    SELECT 'admin', 'admin'
    WHERE NOT EXISTS (SELECT 1 FROM users WHERE username = 'admin');


-- changeset: 2
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_title TEXT NOT NULL,
    job_location TEXT,
    job_link TEXT,
    job_status_id INTEGER DEFAULT 1,
    user_id INTEGER NOT NULL DEFAULT 0
);

