from flask import Flask, jsonify, request
from services.openai_services import chat_openai_services, image_openai_services

app = Flask(__name__)
    
@app.route('/api/v1/chat', methods=['POST'])
def chat_openai():
    data = request.get_json()
    if 'description' not in data:
        return jsonify({"error": "Missing 'description' in request body"}), 400

    description = data['description']
    response = chat_openai_services(description)
    return response
    
@app.route('/api/v1/images', methods=['POST'])
def image_openai():
    data = request.get_json()
    if 'description' not in data:
        return jsonify({"error": "Missing 'description' in request body"}), 400

    description = data['description']
    response = image_openai_services(description)
    return response