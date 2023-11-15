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

    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"