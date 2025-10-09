import streamlit as st
import pandas as pd
import joblib

model = joblib.load('models/tuned_rf_mod.joblib')
scaler = joblib.load('models/scaler.joblib')

X_test_scaled = pd.read_csv('data/X_test_scaled.csv')
model_cols = X_test_scaled.columns

st.title('Bank Term Deposit Prediction')
st.write('This app predicts whether a customer will subscribe to a term deposit.')

st.header('Enter Customer Information:')

col1, col2 = st.columns(2)

with col1:
    age = st.number_input('Age', min_value=18, max_value=100, value=40)
    job = st.selectbox('Job', options=['management', 'technician', ' entrepreneur', 'blue-collar', 'unknown', 'retired', 
                                       'admin.', 'services', 'self-employed', 'unemployed', 'housemaid', 'student'])
    marital = st.selectbox('Marital Status', options=['married', 'single', 'divorced'])
    education = st.selectbox('Education', options=['tertiary', 'secondary', 'unknown', 'primary'])

with col2:
    default = st.selectbox('Has Credit in Default?', options=['no', 'yes'])
    balance = st.number_input('Average Yearly Balance (€)', value=1500)
    housing = st.selectbox('Has Housing Loan?', options=['no', 'yes'])
    loan = st.selectbox('Has Personal Loan?', options=['no', 'yes'])

st.header('Previous Campaign Information:')
col3, col4, col5 = st.columns(3)

with col3:
    contact = st.selectbox('Contact Communication Type', options=['unknown', 'cellular', 'telephone'])

with col4:
    pdays = st.number_input('Days Since Last Contact (-1 if not contacted)', value=-1)

with col5:
    previous = st.number_input('Number of Contacts Before This Campaign', value=0)

poutcome = st.selectbox('Outcome of Previous Campaign', options=['unknown_outcome', 'failure', 'other', 'success'])