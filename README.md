# Telecom-Customer-Churn-Prediction



Table of Contents

Project Overview
Features
Tech Stack
Dataset
Modeling Approach
Results
How to Use
Future Scope

Project Overview

This project focuses on predicting telecom customer churn using machine learning. By identifying customers likely to leave, telecom companies can implement proactive retention strategies and reduce churn rates, leading to improved revenue and customer satisfaction.

Features

Data Preprocessing: Handled missing values, normalized data, and encoded categorical features for model training.
Exploratory Data Analysis (EDA): Visualized customer trends and churn patterns to inform feature engineering.
Feature Selection: Applied correlation heatmaps, chi-square tests, Recursive Feature Elimination (RFE), and ANOVA F-tests to identify the most important features.
Predictive Modeling: Built and optimized a stacking classifier combining Random Forest, XGBoost, and Logistic Regression.
Evaluation Metrics: Assessed models using precision, recall, F1 score, and accuracy, focusing on high recall for actionable insights.

Tech Stack

Programming Language: Python
Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn, XGBoost, Joblib
Environment: Jupyter Notebook

Dataset

Source: Kaggle Telecom Churn Dataset
Description: Contains customer demographics, usage behavior, and account details, with churn as the target variable.

Modeling Approach

Data Cleaning and Preprocessing
Imputed missing values and normalized numerical features.
Encoded categorical variables using one-hot encoding.
Feature Selection
Used statistical tests and feature importance methods to select the top features.
Stacking Classifier
Combined Random Forest and XGBoost as base learners.
Used Logistic Regression as the meta-learner for final predictions.
Model Evaluation
Compared performance across multiple models and finalized the stacking classifier for deployment.

Results

Final Model: Stacking Classifier
Metrics:
Accuracy: 91.37%
Precision:
Non-Churn: 93%
Churn: 90%
Recall:
Non-Churn: 89%
Churn: 94%
F1 Score:
Non-Churn: 91%
Churn: 92%
Macro Avg F1 Score: 91%
Key Insight: The model achieves high recall, making it effective at minimizing false negatives and identifying potential churners.

How to Use

Clone the repository:
bash

Copy code

git clone https://github.com/nithinbabu/telecom-churn-prediction.git  
Install the required libraries:
bash

Copy code

pip install -r requirements.txt  
Load the stacked_model.joblib for predictions:
python

Copy code

import joblib  
stacked_model = joblib.load('stacked_model.joblib')  
predictions = stacked_model.predict(X_test)  
Evaluate the model or integrate it into your application.

Future Scope

Feature Engineering: Incorporate additional features like sentiment analysis from call records or social media activity.
Deep Learning Models: Experiment with sequential models like RNNs for time-series customer behavior data.
Real-Time Prediction: Develop APIs for real-time churn predictions integrated with CRM tools.
License

Let’s predict and reduce churn! 🚀
