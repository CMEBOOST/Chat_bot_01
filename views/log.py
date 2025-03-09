import streamlit as st
import pandas as pd
import os

LOG_FILE = "chat_logs.csv"

st.title("Chat Logs")

if os.path.exists(LOG_FILE):
    chat_logs = pd.read_csv(LOG_FILE)
    st.subheader("Chat Logs Table")
    st.dataframe(chat_logs)
    
else:
    st.write("No chat logs found.")
