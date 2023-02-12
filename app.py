from pymysql import connect, cursors
from flask import Flask, render_template, session, redirect, url_for, request
from os import environ, urandom
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = urandom(64)
load_dotenv('.env')

def createConnection(passwd):
    return connect(
        user = environ.get('DB_USER'),
        host = environ.get('DB_HOST'),
        passwd = passwd,
        db = environ.get('DB'),
        charset = 'utf8mb4',
        cursorclass = cursors.DictCursor
    )

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

def permission():
    if session['grant'] == True:
        return
    raise

@app.route('/login', methods = ['get', 'post'])
def login():
    if request.method != 'POST':
        return render_template('login.html')
    try:
        createConnection(request.form['passwd'])
    except:
        return render_template(
			       'login.html', 
			       error = 'invalid connection'
			      )
    session['grant'] = True
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    try:
        permission()
    except:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/')
def main():
    try:
        permission()
    except:
        return redirect(url_for('login'))
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(
	    host = environ.get('HOST'), 
	    port = environ.get('PORT')
	)
