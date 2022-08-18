from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():
    return "Hello World!"

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
