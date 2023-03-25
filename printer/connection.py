# import sqlite3
import psycopg2



def create_table():
    conn = psycopg2.connect("dbname='leased_printers' user='postgres' password='post123' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (id SERIAL,firstName VARCHAR(50) not null,lastName VARCHAR(50) not null,email VARCHAR(50) not null,password varchar(50) not null, PRIMARY KEY(id))')
    print('table created successfully')
    conn.commit()
    conn.close()

def insert(firstName,lastName,email,password):
    conn = psycopg2.connect("dbname='leased_printers' user='postgres' password='post123' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute("INSERT INTO users VALUES ('%s','%s','%s','%s')" % (firstName,lastName,email,password))
    print("inserted successfully")
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname='leased_printers' user='postgres' password='post123' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute('select * from users')
    row = cur.fetchall()
    conn.close()
    return row

def delete():
    conn= psycopg2.connect("")
    cur = conn.cur()
    cur.execute('delete * from users')

# insert('kevin','nyayiha','king','password')
print(view())

create_table()