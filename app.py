from flask import Flask
from config import configurations
from flask import render_template

main_app = Flask(__name__)
main_app.config['SECRET_KEY'] = configurations['SECRET_KEY']

@main_app.route('/')
@main_app.route('/index')
def index():
    return render_template('index.html')

@main_app.route('/add_task', methods = ['GET', 'POST'])
def add_task():
    return render_template('task.html', title = 'Создание задачи')