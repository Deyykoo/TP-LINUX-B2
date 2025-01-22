from os import environ
from flask import Flask, jsonify
from flask_mysqldb import MySQL

DB_HOST = environ.get("DB_HOST")
DB_HOST = DB_HOST if DB_HOST is not None else "la_grosse_db"
app = Flask(__name__)
app.config["MYSQL_HOST"] = DB_HOST
app.config["MYSQL_USER"] = "meow"
app.config["MYSQL_PASSWORD"] = "meow"
app.config["MYSQL_DB"] = "soupa_db"

mysql = MySQL(app)


@app.route("/")
def hello_world():
    cursor = mysql.connection.cursor()
    cursor.execute("select id, name from users;")
    items = cursor.fetchall()
    return jsonify([{"name": name, "id": meow} for name, meow in items])


if __name__ == "__main__":
    LISTENING_PORT = environ.get("PORT")
    LISTENING_PORT = LISTENING_PORT if LISTENING_PORT is not None else 8888
    app.run(host="0.0.0.0", port=LISTENING_PORT)