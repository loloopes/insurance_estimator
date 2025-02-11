import streamlit as st

st.set_page_config(
    page_title='Insurance Prediction',
    page_icon='../img/stethoscope.png'
)

st.sidebar.header('Project Description')

st.write('# Welcome to the Insurance Prediction app')
st.write("\n\n")

st.markdown("""
            This App aims to predict the insruance cost using input features like:
            - age
            - BMI
            - Number of children
            - Smoker status
            """)

st.success('Please **go to the next pages** to get the predictions')