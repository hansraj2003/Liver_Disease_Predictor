# Liver Disease Prediction Project

Predicting liver disease in patients using Machine Learning.

## Problem Statement

Given a dataset containing biological and diagnostic data of 583 Indian patients, this project aims to identify a suitable machine learning algorithm capable of identifying whether a person has liver disease or not.

## Overview

This project is an example of supervised learning, where the algorithm learns from labeled data to make predictions.This project aims to develop a predictive model to classify patients based on their liver disease status. The project involves data cleaning, exploratory data analysis (EDA), model building, and deploying the best model using Flask. Multiple machine learning models, including Logistic Regression, Random Forest, and Support Vector Classifier (SVC), were trained. The best-performing model is selected for deployment. This project is an example of supervised learning, where the algorithm learns from labeled data to make predictions.

## Technologies and Frameworks Used

- **Python**: Programming language used for data processing and model building.
- **Jupyter Notebook**: Interactive environment for developing and running code.
- **[Pandas](https://pandas.pydata.org/)**: Data manipulation and analysis library.
- **[NumPy](https://numpy.org/)**: Library for numerical computations.
- **[Matplotlib](https://matplotlib.org/)**: Plotting library for data visualization.
- **[Seaborn](https://seaborn.pydata.org/)**: Statistical data visualization library.
- **[Scikit-Learn](https://scikit-learn.org/)**: Machine learning library for model building and evaluation.
- **[Flask](https://flask.palletsprojects.com/)**: Web framework for deploying the model.
- **[Pickle](https://joblib.readthedocs.io/en/latest/)**: Library for model serialization.

## Steps Involved

### 1. Data Cleaning and Preprocessing

- Loaded the dataset using pandas.
- Inspected the dataset for missing values and handled them appropriately.
- Saved the cleaned dataset for further analysis.

### 2. Exploratory Data Analysis (EDA)

- Performed univariate, bivariate, and multivariate analysis using matplotlib and seaborn.
- Visualized relationships between features to gain insights.

### 3. Model Building

- Selected features and split the data into training and testing sets.
- Trained multiple models: Logistic Regression, Random Forest, and Support Vector Classifier (SVC).
- Evaluated the models using accuracy, precision, recall, and confusion matrix.
- Selected the best-performing model.

### 4. Model Deployment

- Saved the trained model using joblib.
- Created a Flask API to serve the model.
- Built an HTML form to accept user inputs and display predictions.
