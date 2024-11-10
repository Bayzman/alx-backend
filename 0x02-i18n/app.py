#!/usr/bin/env python3

""" Display the current time """

from flask import Flask, render_template, request, g
from flask_babel import Babel, _, gettext
import pytz
from pytz.exceptions import UnknownTimeZoneError
from datetime import datetime

app = Flask(__name__)


class Config:
    """Configuration class for supported languages and default settings."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """ Retrieve a user from the users dictionary
       based on the login_as parameter.
    """
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """Set the current user in flask.g before each request."""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """ Determine the best match for supported languages,
        following the specified priority.
    """
    # 1. Check for locale in URL parameters
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    # 2. Check user's preferred locale, if logged in
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']

    # 3. Check for locale in request headers
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """ Determine the best match for supported time zones,
        following the specified priority.
    """
    # 1. Check for timezone in URL parameters
    timezone = request.args.get('timezone')
    if timezone:
        try:
            return pytz.timezone(timezone).zone
        except UnknownTimeZoneError:
            pass  # Invalid timezone; fall back to the next option

    # 2. Check user's preferred timezone, if logged in
    if g.user and g.user.get('timezone'):
        try:
            return pytz.timezone(g.user['timezone']).zone
        except UnknownTimeZoneError:
            pass  # Invalid timezone; fall back to the default

    # 3. Default timezone
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index():
    """ Render the homepage with the
        current time in the user's inferred time zone.
    """
    # Get the user's timezone
    user_timezone = pytz.timezone(get_timezone())

    # Get current time in that timezone
    current_time = datetime.now(user_timezone)

    # Format time for display in the current locale
    formatted_time = current_time.strftime("%b %d, %Y, %I:%M:%S %p")
    if get_locale() == 'fr':
        formatted_time = current_time.strftime("%d %b %Y à %H:%M:%S")

    # Display translated time in the template
    current_time_message = gettext("current_time_is") % {'current_time':
                                                         formatted_time}
    return render_template('index.html',
                           current_time_message=current_time_message)


if __name__ == "__main__":
    app.run(debug=True)
