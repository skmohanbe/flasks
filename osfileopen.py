import flask
import os
import markdown

from flask import Flask, request, g
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)


@app.route("/")
def index():
    with open(os.path.dirname(app.root_path) + '/anaconda-ks.cfg', 'r') as markdown_file:

        # Read the content of the file
        content = markdown_file.read()
        # Convert to HTML
        return markdown.markdown(content)

app.run(host='0.0.0.0',port=41000)
