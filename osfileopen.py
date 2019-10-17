import flask
import os
import markdown

from flask import Flask, request, g, render_template, jsonify, request, Response
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)

def not_found():
	return render_template('404.html'), 404

@app.route("/")
def index():
    with open(os.path.dirname(app.root_path) + '/anaconda-ks.cfg', 'r') as markdown_file:

        # Read the content of the file
        content = markdown_file.read()
        # Convert to HTML
        return markdown.markdown(content)

if __name__ == '__main__':
    app.error_handler_spec[404] = not_found
    app.run(host='0.0.0.0',port=33331)

