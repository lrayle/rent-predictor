#!/usr/bin/env python
# all the imports
import os
from flask import Flask, request, redirect, url_for, render_template, flash
import models as md


app = Flask(__name__) # create the application instance :)
app.config.from_object('config') # load config from this file, config.py 


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
   
    try:
        feature_values['sqft'] = float(request.form['sqft'])
        feature_values['beds'] = float(request.form['beds'])
        feature_values['baths'] = float(request.form['baths'])
    except:
        errors.append('Please enter valid numbers')
        return render_template('index.html', errors=errors)

    # run the prediction model
    prediction = md.run_model(feature_values)
    prediction = '{:,.0f}'.format(prediction)
    return render_template('index.html', feature_values=feature_values, prediction=prediction)




