
from flask import Flask, abort, request 
import json
from e import pred

app = Flask(__name__)

@app.route('/pre', methods=['POST']) 
def pred():
    if not request.json:
        abort(400)

    res = pred(request.json['mgs'])
    response = app.response_class(
        response=json.dumps(res),
        mimetype='application/json')
    return res.text()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)