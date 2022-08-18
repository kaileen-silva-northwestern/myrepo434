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
            <input type='text' value ="nm">
            <input type='submit' value="Submit">
    </body></html>
    """

if __name__ == '__main__':
   app.run()
