import pandas as pd
from flask import Flask,render_template,request
import pythonTest.day0415.placeholderTest01
app = Flask(__name__)

@app.route("/person_bmi", methods = ["POST","GET"])
def getMember():
    return render_template("bmicheck.html")


if __name__ == '__main__':
    app.run(debug=True, host='203.236.209.99')
