from flask import Flask,redirect,render_template,request
from connection import *

app = Flask(__name__)

# users = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create',methods=('POST', 'GET'))
def create():
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        password = request.form['password']
        
        with psycopg2.connect("dbname='leased_printers' user='postgres' password='post123' host='localhost' port='5432' ") as conn:
            insert(firstName,lastName,email,password)
            return render_template('login.html')
        
    return render_template('create-account.html')


# @app.route('/addrec',methods=('POST','get'))
# def addrec():
#     if request.method == 'post':
#         try:
#             firstname = request.form.get('firstName')
#             lastname = request.form.get('lastName')
#             email = request.form.get('email')
#             password = request.form.get('password')
#             print('passwo') 
#             with psycopg2.connect('leased_printers.db') as conn:
#                 insert(firstname,lastname,email,password)
#                 msg = "success"
#         except:
#             conn.rollback()
#             msg = "record error"
#         finally:
#             return render_template('success.html',msg=msg)
            


@app.route('/login',methods=('POST', 'GET'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['Password']

        with psycopg2.connect(" dbname='leased_printers', user='postgres' password='post123' host='localhost' port='5432' ") as conn:
            for email , password in view():
                print(view())
                if email and password in view():
                    return render_template('createparcel.html')
                else:
                    return render_template('index.html')

    return render_template('login.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/admin/')
def admin():
    return render_template('admin.html')

@app.route('/createparcel/',methods=('POST','GET'))
def createparcel():
    return render_template('createparcel.html')


# @app.route('/success/')
# def success():
#     return render_template('success.html') 

if __name__=='main':
    app.run(debug=True)

# print(users)