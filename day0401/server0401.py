from flask import Flask,render_template,request
import pythonTest.day0401.iris_train04

app = Flask(__name__)

@app.route("/iris.do", methods = ["POST","GET"])
def flower():

    if request.method =='POST':
        r1 = float(request.form['SepalLength'])
        r2 = float(request.form['SepalWidth'])
        r3 = float(request.form['PetalLength'])
        r4 = float(request.form['PetalWidth'])
        # list.append([r1,r2,r3,r4])

        result,ac = pythonTest.day0401.iris_train04.irislist(r1, r2, r3, r4)

        return render_template("iris.html",result=result,ac=ac,r1=r1,r2=r2,r3=r3,r4=r4)

    return render_template("iris.html")

if __name__ == '__main__':
    app.run(debug=True,host='203.236.209.99')


