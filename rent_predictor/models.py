#!/usr/bin/env python

import os
import numpy as np
import pandas as pd


"""This module loads a pre-fitted GB and uses it to make predictions given new values. 
It also gets the necessary features from a dataset. 
TODO: 
	- Load instance of fitted model
	- Load data needed to get values for features
	- Make prediction given new values.

"""

def run_model(input_values):
    """ Will run the model in a separate module. Just a placeholder for now """
    return input_values['sqft']*input_values['beds']*input_values['baths']*10000


#TODO: calculate these defaults. For now, using placeholders
def get_default_values():
    """Get median values"""
    return 

