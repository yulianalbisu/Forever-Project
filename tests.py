import unittest 
from server import app
from model import connect_to_db, db
from flask import session
from test_seed  import create_example_data


class FlaskTests(unittest.TestCase):
    """Integration test for flask app"""

    def setUp(self):
        """Setting up, everytime"""

        self.client = app.test_client()
        app.config['TESTING'] = True

        connect_to_db(app, "postgresql:///testdb")
        db.create_all()
        create_example_data()

    def tearDown(self):
        """Dropping the table"""

        db.session.remove()
        db.drop_all()
        db.engine.dispose()

    def test_landing_route(self):
        """Testing the landing page"""

        result = self.client.get("/")
        self.assertEqual(result.status_code, 200)
        self.assertIn(b"Grow together with your partner...", result.data)

    def test_user_registration(self):
        """Test registration of user"""

        result = self.client.post("/",
                                    data={"email":"user5@gmail.com", "password":"user5", "name":"Cinco", "nickname":"Five", "anniversary":"12/5/2017"}, follow_redirects=True)
        self.assertIn(b"Email is associated with an account.", result.data)


class FlaskTestsSession(unittest.TestCase):
    """Testing a route that requires the user to be in session"""

    def setUp(self):
        """Setting up again"""

        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'key'
        self.client = app.test_client()

        connect_to_db(app, "postgresql:///testdb")
        db.create_all()
        create_example_data()

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1

    def tearDown(self):
        """Drop table down"""

        db.session.remove()
        db.drop_all()
        db.engine.dispose()

    def test_questions_form_page(self):
        """Test to answer the questions"""

        result = self.client.get("/questions", follow_redirects=True)
        self.assertIn(b"Love Quiz", result.data)
        self.assertNotIn(b"Login", result.data)

if __name__ == "__main__":
    import unittest

    unittest.main()    