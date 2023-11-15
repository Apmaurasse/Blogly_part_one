from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://images.app.goo.gl/b523bBuZ6NbKBYRD9"

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

    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"