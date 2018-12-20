from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators, ValidationError

class ContactForm(FlaskForm):
    name = StringField("Name", [validators.Required()])
    email = StringField("Email", [validators.Required(), validators.Email()])
    subject = StringField("Subject", [validators.Required()])
    message = TextAreaField("Message", [validators.Required()])
    submit = SubmitField("Send")