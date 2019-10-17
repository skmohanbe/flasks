from flask import Flask, redirect, request, url_for

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
	return "Welcome Mr.%s" % name

@app.route('/login', methods = ['GET', 'POST'])
def login():
	if request.method == 'POST':
		user = request.form['nm']
		return redirect(url_for('success', name = user))
	else:
		user = request.args.get('nm')
		return redirect(url_for('success', name = user))


app.run(host='0.0.0.0',port=35001,debug=True)
