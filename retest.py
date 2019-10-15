import flask
from flask import request,jsonify


app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def app_all():
	return "<h1>Test page in json by Mohan</h1>"

@app.route('/resources', methods=['GET'])
def app_home():
	return "<h1>This is my second page by Mohan</h1>"

app.run(host='0.0.0.0')
