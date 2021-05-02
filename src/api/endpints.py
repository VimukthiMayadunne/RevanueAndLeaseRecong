from flask import Flask, request, jsonify, Response

app = Flask(__name__)


# endpoint to validate the server
@app.route("/")
def hello():
    return jsonify(isError=False, message="Welcome To Automated Revenue recognition", statusCode=200), 200


# endpoint to validate the Contract
@app.route("/check", methods=['GET', 'POST'])
def check():
    if request.method == 'GET':
        return jsonify(isError=False, message="Success", statusCode=200), 200
    elif request.method == 'POST':
        data = request.json
        return jsonify(isError=False, message=data, statusCode=200), 200
    else:
        return jsonify(isError=True, message="Unauthorized method", statusCode=401), 401


# endpoint to Lease Recognition capabilities
@app.route("/lease", methods=['GET', 'POST'])
def lease():
    if request.method == 'GET':
        return jsonify(isError=False, message="Success", statusCode=200), 200
    elif request.method == 'POST':
        data = request.json
        return jsonify(isError=False, message=data, statusCode=200), 200
    else:
        return jsonify(isError=True, message="Unauthorized method", statusCode=401), 401


# endpoint to Revenue Recognition capabilities
@app.route("/revenue", methods=['GET', 'POST'])
def revenue():
    if request.method == 'GET':
        return jsonify(isError=False, message="Success", statusCode=200), 200
    elif request.method == 'POST':
        data = request.json
        return jsonify(isError=False, message=data, statusCode=200), 200
    else:
        return jsonify(isError=True, message="Unauthorized method", statusCode=401), 401
