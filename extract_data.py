from ourapi  import OuraApiClient
import pandas as pd 
import datetime as dt
from sleep_viz import create_sleep_viz

def extract_data(token):
    now  = dt.date.today()

# API Documentation
# https://cloud.ouraring.com/v2/docs#section/Overview


# Instantiate Client 
    client = OuraApiClient(token)


# Extract Based on Data Genre
    sleep = client.query('sleep', '2023-12-01', now)
    stress = client.query('daily_stress', '2023-12-01', now)
    heart = client.query('heartrate', '2023-12-01', now)
    activity = client.query('daily_activity', '2023-12-01', now)


# Remove columns from Dataframes that we don't need 
    sleep.drop(['id', 'latency', 'period', 'sleep_algorithm_version', 'type'], axis=1)
    stress.drop(['id'], axis=1)
    heart.drop(['source'], axis=1)
    activity.drop(['id', 'inactivity_alerts'], axis=1)
    
# Make Dataframes global
    return sleep, stress, heart, activity


