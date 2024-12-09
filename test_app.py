import unittest
import json
from app import app, message_storage

class ChatAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_send_message(self):
        response = self.app.post('/send_message',
                                 data=json.dumps({'user': 'JohnDoe', 'message': 'Hello world!'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('JohnDoe', message_storage)
        self.assertIn('Hello world!', message_storage['JohnDoe'])

    def test_get_all_messages(self):
        # Ensure the user has messages
        message_storage['JohnDoe'] = ['Hello world!']
        response = self.app.get('/get_all_messages?user=JohnDoe')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('JohnDoe', data)
        self.assertEqual(data['JohnDoe'], ['Hello world!'])

    def test_get_all_messages_user_not_found(self):
        response = self.app.get('/get_all_messages?user=JaneDoe')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'User not found')

if __name__ == '__main__':
    unittest.main()
