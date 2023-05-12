import sqlite3, csv, sqlalchemy, gdown #gdown for downloading big google drive files
import pandas as pd

from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)
DB_FILE = "data.db"

db = None

curl = 'https://drive.google.com/file/d/1DXS_eqGG3AbR1IrdOcWiXc_qPTEbGFHf/view?usp=sharing'
aurl = 'https://drive.google.com/file/d/1HtKO8nK2daRjJm1U50pyUZt_SF0cFmQj/view?usp=sharing'
curl = 'https://drive.google.com/uc?id=' + curl.split('/')[-2]
aurl = 'https://drive.google.com/uc?id=' + aurl.split('/')[-2]

gdown.download(curl)
gdown.download(aurl)


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

cdf = cdf.dropna()
sdf = sdf.dropna()
adf = adf.dropna()
ddf = ddf.dropna()

cdf['CRASH DATE'] = pd.to_datetime(cdf['CRASH DATE'], format='%m/%d/%Y')
sdf['OCCUR_DATE'] = pd.to_datetime(sdf['OCCUR_DATE'], format='%m/%d/%Y')
adf['ARREST_DATE'] = pd.to_datetime(adf['ARREST_DATE'], format='%m/%d/%Y')
cdf = cdf[(cdf['CRASH DATE'] >= '01/01/2017')]
sdf = sdf[(sdf['OCCUR_DATE'] >= '01/01/2017')]
adf = adf[(adf['ARREST_DATE'] >= '01/01/2017')]

cdf.to_sql('collision_info', con=engine, if_exists='fail')
sdf.to_sql('shooting_info', con=engine, if_exists='fail')
adf.to_sql('arrest_info', con=engine, if_exists='fail')
ddf.to_sql('demographic_info', con=engine, if_exists='fail')