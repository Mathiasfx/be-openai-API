from routes.openai_routes import app
from flask_cors import CORS

# Cors routes
CORS(app)

# Server running from Flask
if __name__ == "__main__":
    app.run(port=8000, host='0.0.0.0')
