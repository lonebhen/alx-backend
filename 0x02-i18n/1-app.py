#!/usr/bin/env python3


from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)

babel = Babel(app)


class Config:
    """Config Languages and timezones"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCAL = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/", methods=["GET"])
def hello_world():
    """render template"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
