from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def hello_world():
    marks = {
        "John" : 45,
        "Saurabh" : 55,
        "Jeff" : 67,
        "Lily" : 99
    }
    return render_template("index.html", marks=marks)

app.run(debug=True)