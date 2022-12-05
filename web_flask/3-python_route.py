#!/usr/bin/python3
"""
script starts Flask web app
    listen on 0.0.0.0, port 5000
    routes: /:         display "Hello HBNB!"
            /hbnb:     display "HBNB"
            /c/<text>: display "C" + text (replace underscores with space)
"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """just a friendly hello"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """just another comment"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """
    just another comment:
        new_string: new string
    """
    new_string = text.replace("_", " ")
    return "C {}".format(new_string)

@app.route('/python/', defaults={'text': "is cool"})
def ptext(text):
    """
    just another comment:
        new_string: new string
    """
    new_string = text.replace("_", " ")
    return "Python {}".format(new_string)


if __name__ == '__main__':

    app.run(host="0.0.0.0", port=5000)
