from flask import Flask,render_template,request
import sqlite3
app=Flask(__name__)

def create_tables():
    conn = sqlite3.connect('jp.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            pwd TEXT NOT NULL,
            phone TEXT,
            gender TEXT,
            addrs TEXT,
            resume TEXT NOT NULL
            
    );''')

    c.execute('''CREATE TABLE IF NOT EXISTS login (
        login_id INTEGER PRIMARY KEY,
        u_name VARCHAR NOT NULL,
        password VARCHAR NOT NULL
    );''')

    c.execute('''CREATE TABLE IF NOT EXISTS user_material (
        id INTEGER PRIMARY KEY,
        type VARCHAR NOT NULL,
        name VARCHAR NOT NULL,
        path VARCHAR NOT NULL,
        description VARCHAR NOT NULL
    );''')

    c.execute('''CREATE TABLE IF NOT EXISTS jobs (
            job_id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_title TEXT NOT NULL,
            company_name TEXT NOT NULL,
            job_location TEXT NOT NULL,
            job_region TEXT NOT NULL,
            job_type TEXT NOT NULL,
            job_description TEXT NOT NULL
    );''')

    c.execute('''CREATE TABLE IF NOT EXISTS applications (
            application_id INTEGER PRIMARY KEY AUTOINCREMENT,
            application_date DATE NOT NULL,
            status VARCHAR,
            job_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY(job_id) REFERENCES jobs(job_id),
            FOREIGN KEY(user_id) REFERENCES users(user_id)
    );''')

    c.execute('''CREATE TABLE IF NOT EXISTS gallery (
        photoid INTEGER PRIMARY KEY,
        photo VARCHAR NOT NULL,
        text VARCHAR NOT NULL,
        date_time DATETIME NOT NULL
    );''')

    conn.commit()
    conn.close()

create_tables()