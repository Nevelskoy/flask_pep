from flask import Flask
from flask import render_template


app = Flask(__name__)

users = ['mike', 'mishel', 'adel', 'keks', 'kamila']

'''
@app.errorhandler(404)
def not_found():
    return 'Page not found', 404
'''

@app.route('/')
def hello_world():
    return 'Welcome to Flask from Hexlet!'


@app.route('/users/')
def get_users():
    return render_template(
        '/users/index.html',
        users=users
    )


@app.route('/courses/<id>')
def courses(id):
    return f'Course id: {id}'

    