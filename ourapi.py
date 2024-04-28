import pandas as pd
import json
import requests
import datetime 
import plotly.express as px 

class OuraApiClient:
    
    def __init__(self, token):
        self.token = token  # Directly set the token
        self.base_url = 'https://api.ouraring.com/v2/usercollection'
        self.now  = datetime.date.today()
    

    def query(self, data_type, start_date, end_date):
        """Query Oura API presenting auth Token"""

        url = f'{self.base_url}/{data_type}'
        params = {'start_date': start_date, 'end_date': end_date}
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        df = pd.DataFrame(data['data'])

        return df
    
    
    def extract_data(self, start_date, end_date):
        """Create Dateframes from Various Metrics, 
        start_date and end_date are dynamically set in app.py"""

        self.sleep = self.query('sleep', start_date, end_date)
        self.stress = self.query('daily_stress', start_date, end_date)
        self.heart = self.query('heartrate', start_date, end_date)
        self.activity = self.query('daily_activity', start_date, end_date)
        
        return self.sleep, self.stress, self.heart, self.activity

     
    def create_sleep_viz(self):
        
        color_palete = ['#a8a6f8', '#5b8bda', '#5e8575', '#c9a76e']


        df = self.sleep[self.sleep['rem_sleep_duration']!=0]
        df['record_date'] = pd.to_datetime(df['bedtime_start'], utc=True).dt.date

        fig = px.bar(df, x='record_date', 
            y=['restless_periods', 'rem_sleep_duration', 'light_sleep_duration', 'deep_sleep_duration'],
            color_discrete_sequence=color_palete)
        
        fig.update_layout(xaxis_type='category', xaxis_title="", yaxis_title="")
     
        all_dates = df['record_date'].unique()
        tick_dates = all_dates[::5]  # Select every 5th date
        fig.update_xaxes(tickvals=tick_dates, ticktext=tick_dates, tickangle=45)
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
            ))

        return fig
        
    def create_stress_viz(self):
        color_palete = ['#5e8575']
        df = self.stress
        fig = px.line(df, x='day', y=['stress_high'], color_discrete_sequence=color_palete)
        fig.update_layout(xaxis_type='category', xaxis_title="", yaxis_title="")
        
        all_dates = df['day'].unique()
        tick_dates = all_dates[::5]  # Select every 5th date
        fig.update_xaxes(tickvals=tick_dates, ticktext=tick_dates, tickangle=45)
        
        fig.update_layout(showlegend=False)


        return fig


    def create_activity_viz(self):
        color_palete =  ['#a8a6f8', '#5b8bda', '#5e8575', '#c9a76e']       
        df = self.activity
        fig = px.bar(df, x='day', 
            y=['high_activity_time', 'low_activity_time', 'medium_activity_time', 'resting_time', 'sedentary_time'],
            color_discrete_sequence=color_palete)

        fig.update_layout(xaxis_type='category', xaxis_title="", yaxis_title="")
        
        all_dates = df['day'].unique()
        tick_dates = all_dates[::5]  # Select every 5th date
        fig.update_xaxes(tickvals=tick_dates, ticktext=tick_dates, tickangle=45)
        
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
            ))


        return fig


if __name__ == "__main__":
    token = 'your_actual_token_here'
    client = OuraApiClient(token)
    data_type = 'sleep'
    start_date = '2024-01-01'
    end_date = '2024-01-07'
    df = client.query(data_type, start_date, end_date)
    client.extract_data()
    fig = client.create_sleep_viz()
    fig.show()
