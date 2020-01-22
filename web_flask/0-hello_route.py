#!/usr/bin/python3
from flask import Flask
""" This is a Hello world code """


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Prints Hello HBNB """
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
