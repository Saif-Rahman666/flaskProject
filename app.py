from flask import Flask, jsonify

app = Flask(__name__)

courses = [{'name': "pip",
            'id': "0"},
           {'name': "pip2",
            'id': "1"}
           ]

@app.route('/')
def hello_world():
    return 'Hello World!!'

@app.route("/name",  methods=['GET'])
def get():
    return jsonify({'name': name})
if __name__ == '__main__':
    app.run()
