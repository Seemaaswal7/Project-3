import streamlit as st
import pandas as pd
import catboost as cat

# Load the trained catboost model
model = cat.Booster()
model.load_model('C:\Users\seema\OneDrive\Desktop\Project 3/catboost.pkl')

# Function to preprocess input data
def preprocess_input(data):
    data = pd.read_csv('DataFinal.csv')
    return data

# Function to make predictions
def predict_price(data):
    # Preprocess the input data
    processed_data = preprocess_input(data)

    # Convert the input data to a DMatrix
    dmatrix = cat.DMatrix(processed_data)

    # Make predictions using the loaded model
    predictions = model.predict(dmatrix)

    return predictions

# Main Streamlit app
def main():
    # Set the title of the app
    st.title("Housing Price Prediction")

    # Create input fields for user to enter housing features
    Borough = st.number_input("Borough")
    Neighborhood = st.number_input("Neighborhood")
    Residential_Units = st.number_input("Residential_Units")
    Building_Class_At_Time_Of_Sale = st.number_input("Building_Class_At_Time_Of_Sale")
    Building_Class_Category = st.number_input("Category")
    Land_Square_Feet = st.number_input("Number of bedrooms")
    Year Built = st.number_input("Year Bulit")
    latitude = st.number_input("latitude")
    longitude =st.number_input("latitude")
    # Add more features as needed

    # Create a DataFrame with the input data
    input_data = pd.DataFrame({'Borough': [Borough],
                               'Building_Class_Category':[Building_Category],
                               'Land_Square_Feet':[Land_Square_Feet],
                               'Building_Class_At_Time_Of_Sale':[Building_Class_At_Time_Of_Sale],
                               'Neighborhood':[Neighborhood],
                               'Residential_Units':[Residential_Units],
                               'Year Built': [Year_Built],
                               'latitude': [latitude],
                               'longitude': [Longiude]})
    # Add more features as needed

    # Make predictions when the user clicks the "Predict" button
    if st.button("Predict"):
        # Call the predict_price function to get the predicted price
        predicted_price = predict_price(input_data)

        # Display the predicted price to the user
        st.success(f"The predicted price is ${predicted_price[0]:,.2f}")

# Run the app
if __name__ == '__main__':
    main()