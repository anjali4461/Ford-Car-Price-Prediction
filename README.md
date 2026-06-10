# 🚗 Ford Car Price Prediction

A Machine Learning project that predicts the selling price of Ford cars based on various vehicle features such as model, year, transmission type, mileage, fuel type, engine size, and tax information.

The project uses multiple regression algorithms and identifies **XGBoost Regressor (XGBRegressor)** as the best-performing model for accurate price prediction.

---

## 📌 Project Overview

Car price prediction is an important problem in the automotive industry. Accurate valuation helps buyers, sellers, dealerships, and insurance companies make informed decisions.

This project analyzes historical Ford car data and builds a predictive model capable of estimating vehicle prices based on key specifications.

---

## 🎯 Objectives

* Analyze Ford car dataset
* Perform data cleaning and preprocessing
* Conduct exploratory data analysis (EDA)
* Train multiple regression models
* Compare model performance
* Select the best-performing model
* Predict car prices for new vehicle data

---

## 📂 Dataset

The dataset contains information about Ford vehicles, including:

| Feature      | Description                     |
| ------------ | ------------------------------- |
| model        | Car model                       |
| year         | Manufacturing year              |
| price        | Vehicle price (Target Variable) |
| transmission | Transmission type               |
| mileage      | Distance traveled               |
| fuelType     | Fuel type                       |
| tax          | Road tax                        |
| mpg          | Miles per gallon                |
| engineSize   | Engine size in liters           |

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* XGBoost
* Jupyter Notebook
* Streamlit

---

## 📊 Exploratory Data Analysis

Key analyses performed:

* Price distribution
* Correlation heatmap
* Model-wise price comparison
* Mileage vs Price relationship
* Fuel type analysis
* Engine size impact on pricing
* Outlier detection and treatment

---

## ⚙️ Machine Learning Workflow

### 1. Data Preprocessing

* Handle missing values
* Remove duplicates
* Feature encoding
* Feature scaling (if required)
* Train-test split

### 2. Model Training

The following regression models were evaluated:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor
* XGBoost Regressor

### 3. Model Evaluation

Evaluation metrics used:

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)

---

## 🏆 Best Model

### XGBoost Regressor (XGBRegressor)

XGBoost achieved the highest prediction accuracy among all tested models.

**Advantages:**

* High predictive performance
* Handles complex feature interactions
* Robust against overfitting
* Efficient and scalable

---

## 📈 Model Performance

| Model                       | R² Score      |
| --------------------------- | ------------- |
| Linear Regression           | 84            |
| Random Forest Regressor     | 92            |
| XGBoost Regressor           | **93 (Best)** |

---

## 📉 Features Influencing Price

Important factors affecting car price include:

* Vehicle age
* Mileage
* Engine size
* Model type
* Fuel type
* Fuel efficiency (MPG)
* Transmission type

---

## 🔮 Future Improvements

* Hyperparameter tuning with Optuna
* Add support for multiple car brands
* Real-time vehicle valuation API
* Advanced ensemble models

---

Website link : https://ford-car-price-prediction-zopwaqbxvhoy3r8xznjsb5.streamlit.app/
