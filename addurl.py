import flask

app = flask.Flask(__name__)

def app_all(name):
	return "This is %s's world" % name

app.add_url_rule('/<name>/','app', app_all)

def app_id(id):
	return "This is an int number %r" % id

app.add_url_rule('/int/<id>','', app_id)

app.run(host='0.0.0.0',debug='True')

