import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery
druguomlist=['ML','MG','MCG','UNIT/ML']
freqlist=['Daily Once','Twice a day','Three times a day']

st.title("Patient Registration")
st.subheader("Enter patient's details below")
CREDS = r'medadsquad-8740fa9fa089.json'
client = bigquery.Client.from_service_account_json(json_credentials_path=CREDS)
# job = client.query(query)
table_name='medadsquad.patient_reg_db.patient_info'
def call_success_func():
    st.success("Patient Registration Successful!!")

#CREATING OUR FORM FIELDS
with st.form("form1", clear_on_submit=True):
  seq_id=st.number_input('Enter Patient ID', min_value=0, max_value=1000)
  patient_name = st.text_input("Enter patient full name")
  medication = st.text_input("Enter medication name")
  drugstr = st.slider("Enter medication strength", min_value = 1, max_value = 1000)
  druguom = st.multiselect("Enter medication UOM",druguomlist)
  contact = st.number_input('Enter contact number', min_value=1000000000, max_value=9999999999)
  ml_nonadhere_score = st.number_input("Enter Patients Non Adherence Score", min_value=0.0, max_value=1.0,format="%.2f")
  doctor = st.text_input("Enter prescriber full name")
  medication_time = st.time_input('Enter medication time', value=None)
  frequency = st.multiselect("Enter medication frequency",freqlist)
  interests = st.text_area("Enter patients interests")
  location = st.text_input("Enter patient's city")
  streak_value=st.number_input('Enter patients streak value', min_value=0, max_value=10)
  submit = st.form_submit_button("Submit Details", on_click=call_success_func)
  drug_str_uom=str(drugstr)+" "+str(druguom)
  insert_query = f""" INSERT INTO `{table_name}` (patient_name, medication , dosage , doctor ,interests ,
  location ,ml_nonadhere_score , medication_time, contact ,seq_id , runstreak)
  VALUES ('{patient_name}', '{medication}', '{drug_str_uom}','{doctor}','{interests}','{location}','{ml_nonadhere_score}',
        '{medication_time}','{contact}','{streak_value}','{seq_id}')"""
  client.query(insert_query)
