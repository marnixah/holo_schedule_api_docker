from flask import Flask
from flask import request, jsonify
from flask_cors import CORS
from gevent.pywsgi import WSGIServer
from gevent import monkey
from web_service import WebService

app = Flask(__name__)
CORS(app)

WebService.register(app, route_base="/")

if __name__ == "__main__":
    http = WSGIServer(('', 5000), app)
    http.serve_forever()