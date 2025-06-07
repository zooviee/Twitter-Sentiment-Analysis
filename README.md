# Twitter Sentiment Analysis

This project is a machine learning-powered web app that analyzes the sentiment of tweets using a pre-trained model. Built with Streamlit, the app predicts whether a tweet expresses a positive, negative, or neutral sentiment.

🚀 Features
- 🌐 Web interface using Streamlit
- 🔍 Input any tweet and get instant sentiment prediction
- ⏱️ Fast model inference using a pre-trained Scikit-learn model (.sav file)
- 📦 Lightweight and easily deployable on Streamlit Cloud

🧰 Technologies Used
- Python
- Scikit-learn
- Joblib
- Streamlit
- Pandas, NumPy
- Matplotlib, Seaborn

📁 Project Structure
.
├── app.py                     # Main Streamlit app
├── models/
│   └── twitter_sentiment.sav  # Trained model (compressed)
├── requirements.txt           # Project dependencies
├── sentiment.ipynb            # Jupyter notebook
├── twitter_sentiment.csv      # Dataset
└── .gitignore

📦 How to Run Locally
# Clone the repo
git clone https://github.com/yourusername/twitter-sentiment-streamlit.git
cd twitter-sentiment-streamlit

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch Streamlit app
streamlit run app.py

☁️ Deploy on Streamlit Cloud

To deploy this app:

1. Go to streamlit.io/cloud and sign in
2. Click “New App”
3. Connect your GitHub repo (twitter-sentiment-streamlit)
4. Set app.py as the entry point
5. Click “Deploy”

NOTE: Make sure requirements.txt is in the root and your model file is committed to models/
