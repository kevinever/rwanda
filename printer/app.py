from flask import Flask,redirect,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create')
def create():
    return render_template('create-account.html')