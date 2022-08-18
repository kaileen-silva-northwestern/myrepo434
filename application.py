from flask import Flask

app = Flask(__name__)

@app.route("/")

##def hello():
##    return "Hello World!"

##@app.route('/hello', methods=['POST'])

#def hello_world():
#    return 'Hello World'

def home():
    return """
    <html><body>
    <h2> Spin yo records </h2>
        <form action="/query">
            <input type='submit' value="I'm Feeling Lucky">
    </body></html>
    """

if __name__ == '__main__':
   app.run()
