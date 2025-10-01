# **🚚 Amazon Delivery Time Prediction**

This end-to-end project predicts delivery times for Amazon orders based on factors such as product category, distance, traffic conditions, weather, and agent details.  
The solution includes data cleaning, feature engineering, machine learning model development, MLflow tracking, and a Streamlit web application for real-time prediction.  

---

## **Table of Contents**
- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [How to Run the Application](#how-to-run-the-application)
- [Model and Data Details](#model-and-data-details)
- [Results](#results)
- [Conclusion](#conclusion)
- [Acknowledgments](#acknowledgments)

---

## **Introduction**

The goal of this project is to build a **delivery time prediction system** for e-commerce logistics.  
By analyzing order details and external factors (traffic, weather, etc.), the system can provide accurate delivery time estimates to improve **customer satisfaction** and **operational efficiency**.  

---

## **Features**
- 📊 **Data Cleaning & Preprocessing** – handle missing values, duplicates, and inconsistent formats.  
- 🛠 **Feature Engineering** – compute distance, extract time features (hour, day, month, weekday, year).  
- 🤖 **Machine Learning Models** – Linear Regression, Random Forest, Gradient Boosting, XGBoost.  
- 📈 **Model Tracking** – log and compare models with MLflow.  
- 🌐 **Streamlit Application** – user-friendly web interface for delivery time predictions.  
- 🔍 **EDA Visualizations** – insights into factors affecting delivery times (distance, traffic, weather).  

---

## **Project Structure**
Amazon-Delivery-Time-Prediction/
│── data/ # Dataset (amazon_delivery.csv)
│── notebooks/ # Jupyter notebooks for EDA & modeling
│── src/ # Python scripts (data prep, feature engineering, models)
│── models/ # Saved ML models and pipelines
│── streamlit_app/ # Streamlit application files
│── requirements.txt # Project dependencies
│── README.md # Project documentation

---

## **Technologies Used**
- **Python** (Pandas, NumPy, Matplotlib, Seaborn)  
- **Scikit-learn** (Regression models, Pipelines, Preprocessing)  
- **XGBoost** (Gradient boosting regression)  
- **MLflow** (Model tracking & experiment management)  
- **Streamlit** (Web application for predictions)  

---

## **Setup and Installation**
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Amazon-Delivery-Time-Prediction.git
   cd Amazon-Delivery-Time-Prediction
2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # (Linux/Mac)
    venv\Scripts\activate      # (Windows)
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
4. Run the application:
    ```bash
    streamlit run app.py

---

## **Model and Data Details**
- Dataset: amazon_delivery.csv

    - Agent details (age, rating)

    - Order details (date, time, category)

    - Environmental factors (weather, traffic)

    - Delivery time (target variable in hours)

- Feature Engineering:

    - Distance_km (store → drop location)

    - Order_Hour, Order_Day, Order_Month, Order_Weekday, Order_Year

    - Encoded categorical variables (Weather, Traffic, Vehicle, Area, Category)

    - Evaluation Metrics: RMSE, MAE, R²

---

## **Results**
- 📉 Cleaned and preprocessed dataset ready for analysis

- 🔎 Insights into how traffic, weather, and distance affect delivery times

- 🤖 Trained ML models tracked with MLflow

- 🌐 Streamlit app for interactive delivery time predictions

---

## **Conclusion**
This project demonstrates how machine learning and feature engineering can improve logistics operations by predicting delivery times accurately.
By integrating a web-based interface, the system provides real-time predictions that can be used to optimize delivery schedules, monitor agent performance, and enhance customer satisfaction.

---

## **Acknowledgments**
- 📦 Amazon dataset (sample) for analysis and modeling.

- 🔧 Open-source libraries (Scikit-learn, XGBoost, Streamlit, MLflow).

- 🙌 Inspired by real-world e-commerce logistics challenges.

---

## 🗂️ Data sets
* This project was created during an Internship.
* If you want to use the data that I have used, you can contact me.

---

## 🙋‍♂️ Author

**Shubham Pandey**
📧 [Email Me](mailto:shubhamppandey1084@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/shubham-pandey-6a65a524a/) • [GitHub](https://github.com/Shubhampandey1git)

---