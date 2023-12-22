from flask import Flask,request,url_for,redirect
app=Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'Welcome %s!' %name

@app.route('/fail')
def fail():
    return 'Authentication Failed.'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        user=request.form['uname']
        pw=request.form['passw']
        if user=='admin' and pw=='123':
            return redirect(url_for('success', name=user))
        else:
            return redirect(url_for('fail'))

if __name__=='__main__':
    app.run(debug=True)