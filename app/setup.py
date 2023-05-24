import sqlite3, gdown, fiona, pyproj, json #gdown for downloading big google drive files
import pandas as pd

from collections import OrderedDict
from ast import literal_eval
DB_FILE = "data.db"

db = sqlite3.connect(DB_FILE, check_same_thread = False)
c = db.cursor()

curl = 'https://drive.google.com/file/d/1DXS_eqGG3AbR1IrdOcWiXc_qPTEbGFHf/view?usp=sharing'
aurl = 'https://drive.google.com/file/d/1HtKO8nK2daRjJm1U50pyUZt_SF0cFmQj/view?usp=sharing'
curl = 'https://drive.google.com/uc?id=' + curl.split('/')[-2]
aurl = 'https://drive.google.com/uc?id=' + aurl.split('/')[-2]

gdown.download(curl)
gdown.download(aurl)


# Collision and arrest data is obtained separately with gdown because they're too big
surl = 'https://drive.google.com/file/d/1EJRFulkdL0sKhH2py9YVXH6gfdvNN_6Q/view?usp=sharing'
durl = 'https://drive.google.com/file/d/1sGjh289FyxkBNQ-wdruaxxN0k1WTp2xg/view?usp=sharing'
surl = 'https://drive.google.com/uc?id=' + surl.split('/')[-2]
durl = 'https://drive.google.com/uc?id=' + durl.split('/')[-2]

ccols_to_use = ["LATITUDE", "LONGITUDE", "CRASH DATE", "CRASH TIME", "ZIP CODE", "NUMBER OF PERSONS INJURED", "NUMBER OF PERSONS KILLED", "VEHICLE TYPE CODE 1"]
cdf = pd.read_csv('Motor_Vehicle_Collisions_-_Crashes.csv', usecols=ccols_to_use, low_memory = False)[ccols_to_use]

scols_to_use = ['Latitude', 'Longitude', 'OCCUR_DATE', 'PERP_AGE_GROUP', 'PERP_SEX', 'PERP_RACE', 'VIC_AGE_GROUP', 'VIC_SEX', 'VIC_RACE']
sdf = pd.read_csv(surl, usecols=scols_to_use)[scols_to_use]

acols_to_use = ['Longitude', 'Latitude', 'ARREST_DATE', 'OFNS_DESC', 'LAW_CODE', 'LAW_CAT_CD', 'ARREST_PRECINCT', 'AGE_GROUP', 'PERP_SEX', 'PERP_RACE']
adf = pd.read_csv('NYPD_Arrests_Data__Historic_.csv', usecols=acols_to_use)[acols_to_use]

# Missing 'Hispanic or Latinx Count', 'Hispanic or Latinx Percentage', 'Two Spirit (Native American/ First Nations) Count',
# 'Two Spirit (Native American/ First Nations) Percentage', 'Native Hawaiian or Pacific Islander Count', 'Native Hawaiian or Pacific Islander Percentage'
dcols_to_use = ['Zip Code', 'Program Type', 'Female Count', 'Male Count']
ddf = pd.read_csv(durl, usecols=dcols_to_use)[dcols_to_use]

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

cdf.to_sql('collision_info', db, if_exists='fail')
sdf.to_sql('shooting_info', db, if_exists='fail')
adf.to_sql('arrest_info', db, if_exists='fail')
ddf.to_sql('demographic_info', db, if_exists='fail')

# Do a lot of shapefile stuff in order to convert the zipcodes into geographic coordinate data that can be made into polygons.

zipcodeurl = 'https://drive.google.com/file/d/17d8We1qNCsRIm7eH6P9qcBUsQ9iGNhmZ/view?usp=sharing'
zipcodeurl = 'https://drive.google.com/uc?id=' + zipcodeurl.split('/')[-2]
gdown.download(zipcodeurl)

c.execute("CREATE TABLE IF NOT EXISTS geo_info (id INTEGER PRIMARY KEY AUTOINCREMENT, properties TEXT, geometry TEXT)")

source_crs = pyproj.CRS.from_string('PROJCS["NAD_1983_StatePlane_New_York_Long_Island_FIPS_3104_Feet",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Lambert_Conformal_Conic"],PARAMETER["False_Easting",984250.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-74.0],PARAMETER["Standard_Parallel_1",40.66666666666666],PARAMETER["Standard_Parallel_2",41.03333333333333],PARAMETER["Latitude_Of_Origin",40.16666666666666],UNIT["Foot_US",0.3048006096012192]]')
target_crs = pyproj.CRS.from_string('EPSG:4326')

transformer = pyproj.Transformer.from_crs(source_crs, target_crs)

with fiona.open('zip://ZIP_CODE_040114.zip') as src:
    asdict = OrderedDict()
    asdict['type'] = 'FeatureCollection'
    asdict['features'] = []
    for feature in src:
        feature_dict = OrderedDict()
        feature_dict['type'] = 'Feature'
        feature_dict['properties'] = {}
        for k, v in feature.properties.items():
            feature_dict['properties'][k] = v
        samezip = c.execute("SELECT `Program Type`, `Female Count`, `Male Count` FROM demographic_info WHERE `Zip Code` = " + feature_dict['properties']['ZIPCODE']).fetchall()
        i = 1
        for row in samezip:
            feature_dict['properties'][row[0]] = {}
            feature_dict['properties'][row[0]]['female'] = row[1]
            feature_dict['properties'][row[0]]['male'] = row[2]
            feature_dict['properties'][row[0]]['(female + male)'] = row[1] + row[2]
            i = i + 1
        # Change coordinates system to lon lat
        feature['geometry']['coordinates'][0] = [transformer.transform(x, y)[::-1] for x, y in feature['geometry']['coordinates'][0]]
        feature_dict['geometry'] = {}
        feature_dict['geometry']['type'] = feature['geometry']['type']
        feature_dict['geometry']['coordinates'] = [feature['geometry']['coordinates'][0]]
        asdict['features'].append(feature_dict)
        
for feature in asdict['features']:
    properties = json.dumps(feature['properties'])
    geometry = json.dumps(feature['geometry'])
    c.execute("INSERT INTO geo_info (properties, geometry) VALUES (?, ?)", (properties, geometry))
        
print(asdict)

#asdict['features'][index]['geometry']['coordinates'] for the bounding coordinates for a zip code
#asdict['features'][index]['geometry']['type'] to get type (should always be polygon)
#json.dumps(asdict['features'][index]) to get as json
db.commit()