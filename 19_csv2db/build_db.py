# Suhana Kumar
# K^3: Suhana Kumar, Kyle Lee, Vedant Kothari
# SoftDev
# SQLITE3 BASICS
# Oct 20 2024

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

c.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY, -- 'id' is the identifier for each student (PRIMARY KEY)
    name TEXT,              -- 'name' is text
    age INTEGER             -- 'age' is an integer
    );
    ''')


with open('students.csv', newline = "") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute('INSERT OR IGNORE INTO students (id, name, age) VALUES (?, ?, ?)',
                  (row['id'], row['name'], row['age']))

c.execute('''
CREATE TABLE IF NOT EXISTS courses {
    student_id INTEGER, -- 'id' is an integer
    code TEXT,          -- 'code' is text in the form of a name
    mark INTEGER,       -- 'mark' is an integer in the form of a grade
    FOREIGN KEY(student_id) REFERENCES students(id) --checks whether student_id exists in original csv
    );
    ''')

with open('courses.csv', newline = "") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute('INSERT OR IGNORE INTO courses (student_id, code, mark) VALUES (?, ?, ?)',
                  (row['id'], row['code'], row['mark']))

command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
