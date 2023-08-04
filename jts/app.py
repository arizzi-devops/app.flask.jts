from flask import Flask, render_template, request, redirect, session
import sqlite3


app = Flask(__name__)
app.secret_key = '7fb1a5'

# @app.after_request
def remove_empty_lines(response):
    lines = response.get_data().decode().splitlines()
    non_empty_lines = [line for line in lines if line.strip()]
    response.set_data('\n'.join(non_empty_lines).encode())
    return response

from users import users
from jobs import jobs_bp
app.register_blueprint(users)
app.register_blueprint(jobs_bp)


initdb_file = 'ddl/sqlite_initdb.sql'
db_file = 'database.db'

def get_db_connection():
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    return conn


def check_create_database():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    with open(initdb_file, 'r') as sql_file:
        sql_script = sql_file.read()
        cursor.executescript(sql_script)
    conn.commit()
    conn.close()
check_create_database()

@app.route('/')
def index():
    if 'username' not in session:
        return redirect('/login')
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()

    return render_template('index.html', users=users)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print (request.form['username'])
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()

        if user and user['password'] == password:
            session['username'] = user['username']
            session['user_id'] = user['id']
            return redirect('/')
        else:
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')



@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
