from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo



class DestinationForm(FlaskForm):
  name = StringField('Country', validators=[InputRequired()])
  # adding two validators, one to ensure input is entered and other to check if the 
  #description meets the length requirements
  description = TextAreaField('Description', 
            validators=[InputRequired()])
  image = StringField('Cover Image', validators=[InputRequired()])
  currency = StringField('Currency', validators=[InputRequired()])
  submit = SubmitField("Create")
  
  #this should already be there in the forms.py
  
class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [InputRequired()])
  submit = SubmitField('Create')

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[InputRequired("Please enter your username")])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    email = StringField('Email', validators=[Email("Please enter an email address")])
    password = PasswordField('Password', validators=[InputRequired(),
        EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    submit = SubmitField('Register')