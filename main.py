import pandas as pd
import streamlit as st
import pickle

# Load the Excel file
file_path = 'data.xlsx'  # Replace with the path to your Excel file
df = pd.read_excel(file_path)

# Load the trained model
model_file_path = 'rf.pkl'  # Replace with your actual model file path
with open(model_file_path, 'rb') as file:
    model = pickle.load(file)

# Load the encoders for categorical columns
encoder_file_path = 'encoders.pkl'  # Path to the encoders (if saved)
with open(encoder_file_path, 'rb') as file:
    encoders = pickle.load(file)

# Streamlit App Function
def create_streamlit_app(df, model, encoders):
    st.title('Car Dheko Selection Interface')

    # Step-by-step selections
    selected_city = st.selectbox('Select City', options=df['city'].unique())
    
    if selected_city:
        selected_ft = st.selectbox('Select Fuel Type', options=df['ft'].unique())
        
        if selected_ft:
            selected_bt = st.selectbox('Select Body Type', options=df['bt'].unique())
            
            if selected_bt:
                km_ranges = [(i, i + 5000) for i in range(5000, 200001, 5000)]
                selected_km_range = st.selectbox('Select Kilometers Range', options=[f"{km[0]}-{km[1]}" for km in km_ranges])
                
                if selected_km_range:
                    selected_transmission = st.selectbox('Select Transmission Type', options=df['transmission'].unique())
                    
                    if selected_transmission:
                        selected_ownerNo = st.selectbox('Select Number of Owners', options=df['ownerNo'].unique())
                        
                        if selected_ownerNo:
                            selected_oem = st.selectbox('Select OEM', options=df['oem'].unique())
                            
                            if selected_oem:
                                filtered_models = df[df['oem'] == selected_oem]['model'].unique()
                                selected_model = st.selectbox('Select Model', options=filtered_models)
                                
                                if selected_model:
                                    # Filter the DataFrame for selected OEM and model to retrieve specific details
                                    filtered_data = df[(df['oem'] == selected_oem) & (df['model'] == selected_model)]

                                    # Model year selection based on selected OEM and model
                                    model_year_options = filtered_data['modelYear'].unique()
                                    selected_model_year = st.selectbox('Select Model Year', options=model_year_options)

                                    # Retrieve specific attributes based on selection
                                    car_details = filtered_data[filtered_data['modelYear'] == selected_model_year].iloc[0]
                                    selected_engine = car_details['Engine']
                                    selected_max_power = car_details['Max Power']
                                    selected_seat = car_details['Seats']
                                    selected_mileage = car_details['Mileage']

                                    st.write("Automatically Retrieved Details:")
                                    st.write(f"Engine Capacity: {selected_engine}")
                                    st.write(f"Max Power: {selected_max_power}")
                                    st.write(f"Number of Seats: {selected_seat}")
                                    st.write(f"Mileage: {selected_mileage}")

                                    # Variant selection specific to the chosen OEM, model, and model year
                                    variant_options = filtered_data[filtered_data['modelYear'] == selected_model_year]['variantName'].unique()
                                    selected_variant = st.selectbox('Select Variant', options=variant_options)

    # Prediction process only runs when the button is clicked
    if st.button('Predict Ideal Price'):
        # Prepare the input for prediction
        input_data = pd.DataFrame({
            'km': [int(selected_km_range.split('-')[0])],  # Convert range to start value
            'ownerNo': [selected_ownerNo],
            'modelYear': [selected_model_year],
            'Seats': [selected_seat],
            'Mileage': [selected_mileage],
            'Engine': [selected_engine],
            'Max Power': [selected_max_power],
            'city': [selected_city],
            'ft': [selected_ft],
            'bt': [selected_bt],
            'transmission': [selected_transmission],
            'oem': [selected_oem],
            'model': [selected_model],
            'variantName': [selected_variant]
        })

        # Apply the encoders for categorical features with default encoding for unknown values
        for col in ['city', 'ft', 'bt', 'transmission', 'oem', 'model', 'variantName']:
            if input_data[col][0] not in encoders[col].classes_:
                input_data[col] = -1  # Assign a default encoding if the value is not in the encoder's classes
            else:
                input_data[col] = encoders[col].transform(input_data[col])

        # Ensure only columns that match model's features are used, and reorder to match the model's training order
        input_data = input_data[['km', 'ownerNo', 'modelYear', 'Seats', 'Mileage', 'Engine', 'Max Power', 
                                 'city', 'ft', 'bt', 'transmission', 'oem', 'model', 'variantName']]

        # Perform the prediction
        try:
            predicted_price = model.predict(input_data)[0]
            st.success(f"The predicted ideal price for the selected car is: ₹{predicted_price:.2f} Lakh")
        except ValueError as e:
            st.error(f"Prediction Error: {str(e)}")
        except Exception as e:
            st.error(f"Unexpected Error: {str(e)}")

# Main function to run the Streamlit app
if __name__ == '__main__':
    create_streamlit_app(df, model, encoders)
