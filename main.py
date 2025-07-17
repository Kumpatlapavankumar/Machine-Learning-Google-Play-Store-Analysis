import streamlit as st
import pandas as pd
import joblib

# Load pre-trained model and scaler
model = joblib.load("app_type_model.joblib")      # DecisionTreeClassifier
scaler = joblib.load("scaler_app_type.joblib")    # MinMaxScaler

st.set_page_config(page_title="App Type Classifier", layout="centered")
st.title("📱 Google Play App Type Classifier")
st.markdown("Predict whether an app is **Free** or **Paid** using key app features.")

# Sidebar input
st.sidebar.header("Enter App Details")

rating = st.sidebar.slider("App Rating", min_value=0.0, max_value=5.0, value=4.2, step=0.1)
size_mb = st.sidebar.number_input("App Size (MB)", min_value=0.0, max_value=1000.0, value=20.0, step=0.1)
installs = st.sidebar.number_input("Number of Installs", min_value=0, value=10000, step=1000)
reviews = st.sidebar.number_input("Number of Reviews", min_value=0, value=1000, step=100)

# Prepare input
input_df = pd.DataFrame(
    [[rating, size_mb * 1e6, installs, reviews]],
    columns=["Rating", "Size", "Installs", "Reviews"]
)

# Scale
input_df[["Rating", "Size", "Installs", "Reviews"]] = scaler.transform(input_df[["Rating", "Size", "Installs", "Reviews"]])

# Prediction
if st.sidebar.button("Predict App Type"):
    prediction = model.predict(input_df)[0]
    app_type = "Free" if prediction == 0 else "Paid"
    st.subheader("🔍 Predicted App Type:")
    st.success(f"**{app_type} App**")

