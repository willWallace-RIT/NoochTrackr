CREATE TABLE users (
  id TEXT PRIMARY KEY,
  nutrition_score FLOAT
);

CREATE TABLE crops (
  id TEXT PRIMARY KEY,
  name TEXT,
  calories INT
);

CREATE TABLE trades (
  id SERIAL PRIMARY KEY,
  offer TEXT,
  request TEXT
);
