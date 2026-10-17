from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
    "Aarav Sharma": 85,
    "Diya Patel": 92,
    "Rohan Verma": 78
    }
    values = [1, marks, 67]
    return jsonify(values)

app.run(debug=True)