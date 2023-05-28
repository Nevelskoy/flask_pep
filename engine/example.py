from flask import Flask, request, render_template, redirect
import json
import re


app = Flask(__name__)

#users = ['mike', 'mishel', 'adel', 'keks', 'kamila']

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

    nicknames = []
    with open("db/users.json", 'r') as rf:
         db_users = json.load(rf)
         for user in db_users:
           nicknames.append(db_users[user]['nickname'])

    term = request.args.get('term')
  #  filtered_courses = # filter courses by term

    # if term is None:
    #     return render_template(
    #         '/users/index.html',
    #         users=users
    #     )

    # filtred = [x for x in users if re.search(term, x)]


    return render_template(
            '/users/index.html',
            users=nicknames,
            search=term,
        )


@app.post('/users')
def users_post():
    repo = users
    user = request.form.to_dict()
    # errors = validate(user)
    # if errors:
    #     return render_template(
    #       'users/new.html',
    #       user=user,
    #       errors=errors,
    #     )
    repo.append(user)
    return redirect('/users', code=302)

    
@app.route('/users/new')
def users_new():
    user = {'nickname': '',
            'email ': ''}

    return render_template(
        '/users/new.html',
        user=user,
    )


@app.route('/courses/<id>')
def courses(id):
    return f'Course id: {id}'

    