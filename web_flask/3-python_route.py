#!/usr/bin/python3
from flask import Flask
""" This is a Hello world code with different routes """


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Prints Hello HBNB """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Prints HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text=None):
    """ Prints with a parameter"""
    txt = text.replace('_', ' ')
    return 'C {}'.format(txt)


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ Prints with a parameter"""
    txt = text.replace('_', ' ')
    return 'Python {}'.format(txt)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
