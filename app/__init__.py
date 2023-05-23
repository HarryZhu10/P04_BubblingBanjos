from flask import Flask, render_template, request
import os
import json, sqlite3

from db import geodata_to_dict, getData


app = Flask(__name__)

app.secret_key = os.urandom(12)

# Make sure to run in the /app directory so the database file is in the right spot



@app.route("/")
def index():
    return render_template("home.html")

@app.route("/map", methods=['GET', 'POST'])
def map():
    # if request.method == 'GET':
    #     return render_template('map.html')
#     otherData = {"type":"FeatureCollection","features":[{"type": "Feature", "id": "51", "properties": {"ZIPCODE": "10048", "BLDGZIP": "0", "PO_NAME": "New York", "POPULATION": 0.0, "AREA": 972788.42397429, "STATE": "NY", "COUNTY": "New York", "ST_FIPS": "36", "CTY_FIPS": "061", "URL": "http://www.usps.com/", "SHAPE_AREA": 0.0, "SHAPE_LEN": 0.0}, "geometry": {"type": "Polygon", "coordinates": [[[-74.01162614660633, 40.70977173918315], [-74.01167375613933, 40.709687089036535], [-74.01264557237943, 40.71013431699109], [-74.01270117958505, 40.710236720571196], [-74.01298572580237, 40.71036639030841], [-74.01303297018926, 40.71038791978647], [-74.01341871863228, 40.71056370831919], [-74.01395920099478, 40.71079685294411], [-74.01405350355753, 40.710837530151586], [-74.01440986247805, 40.71099124561641], [-74.01403725317621, 40.7125242976917], [-74.01397793121771, 40.71276836850068], [-74.01390617438513, 40.71306371404465], [-74.0138861722932, 40.713145922267074], [-74.01375387073819, 40.71369024092861], [-74.01342045910135, 40.71354214990464], [-74.01330440131579, 40.71350814028779], [-74.0132282650045, 40.71347926068435], [-74.01265682463904, 40.71322210760425], [-74.01254377556586, 40.713178797316], [-74.01243344521853, 40.71313652851358], [-74.01204901188855, 40.71297148869617], [-74.01194101951968, 40.712929303824005], [-74.01184559387944, 40.71289143370511], [-74.0117886315688, 40.71285399272018], [-74.01176009768392, 40.71283476073252], [-74.01169132093239, 40.712775846429345], [-74.0115900752701, 40.712689118585594], [-74.01156448286989, 40.71267279220053], [-74.01152738668561, 40.712652155317414], [-74.01056043588646, 40.71221217843969], [-74.01045133189831, 40.712153740752015], [-74.01036394439315, 40.712120216336736], [-74.01015299265806, 40.71206415403185], [-74.01019567324249, 40.71198000924298], [-74.01042312033985, 40.71159556355287], [-74.0104653387816, 40.71153423854334], [-74.0108007668292, 40.71101709465278], [-74.01123100039382, 40.71036655056466], [-74.01162614660633, 40.70977173918315]]]}}]}


    points = [
        [40.736941352203026, -74.00542165571395],
        [40.73837210883931, -73.9916887455577],
        [40.740193027326065, -73.98181821638289],
        [40.74817196963256, -74.00230943631958],
        [40.75148811664014, -73.99801790189575],
        [40.753503733027394, -73.97389947843384],
        [40.7463512695814, -73.97269784879516],
        [40.73308466465735, -73.97570192289184],
        [40.746156191619384, -73.95458757352661],
        [40.72846674520867, -73.95913660001587],
        [40.726710550885535, -74.00402605008911],
        [40.724238791471926, -73.97827684354614],
        [40.75577935550959, -74.00050699186157],
        [40.75558430520601, -73.97115289640259],
    ]
    
    zipareas = geodata_to_dict()
    collision_points = getData("collision_info")
    shooting_points = getData("shooting_info")
    arrest_points = getData("arrest_info")
    demo_info = getData("demographic_info")
    
    collision_points_json = json.dumps(collision_points)
    shooting_points_json = json.dumps(shooting_points)
    arrest_points_json = json.dumps(arrest_points)
    

    # print("ahahahha")
    # print (type(statesData))
#     otherData_json = json.dumps(otherData)
#     print(otherData_json)

    points_json = json.dumps(points)
    zipdata_json = json.dumps(zipareas)
    print(zipdata_json)

    # print(type(statesData_json))
    # print(statesData_json)
    
#     return render_template('map.html', data=statesData_json,point_data=points_json)
    # return render_template('map.html')
#     return render_template('map.html', data=zipdata_json, point_data=points_json)
    return render_template('map.html', data=zipdata_json, point_data=points_json, col_data=collision_points_json, sho_data=shooting_points_json, arr_data=arrest_points_json, demo_data = demo_info)
#     return render_template('map.html', data=otherData_json)


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run(host='0.0.0.0')


