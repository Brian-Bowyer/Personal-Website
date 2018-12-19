from flask import Flask, render_template
from flask_scss import Scss
from flask_bootstrap import Bootstrap
from collections import namedtuple
Project = namedtuple('Project', ['filename', 'title', 'description'])

PROJECTS = [
    Project('bagofnouns.jpg', 
            "Bag of Nouns", 
            "Web app to play the game Bag of Nouns (also sometimes called Monikers)"),
    Project('bta.jpg', 
            "Bubble Turtle Adventure", 
            "Sidescrolling video game"),
    Project('blorb.png', 
            "Blorb", 
            "Procedurally generated resource-collecting video game with infinite map"),
    Project('story_scraper.jpg', 
            "Story Scraper", 
            "Computational linguistics class projects which scraped large amounts of fanfiction to produce linguistic corpus"),
    Project('self.jpg', 
            "This Very Website", 
            "This website! The one that you are reading right now.")
]

def create_app(test_config=None):
    app = Flask(__name__)
    Bootstrap(app)
    Scss(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/projects')
    def projects():
        return render_template('projects.html', PROJECTS=PROJECTS)

    @app.route('/contact')
    def contact():
        return render_template('contact.html')

    return app