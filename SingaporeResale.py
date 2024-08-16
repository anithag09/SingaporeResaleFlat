import streamlit as st
import pandas as pd
import numpy as np
import pickle
from streamlit_option_menu import option_menu

# Load the cleaned data
data = pd.read_csv('/Users/anithasmac/PycharmProjects/SingaporeFlat/SingaporeResaleFlat/Data.csv')

# Extract unique types for the dropdown
town = data['town'].unique()
flat_type = data['flat_type'].unique()
storey_range = data['storey_range'].unique()
flat_model = data['flat_model'].unique()

# Load the model
with open('RandomForest.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Streamlit setup
st.set_page_config(page_title="Singapore Resale Flat Prices Prediction", layout="wide")
st.header(':orange[Singapore Resale Flat Prices Prediction]')

with st.sidebar:
    selected = option_menu("Menu", ["Home", "Price Prediction"], 
        icons=['house', 'currency-exchange'], menu_icon="menu-button"
       )

if selected == "Home":
    st.write(" ")
    st.markdown("### :blue[Tools Used:] Pandas, Data Cleaning, Streamlit, ML Algorithms, Render")
    st.markdown("### :blue[About the Project:] This project offers a streamlined solution for predicting Singapore resale flat prices using advanced machine learning models. It empowers users to forecast the resale value of flats by leveraging a user-friendly interface that simplifies data input. The application provides quick and accurate predictions, enabling informed decision-making for buyers, sellers, and real estate professionals alike.")
    st.markdown("### :blue[Domain:] Real Estate")
    st.write(" ")
    st.markdown("### Dataset: [Click Here](https://beta.data.gov.sg/collections/189/view).")

if selected == "Price Prediction":

    st.write("### Resale Price Prediction")
    town = st.selectbox("Select a Town", options=town)
    flat_type = st.selectbox("Select Flat Type", options=flat_type)
    storey_range = st.selectbox("Select Storey Range", options=storey_range)
    floor_area_sqm = st.number_input("Area (sq.m)", min_value=0.0, step=50.0, value=50.0)
    flat_model = st.selectbox("Select Flat Model", options=flat_model)
    lease_commence_date = st.number_input("Lease Commence Date", min_value=1900, max_value=2100, value=2018, step=1)
    year = st.number_input("Year of Sale", min_value=1900, max_value=2100, value=2018, step=1)

    if lease_commence_date > year:
        st.error("Lease Commence Date must be less than or equal to Year of Sale.")
    else:
        new_data = pd.DataFrame({
            'town': [town],
            'flat_type': [flat_type],
            'storey_range': [storey_range],
            'floor_area_sqm': [floor_area_sqm],
            'flat_model': [flat_model],
            'lease_commence_date': [lease_commence_date],
            'year': [year]
        })
        
        # Predict the price
        if st.button("Predict Resale Price"):
            predicted_price = loaded_model.predict(new_data)
            st.success(f"Predicted Resale Price: ${np.exp(predicted_price[0]):,.2f}")
