from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,\
    BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, Regexp


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')
