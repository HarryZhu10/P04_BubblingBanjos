import sqlite3, csv, sqlalchemy
import pandas as pd

DB_FILE = "data.db"

db = None

curl = 'https://drive.google.com/file/d/1DXS_eqGG3AbR1IrdOcWiXc_qPTEbGFHf/view?usp=sharing'
surl = 'https://drive.google.com/file/d/1EJRFulkdL0sKhH2py9YVXH6gfdvNN_6Q/view?usp=sharing'
aurl = 'https://drive.google.com/file/d/1HtKO8nK2daRjJm1U50pyUZt_SF0cFmQj/view?usp=sharing'
durl = 'https://drive.google.com/file/d/1sGjh289FyxkBNQ-wdruaxxN0k1WTp2xg/view?usp=sharing'
curl = 'https://drive.google.com/uc?id=' + curl.split('/')[-2]
surl = 'https://drive.google.com/uc?id=' + surl.split('/')[-2]
aurl = 'https://drive.google.com/uc?id=' + aurl.split('/')[-2]
durl = 'https://drive.google.com/uc?id=' + durl.split('/')[-2]

# cdf = pd.read_csv(curl, usecols=["CRASH DATE", "CRASH TIME", "ZIP CODE", "LATITUDE", "LONGITUDE", "NUMBER OF PERSONS INJURED", "NUMBER OF PERSONS KILLED"])
# sdf = pd.read_csv(surl, usecols=[])
# adf = pd.read_csv(aurl, usecols=[])
ddf = pd.read_csv(durl, usecols=['Zip Code', 'Female Count', 'Female Percentage', 'Male Count', 'Male Percentage'])

# def db_connect():
#     global db
#     db = sqlite3.connect(DB_FILE)
#     return db.cursor()

# def db_close():
#     db.commit()
#     db.close()

# db_fill_tables()

# def db_init_tables():
#     c = db_connect(DB_FILE)
    # Can change table laters based on need
#     c.execute("CREATE TABLE IF NOT EXISTS collisions (date text, borough text, latitude real, longitude real, numkilled integer, numinjured integer)")
#     c.execute("CREATE TABLE IF NOT EXISTS shootings (date text, borough text, latitude real, longitude real, perpsex text, perprace text, victsex text, victrace text)")
#     c.execute("CREATE TABLE IF NOT EXISTS arrests (date text, borough text, latitude real, longitude real, ofnsdisc text, ofnslevel text)")
#     c.execute("CREATE TABLE IF NOT EXISTS demographics ()")
#     db_close()/