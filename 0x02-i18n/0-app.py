#!/usr/bin/env python3
"""A Basic Flask app with a single route"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_index() -> str:
    """Function that renders the 0-index.html"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
