import uuid

from flask import Flask
from flask import render_template, request, session, redirect, url_for
from config import configurations
from db_agent import Agent

main_app = Flask(__name__)
main_app.config['SECRET_KEY'] = configurations['SECRET_KEY']

@main_app.route('/')
@main_app.route('/login', methods = ['GET', 'POST'])
def login():
    if 'userLogged' in session:
        return redirect(url_for('user_page', user_name = session['userLogged']))
    
    elif request.form.get('user_name') == 'admin' and request.form.get('password') == '12345':
        session['userLogged'] = request.form.get('user_name')
        return redirect(url_for('user_page', user_name = session['userLogged']))

    return render_template('login.html', title = 'Авторизация')

@main_app.route('/registration', methods = ['GET', 'POST'])
def registration():
    if request.method == 'GET':
        return render_template('registration.html')
    elif request.method == 'POST':
        if request.form.get('password') == request.form.get('confirm_password'):
            try:
                agent_db = Agent(configurations['TODO_DB'])
                user_id = str(uuid.uuid4().hex)
            except:
                pass
            else:
                agent_db.add_user(user_id, request.form.get('first_name'), request.form.get('last_name'), request.form.get('email'), request.form.get('username'), str(request.form.get('password')))
        return render_template('registration.html')

@main_app.route('/user/<user_name>')
def user_page(user_name : str = None):
    print(session)
    return render_template('user_page.html', user_name = user_name)

@main_app.route('/user/add_task', methods = ['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        pass
    return render_template('task.html', user_name = session['userLogged'])
