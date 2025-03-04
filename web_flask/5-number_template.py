#!/usr/bin/python3
"""
script starts Flask web app
    listen on 0.0.0.0, port 5000
    routes: /:         display "Hello HBNB!"
            /hbnb:     display "HBNB"
            /c/<text>: display "C" + text (replace underscores with space)
"""


from flask import Flask, render_template


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
@app.route('/python/<text>')
def ptext(text):
    """
    just another comment:
        new_string: new string
    """
    new_string = text.replace("_", " ")
    return "Python {}".format(new_string)


@app.route('/number/<int:n>')
def ntext(n):
    """
    just another comment:
        n: must be a number
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def template_1(n):
    '''first template attempt'''
    data = n
    return render_template('5-number.html', data=data)


if __name__ == '__main__':
    '''dont know'''
    app.run(host="0.0.0.0", port=5000)
