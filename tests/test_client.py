import unittest
from dotenv import load_dotenv
from flask import current_app
from app import create_app, db
import os

load_dotenv()

class FlaskSimpleTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testingConfigWithDocker')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exist(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        # print(current_app.config)
        self.assertTrue(current_app.config['TESTING'])

