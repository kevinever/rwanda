from flask import Flask,redirect,render_template,request
from connection import *

app = Flask(__name__)

users = []

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create/',methods=('post','get'))
def create():
    if request.method == 'post':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        password = request.form.get('password')
        with psycopg2.connect('leased_printers.db'):
            insert(firstname,lastname,email,password)
    # msg = 'hello'
    return render_template('index.html')


@app.route('/login/')
def login():
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


@app.route('/success/')
def success():
    return render_template('success.html') 

if __name__=='main':
    app.run(debug=True)

print(users)