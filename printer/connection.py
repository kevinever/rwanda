# import sqlite3
import psycopg2



def create_table():
    conn = psycopg2.connect("dbname='leased_printers' user='postgres' password='post123' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (firstName VARCHAR(50),lastName VARCHAR(50),email VARCHAR(50),password varchar(50))')
    print('table created successfully')
    conn.commit()
    conn.close()

def insert(firstName,):
    conn = psycopg2.connect("dbname='leased_printers' user='postgres' password='post123' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute("INSERT INTO ")

def view():
    conn = psycopg2.connect("")
    cur = conn.cursor()
    cur.execute('select * from users')
    row = cur.fetchall()
    conn.close()
    return row

def delete(email):
    conn= psycopg2.connect('leased_printers')
    cur = conn.cur()
    cur.execute('delete from users where email=?',(email,))

insert('firstName','lastName','email','password')
# print(view)

create_table()