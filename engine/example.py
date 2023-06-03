from flask import Flask, request, render_template, redirect
import json
import re


app = Flask(__name__)

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
         curr_db = db_users['persons']       
         for user in curr_db:
           nicknames.append(user['nickname'])

    term = request.args.get('term')
    if term:
        filtred = [x for x in nicknames if re.search(term, x)]
        return render_template(
            '/users/index.html',
            users=filtred
        )

    return render_template(
            '/users/index.html',
            users=nicknames,
            search=term,
        )


@app.route('/users/new')
def users_new():
    user = {'nickname': '',
            'email ': '',
            'city': ''}

    return render_template(
        '/users/new.html',
        user=user,
    )


@app.post('/users/')
def users_post():
    user_add = request.form.to_dict()

    nicknames = []
    with open("db/users.json", 'r') as rf:
        db_users = json.load(rf)
        print(db_users)
        curr_db = db_users['persons']       
        for user in curr_db:
           nicknames.append(user)
        nicknames.append(user_add)
        db_users['persons'] = nicknames
        print(db_users)

    write_to_json("db/users.json", db_users)

    return redirect('/users', code=302)


@app.route('/courses/<id>')
def courses(id):
    return f'Course id: {id}'

def write_to_json(path, data):
    with open(path, 'w') as rf:
        json.dump(data, rf)

    