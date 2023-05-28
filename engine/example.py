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


# @app.post('/users/')
# def users_post():
#     user = request.form.to_dict()
#     print(user)

#     with open("db/users.json", 'r') as rf:
#         db_users = json.load(rf)
#         id = len(db_users)
#         db_users.append(user)
    
#     with open("db/users.json", 'w', encoding='utf8') as outfile: #Открываем файл для записи
#         json.dump(db_users, outfile, ensure_ascii=False, indent=2)
#     # errors = validate(user)
#     # if errors:
#     #     return render_template(
#     #       'users/new.html',
#     #       user=user,
#     #       errors=errors,
#     #     )

#     return redirect('/users', code=302)


@app.route('/courses/<id>')
def courses(id):
    return f'Course id: {id}'

    