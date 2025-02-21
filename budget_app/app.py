from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    db = sqlite3.connect("db/app.db")
    return db

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create_new/")
def create_new():
    return render_template("create_new.html")

@app.route("/view_all/")
def view_all():
    return render_template("view_all.html")
        


if __name__ == "__main__":
    app.run(debug=True)
