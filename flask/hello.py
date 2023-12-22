from flask import Flask
app=Flask(__name__)

@app.route('/hello')
def hello_world():
    return ('Welcome to AI')

if __name__=='__main__':
    app.run(debug=True) # run(host,port(5000),debug(False),options)
