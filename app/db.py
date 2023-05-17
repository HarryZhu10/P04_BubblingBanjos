import sqlite3, csv, sqlalchemy, gdown #gdown for downloading big google drive files
import pandas as pd

DB_FILE = "data.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()


def db_connect():
    return db.cursor()

def db_close():
    db.commit()
    db.close()

def getData(tablename):
    data = c.
    return data