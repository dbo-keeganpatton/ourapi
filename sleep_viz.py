import pandas as pd 
import plotly.express as px  
from datetime import datetime as dt  
from utils import convert_to_min  
pd.set_option('display.max_columns', 500)


def create_sleep_viz(df):

    df = df[df['rem_sleep_duration']!=0]
    df['record_date'] = pd.to_datetime(df['bedtime_start'], utc=True).dt.date
    
    conversion_columns_list = [ 
        'total_sleep_duration', 
        'time_in_bed', 
        'rem_sleep_duration',
        'restless_periods', 
        'light_sleep_duration', 
        'deep_sleep_duration', 
        'awake_time'
    ]

    convert_to_min(df, conversion_columns_list)

    fig = px.bar(df, 
        x='record_date', 
        y=['restless_periods_min',
           'rem_sleep_duration_min', 
           'light_sleep_duration_min', 
           'deep_sleep_duration_min'
           ])

    fig.update_layout(xaxis_type='category')

    return fig
