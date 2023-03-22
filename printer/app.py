from flask import Flask,redirect,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create/')
def create():
    # msg = 'hello'
    return render_template('create-account.html')


@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/admin/')
def admin():
    return render_template('admin.html')



if __name__=='main':
    app.run(debug=True)
