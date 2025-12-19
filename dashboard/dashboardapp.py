import streamlit as st
import pandas as pd
import joblib

model = joblib.load("models/health_model.pkl")

st.title("Smart Health Surveillance")

data = pd.read_csv("data/health_data.csv")

predictions = model.predict(data.drop("risk", axis=1))
data["Predicted Risk"] = predictions

st.write(data)
st.bar_chart(data["Predicted Risk"])
