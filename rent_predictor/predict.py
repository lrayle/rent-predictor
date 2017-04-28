p#!/usr/bin/env python

import os
import pickle
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor


"""This module loads a pre-fitted GB and uses it to make predictions given new values. 
It also gets the necessary features from a dataset. 
TODO: 
	- Load instance of fitted model
	- Load data needed to get values for features
	- Make prediction given new values.

"""

DATA_DIR = os.path.join('data')
MODEL_FNAME = 'fitted_gb.p'
DATA_AVG_FNAME = 'data_averages.p'

def load_fitted_model():
	"""Load fitted model from pickled object. Return instance of model class"""
	# to load the pickled object: 
	
	try: 
		with open(os.path.join(DATA_DIR,MODEL_FNAME), 'rb') as pfile:
			fitted_model = pickle.load(pfile)
	except: 
		try:
			with open(os.path.join('..',DATA_DIR,MODEL_FNAME), 'rb') as pfile:
				fitted_model = pickle.load(pfile)
		except: 
			print('cannot find file {}'.format(os.path.join(DATA_DIR,MODEL_FNAME)))

	return fitted_model

def run_model(input_values):
    """ Runs prediction model"""
    gb = load_fitted_model()
    X = get_default_values()  # load X values
    y = gb.predict(X)  # predict Y

    # input_values['sqft']*input_values['beds']*input_values['baths']*10000   # just placeholder model
    return y[0]*input_values['sqft']


#TODO: calculate these defaults. For now, using placeholders
def get_default_values():
    """Get averages values"""
    try: 
    	with open(os.path.join(DATA_DIR,DATA_AVG_FNAME), 'rb') as pfile: 
	    	data = pickle.load(pfile)
    except:
        try:
            with open(os.path.join('..',DATA_DIR,DATA_AVG_FNAME), 'rb') as pfile: 
                data = pickle.load(pfile)
        except: 
                print('cannot find file {}'.format(os.path.join(DATA_DIR,DATA_AVG_FNAME)))
    print('loaded data. len:',len(data))
    return data



