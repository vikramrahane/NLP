from flask import Flask
app=Flask(__name__)

@app.route('/well')
def welcome():
    return "<marquee> <b>Welcome</b> </marquee>"

@app.route('/good')
def good():
    return "<marquee> <b>Good bye all</b> </marquee>"

@app.route('/')
def home():
    return "<center> <b>You are at home page</b> </center>"

if __name__=='__main__':
    app.run(debug=True) # run(host,port(5000),debug(False),options)
