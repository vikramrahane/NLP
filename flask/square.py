from flask import Flask
app=Flask(__name__)

@app.route('/square/<num>')
def hello_world(num):
    sq=int(num)**2
    return "<center><h1>Square of %s is <b>%d</b>.</h1></center>" %(num,sq)

if __name__=='__main__':
    app.run(debug=True) # run(host,port(5000),debug(False),options)
