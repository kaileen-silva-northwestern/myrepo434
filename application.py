from flask import Flask
from flask_googlemaps import GoogleMaps

app = Flask(__name__)

@app.route("/input")
def input():
    cityList=["SF","TF","MF"]
    return render_template("input.html",cityList=cityList )
