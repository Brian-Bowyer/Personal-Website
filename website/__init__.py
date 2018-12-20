import os
from collections import namedtuple

from flask import Flask, render_template, redirect, flash, request
from flask_scss import Scss
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from flask_mail import Message, Mail

from .forms import ContactForm

Project = namedtuple('Project', ['filename', 'title', 'description'])
PROJECTS = [
    #Project('bagofnouns.jpg', 
    #        "Bag of Nouns", 
    #        "Web app to play the game Bag of Nouns (also sometimes called Monikers)"),
    #Project('bta.jpg', 
    #        "Bubble Turtle Adventure", 
    #        "Sidescrolling video game"),
    Project('blorb.png', 
            "Blorb", 
            "Procedurally generated resource-collecting video game with infinite map"),
    #Project('story_scraper.jpg', 
    #        "Story Scraper", 
    #        "Computational linguistics class project which scraped large amounts of fanfiction to produce linguistic corpus"),
    Project('self.jpg', 
            "This Very Website", 
            "This website! The one that you are reading right now.")
]


def create_app(test_config=None):
    app = Flask(__name__)
    Bootstrap(app)
    Scss(app)
    CSRFProtect(app)
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

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