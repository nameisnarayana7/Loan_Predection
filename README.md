# Loan_Predection
Built a machine learning model to predict loan prices using applicant financial data. Performed data cleaning, EDA, and feature engineering, and applied regression models like Linear Regression and Random Forest. Evaluated performance using MAE, MSE, and R² to improve prediction accuracy.

Loan Price Prediction Using Machine Learning
1. Introduction

Loan Price Prediction is a machine learning project aimed at predicting the loan amount or approval likelihood based on applicant details such as income, credit history, employment status, and other financial factors. It helps financial institutions make faster and more accurate lending decisions.

2. Objective

The main objective of this project is to build a predictive model that:

Estimates loan amount or approval status
Reduces manual decision-making errors
Improves efficiency in loan processing
3. Dataset Description

The dataset includes the following features:

Applicant Income
Co-applicant Income
Loan Amount
Loan Term
Credit History
Gender, Marital Status, Education
Property Area

Data preprocessing steps:

Handled missing values (~10–20%)
Encoded categorical variables
Normalized numerical features
4. Methodology

The project follows these steps:

Data Collection
Data Cleaning & Preprocessing
Exploratory Data Analysis (EDA)
Feature Engineering
Model Training
Model Evaluation
5. Machine Learning Models Used
Logistic Regression
Decision Tree
Random Forest
Support Vector Machine (SVM)
6. Evaluation Metrics
Accuracy
Precision
Recall
F1-Score

The best model achieved:

Accuracy: ~80–90% (depending on dataset)
7. Results & Insights
Credit History is the most important factor
Higher income increases approval chances
Loan amount is directly influenced by applicant income and employment status
8. Deployment

The model is deployed using Streamlit, where users can:

Input their details
Get instant loan prediction results
9. Conclusion

This project demonstrates how machine learning can automate loan prediction and assist financial institutions in making data-driven decisions efficiently.

10. Future Enhancements
Use advanced models like XGBoost
Improve accuracy with larger datasets
Integrate real-time banking APIs
