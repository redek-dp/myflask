from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = requests.post(
        'https://api.qwen.com/v1/chat ',
        headers={'Authorization': f'Bearer {os.getenv("QWEN_API_KEY")}'},
        json={'prompt': user_message}
    )
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)  
