CREATE TABLE IF NOT EXISTS Users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL ,
    last_name TEXT NOT NULL ,
    phone TEXT NOT NULL ,
    email TEXT NOT NULL UNIQUE ,
    password TEXT NOT NULL ,
    date_created TEXT NOT NULL ,
    hire_date TEXT NOT NULL ,
    user_type TEXT NOT NULL ,
    active INTEGER DEFAULT 1
);

CREATE TABLE IF NOT EXISTS Competencies(
    competency_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL ,
    date_created TEXT NOT NULL ,
    active INTEGER DEFAULT 1
);