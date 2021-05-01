import server
import unittest

class MyAppIntegrationTestCase(unittest.TestCase):
    """Integration test"""

    def test_homepage(self):
        user = server.app
        result = client.get('/')
        self.assertIn(b'<h2>Register User</2>', result.data)

    










if __name__ == '__main__':
    from doctest import testmod
    if testmod().failed == 0:
        app.run(debug=True)