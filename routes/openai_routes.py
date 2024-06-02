from flask import Flask, jsonify, request
from services.openai_services import chat_openai_services, image_openai_services
from utils.auth import auth_token

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return jsonify({"response": "Hello API OpenAI"}), 200
    
@app.route('/api/v1/chat', methods=['POST'])
def chat_openai():
    data = request.get_json()
    auth_header = request.headers.get('Authorization')
    auth_token(auth_header)

    if 'description' not in data:
        return jsonify({"error": "Missing 'description' in request body"}), 400
    response = chat_openai_services(data['description'])
    return response
    
@app.route('/api/v1/image', methods=['POST'])
def image_openai():
    data = request.get_json()
    auth_header = request.headers.get('Authorization')
    auth_token(auth_header)

    if 'description' not in data:
        return jsonify({"error": "Missing 'description' in request body"}), 400
    response = image_openai_services(data['description'])
    return response