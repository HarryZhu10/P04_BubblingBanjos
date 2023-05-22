import sqlite3 #gdown for downloading big google drive
import pandas as pd

from collections import OrderedDict
from ast import literal_eval

DB_FILE = "data.db"

db = sqlite3.connect(DB_FILE, check_same_thread = False)
c = db.cursor()


def db_connect():
    return db.cursor()

def db_close():
    db.commit()
    db.close()

def getData(tablename):
    c = db_connect()
    data = c.execute("SELECT * FROM " + tablename).fetchall()
    return data

def geodata_to_dict():
    c = db_connect()
    rows = c.execute("SELECT id, properties, geometry FROM geo_info").fetchall()
    geodict = OrderedDict()
    geodict['type'] = 'FeatureCollection'
    geodict['features'] = []
    for row in rows:
        feature_dict = OrderedDict()
        feature_dict['type'] = 'Feature'
        feature_dict['id'] = str(row[0])
        feature_dict['properties'] = literal_eval(row[1])
        feature_dict['geometry'] = literal_eval(row[2])
        geodict['features'].append(feature_dict)
    return geodict