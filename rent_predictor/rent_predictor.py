#!/usr/bin/env python
# rent_predictor.py

"""This app estimates a rental price based on user input

    TODO: 
        - add fitted model
        - add map to get lat/long from user input
        - figure data table/database to get feature values based on lat/long
        - add confidence interval
"""


# all the imports
import os
from flask import Flask, request, g, redirect, url_for, render_template, flash
from sqlite3 import dbapi2 as sqlite3
import models as md
import features as ft


app = Flask(__name__) # create the application instance :)
app.config.from_object('config') # load config from this file, config.py 


   
def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/', methods=['GET'])  # this executes when client loads page
def index():
    # TODO: Maybe initially fill form with default values, rather than as example
    #feature_values = models.get_default_values()
    return render_template('index.html', prediction=None)


@app.route('/', methods=['POST'])  
def make_prediction(): 
    # In this case, get the form input and pass values to the model
    # TODO: More specific form validation. (Specify what input was wrong and why.)
    feature_values = {}
    errors = []
    
    # get rental unit feature values
    try:
        feature_values['sqft'] = float(request.form['sqft'])
        feature_values['beds'] = float(request.form['beds'])
        feature_values['baths'] = float(request.form['baths'])

    except:
        errors.append('Please enter valid numbers')
        return render_template('index.html', errors=errors)

    # # TODO: get lat/long coordinates
    # try: 
    #     # feature_values['lng'] = ...
    #     # feature_values['lat'] = ... 
    # except:
    #     errors.append('Please choose a location within Bay Area')
    #     return render_template('index.html', errors=errors)

    # # TODO: look up feature values based on coordinates
    #df_features = ft.get_feature_values(var_list=VARLIST, lng=features_values['lng'], lat=features_values['lat'])

    # run the prediction model
    prediction = md.run_model(df_features)
    prediction = '{:,.0f}'.format(prediction)
    return render_template('index.html', feature_values=feature_values, prediction=prediction)


