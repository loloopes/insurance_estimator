import os
import pickle

import pandas as pd
import streamlit as st

st.set_page_config(page_title='Insurance Prediction', page_icon='../../img/stethoscope.png')
st.sidebar.header('What if Prediction')
st.title('Insurance Prediction')

st.markdown("Predict medical insurance based on the following features:")

age = st.number_input(label='Age', value=18, min_value=18, max_value=120)
bmi = st.number_input(label='BMI', value=30.)
children = st.slider(label='Children', min_value=0, max_value=5)
smoker = st.selectbox(label='Smoker', options=['no', 'yes'])

# -- Model -- #
# Get the absolute path to the model file
model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../models/model.pkl'))

with open(model_path, 'rb') as file:
    model = pickle.load(file)
    
data = st.file_uploader("Upload your file")
if data:
    df_iput = pd.read_csv(data)
    insurance_prediction = model.predict(df_iput)
    df_output = df_iput.assign(predictions=insurance_prediction)
    
    st.markdown("Insurance cost prediction")
    st.write(df_output)
    st.download_button(
        label="Download CSV",
        data=df_output.to_csv(index=False),
        mime='text/csv',
        file_name='predicted_insurance.csv')