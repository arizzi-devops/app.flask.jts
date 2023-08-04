from flask import Flask, render_template, request, redirect, session
import mysql.connector
import os

app = Flask(__name__)
app.secret_key = '7fb1a5'

from users import users
from jobs import jobs_bp
app.register_blueprint(users)
app.register_blueprint(jobs_bp)

initdb_file = 'ddl/mysql_initdb.sql'

def get_db_connection():
    mysql_config = {
        'host': os.environ.get('DB_HOST'),
        'user': os.environ.get('DB_USER'),
        'password': os.environ.get('DB_PASS'),
        'database': os.environ.get('DB_NAME'),
    }
    conn = mysql.connector.connect(**mysql_config)
    return conn


def check_create_database():
    conn = get_db_connection()
    #cursor = conn.cursor(dictionary=True)
    cursor = conn.cursor()

    with open(initdb_file, 'r') as sql_file:
        sql_script = sql_file.read()

    # Split the SQL script into individual statements based on semicolon as delimiter
    statements = sql_script.split(';')

    # Execute each statement one by one
    for statement in statements:
        if statement.strip():
            cursor.execute(statement)

    conn.commit()
    conn.close()
check_create_database()

@app.route('/')
def index():
    if 'username' not in session:
        return redirect('/login')
    return render_template('index.html', users=users)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s AND active = 1", (username,))
        user = cursor.fetchone()
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
    app.run(debug=False)
