import streamlit as st
import joblib
import os
import time

st.title('Twitter Sentiment Analysis')

model = None
model_path = os.path.join('models', 'twitter_sentiment.sav')

if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    st.error("❌ Model file not found. Make sure 'twitter_sentiment.sav' is in the 'models' folder.")
    st.stop()  # Stop the app if model isn't available

tweet = st.text_input('Enter your tweet')

if st.button('Predict'):
    if not tweet.strip():
        st.warning("⚠️ Please enter a tweet.")
    else:
        start = time.time()
        prediction = model.predict([tweet])
        end = time.time()
        st.success(f"Prediction: {prediction[0]}")
        st.write(f"⏱️ Prediction time: {round(end - start, 2)} seconds")
