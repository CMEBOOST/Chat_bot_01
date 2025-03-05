import  streamlit as st
from ollama import chat

col1, col2, col3 = st.columns(3)

with col1:
    container1 = st.container(border=True)

    # ใช้ Markdown + CSS เพื่อจัดกึ่งกลาง
    with container1:
        st.markdown(
            """
            <div style="display: flex; justify-content: center; align-items: center; height: 50px; font-size: 20px; font-weight: bold;">
                Chat me 👋
            </div>
            """,
            unsafe_allow_html=True
        )

    container2 = st.container(border=True)
    clicked = container2.button(' Add chat')
    
    container2.write("Chat mes !")
    st.write("This is outside the container")

# Now insert some more in the container
    container2.write("This is inside too")


    with container1.popover("Open popover"):
        name = container1.text_input("What's your name?")



with col2:
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

    ### send user_massage to ollama and get back the response....
    # answer = f'thank you for your message "{user_message}"'
        with st.chat_message("assistant"):
            response_container = st.empty()
            full_response = ""
            for chunk in chat(model="deepseek-r1", messages=[{'role': 'user', 'content': user_message}], stream=True):
                full_response += chunk["message"]["content"]
            response_container.markdown(full_response + "▌")
            response_container.markdown(full_response)

        st.session_state.messages.append({"role": "assistant", "content": full_response})


with col1:
    with st.popover("Setting"):
        st.write("font_size")
        st.markdown("Hello World 👋")
