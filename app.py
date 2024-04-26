import streamlit as st
from ourapi import OuraApiClient  # Assuming your class is saved in this module
import plotly.express as px
import pandas as pd 


def main():
    

    st.set_page_config(layout='wide')
    st.title("Dark Oura")
    
    token = st.sidebar.text_input("Enter Oura API Token:")
    start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2023-12-01"))
    end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("today"))
    
    if st.sidebar.button("Get my Data!"):
        
        
        #########################################
        #       If Token is Valid Proceed       # 
        #########################################
        if token:
            client = OuraApiClient(token)
           

            #####################################
            #         Main Application          #
            #####################################
            try:
                sleep_df, stress_df, heart_df, activity_df = client.extract_data(start_date, end_date)
                st.success("Data loaded successfully!")
                
                # Sleep
                st.write("Sleep Data", sleep_df)
                sleep_fig = client.create_sleep_viz()
                st.plotly_chart(sleep_fig)


                # Stress
                st.write("Stress Data", stress_df)
                stress_fig = client.create_stress_viz()
                st.plotly_chart(stress_fig)
                

                # Activity
                st.write("Activity Data", activity_df)
                activity_fig = client.create_activity_viz()
                st.plotly_chart(activity_fig)

                # Heart Rate
                st.write("Heart Rate Data", heart_df)
                


            ##########################################
            #        End of Main Application         # 
            ########################################## 

            except Exception as e:
                st.error(f"Failed to load data: {str(e)}")
        else:
            st.error("Please enter a valid token.")
    else:
        
        ###################################################
        # Once a Token is Presented the below Disappears  #
        ###################################################

        st.write("Sign in to Oura Web here: https://cloud.ouraring.com/user/sign-in ")
        st.write("Then create access token here: https://cloud.ouraring.com/personal-access-tokens")
        st.image('./images/sample_token.png')
        st.write("Enter your Personal Access Token into the sidebar and set dates to view!")



if __name__ == "__main__":
    main()
