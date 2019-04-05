from flask import Flask, render_template, request
import pythonTest.day0404.Sinfo

app = Flask(__name__)

#존재하지 않는 학생이름을 입력하면
#적당한 메세지를 출력하도록 수정합니다.

@app.route("/student", methods=['GET','POST'])
def student():
    name = ""
    fname = ""
    msg = ""
    if request.method == 'POST':
        name= request.form['name']
        fname = pythonTest.day0404.Sinfo.makeChart(name)
        if fname == 'no':
            msg = "해당학생은 존재하지 않습니다."
    return render_template("studentInfo.html",name=name, fname=fname, msg=msg)



@app.route('/subject.do',methods=['GET','POST'])
def subjectSco():
    fname =''
    msg = ''
    if request.method =='POST':
        name = request.form['name']
        fname = pythonTest.day0404.Sinfo.getSubjectScore(name)
        if fname == "no":
            msg = "해당 과목이 존재하지 않습니다."

    return render_template('subject.html',fname=fname,msg=msg)


if __name__ == '__main__':
    app.run(host="203.236.209.99", debug=True)
