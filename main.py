import sqlite3
from sqlite3 import Error


def create_connection_to_DB(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as error:
        print(f"The error '{error}' occurred")

    return conn


def create_parents_table(conn):
    try:
        with conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS Parents(
                       uuid uuid PRIMARY KEY,
                       name TEXT NOT NULL,
                       age INT NOT NULL)
                    """)
            print("Creating Parents table successful")
    except Error as error:
        print(f"The error '{error}' occurred")


def adding_parents_to_DB(conn):
    try:
        with conn:
            if not conn.execute("SELECT uuid FROM Parents WHERE uuid = 1;").fetchall():
                conn.execute("""INSERT INTO Parents VALUES(
                            1,
                            'Юля', 
                            41);""")
                print("Adding to Parents table successful")
            if not conn.execute("SELECT uuid FROM Parents WHERE uuid = 2").fetchall():
                conn.execute("""INSERT INTO Parents VALUES(
                            2,
                            'Миша', 
                            44)""")
                print("Adding to Parents table successful")
    except Error as error:
        print(f"The error '{error}' occurred")


def delete_table(conn, name_table):
    try:
        with conn:
            conn.execute(f"DROP TABLE {name_table}")
            print("Deletion table successful")
    except Error as error:
        print(f"The error '{error}' occurred")


if __name__ == '__main__':
    connection = create_connection_to_DB('my_family.db')

    create_parents_table(connection)

    adding_parents_to_DB(connection)


