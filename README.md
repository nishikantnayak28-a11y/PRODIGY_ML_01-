# House Price Prediction using Linear Regression

## 📌 Overview

This project is part of my Machine Learning Internship at Prodigy Infotech.

The objective of this project is to implement a Linear Regression model to predict house prices based on:

* Living Area (Square Footage)
* Number of Bedrooms
* Number of Bathrooms

The model is trained using the House Prices dataset and evaluated using standard regression metrics.

---

## 🎯 Objective

To build a machine learning model that predicts house prices based on selected house features and analyze the relationship between these features and the target variable.

---

## 📂 Dataset

Dataset Used: House Prices - Advanced Regression Techniques

* Total Records: 1460
* Total Features: 81

Target Variable:

* SalePrice

Selected Features:

* GrLivArea (Above Ground Living Area)
* BedroomAbvGr (Number of Bedrooms)
* FullBath (Number of Full Bathrooms)

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Joblib

---

## 📊 Exploratory Data Analysis (EDA)

The following analyses were performed:

1. Missing Value Analysis
2. Correlation Analysis
3. Correlation Heatmap
4. Living Area vs Sale Price Visualization
5. Bedrooms vs Sale Price Visualization
6. Bathrooms vs Sale Price Visualization

### Correlation with Sale Price

| Feature      | Correlation |
| ------------ | ----------- |
| GrLivArea    | 0.7086      |
| FullBath     | 0.5607      |
| BedroomAbvGr | 0.1682      |

Observation:

* Living Area has the strongest positive relationship with house prices.
* Number of bathrooms also significantly influences house prices.
* Number of bedrooms has comparatively lower impact.

---

## 🤖 Model Used

Linear Regression

The dataset was split into:

* Training Data: 80%
* Testing Data: 20%

Random State:

* 42

---

## 📈 Model Performance

| Metric                    | Value            |
| ------------------------- | ---------------- |
| Mean Absolute Error (MAE) | 35,788.06        |
| Mean Squared Error (MSE)  | 2,806,426,667.25 |
| R² Score                  | 0.6341           |

### Interpretation

The model achieved an R² score of 63.41%, indicating that it can explain approximately 63% of the variation in house prices using the selected features.

---

## 🚀 How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Project

```bash
python house_price_prediction.py
```

---

## 🏆 Internship Information

Task: House Price Prediction using Linear Regression

Internship: Prodigy Infotech Machine Learning Internship

Task Code: PRODIGY_ML_01

---

## 👨‍💻 Author

Ashutosh Agrawal

B.Tech CSE Student
Government College of Engineering, Kalahandi

Machine Learning Enthusiast | Aspiring Software Engineer
