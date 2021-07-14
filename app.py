from flask import Flask
from flask import json
import logging
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
@app.route('/status')
def status():
    response=app.response_class(
        response=json.dumps({
            "result":"OK-healthy"
        }),
        status=200,
        mimetype='application/json'
    )
    app.logger.info("Status request successful")
    return response
@app.route('/metrics')
def metrics():
    response=app.response_class(
        response=json.dumps({
            "status":"success",
            "code":0,
            "data":{"UserCount":140,"UserCountActive":50}
        }),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('Metrics request successful')
    return response


if __name__ == "__main__":
    logging.basicConfig(filename='app.log',level=logging.DEBUG)

    app.run(host='0.0.0.0',port=8080)
