#!/usr/bin/env python3

""" Force locale with URL parameter """

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """ Babel configuration """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Get locale from request """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    # Default to the best match from request.accept_languages
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ index page """
    return render_template('4-index.html',
                           title=_("home_title"), header=_("home_header"))


if __name__ == "__main__":
    app.run(debug=True)