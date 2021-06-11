from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo


class DestinationForm(FlaskForm):
    name = StringField('Country', validators=[InputRequired()])
    # adding two validators, one to ensure input is entered and other to check if the
    # description meets the length requirements
    description = TextAreaField('Description',
                                validators=[InputRequired()])
    image = StringField('Cover Image', validators=[InputRequired()])
    currency = StringField('Currency', validators=[InputRequired()])
    submit = SubmitField("Create")

class CommentForm(FlaskForm):
    text = TextAreaField('Comment', [InputRequired()])
    submit = SubmitField('Create')

# creates the login information

class LoginForm(FlaskForm):
    username = StringField("User Name", validators=[
                            InputRequired('Enter user name')])
    password = PasswordField("Password", validators=[
                             InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form

class RegisterForm(FlaskForm):
    username = StringField("User Name", validators=[InputRequired()])
    email = StringField("Email Address", validators=[
                           Email("Please enter a valid email")])

    # linking two fields - password should be equal to data entered in confirm
    password = PasswordField("Password", validators=[InputRequired(),
                                                     EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    # submit button
    submit = SubmitField("Register")
