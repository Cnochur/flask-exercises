from flask import Flask, render_template, redirect, request
import sqlite3
import datetime

app = Flask(__name__)

def get_db_connection():
    db = sqlite3.connect("db/app.db")
    return db

@app.route("/")
def home():
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM monthly_budget")
    months = cursor.fetchall()
    return render_template("index.html", months=months)

@app.route("/create_new/")
def create_new():
    return render_template("create_new.html")

@app.route("/create_new/", methods=["POST"])
def add_new_month():
    if request.method == "POST":
        month = datetime.datetime.now().strftime("%B %Y")
        sal = request.form["salary"]
        bill_items = request.form["bill_item"]
        nec_items = request.form["nec_item"]
        
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("INSERT INTO monthly_budget(created_at, sal, bills, necs) VALUES (?, ?, ?, ?)",
                       (month, sal, bill_items, nec_items))
        db.commit()
        db.close()
        
        
    return redirect("/")

@app.route("/view_all/", methods=["GET"])
def view_all():
    if request.method == "GET":
        ...
    return render_template("view_all.html")
        


if __name__ == "__main__":
    app.run(debug=True)
