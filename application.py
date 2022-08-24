from flask import Flask, redirect, url_for, render_template, request
import pandas
from haversine import Unit

app = Flask(__name__)
 
 
  

@app.route('/')
def homepage():
        return render_template("home.html")

                                 
@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == "POST":
       lat1 = request.form.get("Latitude1")
       long1 = request.form.get("Longitude1")
       lat2 = request.form.get("Latitude2")
       long2 = request.form.get("Longitude2")
       loc1 = "(" + lat1 + "," + long1 + ")"
       loc2 = "(" + lat1 + "," + long1 + ")"
       return "Distance is " haversine.haversine(loc1,loc2,unit=Unit.MILES)
    #result = request.form
    return render_template("result.html",result = result)
 
                             


  
  
  

#def hello():
#    return "Hello World!" 

#def home():
#    return """
#    <html>
#    <head>
#    <title>HTML JavaScript output on same page</title>
#    <script type="text/JavaScript">
#        function showMessage(){
#            var lat1coor = document.getElementById("lat1id").value;
#            var long1coor = document.getElementById("long1id").value;
#            var lat2coor = document.getElementById("lat2id").value;
#            var long2coor = document.getElementById("long2id").value;            
#            var message = haversine.haversine((lat1coor,long1coor),(lat2coor,long2coor),unit=Unit.MILES);
#            display_message.innerHTML= message;
#        }
#    </script>
      
#    </head>
#    <body>
#    <h2> Predict Fare Prices </h2>
#        <form action="/query" method ="post">
#            <label for="lat1">Latitude 1:</label><br>
#            <input type='text' name="lat1" id="lat1id" ><br>
#            <label for="long1">Longitude 1:</label><br>
#            <input type='text' name="long1" id="long1id"><br>
#            <label for="lat2">Latitude 2:</label><br>
#            <input type='text' name="lat2" id="lat2id" ><br>
#            <label for="long2">Longitude 2:</label><br>
#            <input type='text' name="long2" id="long2id"><br>
#            <input type="button" onclick="showMessage()" value="submit" />
#          </form>
#          <p> Distance between points: <span id = "display_message"></span> </p>
#    </body></html>
#    """

if __name__ == '__main__':
   app.run()
