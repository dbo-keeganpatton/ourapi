import pandas as pd 
import json 
import requests


class OuraApiClient:

    def __init__(self, token_path='./secrets/secret.json'):
        self.token = self.load_token(token_path)
        self.base_url = 'https://api.ouraring.com/v2/usercollection'
    
    def load_token(self, token_path):
        with open(token_path) as f:
            data = json.load(f)
            return data['secret']

    def query(self, data_type, start_date, end_date):

        url = f'{self.base_url}/{data_type}'
        params = {'start_date': start_date  , 'end_date': end_date }
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        df = pd.DataFrame(data['data'])
        return df


if __name__ == "__main__":
    client = OuraApiClient



