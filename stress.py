import pandas as pd 
import plotly.express as px  
from datetime import datetime as dt  
from utils import convert_to_min  
pd.set_option('display.max_columns', 500)

# Data Frame
csv = './data/stress.csv'
df = pd.read_csv(csv)

stress_fig = px.line(df, 
    x='day', 
    y=['stress_high'])

stress_fig.update_layout(xaxis_type='category')
