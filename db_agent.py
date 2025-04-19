import sqlite3

from config import configurations
from db_scripts import CREATE_DB_SCRIPT

class Agent:
    def __init__(self, db_name : str):
        self.db_name = db_name

    def db_connection(self):
        try:
            self.db_conn = sqlite3.connect(self.db_name)
            print('Connection was installed!')
            return self.db_conn
        
        except sqlite3.DatabaseError as sqlite_error:
            return sqlite_error

    def create_table(self):
        try:
            self.db_conn = self.db_connection()
            self.db_cursor = self.db_conn.cursor()
            self.db_cursor.execute(CREATE_DB_SCRIPT)
        except sqlite3.DatabaseError as sqlite_error:
            return sqlite_error
        else:
            print('Table was created!')
            self.db_conn.close()

    def add_task(self):
        pass

db_agent = Agent(configurations['DB_NAME'])
db_agent.create_table()
