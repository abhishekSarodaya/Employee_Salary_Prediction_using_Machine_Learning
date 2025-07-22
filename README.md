# 🧠 Employee Salary Prediction using Machine Learning

This project aims to predict whether an individual's annual income exceeds $50K using machine learning algorithms applied to census income data. The implementation includes comprehensive data preprocessing, feature engineering, model development, and deployment via an interactive **Streamlit** web application.

---

## 📌 Project Overview

The goal is to build a classification model that can determine an employee's income bracket (<=50K or >50K) using demographic and employment-related features such as:

- Age
- Education
- Occupation
- Hours per week
- Gender
- ...and more

This comprehensive machine learning project demonstrates the complete data science pipeline — transforming raw data into a production-ready predictive system for real-world salary classification.
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
| Logistic Regression      | 77.76%     |
| Random Forest Classifier | 80.78%     |
| K-Nearest Neighbors      | 77.91%     |
| Support Vector Machine   | 78.95%     |
| **Gradient Boosting**    | **82.95%** ✅ |

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

