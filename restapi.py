import flask
from flask import request, jsonify

app = flask.Flask(__name__)

mohan = [
	{'id': 3,
	 'title': 'A Mohans book',
         'author': 'Mohanasundaram',
         'year_publish': '1972'},
	{ 'id':4,
          'title': 'Second page of the book'},
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route('/')
def home():
    return "This is my first flask api"

@app.route('/api/all', methods=['GET'])
def api_all():
     return jsonify(mohan)

@app.route('/api/id', methods=['GET'])
def api_id():
	if 'id' in request.args:
		id = int(request.args['id'])
	else:
		return "No ID specified"

	results = []
	
	for mo in mohan:
		if mo['id'] == id:
			results.append(mo)
	return jsonify(results)

app.run(host='0.0.0.0')
