import sqlite3
from pathlib import Path
from main import DB_FILE, TABLE_NAME

#connection
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
    'WHERE id = "3"'
)
row = cursor.fetchone()
_id, name, weight = row
print(_id, name, weight)
# for row in cursor.fetchall():
#     _id, name, weight = row
#     print(_id, name, weight )

#desconnection
cursor.close()
connection.close()
