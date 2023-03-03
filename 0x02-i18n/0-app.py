#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    """render template"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
