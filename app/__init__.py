from flask import Flask, render_template, request
import os

app = Flask(__name__)

app.secret_key = os.urandom(12)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/map", methods=['GET', 'POST'])
def map():
    if request.method == 'GET':
        return render_template('map.html')

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()