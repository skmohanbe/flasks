from flask import Flask, render_template, jsonify, request, Response

app = Flask(__name__)

def not_found():
  return render_template('404.html'), 404

#def create_app(config_filename):
#    app = Flask(__name__)
#    app.register_error_handler(404, page_not_found)
#    return app

@app.route('/users/<userid>', methods = ['GET'])
def api_users(userid):
    users = {'1':'mohan', '2':'magi', '3':'sathya'}

    if userid in users:
        return jsonify({userid:users[userid]})
    else:
        return not_found()

if __name__ == '__main__':
    app.error_handler_spec[404] = not_found
    app.run(host='0.0.0.0',port=33331)
