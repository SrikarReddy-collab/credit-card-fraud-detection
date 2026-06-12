import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("models/random_forest_model.pkl")

st.title("💳 Credit Card Fraud Detection")

st.write("Enter transaction details")

time = st.number_input("Time", value=0.0)
amount = st.number_input("Amount", value=0.0)

if st.button("Predict"):

    features = np.zeros((1, 30))

    features[0][0] = time
    features[0][-1] = amount

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("⚠️ Fraudulent Transaction Detected")
    else:
        st.success("✅ Legitimate Transaction")