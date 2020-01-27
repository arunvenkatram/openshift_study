import os
from flask import Flask, Response, request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello! Welcome to python app running in openshift'
@app.route('/arun')
def message():
    return 'Welcome Arun....'

if __name__ == '__main__':
    PORT = int(os.getenv('PORT')) if os.getenv('PORT') else 8080
    app.run(host='0.0.0.0', port=PORT, debug=True)