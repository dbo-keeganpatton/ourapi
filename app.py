import streamlit as st
from ourapi import OuraApiClient  # Assuming your class is saved in this module
import plotly.express as px
import pandas as pd 


def main():
    

    st.set_page_config(layout='wide')
    st.title("Dark Oura")
    
    token = st.sidebar.text_input("Enter Oura API Token:")
    st.write("Get Access Token Here")
    st.write("https://cloud.ouraring.com/personal-access-tokens")
    start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2023-12-01"))
    end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("today"))

    if st.sidebar.button("Get my Data!"):
        if token:
            client = OuraApiClient(token)
            try:
                sleep_df, stress_df, heart_df, activity_df = client.extract_data(start_date, end_date)
                st.success("Data loaded successfully!")
                
                # Sleep
                st.write("Sleep Data", sleep_df)
                fig = client.create_sleep_viz()
                st.plotly_chart(fig)


                # Stress
                st.write("Stress Data", stress_df)
                
                # Heart Rate
                st.write("Heart Rate Data", heart_df)
                
                # Activity
                st.write("Activity Data", activity_df)
                

            except Exception as e:
                st.error(f"Failed to load data: {str(e)}")
        else:
            st.error("Please enter a valid token.")
    else:
        st.write("Enter a token and click 'Load Data' to view your Oura Ring data.")

if __name__ == "__main__":
    main()
