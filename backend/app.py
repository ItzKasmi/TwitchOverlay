from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def home():
    return "Backend Service is Running"

@socketio.on('connect')
def handle_connect():
    print("Client Connected")

@socketio.on('disconnect')
def handle_connect():
    print("Client Disconnected")

@socketio.on('message')
def handle_message(data):
    print(f"Received message: {data}")
    emit('response', {'data': 'Message recieved'})

if __name__ == '__main__':
    app.run(debug=True)