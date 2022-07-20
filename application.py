from flask import Flask
from flask_googlemaps import GoogleMaps

app = Flask(__name__)

app = Flask(__name__, template_folder=".")
GoogleMaps(app)

@app.route("/input")
def input():
    cityList=db.execute("SELECT * FROM cities order by city_name")
    return render_template("input.html",cityList=cityList )
