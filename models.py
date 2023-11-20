import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://i.insider.com/602ee9ced3ad27001837f2ac?width=500&format=jpeg&auto=webp"

def connect_db(app):
    db.app = app
    db.init_app(app)

"""Models for Blogly."""

class User(db.Model):
    __tablename__= "users"


    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    first_name = db.Column(db.String(50),
                     nullable=False,
                     unique=False)
    
    last_name = db.Column(db.String(50),
                    nullable=False,
                    unique=False)

    image_url = db.Column(db.String(100),
                    nullable=False,
                    unique=False,
                    default=DEFAULT_IMAGE_URL)
    
    posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")

    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"
    
class Post(db.Model):

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    @property
    def friendly_date(self):

        return self.created_at.strftime("%a %b %-d  %Y, %-I:%M %p")