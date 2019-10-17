import flask
from flask import Flask, url_for, request, redirect

app = Flask(__name__)

@app.route('/login')
def login_all():
	return "This is test page to see url is up or not"

#@app.register_error_handler(404, page_not_found)
#def method_not_found(e):
#      return render_template('404.html'),404

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/form-example', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
	if request.method == 'POST':
            language = request.form.get('language')
            framework = request.form['framework']

            return '''<h1>The language is: {}</h1>
                      <h1>The framework is: {}</h1>'''.format(language, framework)

	return '''<form method="POST">
                  Language: <input type="text" name="language"><br>
                  Framework: <input type="text" name="framework"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

app.run(host='0.0.0.0',port=33332)
