from flask import Flask, render_template, request
from flask_googlemaps import GoogleMaps

app = Flask(__name__)

@app.route("/", methods= ['GET','POST'])

def predict():
    if request.method == "POST":
        #get form data
        latitude = request.form.get('Latitude')
        longitude = request.form.get('Longitude')
        return render_template('predict.html')
    pass
