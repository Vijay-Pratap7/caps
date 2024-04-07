import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load the trained model
with open('best_model1.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to preprocess input data
def preprocess_input(data):
    # Define categorical columns
    categorical_cols = ['fuel', 'seller_type', 'transmission', 'owner', 'car_maker', 'car_model']

    # Apply label encoding and one-hot encoding
    encoder = LabelEncoder()
    data_encoded = data.copy()
    for col in categorical_cols:
        data_encoded[col] = encoder.fit_transform(data[col])
    return data_encoded

# Function to predict car selling price
def predict_selling_price(data):
    # Preprocess input data
    data_processed = preprocess_input(data)
    # Predict selling price
    prediction = model.predict(data_processed)
    return prediction

# Streamlit app
def main():
    st.title('Car Selling Price Prediction')

    # Input form
    st.sidebar.header('Input Features')
    name = st.selectbox("Select Car Name", options = data["name"].unique())
    st.write(name)
    plit = name.split(" ")
    car_maker = split[0]
    car_model = split[1]
    fuel = st.sidebar.selectbox('Fuel', ['Petrol', 'Diesel', 'CNG', 'LPG', 'Electric'])
    seller_type = st.sidebar.selectbox('Seller Type', ['Individual', 'Dealer', 'Trustmark Dealer'])
    transmission = st.sidebar.selectbox('Transmission', ['Manual', 'Automatic'])
    owner = st.sidebar.selectbox('Owner', ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'])
    year = st.sidebar.number_input('Year', min_value=1980, max_value=2023)
    km_driven = st.sidebar.number_input('Kilometers Driven', min_value=0)

    # Prepare input data
    input_data = pd.DataFrame({
        'fuel': [fuel],
        'seller_type': [seller_type],
        'transmission': [transmission],
        'owner': [owner],
        'car_maker': [car_maker],
        'car_model': [car_model],
        'year': [year],
        'km_driven': [km_driven]
    })

    # Predict selling price
    if st.sidebar.button('Predict'):
        prediction = predict_selling_price(input_data)
        st.sidebar.header('Prediction')
        st.sidebar.write(f'Predicted Selling Price: {prediction[0]}')

if __name__ == '__main__':
    main()
