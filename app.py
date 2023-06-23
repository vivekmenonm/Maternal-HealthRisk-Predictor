import streamlit as st
import pickle
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
# Load the pickled model
model = pickle.load(open('model.pkl', 'rb'))

# Function to make predictions
def predict_category(input_features):
    input_array = [input_features]  # Convert to 2D array
    prediction = model.predict(input_array)
    risk_levels = ['High Risk', 'Low Risk','Mid Risk']
    original_label = risk_levels[prediction[0]]
    return original_label



# Streamlit app
def main():
    st.set_page_config(page_title="Maternal Health Risk Predictor", page_icon="❤️")
    st.title("Maternal Health Risk Predictor")
    st.write("Enter the values")

    # Input boxes
    feature1 = st.number_input("Age", step=1)
    feature2 = st.number_input("SystolicBP", step=1)
    feature3 = st.number_input("DiastolicBP", step=1)
    feature4 = st.number_input("BS", step=0.1)
    feature5 = st.number_input("BodyTemp", step=0.1)
    feature6 = st.number_input("HeartRate", step=1)

    if st.button("Predict"):
        # Make prediction
        input_features = [feature1, feature2, feature3, feature4, feature5, feature6]
        category = predict_category(input_features)
        st.write(f"Category of risk: {category}")

if __name__ == "__main__":
    main()
