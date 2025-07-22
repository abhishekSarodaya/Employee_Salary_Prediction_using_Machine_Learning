import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("best_model.pkl")

# Streamlit setup
st.set_page_config(layout="wide")
st.title("💼 Employee Salary Classification App")
st.markdown("Predict whether an employee earns >50K or ≤50K based on input features.")

# Sidebar Inputs
st.sidebar.header("📥 Input Employee Details")

age = st.sidebar.slider("Age", 17, 65, 30)

# Education Levels (with complete mapping to educational-num)
education_map = {
    "Preschool": 1, "1st-4th": 2, "5th-6th": 3, "7th-8th": 4,
    "9th": 5, "10th": 6, "11th": 7, "12th": 8, "HS-grad": 9,
    "Some-college": 10, "Assoc-voc": 11, "Assoc-acdm": 12,
    "Bachelors": 13, "Masters": 14, "Prof-school": 15, "Doctorate": 16
}
education = st.sidebar.selectbox("Education Level", list(education_map.keys()))

# Occupation mapping (complete)
occupation_map = {
    "Adm-clerical": 0, "Armed-Forces": 1, "Craft-repair": 2, "Exec-managerial": 3,
    "Farming-fishing": 4, "Handlers-cleaners": 5, "Machine-op-inspct": 6,
    "Other-service": 7, "Priv-house-serv": 8, "Prof-specialty": 9,
    "Protective-serv": 10, "Sales": 11, "Tech-support": 12,
    "Transport-moving": 13
}
occupation = st.sidebar.selectbox("Occupation", list(occupation_map.keys()))

hours_per_week = st.sidebar.slider("Hours per Week", 1, 80, 40)

# Marital status and workclass maps (you already had them)
marital_status_map = {
    "Never-married": 4, "Married-civ-spouse": 2, "Divorced": 0,
    "Separated": 5, "Widowed": 6, "Married-spouse-absent": 3
}
marital_status = st.sidebar.selectbox("Marital Status", list(marital_status_map.keys()))

workclass_map = {
    "Private": 4, "Self-emp-not-inc": 6, "Self-emp-inc": 5, "Federal-gov": 1,
    "Local-gov": 3, "State-gov": 7, "Without-pay": 8, "Never-worked": 2
}
workclass = st.sidebar.selectbox("Workclass", list(workclass_map.keys()))

# Create input DataFrame
input_dict = {
    "educational-num": education_map[education],
    "occupation": occupation_map[occupation],
    "age": age,
    "hours-per-week": hours_per_week,
    "marital-status": marital_status_map[marital_status],
    "workclass": workclass_map[workclass]
}
input_df = pd.DataFrame([input_dict])

# Display inputs
st.subheader("📄 Input Summary")
st.table(pd.DataFrame({
    "Age": [age],
    "Education": [education],
    "Occupation": [occupation],
    "Hours/Week": [hours_per_week],
    "Marital Status": [marital_status],
    "Workclass": [workclass]
}))

# Predict
if st.button("🔮 Predict Salary Class"):
    prediction = model.predict(input_df)[0]
    result = ">50K" if prediction == 1 else "≤50K"
    st.success(f"🧠 Predicted Salary Class: **{result}**")

# # Batch prediction placeholder
# st.markdown("---")
# st.subheader("📁 Batch Prediction")
# st.markdown("Upload a CSV file for batch prediction (optional).")
