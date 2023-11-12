import sqlite3
from contextlib import contextmanager


db_file = './university.db'


@contextmanager
def create_connection():
    """ create a database connection to a SQLite database """
    conn = sqlite3.connect(db_file)
    yield conn
    conn.rollback()
    conn.close()