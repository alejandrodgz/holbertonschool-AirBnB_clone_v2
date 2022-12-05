#!/usr/bin/python3

'''comments without meaning'''

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''just a friendly hello'''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def text(text):
    new_string = text.replace("_"," ")
    return f"C {new_string}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
