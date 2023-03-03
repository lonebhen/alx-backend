#!/usr/bin/env python3


from flask import Flask, request, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCAL = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/", methods=['GET'], strict_slashes=False)
def hello_world():
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
