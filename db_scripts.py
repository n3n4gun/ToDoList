CREATE_TABLE_SCRIPT_TASKS = '''CREATE TABLE IF NOT EXISTS tasks (
                task_id TEXT,
                user_id TEXT,
                name TEXT,
                description TEXT,
                terms TEXT,
                priority TEXT,
                added INT
                )'''

CREATE_TABLE_SCRIPT_USERS = '''CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                name TEXT,
                second_name TEXT,
                email TEXT,
                login TEXT,
                password TEXT
                )'''

ADD_TASK_SCRIPT = "INSERT INTO tasks (task_id, user_id, name, description, terms, priority, added) VALUES (?, ?, ?, ?, ?, ?, ?)"

ADD_USER_SCRIPT = "INSERT INTO users (user_id, name, second_name, email, login, password) VALUES (?, ?, ?, ?, ?, ?)"

SELECT_USER_INFO = "SELECT name, user_id FROM users WHERE login=?"

CHECK_USER_PASSWORD = "SELECT password FROM users WHERE login=?"

SELECT_USER_TASKS = "SELECT name, description, terms, priority FROM tasks WHERE user_id=? ORDER BY added DESC"

DELET_USER_TASK = "DELET FROM tasks WHERE task_id=?"