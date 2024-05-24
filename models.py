# from flask_sqlalchemy import SQLAlchemy
#
# db = SQLAlchemy()
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
