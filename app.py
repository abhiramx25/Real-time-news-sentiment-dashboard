import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="News Sentiment Dashboard", layout="wide")
st.title("Abhiram's Real-Time News Sentiment Dashboard <3 ")

# Load predictions.csv from local repo
if os.path.exists("predictions.csv"):
    df = pd.read_csv("predictions.csv")
else:
    df = pd.DataFrame()
    st.warning("predictions.csv not found! Please run the notebook first.")

if not df.empty:
    st.subheader("Sentiment Distribution")
    st.bar_chart(df["sentiment"].value_counts())

    st.subheader("Recent Headlines")
    st.dataframe(df[["publishedAt", "source", "text", "sentiment", "prob_pos", "url"]].head(20))


