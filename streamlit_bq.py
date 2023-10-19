import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery
import os
st.title("Patient Registration")
st.subheader("Enter patient's details below")

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)
# st.write(type(client))
# st.write(client)
st.subheader("Enter patient's details below")
# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
# @st.cache_data(ttl=600)
def run_query(query):
    st.write(os.getcwd())
    CREDS = r'medadsquad-8740fa9fa089.json'
    client = bigquery.Client.from_service_account_json(json_credentials_path=CREDS)
    job = client.query(query)
    df=job.result().to_dataframe()
    st.table(df)
    # # st.write("Some wise words from Shakespeare:")
    # for row in job.result():
    #     st.write(row)


rows = run_query("SELECT patient_name FROM `medadsquad.patient_reg_db.patient_info` LIMIT 10")

# Print results.
# st.write("Some wise words from Shakespeare:")
# for row in rows:
#     st.write(" " + row['word'])
