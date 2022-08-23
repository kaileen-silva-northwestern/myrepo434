from flask import Flask, render_template, request
import pandas
from haversine import Unit

app = Flask(__name__)

#def hello():
#    return "Hello World!"

@app.route('/')

def index():
   print('Request for index page received')
   return render_template('data.html')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('form.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))
 

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
#      
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
