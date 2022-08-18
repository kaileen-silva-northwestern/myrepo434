from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['POST'])

##def hello():
##    return "Hello World!"

##@app.route('/hello', methods=['POST'])

def hello_world():
    return 'Hello World'
if __name__ == '__main__':
   app.run()
