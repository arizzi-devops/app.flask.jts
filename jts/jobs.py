from flask import Blueprint, render_template, session, redirect, url_for, request, jsonify
import mysql.connector
import os

jobs_bp = Blueprint("jobs", __name__)

statuses = ["New", "Applied", "H.R.", "Tech", "Finished"]


def get_db_connection():
    mysql_config = {
        'host': os.environ.get('DB_HOST'),
        'user': os.environ.get('DB_USER'),
        'password': os.environ.get('DB_PASS'),
        'database': os.environ.get('DB_NAME'),
    }
    conn = mysql.connector.connect(**mysql_config)
    return conn

@jobs_bp.route("/jobs")
def view_jobs():
    if 'username' not in session:
        return redirect('/login')
    user_id = session['user_id']
    print(user_id)
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM jobs WHERE user_id = %s", (user_id,))
    jobs = cursor.fetchall()
    conn.close()
    return render_template("jobs_list.html", statuses=statuses, jobs=jobs)



@jobs_bp.route("/jobs/add", methods=["GET", "POST"])
def add_job():
    if 'username' not in session:
        return redirect('/login')
    if request.method == "POST":
        job_title = request.form["job_title"]
        job_location = request.form["job_location"]
        job_link = request.form["job_link"]

        conn = get_db_connection()
        c = conn.cursor(dictionary=True)
        c.execute(
            "INSERT INTO jobs (job_title, job_location, job_link, user_id) VALUES (%s, %s, %s, %s)",
            (job_title, job_location, job_link, session['user_id']),
        )
        conn.commit()
        conn.close()

        return redirect(url_for("jobs.view_jobs"))

    return render_template("jobs_form.html", job={})


@jobs_bp.route("/jobs/edit/<int:job_id>", methods=["GET", "POST"])
def edit_job(job_id):
    if 'username' not in session:
        return redirect('/login')
    conn = get_db_connection()
    c = conn.cursor(dictionary=True)

    if request.method == "POST":
        job_title = request.form["job_title"]
        job_location = request.form["job_location"]
        job_link = request.form["job_link"]

        print("OK")
        c.execute(
            "UPDATE jobs SET job_title = %s, job_location = %s, job_link = %s WHERE id = %s",
            (job_title, job_location, job_link, job_id),
        )
        conn.commit()
        conn.close()

        return redirect(url_for("jobs.view_jobs"))

    c.execute("SELECT * FROM jobs WHERE id = %s", (job_id,))
    job = c.fetchone()

    return render_template("jobs_form.html", job=job)


@jobs_bp.route("/jobs/delete/<int:job_id>", methods=["POST"])
def delete_job(job_id):
    if 'username' not in session:
        return redirect('/login')
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("DELETE FROM jobs WHERE id = %s", (job_id,))
    conn.commit()
    conn.close()

    return redirect(url_for("jobs.view_jobs"))


@jobs_bp.route("/jobs/update_status/<int:job_id>", methods=["POST"])
def update_job_status(job_id):
    if 'username' not in session:
        return redirect('/login')
    new_status = request.json["new_status_id"]

    conn = get_db_connection()
    c = conn.cursor()
    c.execute("UPDATE jobs SET job_status_id = %s WHERE id = %s", (new_status, job_id))
    conn.commit()
    conn.close()

    return jsonify({'status': 'success', 'message': 'Job status updated'}), 200
