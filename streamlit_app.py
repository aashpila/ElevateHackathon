import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery
import datetime
druguomlist=['ML','MG','MCG','UNIT/ML']
freqlist=['Daily Once','Twice a day','Three times a day']


CREDS = r'hackathon101423-51887557308b.json'
client = bigquery.Client.from_service_account_json(json_credentials_path=CREDS)
# job = client.query(query)
table_name='hackathon101423.hackathon_data.patient_info'
def call_success_func():
    st.success("Patient Registration Successful!!")

def run_query():
    st.session_state["form_visible"]=False
    st.subheader("Patients Details")
    job = client.query("SELECT * FROM `hackathon101423.hackathon_data.patient_info` LIMIT 100")
    df=job.to_dataframe()
    
    st.table(df)
  
form_visible=st.session_state.get("form_visible",True)

#CREATING OUR FORM FIELDS
if form_visible:
    with st.form("form1", clear_on_submit=True):
      st.title("Patient Registration")
      st.subheader("Enter patient's details below")
      # seq_id=st.number_input('Enter Patient ID', min_value=0, max_value=1000)
      patient_name = st.text_input("Enter patient full name")
      patient_mobile = st.number_input('Enter contact name', min_value=0000000000, max_value=9999999999)
      patient_country = st.text_input("Enter Country")
      medication = st.text_input("Enter medication name")
      drugstr = st.text_input("Enter medication strength")
      druguom = st.selectbox("Enter medication UOM",druguomlist)
      doctor = st.text_input("Enter prescriber full name")
      interests = st.text_area("Enter patients interests")
      location = st.text_input("Enter patient's city")  
      ml_nonadhere_score = st.number_input("Enter Patients Non Adherence Score", min_value=0.0, max_value=1.0,format="%.2f")
      medication_time = st.time_input('Enter medication time', value=None)
      Relation_contact_name = st.text_input("Enter Relation contact full name")
      streak_value=st.number_input('Enter patients streak value', min_value=0, max_value=10)
      frequency = st.selectbox("Enter medication instructions ",freqlist)
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
        insert_time=datetime.datetime.now()
        # medication_time=str(medication_time)
        # st.write(type(medication_time))
        insert_query = f""" INSERT INTO `hackathon101423.hackathon_data.patient_info`
(patient_name ,patient_mobile, country, medication,dosage, doctor ,interests,location,ml_nonadherence_score,medication_time,contact,insert_time,instructions)
VALUES ('{patient_name}','{patient_mobile}','{patient_country}', '{medication}','{drug_str_uom}', '{doctor}','{interests}','{location}',
'{ml_nonadhere_score}','{medication_time}','{Relation_contact_name}','{insert_time}', '{frequency}'

)"""

        client.query(insert_query)
            
        st.success("Form Submitted")

st.button("View Patients", on_click=run_query)


  
