from flask import Blueprint, render_template, request, redirect, session, Flask
import mysql.connector
import os

app = Flask(__name__)
users = Blueprint('users', __name__)

def get_db_connection():
    mysql_config = {
        'host': os.environ.get('DB_HOST'),
        'user': os.environ.get('DB_USER'),
        'password': os.environ.get('DB_PASS'),
        'database': os.environ.get('DB_NAME'),
    }
    conn = mysql.connector.connect(**mysql_config)
    return conn

# Register the login check function to be executed before each request

@users.route('/users')
def user_list():
    if 'username' not in session:
        return redirect('/login')
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT id, username FROM users')
    users = cursor.fetchall()
    conn.close()
    return render_template('users_list.html', users=users)


@users.route("/users/add", methods=["GET", "POST"])
def add_user():
    if 'username' not in session:
        return redirect('/login')
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        error = False
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, password))
        except mysql.connector.IntegrityError as e: # Check if user already exists
            error = "Error: Username already exists or constraint violation:"
            print(error, e)
        except mysql.connector.Error as e:
            error = "Error executing query:"
            print(error, e)
        conn.commit()
        conn.close()

        if error:
            return render_template('users_form.html', error=error, user={})
        return redirect('/users')
    return render_template('users_form.html', user={})


@users.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
def edit_user(user_id):
    if 'username' not in session:
        return redirect('/login')
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
    user = cursor.fetchone()

    if request.method == 'POST':
        new_username = request.form['username']
        new_password = request.form['password']

        print ('UPDATE users SET username = %s, password = %s WHERE id = %s')
        cursor.execute('UPDATE users SET username = %s, password = %s WHERE id = %s', (new_username, new_password, user_id))
        conn.commit()
        conn.close()

        return redirect('/users')
    else:
        conn.close()
        return render_template('users_form.html', user=user)

@users.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    if 'username' not in session:
        return redirect('/login')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = %s', (user_id,))
    conn.commit()
    conn.close()

    return redirect('/users')
