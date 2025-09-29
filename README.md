# Real-time News Sentiment Dashboard

# Overview
This project performs real-time news sentiment classification using PySpark ML pipeline and visualizes the results in an interactive Streamlit dashboard.  

- Fetches live news headlines from [NewsAPI](https://newsapi.org/).  
- Uses **VADER** for weak labeling of news headlines.  
- Trains a **PySpark ML pipeline** (Tokenizer → StopWords → TF-IDF → Logistic Regression).  
- Predicts sentiment (Positive / Negative) on fresh news.  
- Visualizes sentiment distribution and recent headlines on Streamlit.
-
# Features
- Real-time news fetching from NewsAPI.  
- Automatic weak-labeling using VADER.  
- Trainable PySpark ML model for sentiment classification.  
- Streamlit dashboard for interactive visualization.  
- Save predictions to `predictions.csv` for further analysis.

---

