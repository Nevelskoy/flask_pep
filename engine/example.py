from flask import Flask, request
from flask import render_template
import re


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

    term = request.args.get('term')
  #  filtered_courses = # filter courses by term

    if term is None:
        return render_template(
            '/users/index.html',
            users=users
        )

    filtred = [x for x in users if re.search(term, x)]
    
    return render_template(
            '/users/index.html',
            users=filtred,
            search=term,
        )


@app.route('/courses/<id>')
def courses(id):
    return f'Course id: {id}'

    