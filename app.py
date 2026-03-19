import streamlit as st
import pandas as pd
import pickle as pk

st.title("🏠 Bengaluru House Price Predictor")

st.write("Enter house details to predict price")

# Load model
@st.cache_resource
def load_model():
    model = pk.load(open(r"C:\\projects\\house_price_prediction\\House_price_prediction_model.pkl", "rb"))
    return model

model = load_model()

# Load dataset
@st.cache_data
def load_data():
    data = pd.read_csv(r"C:\\projects\\house_price_prediction\\cleaned_data_csv")
    return data

data = load_data()

# Remove unwanted column
if "Unnamed: 0" in data.columns:
    data = data.drop(columns=["Unnamed: 0"])

# User Inputs
location = st.selectbox("Choose Location", data["location"].unique())

sqft = st.number_input("Total Square Feet", min_value=300)

bath = st.number_input("Number of Bathrooms", min_value=1)

balcony = st.number_input("Number of Balconies", min_value=0)

bedrooms = st.number_input("Number of Bedrooms", min_value=1)

# Input dataframe
input_data = pd.DataFrame({
    "location":[location],
    "total_sqft":[sqft],
    "bath":[bath],
    "balcony":[balcony],
    "bedrooms":[bedrooms]
})

# Convert location to dummy variables
input_data = pd.get_dummies(input_data)

# Get model columns
model_columns = model.feature_names_in_

# Align columns
for col in model_columns:
    if col not in input_data.columns:
        input_data[col] = 0

input_data = input_data[model_columns]

# Prediction
if st.button("Predict Price"):
    
#     prediction = model.predict(input_data)

#     st.success(f"Estimated House Price: ₹ {prediction[0]:.2f} Lakhs")
    prediction = model.predict(input_data)

    price = max(0, prediction[0])

    st.success(f"Estimated House Price: ₹ {price:,.2f} Lakhs")