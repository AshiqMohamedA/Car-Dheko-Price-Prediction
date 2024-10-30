# Car Price Prediction Application

This repository contains a **Streamlit-based Car Price Prediction Application** that estimates the ideal price of a car based on selected car specifications. It uses a trained machine learning model to provide a price prediction based on specific features chosen by the user, such as city, fuel type, body type, kilometers driven, transmission type, number of owners, and car model.

## Table of Contents
- [Project Overview](#project-overview)
- [Data and Model Loading](#data-and-model-loading)
- [Application Workflow](#application-workflow)
- [Dependencies](#dependencies)
- [Installation and Usage](#installation-and-usage)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Project Overview

The Car Price Prediction Application uses a machine learning model to predict the price of a car based on various features. The app allows users to input information about the car and, upon clicking the "Predict Ideal Price" button, returns the estimated price based on the selected characteristics.

## Data and Model Loading

### Data
The app loads car data from an **Excel file** (`data.xlsx`), which contains relevant details like city, fuel type, body type, kilometers driven, transmission type, number of owners, car model, and other attributes required for the prediction.

### Model
A pre-trained **Random Forest model** (`rf.pkl`) is loaded from a pickle file. The model was trained on a dataset similar in structure to the data provided in `data.xlsx`.

### Encoders
To handle categorical data, the application loads pickled **encoders** (`encoders.pkl`) for each categorical column. These encoders ensure the categorical features match the format used during model training, enabling accurate predictions.

## Application Workflow

1. **User Input**:
   - Users are prompted to select details about the car, including:
     - City
     - Fuel Type
     - Body Type
     - Kilometers Range
     - Transmission Type
     - Number of Owners
     - OEM (Original Equipment Manufacturer)
     - Model
     - Model Year
     - Variant

2. **Automatic Retrieval of Additional Details**:
   - Based on the selected model and year, specific details about engine capacity, max power, seats, and mileage are automatically populated from the loaded dataset.

3. **Encoding Categorical Variables**:
   - Before prediction, categorical features are encoded using the preloaded encoders. If an unknown category is encountered, a default encoding of `-1` is applied.

4. **Prediction**:
   - Upon clicking the **"Predict Ideal Price"** button, the application:
     - Prepares the selected input features in the format expected by the model.
     - Predicts the ideal car price using the loaded machine learning model.
     - Displays the predicted price in the application interface.

5. **Error Handling**:
   - The application includes error handling for any prediction issues, displaying relevant messages if a problem arises.

## Dependencies

- **Python 3.7 or higher**
- Libraries:
  - `pandas`
  - `streamlit`
  - `pickle` (part of Python's standard library)

## Installation and Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/username/car-price-prediction-app.git
   cd car-price-prediction-app


##Install Dependencies:
pip install -r requirements.txt

##Place Required Files:
Add the Excel data file (data.xlsx) to the root of the project.
Add the trained model file (rf.pkl) and encoders file (encoders.pkl) to the root of the project.


##Run the Application:
streamlit run main.py

##Use the Application:
The app will open in your web browser.
Select car specifications step-by-step.
Click "Predict Ideal Price" to get an estimated price.


##Future Enhancements
Enhanced Model Training: Retrain the model on a larger and more diverse dataset.
Real-time Data Update: Enable dynamic updates to the dataset and retrain the model periodically.
Expanded Feature Selection: Allow more features for users to select and refine the prediction further.
Visualization: Add data visualizations to show feature importances or model performance metrics.

##License
This project is licensed under the MIT License. See the LICENSE file for more details.


This `README.md` provides a structured overview of your Car Price Prediction app, explaining the application
