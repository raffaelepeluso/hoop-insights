import sqlite3, os

query = """
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS games;
DROP TABLE IF EXISTS player_stats;

CREATE TABLE players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255),
    jersey INTEGER,
    position VARCHAR(255),
    height REAL,
    weight REAL,
    age INTEGER,
    ppg REAL DEFAULT 0,
    rpg REAL DEFAULT 0,
    apg REAL DEFAULT 0,
    fpg REAL DEFAULT 0
);

CREATE TABLE games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    home_team VARCHAR(255),
    away_team VARCHAR(255),
    home_score INTEGER,
    away_score INTEGER,
    location VARCHAR(255),
    date DATE
);

CREATE TABLE player_stats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER,
    game_id INTEGER,
    pts INTEGER,
    reb INTEGER,
    ast INTEGER,
    stl INTEGER,
    blk INTEGER,
    turn INTEGER,  
    pf INTEGER,
    FOREIGN KEY (player_id) REFERENCES players (id),
    FOREIGN KEY (game_id) REFERENCES games (id)
);

INSERT INTO players (name, jersey, position, height, weight, age)
VALUES
    ('Raffaele Peluso', 2, 'Guard', 1.80, 73, 23),
    ('Emiliano Annese', 7, 'Guard', 1.80, 67, 23),
    ('Gianpiero Aurilia', 8, 'Guard', 1.82, 74, 24),
    ('Luigi Omar Marzullo', 3, 'Guard', 1.85, 75, 22),
    ('Emanuele Pio Evangelista', 11, 'Forward', 1.86, 80, 20),
    ('Giuseppe Accomando', 21, 'Center', 1.92, 89, 27),
    ('Angelo Giella', 22, 'Guard', 1.70, 65, 29),
    ('Davide Festa', 77, 'Center', 1.93, 97, 22),
    ('Daniele Lenguito', 90, 'Forward', 1.86, 90, 26),
    ('Daniele Fratello', 0, 'Forward', 1.88, 90, 27),
    ('Emanuele Flora', 15, 'Forward', 1.86, 79, 27),
    ('Massimo Valore', 4, 'Center', 1.87, 140, 32),
    ('Luca Santomassimo', 34, 'Center', 1.98, 110, 39);

INSERT INTO games (home_team, away_team, home_score, away_score, location, date)
VALUES
    ('BPT Polisportiva Toriello', 'Borace', 37, 47, 'Palestra Comunale, Santo Stefano Del Sole', '2024-12-11'),
    ('Mata Leao Benevento', 'BPT Polisportiva Toriello', 55, 29, 'Palestra Rummo, Benevento', '2024-12-16'),
    ('BPT Polisportiva Toriello', 'Hirpinian Nuts', 62, 61, 'Palestra Comunale, Santo Stefano Del Sole', '2025-01-15'),
    ('Avellino Boars', 'BPT Polisportiva Toriello', 53, 30, 'Palestra Bellizzi, Avellino', '2025-01-23');
    

INSERT INTO player_stats (player_id, game_id, pts, reb, ast, stl, blk, turn, pf)
VALUES
    (2, 3, 12, 0, 0, 0, 0, 0, 3),
    (3, 3, 5, 0, 0, 0, 0, 0, 3),
    (4, 3, 26, 0, 0, 0, 0, 0, 4),
    (5, 3, 0, 0, 0, 0, 0, 0, 1),
    (6, 3, 5, 0, 0, 0, 0, 0, 4),
    (7, 3, 1, 0, 0, 0, 0, 0, 1),
    (9, 3, 1, 0, 0, 0, 0, 0, 5),
    (10, 3, 12, 0, 0, 0, 0, 0, 4),
    (1, 4, 0, 0, 0, 0, 0, 0, 1),
    (2, 4, 12, 0, 0, 0, 0, 0, 1),
    (3, 4, 0, 0, 0, 0, 0, 0, 3),
    (4, 4, 13, 0, 0, 0, 0, 0, 4),
    (5, 4, 0, 0, 0, 0, 0, 0, 0),
    (6, 4, 1, 0, 0, 0, 0, 0, 1),
    (7, 4, 0, 0, 0, 0, 0, 0, 0),
    (8, 4, 2, 0, 0, 0, 0, 0, 2),
    (9, 4, 2, 0, 0, 0, 0, 0, 2),
    (11, 4, 0, 0, 0, 0, 0, 0, 0),
    (1, 1, 6, 0, 0, 0, 0, 0, 5),
    (2, 1, 7, 0, 0, 0, 0, 0, 2),
    (3, 1, 11, 0, 0, 0, 0, 0, 2),
    (5, 1, 0, 0, 0, 0, 0, 0, 0),
    (6, 1, 4, 0, 0, 0, 0, 0, 1),
    (7, 1, 0, 0, 0, 0, 0, 0, 1),
    (8, 1, 2, 0, 0, 0, 0, 0, 0),
    (9, 1, 7, 0, 0, 0, 0, 0, 1),
    (12, 1, 0, 0, 0, 0, 0, 0, 1),
    (1, 2, 2, 0, 0, 0, 0, 0, 0),
    (2, 2, 4, 0, 0, 0, 0, 0, 1),
    (3, 2, 6, 0, 0, 0, 0, 0, 0),
    (4, 2, 8, 0, 0, 0, 0, 0, 2),
    (5, 2, 0, 0, 0, 0, 0, 0, 2),
    (6, 2, 2, 0, 0, 0, 0, 0, 1),
    (8, 2, 1, 0, 0, 0, 0, 0, 1),
    (9, 2, 4, 0, 0, 0, 0, 0, 2),
    (10, 2, 2, 0, 0, 0, 0, 0, 3),
    (13, 2, 0, 0, 0, 0, 0, 0, 1);
"""

# Creazione della cartella 'data' se non esiste
os.makedirs("data", exist_ok=True)

# Connessione al database e creazione delle tabelle
connection = sqlite3.connect("data/database.db")
cursor = connection.cursor()
cursor.executescript(query)
connection.commit()

# Calcolo e aggiornamento di ppg, rpg e apg per ogni giocatore
cursor.execute("""
    UPDATE players
    SET 
    ppg = (SELECT ROUND(COALESCE(AVG(pts), 0), 1) FROM player_stats WHERE player_stats.player_id = players.id),
    rpg = (SELECT ROUND(COALESCE(AVG(reb), 0), 1) FROM player_stats WHERE player_stats.player_id = players.id),
    apg = (SELECT ROUND(COALESCE(AVG(ast), 0), 1) FROM player_stats WHERE player_stats.player_id = players.id),
    fpg = (SELECT ROUND(COALESCE(AVG(pf), 0), 1) FROM player_stats WHERE player_stats.player_id = players.id)

""")
connection.commit()
connection.close()
