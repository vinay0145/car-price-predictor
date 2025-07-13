import streamlit as st
import pandas as pd
import joblib

model = joblib.load('model.pkl')

st.title("🚗 Car Price Prediction")

with st.form("input_form"):
    year = st.number_input("Year", min_value=1990, max_value=2025, value=2015)
    price = st.number_input("Present Price (Lakhs)", value=5.0)
    kms = st.number_input("KMs Driven", value=30000)
    owner = st.selectbox("Owner count", [0, 1, 2, 3])
    fuel = st.selectbox("Fuel", ["Petrol", "Diesel", "CNG"])
    seller = st.selectbox("Seller Type", ["Dealer", "Individual"])
    trans = st.selectbox("Transmission", ["Manual", "Automatic"])
    submit = st.form_submit_button("Predict")

if submit:
    fuel_petrol = 1 if fuel == 'Petrol' else 0
    fuel_diesel = 1 if fuel == 'Diesel' else 0
    seller_indiv = 1 if seller == 'Individual' else 0
    trans_manual = 1 if trans == 'Manual' else 0

    input_df = pd.DataFrame([[year, price, kms, owner, fuel_diesel, fuel_petrol, seller_indiv, trans_manual]],
                            columns=['Year', 'Present_Price', 'Kms_Driven', 'Owner',
                                     'Fuel_Type_Diesel', 'Fuel_Type_Petrol',
                                     'Seller_Type_Individual', 'Transmission_Manual'])

    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Price: ₹ {round(prediction, 2)} Lakhs")
