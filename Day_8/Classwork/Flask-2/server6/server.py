from flask import Flask, request

from createCustomResponse import createCustomResponse

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@app.route('/student', methods=['GET', 'POST', 'PUT', 'DELETE'])
def student_ops():
    if request.method == 'POST':
        # TODO
        msg = "student is added successfully"
    elif request.method == 'GET':
        # TODO
        msg = "student : []"
    elif request.method == 'PUT':
        # TODO
        msg = "student is updated successfully"
    elif request.method == 'DELETE':
        # TODO
        msg = "student is deleted successfully"

    return createCustomResponse(msg, error=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)