# SingaporeResaleFlat

This project offers a streamlined solution for predicting Singapore resale flat prices using advanced machine learning models. It empowers users to forecast the resale value of flats by leveraging a user-friendly interface that simplifies data input. The application provides quick and accurate predictions, enabling informed decision-making for buyers, sellers, and real estate professionals alike. Through meticulous data preprocessing, feature engineering, and model tuning, the system ensures reliable outputs that cater to the unique dynamics of the Singaporean housing market.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Models](#models)

## Features

- **Resale Price Prediction**: Predict the resale price of a flat based on features such as town, flat type, flat model, floor area using a Random Forest Regressor model.
- **User-Friendly Interface**: Simple and easy-to-use interface built with Streamlit.
  
## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/anithag09/SingaporeResaleFlat.git
    ```

2. **Install the Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit App**:
    ```bash
    streamlit run SingaporeResale.py
    ```

## Usage

After running the Streamlit app, you can:

1. Access the app through your web browser.
2. Navigate through the sidebar menu to choose between "Price Prediction".
3. Enter the required input data in the provided fields.
4. Click on the "Predict" button to get the results.

## Data

Ensure that your input data is encoded and structured similarly to how the models were trained.

## Models

- **Random Forest Regressor**: Used for predicting the resale price for a flat based on input features.

The model is saved as pickle file and is loaded within the Streamlit application for making predictions.

The web application is deployed to Rendor platform.

<img width="1440" alt="Screenshot 2024-08-16 at 6 08 47 PM" src="https://github.com/user-attachments/assets/d710f307-2c82-4b09-9b46-53cfff51dbca">

