from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)  # Store hashed passwords
    books = db.relationship('Book', backref='user', lazy=True)  # Defines the relationship

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100))
    # description = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

# class Book(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     author = db.Column(db.String(100), nullable=True)
#     image_url = db.Column(db.String(255), nullable=True)
#     description = db.Column(db.Text, nullable=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password = db.Column(db.String(80), nullable=False)
#     # Additional fields and relationships can be defined here.
#
# class Book(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(150), nullable=False)
#     author = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.String(500))
#     read = db.Column(db.Boolean, default=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     # This sets a relationship with the User who owns this book.
from datetime import datetime
# from app import db


