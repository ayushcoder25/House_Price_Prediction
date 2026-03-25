import streamlit as st
import pickle
import pandas as pd

# load model
model = pickle.load(open("model.pkl", "rb"))
cols = pickle.load(open("columns.pkl", "rb"))

st.title("🏠 House Price Predictor")

# inputs
area = st.number_input("Area (sq ft)")
bed = st.number_input("Bedrooms")
bath = st.number_input("Bathrooms")
stories = st.number_input("Stories")
parking = st.number_input("Parking")

ac = st.selectbox("Air Conditioning", ["yes", "no"])
road = st.selectbox("Main Road", ["yes", "no"])

# input dict
input_data = {
    "area": area,
    "bedrooms": bed,
    "bathrooms": bath,
    "stories": stories,
    "parking": parking,
    "airconditioning_yes": 1 if ac == "yes" else 0,
    "mainroad_yes": 1 if road == "yes" else 0
}

df = pd.DataFrame([input_data])

# match columns
df = df.reindex(columns=cols, fill_value=0)

# predict
if st.button("Predict"):
    result = model.predict(df)[0]
    st.success(f"Price: ₹ {int(result)}")
