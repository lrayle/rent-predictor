#!/usr/bin/env python
#features.py

""""This module loads the feature data from a data table or database, given lat/long coordinates

"""
import pandas as pd
import psycopg2


DATA_DIR=os.path.join('..','data') 
"""Path to local data directory"""

#read postgres connection parameters
with open(os.path.join('..','postgres_config.json') as settings_file:    
    settings = json.load(settings_file)

DBNAME = settings['dbname']
USER = settings['user']
PASSWORD = settings['password']

conn_str = "dbname = {0} user = {1} password = {3}".format(DBNAME, USER, PASSWORD)

try:
    conn = psycopg2.connect(conn_str)
    cur = conn.cursor()
except:
    print ("Cannot connection. Check settings")


def get_feature_values(var_list,lng,lat):
    """Get block-level variable data from database, given lat/long
    Args: 
        var_list (list): list of variables to use. 
        lng (float): long coordinate
        lat (float): lat coordinate
    Returns: 
        DataFrame: pandas df with data. Colnames=feature names. 
    """
    # format list as SQL string
    var_string = ','.join(var_list)

    # Get data
    # This query gets the list of variables that matches the block which contains the lat/long point.
    query = "SELECT {vars} FROM block_vars v INNER JOIN blocks b ON v.block_id=b.blkidfp00 WHERE ST_Within(ST_SetSRID(ST_Point({x},{y}),4326), b.geom);".format(vars=var_string,x=lng,y=lat)
    cur.execute(query)
    results = cur.fetchall()
    df = pd.DataFrame(results, columns=var_list)

    # don't forget to include the lat /long values as features. 
    df['lng'] = lng
    df['lat'] = lat
    return df





