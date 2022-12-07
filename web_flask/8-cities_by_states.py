#!/usr/bin/python3
'''
connection between the database and
front
'''
from models.state import State
from models.state import *
from flask import Flask, render_template
from models import storage
from models import *
import sys
import os
sys.path.append("..")

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """just a friendly hello"""
    return "Hello HBNB!"


@app.route('/states_list', strict_slashes=False)
def hello1():
    data = storage.all(State).values()
    return render_template('7-states_list.html', data=data)


@app.route('/cities_by_states', strict_slashes=False)
def hello2():
    data = storage.all(State).values()
    return render_template('8-cities_by_states.html', data=data)


@app.teardown_appcontext
def tear_down(self):
    """after each request remove current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
