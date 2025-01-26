from flask import Flask, render_template
import sqlite3

def get_connection():
    connection = sqlite3.connect("data/database.db")
    connection.row_factory = sqlite3.Row
    return connection

app = Flask(__name__)

@app.route("/")
def home():
    connection = get_connection()
    if connection:
        cursor = connection.cursor()

        # Recupera le partite
        cursor.execute("SELECT * FROM games")
        games = cursor.fetchall()

        # Recupera i giocatori
        cursor.execute("SELECT * FROM players")
        players = cursor.fetchall()

        connection.close()
        # Passa i dati al template
        return render_template("home.html", games=games, players=players)
    else:
        return {"error": "Database error"}, 500

@app.route("/games/<int:id>")
def get_game(id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM games WHERE id = ?", (id,))
    game = cursor.fetchone()

    if game:
        cursor.execute("""
            SELECT players.name, players.id, player_stats.pts, player_stats.reb, player_stats.ast, 
                   player_stats.stl, player_stats.blk, player_stats.turn, player_stats.pf
            FROM player_stats
            JOIN players ON player_stats.player_id = players.id
            WHERE player_stats.game_id = ?
        """, (id,))
        player_stats = cursor.fetchall()
        connection.close()

        return render_template("game.html", game=game, player_stats=player_stats)
    else:
        connection.close()
        return {"error": "Game not found"}, 404

@app.route("/player/<int:id>")
def get_player(id):
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM players WHERE id = ?", (id,))
        player = cursor.fetchone()
        connection.close()

        if player:
            return render_template("player.html", player=player)
        else:
            return {"error": "Player not found"}, 404
    else:
        return {"error": "Database error"}, 500

if __name__ == "__main__":
    app.run(debug=True)
