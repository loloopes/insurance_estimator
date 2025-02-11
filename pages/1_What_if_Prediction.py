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
    
    
df_input = pd.DataFrame([{
    'age': age,
    'bmi': bmi,
    'children': children,
    'smoker': smoker
}])

def prediction(input):
    prediction = model.predict(input)[0]
    
    return prediction

# Predict
if st.button('Predict'):
    try:
        insurance = prediction(df_input)
        st.success(f'**Predicted insurance price:** ${insurance:.2f}')
    except Exception as error:
        st.error(f"Couldn't predict the input data. THe following error occurred: \n\n{error}")
        print(error)