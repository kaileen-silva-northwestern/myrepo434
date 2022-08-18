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

#<form>
#  <label for="fname">First name:</label><br>
#  <input type="text" id="fname" name="fname"><br>
#  <label for="lname">Last name:</label><br>
#  <input type="text" id="lname" name="lname">
#</form>

def home():
    return """
    <html><body>
    <h2> Predict Fare Prices </h2>
        <form action="/query" method ="post">
            <label for="lat1">Latitude 1:>
            <input type='text' id="lat1" value ="nm">
            <input type='submit' value="Submit">
    </body></html>
    """

if __name__ == '__main__':
   app.run()
