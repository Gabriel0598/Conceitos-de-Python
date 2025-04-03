import sqlite3
from contextlib import contextmanager

default_path = "C:/Users/Proprietario/AppData/Roaming/JetBrains/PyCharmCE2023.3/scratches"
path_file = f"{default_path}/scratch.txt"
file_writing = f"{default_path}/statement.txt"

file = open(path_file, "r")
try:
    content = file.read()
    print(content)
finally:
    file.close()

with open(path_file, "r") as file:
    content = file.read()
    print(content)

with open(file_writing, "w") as file:
    file.write("Hello, Pyhton with statement!")

with open(file_writing, "r") as file:
    content = file.read()
    print(content)

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

# using the custom context manager
with FileManager(file_writing, 'w') as file:
    file.write('Hello, World!')

# read result
with open(file_writing, "r") as file:
    content = file.read()
    print(content)

@contextmanager
def open_file(filename, mode):
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()

# using the generator-based context manager
with open_file(file_writing, "w") as file:
    file.write("Hello, World 2")

# read result
with open(file_writing, "r") as file:
    content = file.read()
    print(content)

# sqlite config
db_name = "example.db"
columns = ["name", "type", "name"]
table = "sqlite_master"

with sqlite3.connect(db_name) as conn:
    cursor = conn.cursor()
    cursor.execute(f"SELECT {columns[0]} FROM {table} WHERE {columns[1]}='table' AND {columns[2]} = 'users' ")
    res = cursor.fetchone()
    print("Table created successfully!" if res else "Table not found.")