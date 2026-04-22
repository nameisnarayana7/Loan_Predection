import streamlit as st
import pandas as pd
import pickle
import numpy as np

# -----------------------------
# Load Model Files
# -----------------------------
model = pickle.load(open("loan_model.pkl", "rb"))
scaler = pickle.load(open("loan_scaler.pkl", "rb"))
feature_columns = pickle.load(open("loan_features.pkl", "rb"))

st.set_page_config(page_title="Loan Approval Prediction", layout="wide")

st.title("🏦 Smart Loan Approval Prediction System")
st.write("AI-based Loan Eligibility Assessment")

st.markdown("---")

# -----------------------------
# Input Layout
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("👤 Applicant Details")
    
    no_of_dependents = st.number_input("Number of Dependents", 0, 10, 0)
    
    education = st.selectbox(
        "Education Level",
        ["Select Education", "Graduate", "Not Graduate"]
    )
    
    self_employed = st.selectbox(
        "Self Employed",
        ["Select Employment Status", "No", "Yes"]
    )
    
    income_annum = st.number_input("Annual Income", min_value=0, value=0)

with col2:
    st.subheader("💰 Loan Details")
    
    loan_amount = st.number_input("Loan Amount", min_value=0, value=0)
    
    loan_term = st.number_input("Loan Term (Months)", min_value=0, value=0)
    
    cibil_score = st.number_input("CIBIL Score", min_value=300, max_value=900, value=300)
    
    residential_assets_value = st.number_input("Residential Assets Value", min_value=0, value=0)
    
    commercial_assets_value = st.number_input("Commercial Assets Value", min_value=0, value=0)
    
    luxury_assets_value = st.number_input("Luxury Assets Value", min_value=0, value=0)
    
    bank_asset_value = st.number_input("Bank Asset Value", min_value=0, value=0)

# -----------------------------
# Prediction Button
# -----------------------------
if st.button("🔍 Check Loan Eligibility"):

    # Validation check (LIKE CAR PROGRAM)
    if (
        education == "Select Education" or
        self_employed == "Select Employment Status"
    ):
        st.warning("⚠ Please select Education and Employment Status.")
    
    else:
        # Create base input dictionary
        input_data = {
            "no_of_dependents": no_of_dependents,
            "income_annum": income_annum,
            "loan_amount": loan_amount,
            "loan_term": loan_term,
            "cibil_score": cibil_score,
            "residential_assets_value": residential_assets_value,
            "commercial_assets_value": commercial_assets_value,
            "luxury_assets_value": luxury_assets_value,
            "bank_asset_value": bank_asset_value,
            "education_Not Graduate": 1 if education == "Not Graduate" else 0,
            "self_employed_Yes": 1 if self_employed == "Yes" else 0
        }

        sample_df = pd.DataFrame([input_data])
        sample_df = sample_df.reindex(columns=feature_columns, fill_value=0)

        sample_scaled = scaler.transform(sample_df)

        prediction = model.predict(sample_scaled)[0]
        probability = model.predict_proba(sample_scaled)[0][1]

        st.subheader("📊 Prediction Result")

        if prediction == 1:
            st.success(f"✅ Loan Approved (Confidence: {probability*100:.2f}%)")
        else:
            st.error(f"❌ Loan Rejected (Confidence: {(1-probability)*100:.2f}%)")

        # Smart Insights
        if cibil_score < 600:
            st.info("📉 Low CIBIL score affects approval chances.")
        elif income_annum < loan_amount:
            st.info("⚠ Loan amount is high compared to income.")
        else:
            st.info("💼 Financial profile looks stable.")