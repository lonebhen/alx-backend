#!/usr/bin/env python3

"""
    Languages
"""

from flask import Flask, request, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """lang config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """best language"""
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/", methods=['GET'], strict_slashes=False)
def hello_world():
    """Hello"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
