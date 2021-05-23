from PyPDF2 import PdfFileReader
import requests
from flask import Flask, request, jsonify

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
        print(data)
        # Thewnis Code here
        contractType = 'revenue'
        if contractType == "lease":
            var = requests.get('http://0.0.0.0:5000/lease')
            print(var.text)
            return jsonify(isError=False, message="Reciver", statusCode=200), 200
        elif contractType == "revenue":
            var = requests.get('http://0.0.0.0:5000/revenue')
            print(var.text)
            return jsonify(isError=False, message="Reciver", statusCode=200), 200
        else:
            return jsonify(isError=True, message="Unable to determine Contract typedata", statusCode=501), 501
    else:
        return jsonify(isError=True, message="Unauthorized method", statusCode=405), 405


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
        return jsonify(isError=True, message="Unauthorized method", statusCode=405), 405


@app.route("/revenuepdf", methods=['GET', 'POST'])
def revenuepdf():
    if request.method == 'GET':
        return jsonify(isError=False, message="Success", statusCode=200), 200
    elif request.method == 'POST':
        if 'pdf' in request.files:
            incoming_pdf = request.files['pdf']
            pdf_data = PdfFileReader(incoming_pdf, 'rb')
            page = pdf_data.getPage(0)
            pageContent = page.extractText()
            print(pageContent)
            print(incoming_pdf)
            print(page)
        return jsonify(isError=False, message="data", statusCode=200), 200
    else:
        return jsonify(isError=True, message="Unauthorized method", statusCode=405), 405
