from flask import Flask
from flask import json
import logging
import time
app = Flask(__name__)
logging.basicConfig(filename='app.log',level=logging.DEBUG)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def status():
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('Status request successfull')
    return response
@app.route("/metrics")
def metrics():
    response = app.response_class(
        response=json.dumps({"data": {"UserCount": 140, "UserCountActive": 23}, "status":"success", "code":0}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('Metrics request successfull')
    return response
  

if __name__ == "__main__":
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    app.run(host='0.0.0.0', debug=True)
