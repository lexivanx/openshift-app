import unittest
import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    def test_home(self):
        rv = self.app.get('/')
        self.assertIn('Hello, World!', rv.data.decode())

if __name__ == '__main__':
    unittest.main()
