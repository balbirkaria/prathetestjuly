from flask import Flask, request, render_template_string, redirect
import sqlite3
import subprocess
import requests

app = Flask(__name__)

# --- Initialize SQLite Database ---
def init_db():
    conn = sqlite3.connect('vulnlab.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            bio TEXT
        )
    ''')
    conn.commit()
    conn.close()

# --- Home Route ---
@app.route('/')
def home():
    return '''
        <h1>Welcome to the Vulnerable Lab</h1>
        <ul>
            <li><a href="/register">Register (SQLi)</a></li>
            <li><a href="/login">Login (SQLi)</a></li>
            <li><a href="/profile?user=test">View Profile (XSS)</a></li>
            <li><a href="/exec">Execute Command (RCE)</a></li>
            <li><a href="/ssrf?url=http://example.com">Fetch External URL (SSRF)</a></li>
        </ul>
    '''

# --- Registration Page (SQLi) ---
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        bio = request.form.get('bio', 'No bio')

        conn = sqlite3.connect('vulnlab.db')
        cur = conn.cursor()

        # 🚨 SQL Injection vulnerability
        query = f"INSERT INTO users (username, password, bio) VALUES ('{username}', '{password}', '{bio}')"
        cur.execute(query)
        conn.commit()
        conn.close()

        return "Registered successfully!"
    
    return '''
        <h2>Register</h2>
        <form method="POST">
            Username: <input name="username"><br>
            Password: <input name="password"><br>
            Bio: <textarea name="bio"></textarea><br>
            <in
