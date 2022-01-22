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

@app.route("/courses",  methods=['GET'])
def get():
    return jsonify({'courses': courses})
if __name__ == '__main__':
    app.run(debug=True)
