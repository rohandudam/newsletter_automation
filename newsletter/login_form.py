"""Flask Form To Login Newsletter Automation app"""
from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField,SelectField,StringField, PasswordField
from wtforms.validators import DataRequired, Length,  Email, EqualTo


class LoginForm(FlaskForm):
    """User Log-in Form."""
    email = StringField('Email', validators=[ DataRequired(), Email(message='Enter a valid email.')])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')