from flask import Flask, jsonify
import sqlite3

def get_connection():
    try:
        connection = sqlite3.connect("data/database.db")
        connection.row_factory = sqlite3.Row
        return connection
    except sqlite3.Error as e:
        print("Error:", e)
        return None

app = Flask(__name__)

@app.get("/players")
def get_players():
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM players")
        result = cursor.fetchall()
        connection.close()
        return jsonify([dict(row) for row in result])
    else:
        return {"error": "Database error"}, 500

@app.get("/players/<int:id>")
def get_player(id):
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM players WHERE id = ?", (id,))
        result = cursor.fetchone()
        connection.close()
        if result:
            return jsonify(dict(result))
        else:
            return {"error": "Player not found"}, 404
    else:
        return {"error": "Database error"}, 500

@app.get("/games")
def get_games():
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM games")
        result = cursor.fetchall()
        connection.close()
        return jsonify([dict(row) for row in result])
    else:
        return {"error": "Database error"}, 500

@app.get("/games/<int:id>")
def get_game(id):
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM games WHERE id = ?", (id,))
        game = cursor.fetchone()

        if game:
            cursor.execute("""
                SELECT players.name, player_stats.pts, player_stats.reb, player_stats.ast, 
                       player_stats.stl, player_stats.blk, player_stats.turn, player_stats.pf
                FROM player_stats
                JOIN players ON player_stats.player_id = players.id
                WHERE player_stats.game_id = ?
            """, (id,))
            player_stats = cursor.fetchall()
            connection.close()

            return jsonify({
                "game": dict(game),
                "player_stats": [dict(row) for row in player_stats]
            })
        else:
            connection.close()
            return {"error": "Game not found"}, 404
    else:
        return {"error": "Database error"}, 500

if __name__ == "__main__":
    app.run(debug=True)
