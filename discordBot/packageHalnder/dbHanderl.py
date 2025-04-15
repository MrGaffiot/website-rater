import sqlite3
from contextlib import contextmanager

@contextmanager
def get_db():
    con = sqlite3.connect('discordBot/data.db')
    cur = con.cursor()
    try:
        yield cur
    finally:
        con.commit()
        con.close()

class databaseHandler:
    def __init__(self):
        self.con = sqlite3.connect('discordBot/data.db')
        self.cur = self.con.cursor()

    def __enter__(self):
        self.con = sqlite3.connect('discordBot/data.db')
        self.cur = self.con.cursor()
        self.con.commit()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.con is not None:
            self.con.close()

    def addEntry(self, url: str, imagePath: str, quality: str):
        print(url, imagePath, quality)
        if self.cur is not None:
            self.cur.execute("INSERT INTO websites (url, image, quality) VALUES (?, ?, ?)", (url, imagePath, quality))
            self.con.commit()

    def removeUser(self, id: int):
        if self.cur is not None:
            self.cur.execute("DELETE FROM websites WHERE id = ?", (id,))
            self.con.commit()

    def readData(self):
        if self.cur is not None:
            self.cur.execute("SELECT * FROM websites")
            return self.cur.fetchall()
    
    def makeTable(self):
        if self.cur is not None:
            self.cur.execute("CREATE TABLE websites (id INTEGER PRIMARY KEY AUTOINCREMENT, url TEXT, image TEXT, quality TEXT)")
            self.con.commit()

if __name__ == '__main__':
    with databaseHandler() as db:
        print(db.readData())