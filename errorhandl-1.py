from flask import Flask, render_template, jsonify, Response, json, request

app = Flask(__name__)

#method 1
#@app.errorhandler(404)
#def not_found(error=None):
#    message = {
#            'status': 404,
#            'message': 'Not Found: ' + request.url,
#    }
#    resp = jsonify(message)
#    resp.status_code = 404
#
#    return resp

#method 2
def not_found():
    message = { 'message':'The requested page not found ' + request.url }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


@app.route('/users/<userid>', methods = ['GET'])
def api_users(userid):
    users = {'1':'mohan', '2':'magi', '3':'sathya'}

    if userid in users:
        return jsonify({userid:users[userid]})
    else:
        return not_found()

if __name__ == '__main__':
#method 2
	app.error_handler_spec[404] = not_found
	app.run(host='0.0.0.0',port=33330)
