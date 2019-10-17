from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/mohan')
def app_all():
	return "This is mohan"

@app.route('/guest/<guest>/')
def app_guest(guest):
	return "This is NOT Mohan , but %s" % guest

@app.route('/user/<name>/')
def app_user(name):
	if name == 'mohan':
		return redirect(url_for('app_all',))
	else:
		return redirect(url_for('app_guest',guest = name))

app.run(host='0.0.0.0',port='32001')
