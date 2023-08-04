from flask import Blueprint, render_template, request, redirect, session, Flask
import sqlite3

app = Flask(__name__)
users = Blueprint('users', __name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Register the login check function to be executed before each request

@users.route('/users')
def user_list():
    if 'username' not in session:
        return redirect('/login')
    conn = get_db_connection()
    users = conn.execute('SELECT id, username FROM users').fetchall()
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
            conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
        except sqlite3.IntegrityError: # Check if user already exists
            error = "Username already exists. Please choose a different username."
        conn.close()

        if error:
            return render_template('users_form.html', error=error)
        return redirect('/users')
    return render_template('users_form.html', user={})


@users.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
def edit_user(user_id):
    if 'username' not in session:
        return redirect('/login')
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()

    if request.method == 'POST':
        new_username = request.form['username']
        new_password = request.form['password']

        conn.execute('UPDATE users SET username = ?, password = ? WHERE id = ?', (new_username, new_password, user_id))
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
    conn.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()

    return redirect('/users')
