import sqlite3

from config import configurations
from werkzeug.security import generate_password_hash, check_password_hash
from db_scripts import *

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
            self.db_cursor.execute(CREATE_TABLE_SCRIPT_TASKS)
        except sqlite3.DatabaseError as sqlite_error:
            return sqlite_error
        else:
            print('# Table was created!')
            self.db_conn.close()

    def create_table_users(self):
        try:
            self.db_conn, self.db_cursor = self.db_connection()
            self.db_cursor.execute(CREATE_TABLE_SCRIPT_USERS)
        except sqlite3.DatabaseError as sqlite_error:
            return sqlite_error
        else:
            print('# Table was created!')
            self.db_conn.close()

    def add_task(self):
        pass

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

    def select_user(self, name : str):
        try:
            self.db_conn, self.db_cursor = self.db_connection()
        except:
            pass
        else:
            try:
                self.db_cursor.execute(SELECT_USER_INFO, (name,))
                return self.db_cursor.fetchall()[0]
            except IndexError as index_error:
                return 1

#db_agent = Agent(configurations['TODO_DB'])
#db_agent.create_table_users()
#db_agent.add_user('1', 'Fedor', 'Me', 'admin@mail.com', 'admin', '12345')
#print(db_agent.select_user('Fedor'))
