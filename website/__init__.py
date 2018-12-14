from flask import Flask, render_template
from flask_scss import Scss
from flask_bootstrap import Bootstrap

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
        return render_template('projects.html')

    @app.route('/contact')
    def contact():
        return render_template('contact.html')

    return app