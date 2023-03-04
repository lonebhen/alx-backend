#!/usr/bin/env python3


from flask import Flask, request, render_template, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCAL = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.before_request
def before_request():
    g.user = get_user()


def get_locale():
    loc = request.args.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


def get_user():
    ID = request.args.get('login_as')

    if ID and int(ID) in users:
        return users[int(ID)]
    return None


@app.route("/", methods=['GET'], strict_slashes=False)
def hello_world():
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
