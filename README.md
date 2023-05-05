# P04: Map by BubblingBanjos
# Description

# Roster:
Harry : Middleware (Python and Flask)  
Andrew : Front End (Map API)  
Ivan : Middleware (Python and Flask)  
Shinji : Database / API (read data into sqlite)  

# Program Description:
App that displays a map of NYC populated with data on crime in the city over layed with additional info on the city like socioeconomic demographics. This visualization of information can help gauge the relative safety of certain areas in NYC based on various indexes.  
  

# Tools/APIs:
[Maptiler Docs](https://openmaptiles.org/docs/)  
[Maptiler Raster Image](https://docs.maptiler.com/leaflet/raster-layer/)  
[MapTiler Vector Tiles in Leaflet JS](https://docs.maptiler.com/leaflet/vector-tiles-in-leaflet-js/?key=dAqEbdIAjzS0HOvTSmTF&mapId=basic-v2&_gl=1*62ezf4*_ga*MzIwMDk1NDUwLjE2ODI3MDQ4NDc.*_ga_K4SXYBF4HT*MTY4MzA1MDEwNC4xLjEuMTY4MzA1MTAyNS41Ni4wLjA.*_ga_7HWGQGGMCE*MTY4MzA1MDEwNC4zLjEuMTY4MzA1MTAyNi4wLjAuMA..&_ga=2.174521698.1318779432.1682962870-320095450.1682704847)  
Maptiler Account Details:  
Email for API: bubbanjos@gmail.com  
This API will be used to create a map for our project that we will layer information on in many forms and with many different filters that the user will be   able to use.  
Goal: https://cuspmap.org/NYC/  
https://data.cityofnewyork.us/login  
NYC Open Data Account Details:  
Email for NYC Open Data Account: bubbanjos@gmail.com  
This account will allow us to create an app token to use the APIs provided by by NYC Open Data  


# Launch Codes
## How to Clone, Install, and Run

`0) Create and activate an environment`
```
python3 -m venv <<name>>
cd <<name>>
. bin/activate
```
`1) Clone the project `
```
git clone git@github.com:HarryZhu231227919/P04_BubblingBanjos.git
```

`2) Navigate to root directory`

``` 
cd P04_BubblingBanjos/
```
`3) Install requirements`
```
pip install -r requirements.txt
```
`4) Run the program`

``` 
python3 app/__init__.py
```

`5) Open the following link in any web browser`

`6) Have fun!`




# Data  
[NYC OPEN DATA](https://opendata.cityofnewyork.us/)  
[NYC motor vehicle collisions](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95) (The Motor Vehicle Collisions crash table contains details on the crash event. Each row represents a crash event. The Motor Vehicle Collisions data tables contain information from all police reported motor vehicle collisions in NYC)  
[details on the specific vehicles involved in collisions  ](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Vehicles/bm4k-52h4)  
[NYC hate crimes](https://data.cityofnewyork.us/Public-Safety/NYPD-Hate-Crimes/bqiq-cu78) (Dataset containing confirmed hate crime incidents in NYC, doesn’t have latitude, longitude)  
[NYC shooting incidents](https://data.cityofnewyork.us/Public-Safety/NYPD-Shooting-Incident-Data-Historic-/833y-fsy8) (List of every shooting incident that occurred in NYC going back to 2006 through the end of the previous calendar year)  
[NYC arrest data](https://data.cityofnewyork.us/Public-Safety/NYPD-Arrests-Data-Historic-/8h9b-rp9u) (List of every arrest in NYC going back to 2006 through the end of the previous calendar year)   
[Demographics by zip code](https://data.cityofnewyork.us/Social-Services/Demographics-by-Zip-Code/hebw-6hze)



