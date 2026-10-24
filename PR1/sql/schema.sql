CREATE TABLE IF NOT EXISTS accounting_objects (
    id INTEGER PRIMARY KEY,
    address TEXT NOT NULL,
    object_type TEXT NOT NULL,
    area REAL
);

CREATE TABLE IF NOT EXISTS meters (
    id INTEGER PRIMARY KEY,
    number TEXT NOT NULL,
    meter_type TEXT NOT NULL,
    object_id INTEGER NOT NULL,
    status TEXT,
    FOREIGN KEY (object_id) REFERENCES accounting_objects(id)
);

CREATE TABLE IF NOT EXISTS periods (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS readings (
    id INTEGER PRIMARY KEY,
    meter_id INTEGER NOT NULL,
    value REAL NOT NULL,
    reading_date TEXT,
    FOREIGN KEY (meter_id) REFERENCES meters(id)
);