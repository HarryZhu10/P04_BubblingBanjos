import sqlite3, csv, sqlalchemy, gdown #gdown for downloading big google drive files
import pandas as pd

from collections import OrderedDict
from ast import literal_eval

DB_FILE = "data.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()


def db_connect():
    return db.cursor()

def db_close():
    db.commit()
    db.close()

def getData(tablename):
    data = c.execute("SELECT * FROM " + tablename).fetchall()
    db_close()
    return data

def geodata_to_dict():
    rows = c.execute("SELECT properties, geometry from geo_info").fetchall()
    geodict = OrderedDict()
    geodict['type'] = 'FeatureCollection'
    geodict['features'] = []
    for row in rows:
        feature_dict = OrderedDict()
        feature_dict['type'] = 'feature'
        feature_dict['properties'] = literal_eval(row[0])
        feature_dict['geometry'] = literal_eval(row[1])
        geodict['features'].append(feature_dict)
    db_close()
    return geodict