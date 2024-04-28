#OurApi

Hello! This repo has two main files, ourapi and app. 

'''python
ourapi.py
'''
This will be the main file for connecting to Oura's API. It contains a class named __OuraApiClient__.
Simply import this class to instantiate a client instance and invoke various methods such as 
'''python
create_sleep_viz()
'''
to take specific actions with your data. You will need a personal access token to use the Oura API which 
can be obtained [here](https://cloud.ouraring.com/personal-access-tokens).

Refer to the [official API docs](https://cloud.ouraring.com/docs) if you need more substantial use than what is provided out of the box here.


'''python
app.py
'''
A simple Streamlit app to apply the OuraApiClient and extrapolate the data into a visualized application.

