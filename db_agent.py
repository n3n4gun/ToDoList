import sqlite3
import math
import time

from config import configurations
from werkzeug.security import generate_password_hash, check_password_hash
from db_scripts import *
from datetime import datetime

class Agent:
    def __init__(self, db_name : str):
        self.db_name = db_name

    def db_connection(self):
        try:
            self.db_conn = sqlite3.connect(self.db_name)
            self.db_cursor = self.db_conn.cursor()
            print(f'# Connection with {self.db_name} was installed!')
        except sqlite3.DatabaseError as sqlite_error:
            return sqlite_error
        else:
            return self.db_conn, self.db_cursor

    def create_table_tasks(self):
        try:
            self.db_conn, self.db_cursor = self.db_connection()
        except sqlite3.DatabaseError as sqlite_error:
            return sqlite_error
        else:
            self.db_cursor.execute(CREATE_TABLE_SCRIPT_TASKS)
            print('# Table was created!')
            self.db_conn.close()

    def create_table_users(self):
        try:
            self.db_conn, self.db_cursor = self.db_connection()
            self.db_cursor.execute(CREATE_TABLE_SCRIPT_USERS)
        except sqlite3.DatabaseError as sqlite_error:
            return sqlite_error
        else:
            self.db_cursor.execute(CREATE_TABLE_SCRIPT_USERS)
            print('# Table was created!')
            self.db_conn.close()

    def add_task(self, task_id: str, user_id: str, name: str, description: str, terms: datetime, priority: str):
        self.task_id = task_id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.terms = datetime.strptime(terms, '%Y-%m-%d').strftime('%d.%m.%Y')
        self.priority = priority
        self.added = math.floor(time.time())
        self.task = (self.task_id, self.user_id, self.name, self.description, self.terms, self.priority, self.added)
        try:
            self.db_conn, self.db_cursor = self.db_connection()
        except sqlite3.DatabaseError as sqlite_error:
            return sqlite_error
        else:
            self.db_cursor.execute(ADD_TASK_SCRIPT, self.task)
            print('# Task was added!')
            self.db_conn.commit()

    def delete_task(self, task_id: str) -> bool:
        self.task_id = task_id
        

    def add_user(self, user_id : str, name : str, second_name : str, email : str, login : str, password : str):
        self.user_id = user_id
        self.name = name
        self.second_name = second_name
        self.email = email
        self.login = login
        self.password = str(generate_password_hash(password))
        self.user = (self.user_id, self.name, self.second_name, self.email, self.login, self.password)
        try:
            self.db_conn, self.db_cursor = self.db_connection()
        except sqlite3.DatabaseError as sqlite_error:
            return sqlite_error
        else:
            self.db_cursor.execute(ADD_USER_SCRIPT, self.user)
            print('# User was added!')
            self.db_conn.commit()

    def select_user(self, login : str) -> tuple:
        self.login = login
        try:
            self.db_conn, self.db_cursor = self.db_connection()
        except sqlite3.DatabaseError as sqlite_error:
            return sqlite_error
        else:
            try:
                self.db_cursor.execute(SELECT_USER_INFO, (self.login,))
                return self.db_cursor.fetchall()[0]
            except IndexError as index_error:
                return '# User wasn\'t found!'
        
    def login_user(self, login : str, password : str) -> bool:
        self.login = login
        self.password = password
        try:
            self.db_conn, self.db_cursor = self.db_connection()
        except sqlite3.DatabaseError as sqlit_error:
            return sqlit_error
        else:
            db_user_password = self.db_cursor.execute(CHECK_USER_PASSWORD, (self.login,)).fetchall()[0][0]
            if check_password_hash(db_user_password, self.password):
                return True
            else:
                return False
            
    def select_user_tasks(self, user_id: str) -> list:
        self.user_id = user_id
        try:
            self.db_conn, self.db_cursor = self.db_connection()
            #self.db_conn.row_factory = sqlite3.Row
        except:
            pass
        else:
            user_tasks = self.db_cursor.execute(SELECT_USER_TASKS, (self.user_id,)).fetchall()
            if user_tasks: return user_tasks
        return []
            
#date = datetime(2025, 5, 7).strftime('%d.%m.%Y')
#db_agent = Agent(configurations['TODO_DB'])
#print(db_agent.select_user('admin'))
#response = db_agent.select_user_tasks('e33058542c5848e4b660426bb64c2e4d')
#print(response)
#db_agent.add_task('1', 'djfhskjdfh3487', 'Купить хлеб', 'Надо к 9 мая купить свежий хлеб', date, '0')
#db_agent.create_table_tasks()
#db_agent.add_user('1', 'Fedor', 'Me', 'admin@mail.com', 'admin', '12345')
#_, id = db_agent.select_user('admin')
#print(id)
#if db_agent.login_user('admin', '12345'):
#    print('пользователь авторизован')
#else:
#    print('пользователь не авторизован')