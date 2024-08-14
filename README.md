# SingaporeResaleFlat

This project provides a web-based application for predicting the selling price of items and the status of business transactions using machine learning models. The application is built using [Streamlit](https://streamlit.io/) and allows users to input relevant data through an intuitive interface.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Models](#models)

## Features

- **Resale Price Prediction**: Predict the resale price of a flat based on features such as town, flat type, flat model, floor area using a Random Forest Regressor model.
- **User-Friendly Interface**: Simple and easy-to-use interface built with Streamlit.
- **Rendor Platform**: The web application is deployed to Rendor platform for public use.
  
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

