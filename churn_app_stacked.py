import streamlit as st
import pandas as pd
from joblib import load

# Load the trained stacked model
model = load('stacked_model.joblib')

# Create a Streamlit app
st.title("Customer Churn Prediction App - Stacked Model")

# Input fields for feature values on the main screen
st.header("Enter Customer Information")

# Input fields for the feature set
tenure = st.number_input("Tenure (in months)", min_value=0, max_value=100, value=1)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, max_value=200.0, value=50.0)
total_charges = st.number_input("Total Charges", min_value=0.0, max_value=10000.0, value=0.0)

# Select box for Contract type
contract = st.selectbox("Contract", ('Month-to-month', 'One year', 'Two year'))

# Select box for Payment Method
payment_method = st.selectbox("Payment Method", 
                                ('Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'))

# Select box for Online Security
online_security = st.selectbox("Online Security", ('Yes', 'No'))

# Select box for Tech Support
tech_support = st.selectbox("Tech Support", ('Yes', 'No'))

# Select box for Paperless Billing
paperless_billing = st.selectbox("Paperless Billing", ('Yes', 'No'))

# Select box for Internet Service
internet_service = st.selectbox("Internet Service", ('DSL', 'Fiber optic', 'No'))

# Select box for Online Backup
online_backup = st.selectbox("Online Backup", ('Yes', 'No'))

# Map input values to numeric using the label mapping
label_mapping_contract = {
    'Month-to-month': 0,
    'One year': 1,
    'Two year': 2,
}

label_mapping_payment_method = {
    'Electronic check': 0,
    'Mailed check': 1,
    'Bank transfer (automatic)': 2,
    'Credit card (automatic)': 3,
}

label_mapping_online_security = {
    'Yes': 1,
    'No': 0,
}

label_mapping_tech_support = {
    'Yes': 1,
    'No': 0,
}

label_mapping_paperless_billing = {
    'Yes': 1,
    'No': 0,
}

label_mapping_internet_service = {
    'DSL': 0,
    'Fiber optic': 1,
    'No': 2,
}

label_mapping_online_backup = {
    'Yes': 1,
    'No': 0,
}

# Convert input to numeric
contract_encoded = label_mapping_contract[contract]
payment_method_encoded = label_mapping_payment_method[payment_method]
online_security_encoded = label_mapping_online_security[online_security]
tech_support_encoded = label_mapping_tech_support[tech_support]
paperless_billing_encoded = label_mapping_paperless_billing[paperless_billing]
internet_service_encoded = label_mapping_internet_service[internet_service]
online_backup_encoded = label_mapping_online_backup[online_backup]

# Make a prediction using the model
prediction = model.predict([[monthly_charges, tenure, contract_encoded, total_charges,
                             payment_method_encoded, online_security_encoded, tech_support_encoded,
                             paperless_billing_encoded, internet_service_encoded, online_backup_encoded]])

# Display the prediction result on the main screen
st.header("Prediction Result")
if prediction[0] == 0:
    st.success("This customer is likely to stay.")
else:
    st.error("This customer is likely to churn.")

# Add any additional Streamlit components or UI elements as needed.
