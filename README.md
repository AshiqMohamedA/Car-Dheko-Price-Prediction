# Car Dekho Project

This project aims to develop a **used car price prediction tool** leveraging machine learning to improve customer experience and streamline pricing processes. Built as an interactive application using **Streamlit**, this tool enables customers and sales representatives to efficiently estimate used car values based on various features.

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Preprocessing and Feature Engineering](#preprocessing-and-feature-engineering)
- [Modeling](#modeling)
- [Application Deployment](#application-deployment)
- [Installation and Usage](#installation-and-usage)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Project Overview
This application predicts the price of used cars by analyzing various features including **engine specifications, dimensions, mileage**, and **other attributes**. Key objectives include:
- Identifying key features influencing used car prices.
- Handling outliers and adjusting feature distributions.
- Building a reliable and user-friendly price prediction model.
- Deploying the model via Streamlit for easy accessibility.

## Dataset
The dataset comprises information on used cars with multiple features:
- **Basic Information**: Model year, price, and brand.
- **Engine and Transmission**: Engine type, power, torque, and displacement.
- **Dimensions & Capacity**: Length, width, front tread, and wheel size.
- **Miscellaneous Features**: Acceleration, top speed, and fuel capacity.

Data preprocessing involved:
- Handling missing values.
- Removing highly correlated features.
- Addressing outliers using the IQR method.
- Transforming features for normal distribution.

## Preprocessing and Feature Engineering
1. **Outlier Detection**: Identified and addressed using IQR to ensure model robustness.
2. **Correlation Analysis**: Reduced features with a correlation threshold of 0.8, lowering dimensionality to essential features.
3. **Final Feature Selection**: Reduced to 35 key features to optimize model performance.

## Modeling
Multiple machine learning models were tested to select the most accurate and efficient predictor:
- **Algorithms Used**: Linear Regression, Decision Tree Regressor, Random Forest, and XGBoost.
- **Evaluation Metrics**: Used RMSE, MAE, and R-squared to compare model performance.

## Application Deployment
The final model is integrated into a Streamlit app, allowing users to:
- Input car details and receive price predictions.
- Visualize feature importances and predictions with interactive elements.

## Installation and Usage

### Prerequisites
- Python 3.7 or higher
- Libraries: `numpy`, `pandas`, `sklearn`, `streamlit`, `seaborn`, `matplotlib`

### Setup
Clone the repository and navigate to the project folder:
```bash
git clone https://github.com/username/car-dekho-project.git
cd car-dekho-project
