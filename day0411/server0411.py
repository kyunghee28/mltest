from flask import Flask,render_template,request
import pythonTest.day0411.ex03

app = Flask(__name__)

@app.route("/member_loan", methods = ["POST","GET"])
def getMember():

    if request.method =='POST':
        list = []
        r1 = request.form['Age']
        r2 = request.form['Job_kinds']
        r3 = request.form['Education']
        r4 = request.form['Job']
        r5 = request.form['Gender']
        r6 = request.form['Race']
        r7 = request.form['Working hours']

        list.append([int(r1),r2,r3,r4,r5,r6,int(r7)])

        pred_y = pythonTest.day0411.ex03.MemberInfo(list)

        return render_template("member.html",pred_y = pred_y)

    return render_template("member.html")


if __name__ == '__main__':
    app.run(debug=True,host='203.236.209.99')
