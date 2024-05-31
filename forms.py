from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, EmailField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from models import User

class LoginForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6, max=40)])
    # remember_me = BooleanField('Remember Me')
    # submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6, max=40)])
    confirmPassword = PasswordField('confirmPasssord', validators=[DataRequired(), EqualTo('password')])
    # submit = SubmitField('Register')

    # def validate_username(self, username, present=None):
    #     user = User.query.filter_by(username=username.data).first()
    #     if user is not present:
    #         raise ValidationError('Please use a different username.')
    #
    # def validate_email(self, email):
    #     user = User.query.filter_by(email=email.data).first()
    #     if user:
    #         raise ValidationError('Please use a different email address.')
#
# class BookForm(FlaskForm):
#     title = StringField('Title', validators=[DataRequired()])
#     author = StringField('Author', validators=[DataRequired()])
#     description = TextAreaField('Description')
#     submit = SubmitField('Add Book')
