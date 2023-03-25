# import sqlite3
import psycopg2
from flask import Flask,render_template



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
    # cur.execute('drop ')
    cur.execute("INSERT INTO users VALUES (Default,'%s','%s','%s','%s')" % (firstName,lastName,email,password))
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








def create_printer():
    conn = psycopg2.connect("dbname='leased_printers'user='postgres' password='post123' host='localhost' port='5432'  ")
    cur = conn.cursor()
    # cur.execute("DROP TABLE printers if exists")
    cur.execute("CREATE TABLE IF NOT EXISTS printers (id serial,instutition varchar(50),location varchar(50) not null ,serialnumber varchar(50),model varchar(50),types varchar(50),ip varchar(50),primary key(serialnumber))")
    print('table created')
    conn.commit()
    conn.close()


def insert_printer(instutition,location,serialnumber,model,types,ip):
    conn = psycopg2.connect("dbname='leased_printers' user='postgres' password='post123' host='localhost' port='5432' " )
    cur = conn.cursor()
    cur.execute("INSERT INTO printers VALUES(Default,%s,%s,%s,%s,%s,%s)" , (instutition,location,serialnumber,model,types,ip))
    conn.commit()
    conn.close()



def view_printer():
     conn = psycopg2.connect("dbname='leased_printers' user='postgres' password='post123' host='localhost' port='5432' " )
     cur = conn.cursor()
     cur.execute('select * from printers')
     row = cur.fetchall()
     conn.close()
     return row



# insert_printer('kibagabaga', 'accounting', 'asdf12334a', 'brother', 'bw','12.0')






create_printer()
create_table()

print(view_printer())

insert('kevin','nyayiha','king','password')
print(view())