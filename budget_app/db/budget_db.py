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
