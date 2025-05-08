import uuid

from flask import Flask
from flask import render_template, request, session, redirect, url_for, flash
from config import configurations
from db_agent import Agent
from datetime import datetime

main_app = Flask(__name__)
main_app.config['SECRET_KEY'] = configurations['SECRET_KEY']

@main_app.route('/')
@main_app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
            return render_template('login.html', title = 'Авторизация')
    elif request.method == 'POST':
        if 'user_login' in session:
            return redirect(url_for('user_page', user_name = session.get('user_name')))
        else:
            agent_db = Agent(configurations['TODO_DB'])
            try:
                if agent_db.login_user(request.form.get('user_name'), request.form.get('password')):
                    user_name, user_id = agent_db.select_user(request.form.get('user_name'))
                    session['user_login'], session['user_id'], session['user_name'] = request.form.get('user_name'), user_id, user_name
                else:
                    flash('Ошибка авторизации!')
                    print({'Login status' : False})
                    return render_template('login.html', title = 'Авторизация')
            except:
                return render_template('login.html', title = 'Авторизация')
            else:
                print(session)
                return redirect(url_for('user_page', user_name = session.get('user_name')))

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
                flash('Регистрация прошла успешно!')
        return render_template('registration.html')

@main_app.route('/user/<user_name>')
def user_page(user_name : str = None):
    agent_db = Agent(configurations['TODO_DB'])
    try:
        user_tasks = agent_db.select_user_tasks(session.get('user_id'))
    except:
        pass
    else:
        return render_template('user_page.html', user_name = user_name, user_tasks = user_tasks)

@main_app.route('/user/add_task', methods = ['GET', 'POST'])
def add_task():
    if request.method == 'GET':
        return render_template('task.html', user_name = session.get('user_name'))
    elif request.method == 'POST':
        try:
            agent_db = Agent(configurations['TODO_DB'])
            task_id = str(uuid.uuid4().hex)
        except:
            pass
        else:
            agent_db.add_task(task_id, session.get('user_id'), request.form.get('title'), request.form.get('description'), request.form.get('dueDate'), request.form.get('priority'))
            flash('Задача успешно была добавлена!')
    return render_template('task.html', user_name = session.get('user_name'))

@main_app.route('/logout', methods = ['POST'])
def logout():
    session.clear() # clear session
    return redirect(url_for('login'))

if __name__ == '__main__':
    main_app.run(host = 'localhost', port = 5000, debug = True)