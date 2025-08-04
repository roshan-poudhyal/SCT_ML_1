import streamlit as st
import json
import joblib
import numpy as np

# Load model and columns
model = joblib.load("bangalore_home_price_model.pkl")

with open("columns.json", "r") as f:
    data_columns = json.load(f)['data_columns']

# Input fields
st.title("🏠 Bengaluru House Price Predictor")
sqft = st.number_input("Total Square Feet", 500, 10000, step=50)
bhk = st.selectbox("BHK", [1, 2, 3, 4, 5])
bath = st.selectbox("Bathrooms", [1, 2, 3, 4])
location = st.selectbox("Location", sorted([col for col in data_columns if col not in ['total_sqft', 'bath', 'bhk', 'sqft_per_bhk', 'luxury_flag']] + ['other']))

# Predict button
if st.button("Predict Price"):
    # Construct input vector
    x = np.zeros(len(data_columns))
    x[data_columns.index('total_sqft')] = sqft
    x[data_columns.index('bath')] = bath
    x[data_columns.index('bhk')] = bhk
    x[data_columns.index('sqft_per_bhk')] = sqft / bhk
    x[data_columns.index('luxury_flag')] = 1 if (sqft * 100000 / sqft) > 10000 else 0

    if location in data_columns:
        loc_index = data_columns.index(location)
        x[loc_index] = 1

    price = model.predict([x])[0]
    st.success(f"🏷 Estimated Price: ₹{price:.2f} Lakhs")
