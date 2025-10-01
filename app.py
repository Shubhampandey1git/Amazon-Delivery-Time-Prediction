# app.py
import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# Load the full pipeline (preprocessor + model)
pipeline = joblib.load("models/best_model.pkl")

st.set_page_config(page_title="Amazon Delivery Time Prediction", layout="centered")
st.title("🚚 Amazon Delivery Time Prediction App")

st.write("Enter the details below to predict delivery time:")

# --- Inputs ---
col1, col2 = st.columns(2)

with col1:
    category = st.selectbox("Product Category", ["Electronics", "Clothing", "Grocery", "Books", "Other"])
    distance_km = st.number_input("Distance (km)", min_value=0.0, max_value=200.0, step=0.1)
    traffic = st.selectbox("Traffic", ["Low", "Medium", "High", "Jam"])
    weather = st.selectbox("Weather", ["Sunny", "Rainy", "Stormy", "Cloudy", "Foggy"])

with col2:
    agent_age = st.slider("Agent Age", min_value=18, max_value=60, value=30)
    agent_rating = st.slider("Agent Rating", min_value=1.0, max_value=5.0, value=4.5, step=0.1)
    vehicle = st.selectbox("Vehicle", ["Bike", "Car", "Scooter", "Cycle"])
    area = st.selectbox("Area", ["Urban", "Metropolitan", "Rural"])
    order_date = st.date_input("Order Date", datetime.now().date())
    order_time = st.time_input("Order Time", datetime.now().time())
    order_datetime = datetime.combine(order_date, order_time)

# Extract time-based features
order_hour = order_datetime.hour
order_day = order_datetime.day
order_month = order_datetime.month
order_weekday = order_datetime.weekday()
order_year = order_datetime.year

# --- Predict button ---
if st.button("Predict Delivery Time"):
    # Create dataframe in raw format (pipeline will preprocess)
    input_data = pd.DataFrame({
        "Agent_Age": [agent_age],
        "Agent_Rating": [agent_rating],
        "Weather": [weather],
        "Traffic": [traffic],
        "Vehicle": [vehicle],
        "Area": [area],
        "Category": [category],
        "Distance_km": [distance_km],
        "Order_Hour": [order_hour],
        "Order_Day": [order_day],
        "Order_Month": [order_month],
        "Order_Weekday": [order_weekday],
        "Order_Year": [order_year]
    })

    st.write("🔍 Input Data Preview:", input_data)

    # Predict using pipeline
    prediction = pipeline.predict(input_data)[0]
    st.success(f"✅ Estimated Delivery Time: {prediction:.2f} hours")
