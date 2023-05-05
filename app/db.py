import sqlite3, csv, pandas, sqlalchemy

DB_FILE = "data.db"

db = None

# cdf = pd.read_csv()
# sdf = pd.read_csv()
# adf = pd.read_csv()
# ddf = pd.read_csv()

def db_connect():
    global db
    db = sqlite3.connect(DB_FILE)
    return db.cursor()

def db_close():
    db.commit()
    db.close()

db_fill_tables()

def db_init_tables():
    c = db_connect(DB_FILE)
    # Can change table laters based on need
    c.execute("CREATE TABLE IF NOT EXISTS collisions (date text, borough text, latitude real, longitude real, numkilled integer, numinjured integer)")
    c.execute("CREATE TABLE IF NOT EXISTS shootings (date text, borough text, latitude real, longitude real, perpsex text, perprace text, victsex text, victrace text)")
    c.execute("CREATE TABLE IF NOT EXISTS arrests (date text, borough text, latitude real, longitude real, ofnsdisc text, ofnslevel text)")
    c.execute("CREATE TABLE IF NOT EXISTS demographics ()")
    db_close()