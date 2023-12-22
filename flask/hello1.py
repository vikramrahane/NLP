from flask import Flask
app=Flask(__name__)

@app.route('/hello/<name>')
def hello_world(name):
    return "<marquee>Hi <b>%s</b> Welcome to Pune!</marquee>" %name

if __name__=='__main__':
    app.run(debug=True) # run(host,port(5000),debug(False),options)
