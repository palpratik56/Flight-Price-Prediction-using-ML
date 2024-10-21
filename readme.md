## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Dataset](#dataset)
5. [Model Development](#model-development)
6. [Installation and Setup](#installation-and-setup)
7. [Usage](#usage)
8. [Results](#results)
9. [Contributing](#contributing)
10. [License](#license)
11. [Contact](#contact)

## Project Overview

This project focuses on **predicting flight prices** using **Machine Learning algorithms**. The goal is to build a predictive model that can accurately forecast the price of flights based on various features such as departure date, destination, airline, and other relevant information. The project uses different machine learning techniques, including **Linear Regression**, **XGBoost**, and **AdaBoost**, to achieve high accuracy.

The model achieved a prediction accuracy of **93%**, which can be highly useful for both airlines and travelers to get a sense of future flight prices.

## Features

- **Prediction of flight prices** based on input features like airline, source, destination, and date of journey.
- Integration of advanced machine learning techniques like **XGBoost** and **AdaBoost**.
- **Web application** built using Python Flask for a user-friendly experience.
- **Interactive visualization** of the dataset and results.

## Technologies Used

- **Programming Language:** Python
- **Web Framework:** Flask
- **Machine Learning Libraries:** Scikit-learn, XGBoost, AdaBoost
- **Data Analysis Libraries:** Pandas, NumPy
- **Data Visualization Libraries:** Matplotlib, Seaborn
- **IDE:** Jupyter Notebook

## Dataset

The dataset used in this project is taken from Kaggle and contains flight details like:

- **Airline**
- **Source**
- **Destination**
- **Departure Date**
- **Arrival Time**
- **Duration**
- **Total Stops**

You can download the dataset from the 'data' folder

## Model Development

The project includes the following machine learning models:

- **Linear Regression**: A simple regression model to predict flight prices based on input features.
- **XGBoost**: A powerful ensemble learning method that enhances performance using gradient boosting.
- **AdaBoost**: Another ensemble technique that works by combining multiple weak learners to create a strong predictive model.

The data was preprocessed to handle missing values, categorical variables, and outliers. Features were selected based on correlation analysis and domain knowledge.

## Installation and Setup

Follow these steps to set up the project locally:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/palpratik56/Flight-Price-Prediction-using-ML.git
    ```
2. **Navigate to the project directory:**
    ```bash
    cd Flight-Price-Prediction-using-ML
    ```
3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Run the Flask web app:**
    ```bash
    python app.py
    ```
5. **Open your browser** and go to `http://127.0.0.1:5000/` to access the web application.

## Usage

Once the web app is running, you can:

- Input flight details like **airline**, **source**, **destination**, **date of journey**, and more.
- The app will predict the **price of the flight** based on the input data.
- You can also visualize data trends using graphs integrated into the app.

## Results

The model achieves a high accuracy of **93%** for predicting flight prices. This high accuracy was accomplished through feature engineering, data preprocessing, and using robust machine learning algorithms like **XGBoost** and **AdaBoost**.

Example Results:

| Model           | Accuracy |
|-----------------|----------|
| Linear Regression | 85%      |
| XGBoost         | 93%      |
| AdaBoost        | 92%      |

## Contributing

Feel free to submit issues and enhancement requests or create pull requests. Contributions are always welcome!

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request
