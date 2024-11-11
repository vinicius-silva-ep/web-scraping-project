import psycopg2
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD


base_path = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_path, "db")


def read_sql_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


verify_schema = os.path.join(db_path, "verify_schema.sql")
create_schema = os.path.join(db_path, "create_schema.sql")
verify_table = os.path.join(db_path, "verify_table.sql")
create_table = os.path.join(db_path, "create_table.sql")


def db_operations():
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
        )

        print("Connection to the database successfully established!")
        cursor = connection.cursor()

        cursor.execute(read_sql_file(verify_schema))
        if not cursor.fetchone():
            cursor.execute(read_sql_file(create_schema))
            connection.commit()
            print("Schema 'violins' created successfully.")

        cursor.execute(read_sql_file(verify_table))
        if not cursor.fetchone()[0]:
            cursor.execute(read_sql_file(create_table))
            connection.commit()
            print("Table 'violins_data' created successfully.")

        cursor.close()
        connection.close()

    except Exception as e:
        print(f"Error connecting to database: {e}")
