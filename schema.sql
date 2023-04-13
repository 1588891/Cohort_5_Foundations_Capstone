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

CREATE TABLE IF NOT EXISTS Assessments(
    assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    competency_id INTEGER,
    name TEXT,
    active INTEGER DEFAULT 1,

    FOREIGN KEY (competency_id)
        REFERENCES Competencies (competency_id)


);

CREATE TABLE IF NOT EXISTS Assessment_Results(
    assessment_result_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    assessment_id INTEGER,
    score REAL,
    date_taken TEXT NOT NULL,
    manager INT,

    FOREIGN KEY (user_id)
        REFERENCES Users (user_id),
    FOREIGN KEY (assessment_id)
        REFERENCES Assessments (assessment_id),
    FOREIGN KEY (manager)
        REFERENCES Users (user_id)
    
);

