from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField
from wtforms.validators import DataRequired, Email, Length, EqualTo
# from models import User

class LoginForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6, max=40)])


class RegistrationForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6, max=40)])
    confirmPassword = PasswordField('confirmPasssord', validators=[DataRequired(), EqualTo('password')])

