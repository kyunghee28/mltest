from flask import Flask,render_template,request
import pythonTest.day0401.irismodule

app = Flask(__name__)

@app.route('/iris',methods =['GET','POST'])
def irisget():
    r = ''
    str_arr = [['','','','']]
    arr = str_arr
    final_arr=[]
    if request.method == 'POST':
        realdatanum1 = float(request.form['realnum1'])
        realdatanum2 = float(request.form['realnum2'])
        realdatanum3 = float(request.form['realnum3'])
        realdatanum4 = float(request.form['realnum4'])
        r = pythonTest.day0401.irismodule.irismodule(realdatanum1, realdatanum2, realdatanum3, realdatanum4)
        r = r[0]
        print(r)
        final_arr.append([realdatanum1,realdatanum2,realdatanum3,realdatanum4])
        arr = final_arr
    return render_template('iris2.html',r=r,arr=arr)


if __name__ == '__main__':
    app.run(host='203.236.209.99',debug=True)

