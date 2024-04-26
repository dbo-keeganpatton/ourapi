import pandas as pd 
import plotly.express as px  
from datetime import datetime as dt  
from utils import convert_to_min  
pd.set_option('display.max_columns', 500)

# Data Frame
csv = './data/activity.csv'
df = pd.read_csv(csv)

# high_activity_time
# low_activity_time
# medium_activity_time
# resting_time
# sedentary_time

# steps
# total_calories
# target_calories
# day 


activity_fig = px.bar(df, 
    x='day', 
    y=['high_activity_time', 'low_activity_time', 'medium_activity_time', 'resting_time', 'sedentary_time'])

activity_fig.update_layout(xaxis_type='category')
