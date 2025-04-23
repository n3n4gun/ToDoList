import sqlite3

from config import configurations
from werkzeug.security import generate_password_hash, check_password_hash
from db_scripts import CREATE_DB_SCRIPT_TASKS, CREATE_DB_SCRIPT_USERS, ADD_USER_SCRIPT

class Agent:
    def __init__(self, db_name : str):
        self.db_name = db_name

    def db_connection(self):
        try:
            self.db_conn = sqlite3.connect(self.db_name)
            print(f'# Connection with {self.db_name} was installed!')
        except sqlite3.DatabaseError as sqlite_error:
            return sqlite_error
        else:
            return self.db_conn

    def create_table_tasks(self):
        try:
            self.db_conn = self.db_connection()
            self.db_cursor = self.db_conn.cursor()
            self.db_cursor.execute(CREATE_DB_SCRIPT_TASKS)
        except sqlite3.DatabaseError as sqlite_error:
            return sqlite_error
        else:
            print('Table was created!')
            self.db_conn.close()

    def create_table_users(self):
        try:
            self.db_conn = self.db_connection()
            self.db_cursor = self.db_conn.cursor()
            self.db_cursor.execute(CREATE_DB_SCRIPT_USERS)
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
            self.db_user_conn = self.db_connection()
            self.db_user_cursor = self.db_user_conn.cursor()
        except sqlite3.DatabaseError as sqlite_error:
            return sqlite_error
        else:
            self.db_user_cursor.execute(ADD_USER_SCRIPT, self.user)
            print('# User was added!')
            self.db_conn.commit()

db_agent = Agent(configurations['DB_USERS'])
#db_agent.create_table_users()
#db_agent.add_user('1', 'Fedor', 'Naboyshchikov', 'admin@mail.com', 'admin', '12345')
