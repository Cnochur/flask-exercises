from flask import Flask, render_template
import sqlite3

db = sqlite3.connect("app.db")
cursor = db.cursor()
cursor.execute('''
               CREATE TABLE IF NOT EXISTS monthly_budget(
                   budget_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                   sal FLOAT,
                   bills TEXT,
                   necs TEXT,
                   remaining FLOAT
                   )''')
cursor.execute('''
               CREATE TABLE IF NOT EXISTS item(
                   item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT,
                   emoji TEXT,
                   item_price FLOAT
                   )''')
db.commit()
db.close()

app = Flask(__name__)

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
