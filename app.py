#from flask import Flask, render_template

#app = Flask(__name__)

#@app.route('/')
#def index():
#    return render_template('index.html')


#if __name__ == '__main__':
#    app.run(debug=True)


import requests
import json

from flask import Flask,render_template

app=Flask(__name__)

url='https://jsonplaceholder.typicode.com/users'

req=requests.get(url)
json_form=req.json()


@app.route("/")

@app.route('/index')
def index():
    return render_template('index.html',data=json_form)

if __name__ == '__main__':
    app.run(debug=True)