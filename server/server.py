from flask import Flask, request

app = Flask(__name__)


@app.route('/') #, methods=['GET'])
def hello():
    #if request.method == 'GET':
        return '<h1>Welcome!!!</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
