from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    login = StringField("Login2: ", validators=[Length(5)],
                        render_kw={"placeholder": "login name"})
    password = PasswordField("Password2: ", validators=[DataRequired()],
                             render_kw={"placeholder": "password"})
    submit = SubmitField("Submit")
