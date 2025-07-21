from flask import Flask, request, jsonify
import requests

API_KEY = 'sua_chave_api_aqui'
VT_URL = 'https://www.virustotal.com/api/v3/files'

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan_file():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400
    file = request.files['file']
    files = {'file': (file.filename, file.stream)}
    headers = {'x-apikey': API_KEY}
    response = requests.post(VT_URL, files=files, headers=headers)
    if response.status_code == 200:
        result = response.json()
        return jsonify(result), 200
    return jsonify({'error': 'Erro ao escanear o arquivo'}), 500
