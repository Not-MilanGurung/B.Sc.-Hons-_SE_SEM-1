import sqlite3 as sql

con = sql.connect('Tkinter_Class/tkin.db')
cur = con.cursor()
# cur.execute('CREATE TABLE students (id integer primary key AUTOINCREMENT, name varchar(20), age integer, grade varchar(10))')
def insert(user, age, grade):
    query = 'INSERT INTO students(name, age, grade) VALUES(?, ?, ?)'
    cur.execute(query,(user, age, grade))
    con.commit()
    return True

def close():
    con.close()
# cur.execute('drop table students')