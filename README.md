# House Price Prediction

## Overview
This project is a **House Price Prediction** web application built using **Flask** and **Machine Learning**. It predicts house prices based on various input features such as area, location, number of rooms, etc. The aim of this project is to provide accurate price estimates for homes based on historical data, helping users gain insights into real estate trends.

## Features
- User-friendly web interface built with **Flask**
- Machine learning model for price prediction
- Prediction based on multiple property features
- Deployment-ready for cloud services or local hosting

## Live Demo
You can access the live application [here](https://house-price-prediction-flaskapp-1.onrender.com/)

## Deployment Status
![Deploy Status](https://github.com/vish1108/House_Price_Prediction_FlaskApp/actions/workflows/deploy.yml/badge.svg)


## Project Structure
```bash
House_Price_Prediction/
├── app.py                # Flask application file
├── templates/
│   └── index.html        # Main page for user inputs and results display
├── json_file             # This file Store encoding of the location which is used for ML models
│          
├── house_price_model.pkl # Pre-trained machine learning model
│     
├── README.md             # Project documentation
└── requirements.txt      # Project dependencies
