from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired,Length,Email,EqualTo


class RegisterForm(FlaskForm):
    username = StringField("Username",validators=[InputRequired(),Length(min=3,max=50)])
    email = StringField("Email",validators=[InputRequired(),Email()])
    password = PasswordField("Password",validators=[InputRequired(),Length(min=8)])
    confirm_password = PasswordField("COnfirm Password",validators = [InputRequired(),EqualTo("password")])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = StringField("Email",validators=[InputRequired(),Email()])
    password = PasswordField("Password",validators=[InputRequired()])
    submit = SubmitField("Login")




