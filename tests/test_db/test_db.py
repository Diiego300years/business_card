import unittest
from app.models.admin import Admin

class AdminModelTestCase(unittest.TestCase):
    def test_set_password(self):
        u = Admin(password="jiji")
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        a = Admin(password='cat')
        with self.assertRaises(AttributeError):
            a.password