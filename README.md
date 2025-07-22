# 🧠 Employee Salary Prediction using Machine Learning

This project focuses on predicting whether an individual earns more than $50K per year using machine learning techniques on census income data. It involves data cleaning, feature engineering, model training, and deployment through an interactive web app built with **Streamlit**.

---

## 📌 Project Overview

The goal is to build a classification model that can determine an employee's income bracket (<=50K or >50K) using demographic and employment-related features such as:

- Age
- Education
- Occupation
- Hours per week
- Gender
- ...and more

This end-to-end machine learning project walks through the complete data science workflow — from raw data to production-ready deployment.

---

## 🗂️ Dataset Description

The dataset used originates from the U.S. Census Bureau and is available on [Kaggle](https://www.kaggle.com/datasets/uciml/adult-census-income). It includes the following columns:

| Column Name      | Description                                           |
|------------------|-------------------------------------------------------|
| `age`            | Age of the individual (numeric)                      |
| `workclass`      | Type of employment (Private, Government, etc.)       |
| `fnlwgt`         | Final weight representing sample demographics        |
| `education`      | Highest level of education                           |
| `education-num`  | Numeric representation of education level            |
| `marital-status` | Marital status                                       |
| `occupation`     | Job type (e.g., Sales, Tech-support)                 |
| `relationship`   | Relationship to head of household                    |
| `race`           | Race (e.g., White, Black, Asian-Pac-Islander)        |
| `gender`         | Gender (Male or Female)                              |
| `capital-gain`   | Capital gain in dollars                              |
| `capital-loss`   | Capital loss in dollars                              |
| `hours-per-week` | Number of hours worked per week                      |
| `native-country` | Country of origin                                    |
| `income`         | Target label (<=50K or >50K)                         |

---

## 🔧 Key Steps & Techniques

1. **Data Cleaning**
   - Replaced missing values (`?`) with `"Others"`
   - Removed rows with invalid or inconsistent data

2. **Outlier Detection and Removal**
   - Removed extreme values in columns like:
     - `age`
     - `educational-num`
     - `capital-gain`

3. **Label Encoding**
   - Used `LabelEncoder` to convert categorical variables to numeric format

4. **Feature Selection**
   - Removed redundant columns like `education` (used `education-num` instead)
   - Selected features most relevant for prediction

5. **Model Building**
   - Trained multiple models using **scikit-learn** classifiers
   - Evaluated performance using accuracy

---

## 🤖 Models Trained

| Model                    | Accuracy  |
|--------------------------|-----------|
| Logistic Regression      | 79.3%     |
| Random Forest Classifier | 85.2%     |
| K-Nearest Neighbors      | 77.0%     |
| Support Vector Machine   | 78.8%     |
| **Gradient Boosting**    | **85.7%** ✅ |

> ✅ **Gradient Boosting Classifier** was selected as the final model due to its highest accuracy.

---

## 🚀 Deployment – Streamlit Web App

An interactive Streamlit app was built for deployment:

### Features:
- 🔍 Real-time salary prediction based on user input
- 📂 Batch prediction via CSV file upload
- ⬇️ Downloadable prediction results in CSV format

The model is saved as a serialized file (`best_model.pkl`) using `joblib`.

---

## 📂 Files Included

