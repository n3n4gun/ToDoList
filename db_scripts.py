CREATE_TABLE_SCRIPT_TASKS = '''CREATE TABLE IF NOT EXISTS tasks (
                task_id TEXT,
                name TEXT,
                description TEXT,
                terms TEXT,
                priority TEXT
                )'''

CREATE_TABLE_SCRIPT_USERS = '''CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                name TEXT,
                second_name TEXT,
                email TEXT,
                login TEXT,
                password TEXT
                )'''

ADD_TASK_SCRIPT = ""

ADD_USER_SCRIPT = "INSERT INTO users (user_id, name, second_name, email, login, password) VALUES (?, ?, ?, ?, ?, ?)"

#SELECT_USER_INFO = "SELECT login FROM users WHERE name=?"
SELECT_USER_INFO = "SELECT * FROM users WHERE name=?"