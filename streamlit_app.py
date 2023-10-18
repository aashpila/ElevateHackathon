import streamlit as st
druguomlist=['ML','MG','MCG','UNIT/ML']
freqlist=['Daily Once','Twice a day','Three times a day']

st.title("Patient Registration")
st.subheader("Enter patient's details below")

#CREATING OUR FORM FIELDS
with st.form("form1", clear_on_submit=True):
  patient_name = st.text_input("Enter patient full name")
  medication = st.text_input("Enter medication name")
  drugstr = st.slider("Enter medication strength", min_value = 1, max_value = 1000)
  druguom = st.multiselect("Enter medication UOM",druguomlist)
  contact = st.number_input('Enter contact number', min_value=1000000000, max_value=9999999999)
  doctor = st.text_input("Enter prescriber full name")
  medication_time = st.time_input('Enter medication time', value=None)
  frequency = st.multiselect("Enter medication frequency",freqlist)
  interests = st.text_area("Enter patient's interests")
  location = st.text_input("Enter patient's city")
  submit = st.form_submit_button("Submit Details")
