import pandas as pd 
import plotly.express as px  
from datetime import datetime as dt  
pd.set_option('display.max_columns', 500)

# Data Frame
csv = './data/sleep.csv'
sleep_df  = pd.read_csv(csv)


def convert_to_min(df, lst):
    """Input List of Seconds formatted columns to convert to minutes"""

    for col in lst:
        df[f'{col}_min'] = (df[col] / 60).round(0)
        df.drop(col, axis=1,  inplace=True)

    return df[f'{col}_min']


conversion_columns_list = [
    'total_sleep_duration', 'time_in_bed', 'rem_sleep_duration', 'restless_periods',
    'light_sleep_duration', 'deep_sleep_duration', 'awake_time'
]


convert_to_min( 
    sleep_df,
    conversion_columns_list
)
sleep_df['record_date'] = pd.to_datetime(sleep_df['bedtime_start'], utc=True).dt.date


fig = px.line(sleep_df, x='record_date', y='rem_sleep_duration_min')
fig.show()
