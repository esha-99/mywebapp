# app.py
import os
from flask import Flask, request, redirect, url_for, render_template
import sqlite3

app = Flask(__name__)
DATABASE = os.path.join(os.path.dirname(__file__), "users.db")  # absolute path


# Initialize the database
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

# Route to show all users
@app.route('/')
def index():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    print("Users from DB:", users)
    return render_template('index.html', users=users)

# Route to add a new user
@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
            conn.commit()
        except sqlite3.IntegrityError:
            return "Email already exists!"
        finally:
            conn.close()
        return redirect(url_for('index'))
    return render_template('add_user.html')

if __name__ == '__main__':
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
