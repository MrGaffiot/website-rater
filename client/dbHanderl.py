import sqlite3
from contextlib import contextmanager

@contextmanager
def get_db():
    con = sqlite3.connect('files\\data.db')
    cur = con.cursor()
    try:
        yield cur
    finally:
        con.commit()
        con.close()

class databaseHandler:
    def __init__(self):
        self.cur = None
        self.con = None

    def __enter__(self):
        self.con = sqlite3.connect('savesF\\data.db')
        self.cur = self.con.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS websites (id INTEGER PRIMARY KEY AUTOINCREMENT, url TEXT, image TEXT, score INTEGER, misc TEXT)')
        self.con.commit()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.con is not None:
            self.con.close()

    def addEntry(self, name: str, email: str, phone_number: str, question: str):
        print(name, email, phone_number, question)
        if self.cur is not None:
            self.cur.execute("INSERT INTO websites (url, image, score, misc) VALUES (?, ?, ?, ?)", ())
            self.con.commit()

    def removeEbtr(self, id: int):
        if self.cur is not None:
            self.cur.execute("DELETE FROM users WHERE id = ?", (id,))

    def readData(self):
        if self.cur is not None:
            self.cur.execute("SELECT * FROM websites")
            return self.cur.fetchall()

if __name__ == '__main__':
    with databaseHandler() as db:
        print(db.readData())