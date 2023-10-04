import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

#connection
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

#SQL
#cria a tabela
cursor.execute(
    f'CREATE TABLE  IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT, '
    'weight REAL'
    ')'
)
connection.commit()

#delete
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

#registra valores
#risco de sqlinjection
sql = (
    f'INSERT INTO {TABLE_NAME} (name, weight)'
    ' VALUES'
    '(?, ?)'
)
cursor.execute(sql, ['joana', 4])
cursor.executemany(sql, [['luiz', 5], ['jonas', 15]])
connection.commit()

cursor.execute(
    f'DELETE FROM {TABLE_NAME} '
    'WHERE id = "3"'
)
connection.commit()

cursor.execute(
    f'UPDATE {TABLE_NAME} '
    'SET name = "Zeca", weight = 77.89 '
    'WHERE id = 2'
)


connection.commit()

cursor.execute(
    f'SELECT * from {TABLE_NAME}'    
)
for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)




#desconnection
cursor.close()
connection.close()
