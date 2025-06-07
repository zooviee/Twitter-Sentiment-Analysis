import streamlit as st
import joblib
import time
import os

model_path = "models/twitter_sentiment.sav"

# Load the compressed model
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    st.error("Model file not found. Please make sure it's in the 'models' folder.")

# Streamlit interface
st.title('Twitter Sentiment Analysis')
tweet = st.text_input('Enter your tweet')

if st.button('Predict'):
    start = time.time()
    prediction = model.predict([tweet])
    end = time.time()
    st.write('Prediction:', prediction[0])
    st.write('Prediction time:', round(end - start, 2), 'seconds')