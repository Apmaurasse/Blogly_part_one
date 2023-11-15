from unittest import TestCase

from app import app
from models import db, User

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

app.config['TESTING'] = True

app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class UserViewsTestCase(TestCase):
    """Tests for routes for users."""

    def setUp(self):
        """Add test user."""
        User.query.delete()

        user = User(first_name="Fakename", last_name="Notarealperson")
        db.session.add(user)
        db.session.commit()

        self.user_id = user.id

    
    def tearDown(self):
        """Clean up any messed up operations."""

        db.session.rollback()

    
    def test_list_users(self):
        with app.test_client() as client:
            resp = client.get("/users")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Fakename', html)

    def test_show_user(self):
        with app.test_client() as client:
            resp = client.get(f"users/{self.user_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Fakename Notarealperson</h1>', html)

    def test_not_a_user_page(self):
        with app.test_client() as client:
            resp = client.get("/users/500")

            self.assertEqual(resp.status_code, 404)


    def test_add_user(self):
        with app.test_client() as client:
            user_data = {"first_name": "Phoney", "last_name": "Joecool", "image_url": ""}
            resp = client.post("/users/new", data=user_data, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Phoney Joecool", html)       

    
