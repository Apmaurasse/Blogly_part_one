from unittest import TestCase

from app import app
from models import db, User, Post

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()


class UserModelTestCase(TestCase):
    """Tests for model for User."""

    def setUp(self):
        """Delete any existing users."""
        User.query.delete()

    def tearDown(self):
        """Clean up any messed up operations."""
        db.session.rollback()

    def test_user_added(self):
        user = User(first_name="Test", last_name="Rogersonshiresville")
        db.session.add(user)
        db.session.commit()

        person = User.query.filter_by(first_name="Test").first()

        self.assertIsNotNone(person)

