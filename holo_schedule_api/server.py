from flask import Flask
from flask import request, jsonify
from flask_cors import CORS
import waitress
from web_service import WebService

app = Flask(__name__)
CORS(app)

WebService.register(app, route_base="/")

if __name__ == "__main__":
    waitress.serve(app, host="0.0.0.0", port=5000)