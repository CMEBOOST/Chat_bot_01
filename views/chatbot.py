import streamlit as st
import pandas as pd
from ollama import chat
import os

LOG_FILE = "chat_logs.csv"

if os.path.exists(LOG_FILE):
    chat_logs = pd.read_csv(LOG_FILE)
else:
    chat_logs = pd.DataFrame(columns=["Chat", "Role", "Message"])

cols = st.columns(2)

with cols[0]:
    select_bot = st.selectbox(
        "What AI Model You'll use ?",
        ("DeepSeek-R1", "llama3.1")
    )
    st.write(f'Model AI : {select_bot}')
    st.write(f'\n')

with cols[1]:
    if 'chat_list' not in st.session_state:
        st.session_state.chat_list = ['chat_1', 'chat_2']
    
    select_chat = st.selectbox('Select Chat', st.session_state.chat_list)
    
    if 'show_add_chat' not in st.session_state:
        st.session_state.show_add_chat = False
    
    if st.button("➕ Add New Chat"):
        st.session_state.show_add_chat = not st.session_state.show_add_chat
    
    if st.session_state.show_add_chat:
        new_chat_name = st.text_input("Enter new chat name:", key="new_chat_name")
        if st.button("✅ Confirm Add Chat"):
            if new_chat_name and new_chat_name not in st.session_state.chat_list:
                st.session_state.chat_list.append(new_chat_name)
                st.session_state.chat_sessions[new_chat_name] = [] 
                st.session_state.show_add_chat = False 

#สร้่างแยกกัน
if 'chat_sessions' not in st.session_state:
    st.session_state.chat_sessions = {}
if select_chat not in st.session_state.chat_sessions:
    st.session_state.chat_sessions[select_chat] = []

model_name = select_bot

with st.chat_message('assistant'):
    st.write(f"Hello, I'm AI assistant Model : {model_name}\n"
             "What can I help you with today?")

# แสดงข้อความแชทของห้องที่เลือก
for message in st.session_state.chat_sessions[select_chat]:
    with st.chat_message(name=message['role']):
        st.write(message['content'])

# รับข้อความจากผู้ใช้
user_message = st.chat_input("Type something...")

if user_message:
    st.session_state.chat_sessions[select_chat].append({
        'role': 'user',
        'content': user_message
    })
    chat_logs = pd.concat([chat_logs, pd.DataFrame([[select_chat, 'user', user_message]], columns=["Chat", "Role", "Message"])], ignore_index=True)
    chat_logs.to_csv(LOG_FILE, index=False)
    
    with st.chat_message(name='user'):
        st.image("assets/pic.jpg")
        st.write(user_message)
    
    with st.chat_message("assistant"):
        response_container = st.empty()
        full_response = ""
        for chunk in chat(model=model_name,
                          messages=[{'role': 'user', 'content': user_message}] + st.session_state.chat_sessions[select_chat],
                          stream=True):
            full_response += chunk["message"]["content"]
            response_container.markdown(full_response + "▌")
        response_container.markdown(full_response)
    
    st.session_state.chat_sessions[select_chat].append({"role": "assistant", "content": full_response})
    chat_logs = pd.concat([chat_logs, pd.DataFrame([[select_chat, 'assistant', full_response]], columns=["Chat", "Role", "Message"])], ignore_index=True)
    chat_logs.to_csv(LOG_FILE, index=False)


bottom_placeholder = st.empty()
bottom_placeholder.write(" Chat logs saved to file: `chat_logs.csv`")
