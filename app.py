from flask import Flask  
app = Flask(__name__)  

@app.route('/')  
def home():  
    return 'Olá, mundo! Seu servidor Flask está funcionando!'  

if __name__ == '__main__':  
    app.run(debug=True)  
