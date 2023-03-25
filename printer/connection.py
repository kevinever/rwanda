# import sqlite3
import psycopg2



def create_table():
    conn = psycopg2.connect('leseased_printers.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (firstName VARCHAR(50),lastName VARCHAR(50),email VARCHAR(50),password varchar(50))')
    print('table created successfully')
    conn.commit()
    conn.close()

def insert(firstName,lastName,email,password):
    conn = psycopg2.connect('leased_printers.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO users values(?,?,?,?)',(firstName,lastName,email,password))
    print('inserted successfully')
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect('leased_printers')
    cur = conn.cursor()
    cur.execute('select * from users')
    row = cur.fetchall()
    conn.close()
    return row

insert('firstName','lastName','email','password')
print(view())