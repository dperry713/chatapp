from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# HashMap to store messages
message_storage = {}

@app.route('/')
def index():
    return render_template('join_room.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    user = data.get('user')
    message = data.get('message')
    if user and message:
        if user not in message_storage:
            message_storage[user] = []
        message_storage[user].append(message)
        return jsonify({'status': 'Message sent'}), 200
    else:
        return jsonify({'error': 'Invalid data'}), 400

@app.route('/get_all_messages', methods=['GET'])
def get_all_messages():
    user = request.args.get('user')
    if user in message_storage:
        return jsonify({user: message_storage[user]}), 200
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    socketio.run(app, debug=True)
