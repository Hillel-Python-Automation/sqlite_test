import sqlite3
import pytest
import os


@pytest.fixture
def cursor():
    conn = sqlite3.connect('testdb.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE movie(title, year, score)")
    yield cur
    conn.close()
    os.remove("testdb.db")

