import streamlit as st


st.set_page_config(
    page_title="Multipage",
    page_icon="👋",
)

st.title = ("Main page")
st.sidebar.success("Select a page above.")


col1, col2, col3 = st.columns(3)

with col2:
    co = st.text_input("Input your thing ?")
    st.write(f'Your thing is   :  {co}')

