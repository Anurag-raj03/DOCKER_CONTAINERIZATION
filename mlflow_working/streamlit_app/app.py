import streamlit as st
import joblib
import numpy as np
import os
from sklearn.ensemble import RandomForestRegressor

# Set page title and layout
st.set_page_config(page_title="Sleep Efficiency Predictor", page_icon="😴", layout="centered")

# Determine the correct model path dynamically
if os.path.exists("/app/Saved_model/rf_model.jbl"):  # Inside Docker
    model_path = "/app/Saved_model/rf_model.jbl"
elif os.path.exists("Saved_model/rf_model.jbl"):  # Local Run
    model_path = "Saved_model/rf_model.jbl"
else:
    model_path = None

# Load the trained Random Forest model
if model_path is None:
    st.error("⚠️ Model file not found. Please upload the model file.")
    model = None
else:
    try:
        model = joblib.load(model_path)
        if not isinstance(model, RandomForestRegressor):
            raise TypeError("Loaded model is not a RandomForestRegressor!")
        st.success("✅ Model loaded successfully!")
    except Exception as e:
        st.error(f"⚠️ Error loading the model: {e}")
        model = None

# Streamlit UI
st.title("😴 Sleep Efficiency Predictor")
st.markdown("### Enter your sleep details below to get a prediction!")

# Sidebar for user inputs
st.sidebar.header("User Input")

age = st.sidebar.slider("Age", min_value=0, max_value=100, value=25)
gender = st.sidebar.radio("Gender", ["Male", "Female"], index=0)
sleep_duration = st.sidebar.slider("Sleep Duration (hrs)", min_value=0.0, max_value=24.0, value=7.0, step=0.5)
rem_sleep = st.sidebar.slider("REM Sleep (%)", min_value=0.0, max_value=100.0, value=20.0, step=0.5)
deep_sleep = st.sidebar.slider("Deep Sleep (%)", min_value=0.0, max_value=100.0, value=15.0, step=0.5)
light_sleep = st.sidebar.slider("Light Sleep (%)", min_value=0.0, max_value=100.0, value=60.0, step=0.5)
awakenings = st.sidebar.slider("Number of Awakenings", min_value=0, max_value=10, value=2)
caffeine = st.sidebar.slider("Caffeine Consumption (mg/day)", min_value=0.0, max_value=1000.0, value=50.0, step=10.0)
alcohol = st.sidebar.slider("Alcohol Consumption (drinks/day)", min_value=0.0, max_value=10.0, value=0.0, step=0.5)
smoking = st.sidebar.radio("Smoking Status", ["Non-Smoker", "Smoker"], index=0)
exercise = st.sidebar.slider("Exercise Frequency (days/week)", min_value=0, max_value=7, value=3)

# Encode categorical values
gender_encoded = 0 if gender == "Male" else 1
smoking_encoded = 0 if smoking == "Non-Smoker" else 1

# Predict function
def predict():
    features = np.array([[age, gender_encoded, sleep_duration, rem_sleep, deep_sleep,
                          light_sleep, awakenings, caffeine, alcohol, smoking_encoded, exercise]])
    try:
        prediction = model.predict(features)[0]
        return prediction
    except Exception as e:
        st.error(f"⚠️ Prediction error: {e}")
        return None

# Button to trigger prediction
if st.sidebar.button("🔍 Predict Sleep Efficiency"):
    if model is None:
        st.error("⚠️ Please upload a valid model file!")
    else:
        result = predict()
        if result is not None:
            st.success(f"🌙 Your predicted sleep efficiency is **{result:.2f}%**")
