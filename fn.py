import time
import streamlit as st
from datetime import datetime


def stream_data(info):
    for word in info.split(" "):
        yield word + " "
        time.sleep(0.10)

def time_naja():
    time_display = st.empty()
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        time_display.text(f"เวลาปัจจุบัน: {current_time}")
        time.sleep(1)
