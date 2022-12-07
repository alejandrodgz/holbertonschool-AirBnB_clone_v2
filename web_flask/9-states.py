#!/usr/bin/python3
'''states in a html page'''
from flask import Flask, render_template
from models import storage
from models import *
import sys
from models.state import State
sys.path.append("..")

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def first_page():
    '''first page'''
    return "Welcome to the best hbnb page ever"


@app.route('/states', strict_slashes=False)
def states_page():
    '''state page'''
    data = storage.all(State).values()
    return render_template('7-states_list.html', data=data)


@app.route('/states/<id>', strict_slashes=False)
def states_page_id(id):
    '''state page id'''
    data = storage.all(State).values()
    return render_template('9-states.html', data=data, id_url=id)


@app.teardown_appcontext
def teardown(self):
    '''teardown page after sql calling'''


if "__main__" == __name__:
    app.run(host='0.0.0.0', port=5000, debug=True)
