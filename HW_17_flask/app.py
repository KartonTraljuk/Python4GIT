""" This is very low skill website of school
"""

from flask import render_template
from settings import app
from settings import db
from models import Students
from models import Teachers
from settings import HOST
from settings import PORT
from settings import DEBUG

menu = [
    {"name": "Information", "url": "information"},
    {"name": "Students", "url": "students"},
    {"name": "Teachers", "url": "teachers"},
    {"name": "Feedback", "url": "feedback"},
    {"name": "About", "url": "about"},
]


@app.route('/')
def index():
    return render_template('index.html', title='School', menu=menu)


@app.route('/information')
def get_information():
    return render_template('information.html', title='Information')


@app.route('/students')
def students():
    list_students = []
    try:
        list_students = Students.query.all()

    except:
        print("error reading from the database")

    return render_template(
        "students.html", title="Students", list=list_students
    )


@app.route('/teachers')
def teachers():
    list_teachers = []
    try:
        list_teachers = Teachers.query.all()
    except:
        print("error reading from the database")

    return render_template(
        "teachers.html", title="Teachers", list=list_teachers
    )


@app.route('/feedback')
def write_to_us():
    return render_template('about.html', title='Feedback')


@app.errorhandler(404)
def not_found(error):
    return render_template('page404.html')


if __name__ == '__main__':
    app.app_context().push()
    db.create_all()
    app.run(HOST, PORT, DEBUG)
