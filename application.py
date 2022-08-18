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
# <input type='submit' value="Submit">
# <input type="reset">

def home():
    return """
    <html>
    <head>
    <title>HTML JavaScript output on same page</title>
    <script type="text/JavaScript">
        function showMessage(){
            var message = document.getElementById("lat1id").value;
            display_message.innerHTML= message;
        }
    </script>
    </head>
    <body>
    <h2> Predict Fare Prices </h2>
        <form action="/query" method ="post">
            <label for="lat1">Latitude 1:</label><br>
            <input type='text' name="lat1" id="lat1id" ><br>
            <label for="long1">Longitude 1:</label><br>
            <input type='text' id="long1" name="long1"><br>
            <label for="lat2">Latitude 2:</label><br>
            <input type='text' id="lat2" name="lat2"><br>
            <label for="long2">Longitude 2:</label><br>
            <input type='text' id="long2" name="long2"><br>
            <input type="button" onclick="showMessage()" value="submit" />
          </form>
          <p> Message is: <span id = "display_message"></span> </p>
  
    </body></html>
    """

if __name__ == '__main__':
   app.run()
