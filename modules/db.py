import sqlite3
from sqlite3 import Error


class DBConnection:
    def __init__(self, file):
        self.connection = sqlite3.connect(file)
        self.filename = file


    def commit(self):
        self.connection.commit()


    def insert(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.commit()
        return cursor.lastrowid

    def selectall(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def selectone(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchone()


    def close(self):
        self.connection.close()



def connect(file):
    try :
        return sqlite3.connect(file)
    except Error:
        return None




# Method to call to setup the database (add needed tables)
def setup(conn):
    query = """
    CREATE TABLE `shows` (
        `id` integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        `name` VARCHAR(128) NOT NULL,
        `description` TEXT NOT NULL,
        `date` DATETIME NOT NULL
    );
    """
    conn.execute(query)


def close(conn):
    conn.close()


if __name__ == '__main__':
    conn = connect('db')
    setup(conn)
