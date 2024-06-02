from flask import jsonify
from utils.orchestrator import get_image, get_answer

def chat_openai_services(description):
    try:
        result = get_answer(history=description)['answer']
        return jsonify({"response": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
def image_openai_services(description):
    try:
        result = get_image(history=description)['image']
        return jsonify({"response": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
