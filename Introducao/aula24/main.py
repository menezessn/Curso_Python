import pymysql
import dotenv
import os

TABLE_NAME = 'customers'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4'
)

with connection:
    with connection.cursor() as cursor:

        cursor.execute(
            'CREATE TABLE IF NOT EXISTS customers ('
            'id INT NOT NULL AUTO_INCREMENT,'
            'nome VARCHAR(50) NOT NULL ,'
            'idade INT NOT NULL ,'
            'PRIMARY KEY(id)'
            ')'
        )
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
        connection.commit()
        print(cursor)
        with connection.cursor() as cursor:
            sql = (
                f'INSERT INTO {TABLE_NAME} '
                '(nome, idade) '
                'VALUES '
                '(%s, %s)'
            )
            data = ('Luiz', 18)
            result = cursor.execute(sql, data)
            print(result)
            connection.commit()
            with connection.cursor() as cursor:
                sql = (
                    f'INSERT INTO {TABLE_NAME} '
                    '(nome, idade) '
                    'VALUES '
                    '(%(nome)s, %(idade)s)'
                )
                data2 = {
                    "nome": 'Le',
                    "idade": 27
                }
                result = cursor.execute(sql, data2)
                print(result)
                connection.commit()
            with connection.cursor() as cursor:
                sql = (
                    f'INSERT INTO {TABLE_NAME} '
                    '(nome, idade) '
                    'VALUES '
                    '(%(nome)s, %(idade)s)'
                )
                data3 = {
                    "nome": 'zeca',
                    "idade": 19
                }
                data4 = {
                    "nome": 'Arnaldo',
                    "idade": 21
                }
                result = cursor.executemany(sql, (data3, data4))
                print(result)
                connection.commit()