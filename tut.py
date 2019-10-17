from flask import Flask
from flask import render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )


if __name__ == '__main__':
   app.run(host='0.0.0.0',port=33333,debug = True)
