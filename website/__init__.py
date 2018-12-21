import os

from flask import Flask, render_template, redirect, flash, request
from flask_scss import Scss
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from flask_mail import Message, Mail

from .forms import ContactForm
from .projects import PROJECTS

def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
    app.config["MAIL_SERVER"] = "smtp.gmail.com"  # wouldn't hardcode this if it wasn't a personal site, but I know for a fact I use gmail
    app.config["MAIL_PORT"] = 465
    app.config["MAIL_USE_SSL"] = True
    app.config["MAIL_USERNAME"] = os.environ['EMAIL_USER']
    app.config["MAIL_PASSWORD"] = os.environ['EMAIL_PASS']
    
    Bootstrap(app)
    Scss(app)
    CSRFProtect(app)
    mail = Mail(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/projects')
    def projects():
        return render_template('projects.html', PROJECTS=PROJECTS)

    @app.route('/contact', methods=('GET', 'POST'))
    def contact():
        form = ContactForm()
        if form.validate_on_submit():
            msg = Message(form.subject.data, sender=app.config['MAIL_USERNAME'], recipients=[app.config['MAIL_USERNAME']])
            msg.body = f"Someone sent you a message from brianbowyer.com:\n\nFrom {form.name.data} <{form.email.data}>\n{form.message.data}"
            mail.send(msg)
            return redirect('/success')
        elif request.method == 'POST':  # this means that we failed validation
            for key, error_list in form.errors.items():
                for error in error_list:
                    flash(error)
        return render_template('contact.html', form=form)

    @app.route('/success')
    def success():
        return "Success!"

    return app