#from flask import Flask, render_template

#app = Flask(__name__)

#@app.route('/')
#def index():
#    return render_template('index.html')


#if __name__ == '__main__':
#    app.run(debug=True)



from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():

    name = 'R5sal5a'
    nap = '0000000000000000000000'

    return render_template('index.html', title='Welcome', username=name, user01=nap, user02=nap, user03=nap)

if __name__ == '__main__':
    app.run(debug=True)