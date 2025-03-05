import  streamlit as st
from ollama import chat

col1, col2, col3 = st.columns(3)

con1 = st.container(height=110,border=100)

con1.write("Welcome to Chat bot --> DeepSeek-R1")



if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(name=message['role']):
        st.write(message['content'])

user_message = st.chat_input("type something...")
if user_message:
    st.session_state.messages.append({
        'role': 'user',
        'content': user_message
    })
    with st.chat_message(name='user'):
        st.write(user_message)
        
    with st.chat_message("assistant"):
        response_container = st.empty()
        full_response = ""
        for chunk in chat(model="deepseek-r1", messages=[{'role': 'user', 'content': user_message}], stream=True):
            full_response += chunk["message"]["content"]
            response_container.markdown(full_response + "▌")
        response_container.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
