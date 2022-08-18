from flask import Flask

app = Flask(__name__)

@app.route("/")

##def hello():
##    return "Hello World!"

#def home():
#    return """
#    <html><body>
#    <h2> Predict Fare Prices </h2>
#        <form action="/query">
#            <input type='submit' value="Submit">
#    </body></html>
#    """

def home():
    return """
    <html><body>
    <h2> Predict Fare Prices </h2>
        <form action="/query" method ="post">
            <label for="lat1">Latitude 1:</label><br>
            <input type='text' id="lat1" name="lat1"><br>
            <label for="long1">Longitude 1:</label><br>
            <input type='text' id="long1" name="long1"><br>
            <label for="lat2">Latitude 2:</label><br>
            <input type='text' id="lat2" name="lat2"><br>
            <label for="long2">Longitude 2:</label><br>
            <input type='text' id="long2" name="long2"><br>            
            <input type='submit' value="Submit">
            <input type="reset">
    </body></html>
    """

if __name__ == '__main__':
   app.run()
