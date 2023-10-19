import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery
import datetime
druguomlist=['ML','MG','MCG','UNIT/ML']
freqlist=['Daily Once','Twice a day','Three times a day']


CREDS = r'medadsquad-8740fa9fa089.json'
client = bigquery.Client.from_service_account_json(json_credentials_path=CREDS)
# job = client.query(query)
table_name='medadsquad.patient_reg_db.patient_info'
def call_success_func():
    st.success("Patient Registration Successful!!")

def run_query():
    st.session_state["form_visible"]=False
    st.subheader("Patients Details")
    job = client.query("SELECT * FROM `medadsquad.patient_reg_db.patient_info` LIMIT 10")
    df=job.to_dataframe()
    
    st.table(df)
  
form_visible=st.session_state.get("form_visible",True)

#CREATING OUR FORM FIELDS
if form_visible:
    with st.form("form1", clear_on_submit=True):
      st.title("Patient Registration")
      st.subheader("Enter patient's details below")
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
      drug_str_uom=str(drugstr)+" "+str(druguom)
      submit = st.form_submit_button("Submit Details", on_click=call_success_func)
    if submit:
        st.write(patient_name)
        st.write(medication_time)
        # st.write(type(medication_time))
        drug_str_uom=str(drugstr) +" "+str(druguom[0])
        
        medication_time_hr=  str(medication_time).split(":")[0]
        medication_time_min=  str(medication_time).split(":")[1]
    
        
        medication_time = datetime.time(int(medication_time_hr),int(medication_time_min),0).strftime('%H:%M:%S')
        # medication_time=str(medication_time)
        # st.write(type(medication_time))
        insert_query = f""" INSERT INTO `medadsquad.patient_reg_db.patient_info` (patient_name , medication, dosage, doctor, interests,location, ml_nonadhere_score,medication_time,contact,seq_id, runstreak)
            VALUES ('{patient_name}', '{medication}', '{drug_str_uom}', '{doctor}', '{interests}','{location}',
            '{ml_nonadhere_score}', '{medication_time}','{contact}', '{seq_id}', '{streak_value}')"""
        
        client.query(insert_query)
            
        st.success("Form Submitted")

st.button("View Patients", on_click=run_query)


  
