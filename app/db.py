import sqlite3, csv, sqlalchemy, gdown #gdown for downloading big google drive files
import pandas as pd

DB_FILE = "data.db"

db = None

# Collision and arrest data is obtained separately because they're too big
surl = 'https://drive.google.com/file/d/1EJRFulkdL0sKhH2py9YVXH6gfdvNN_6Q/view?usp=sharing'
durl = 'https://drive.google.com/file/d/1sGjh289FyxkBNQ-wdruaxxN0k1WTp2xg/view?usp=sharing'
surl = 'https://drive.google.com/uc?id=' + surl.split('/')[-2]
durl = 'https://drive.google.com/uc?id=' + durl.split('/')[-2]

cdf = pd.read_csv('Motor_Vehicle_Collisions_-_Crashes.csv', usecols=["CRASH DATE", "CRASH TIME", "ZIP CODE", "LATITUDE", "LONGITUDE", "NUMBER OF PERSONS INJURED", "NUMBER OF PERSONS KILLED"], low_memory = False)

sdf = pd.read_csv(surl, usecols=['OCCUR_DATE', 'Latitude', 'Longitude', 'PERP_AGE_GROUP', 'PERP_SEX', 'PERP_RACE', 'VIC_AGE_GROUP', 'VIC_SEX', 'VIC_RACE'])

adf = pd.read_csv('NYPD_ARRESTS_DATA__HISTORIC_.csv', usecols=['ARREST_DATE', 'OFNS_DESC', 'LAW_CODE', 'LAW_CAT_CD', 'Longitude', 'Latitude', 'ARREST_PRECINCT', 'AGE_GROUP', 'PERP_SEX', 'PERP_RACE'])

# Missing 'Hispanic or Latinx Count', 'Hispanic or Latinx Percentage', 'Two Spirit (Native American/ First Nations) Count',
# 'Two Spirit (Native American/ First Nations) Percentage', 'Native Hawaiian or Pacific Islander Count', 'Native Hawaiian or Pacific Islander Percentage'
ddf = pd.read_csv(durl, usecols=['Zip Code', 'Female Count', 'Female Percentage', 'Male Count', 'Male Percentage', 'Gender Nonconforming Count', 'Gender Nonconforming Percentage'
                                 , 'American Indian or Alaskan Native Count', 'American Indian or Alaskan Native Percentage', 'Asian Count', 'Asian Percentage',
                                 'Black or African American Count', 'Black or African American Percentage', 'Multi-race Count', 'Multi-race Percentage', 'White or Caucasian Count', 'White or Caucasian Percentage', 'Middle Eastern and North African Count', 'Middle Eastern and North African Percentage'])

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