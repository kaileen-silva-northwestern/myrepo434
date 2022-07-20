from flask import Flask
from flask_googlemaps import GoogleMaps

app = Flask(__name__)

app = Flask(__name__, template_folder=".")
GoogleMaps(app)

@app.route("/")
def dropdown():
    colours = ['Red', 'Blue', 'Black', 'Orange']
    return render_template('test.html', colours=colours)

if __name__ == "__main__":
    app.run()
