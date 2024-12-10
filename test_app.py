import unittest
import json
from flask_socketio import SocketIOTestClient
from app import app, socketio

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.socket_client = SocketIOTestClient(app, socketio)

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Join a Chat Room', response.data)

    def test_send_message(self):
        self.socket_client.connect()
        self.socket_client.emit('send_message', {'user': 'test_user', 'message': 'Hello, World!'})
        response = self.socket_client.get_received()
        self.assertIn({'user': 'test_user', 'message': 'Hello, World!'}, [msg['args'][0] for msg in response if msg['name'] == 'receive_message'])

    def test_connect_disconnect(self):
        self.socket_client.connect()
        self.assertTrue(self.socket_client.is_connected())
        self.socket_client.disconnect()
        self.assertFalse(self.socket_client.is_connected())

if __name__ == '__main__':
    unittest.main()
