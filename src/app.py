import streamlit as st
import requests



api_url = "http://127.0.0.1:8000"

st.title("Customer Churn Prediction")
st.header("Enter customer details to predict churn:")
id = st.number_input("**Customer ID**", min_value=0, step=1)
gender = st.selectbox("*Gender*", ["Male", "Female"])
SeniorCitizen = st.selectbox('*Senior Citizen?*',['Yes', 'No'])
Partner = st.selectbox('*Has Partner?*',['Yes', 'No'])
Dependents = st.selectbox('*Has Dependents?*',['Yes', 'No'])
tenure = st.number_input("*Tenure (months)*", min_value=0, max_value=100, step=1)
PhoneService = st.selectbox('*Has Phone Service?*',['Yes', 'No'])
MultipleLines = st.selectbox('*Has Multiple Lines?*',['Yes', 'No', 'No phone service'])
InternetService = st.selectbox('*Type of Internet Service*',['DSL', 'Fiber optic', 'No'])
OnlineSecurity = st.selectbox('*Has Online Security?*',['Yes', 'No', 'No internet service'])
OnlineBackup = st.selectbox('*Has Online Backup?*',['Yes', 'No', 'No internet service'])
DeviceProtection = st.selectbox('*Has Device Protection?*',['Yes', 'No', 'No internet service'])
TechSupport = st.selectbox('*Has Tech Support?*',['No', 'Yes', 'No internet service'])
StreamingTV = st.selectbox('*Has Streaming TV?*',['No', 'Yes', 'No internet service'])
StreamingMovies = st.selectbox('*Has Streaming Movies?*',['No', 'Yes', 'No internet service'])
Contract = st.selectbox('*Type of Contract*',['Month-to-month', 'One year', 'Two year'])
PaperlessBilling = st.selectbox('*Has Paperless Billing?*',['Yes', 'No'])
PaymentMethod = st.selectbox('*Payment Method*',['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
MonthlyCharges = st.number_input("*Monthly Charges*", min_value=0.0, step=0.01)
TotalCharges = st.number_input("*Total Charges*", min_value=0.0, step=0.01)

st.space()  # Add a line break for better spacing

col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])

with col3:
    if st.button('*Predict Churn*', type='primary'):
        data = {
            "id": id,
            "gender": gender,
            "SeniorCitizen": SeniorCitizen,
            "Partner": Partner,
            "Dependents": Dependents,
            "tenure": tenure,
            "PhoneService": PhoneService,
            "MultipleLines": MultipleLines,
            "InternetService": InternetService,
            "OnlineSecurity": OnlineSecurity,
            "OnlineBackup": OnlineBackup,
            "DeviceProtection": DeviceProtection,
            "TechSupport": TechSupport,
            "StreamingTV": StreamingTV,
            "StreamingMovies": StreamingMovies,
            "Contract": Contract,
            "PaperlessBilling": PaperlessBilling,
            "PaymentMethod": PaymentMethod,
            "MonthlyCharges": MonthlyCharges,
            "TotalCharges": TotalCharges
        }

        response = requests.post(f"{api_url}/predict", json=data)

        if response.status_code == 200:
            result = response.json()
            st.success(result)
        else:
            st.error("Error in prediction. Please try again.")
