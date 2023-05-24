from flask import Flask, render_template
import os
import json

from db import geodata_to_dict, getData


app = Flask(__name__)

app.secret_key = os.urandom(12)

# Make sure to run in the /app directory so the database file is in the right spot



@app.route("/")
def index():
    return render_template("home.html")

@app.route("/map", methods=['GET', 'POST'])
def map():

    demo_info = getData("demographic_info")
    
    collision_points_json = json.dumps(getData("collision_info"))
    shooting_points_json = json.dumps(getData("shooting_info"))
    arrest_points_json = json.dumps(getData("arrest_info"))
    zipdata_json = json.dumps(geodata_to_dict())

    return render_template('map.html', data=zipdata_json, col_data=collision_points_json, sho_data=shooting_points_json, arr_data=arrest_points_json, demo_data = demo_info)


if __name__ == "__main__": #false if this file imported as module

    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run(host='0.0.0.0')


