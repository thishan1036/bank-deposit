import streamlit as st
import pandas as pd
import joblib

# load model and data
try:
    model = joblib.load('models/tuned_rf_mod.joblib')
    scaler = joblib.load('models/scaler.joblib')
    
    X_test_scaled = pd.read_csv('data/X_test_scaled.csv')
    model_cols = list(X_test_scaled.columns)
except FileNotFoundError:
    st.error('Model or data files not found.')
    st.stop()

# helper function to process inputs
def preprocess_inputs(age, job, marital, education, default, balance, housing, loan, contact, pdays, previous, poutcome, all_columns):
    binary_map = {'yes': 1, 'no': 0}
    raw_data = {
        'age': age,
        'job': job,
        'marital': marital,
        'education': education,
        'default': binary_map[default],
        'balance': balance,
        'housing': binary_map[housing],
        'loan': binary_map[loan],
        'contact': contact,
        'pdays': pdays,
        'previous': previous,
        'poutcome': poutcome
    }

    input_df = pd.DataFrame([raw_data])
    input_df = pd.get_dummies(input_df)
    input_df = input_df.reindex(columns=all_columns, fill_value=False)

    num_cols = ['age', 'balance', 'pdays', 'previous']
    input_df[num_cols] = scaler.transform(input_df[num_cols])

    return input_df

# app title and description
st.title('Bank Term Deposit Prediction')
st.write('This app predicts whether a customer will subscribe to a term deposit.')

# input widgets
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

# prediction button and output
if st.button('Predict Subscription Probability'):
    processed_input = preprocess_inputs(age, job, marital, education, default, balance, housing, loan, contact, pdays, previous, poutcome, model_cols)
    # probability score
    prediction_prob = model.predict_proba(processed_input)[0][1]
    # display the result
    st.subheader('Prediction Result:')
    st.write(f'**The predicted probability of subscription is: {prediction_prob:.1%}**')
    if prediction_prob > .5:
        st.success('This customer is likely to subscribe to a term deposit')
    else:
        st.error('This customer is not likely to subscribe to a term deposit')
