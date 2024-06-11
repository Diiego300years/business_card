import re
import unittest
from app import create_app, db

class FlaskClientTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client(use_cookies=True)


    def test_concat_page(self):
        response = self.client.get('/wtf')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('stranger' in response.get_data(as_text=True))