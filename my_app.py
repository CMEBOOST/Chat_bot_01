import streamlit as st


# -- Page setup --

about_page = st.Page(
    page ='views/about_me.py',
    title="About me",
    icon='',
    default=True,
)


project_1_page = st.Page(
    page="views/chatbot.py",
    title='Chat bot',
    icon=':material/chat:'
)
project_2_page = st.Page(
    page="views/log.py",
    title='Log na',
    icon=':material/settings:',
)

pg =st.navigation(
    {
        "info":[about_page],
        "Project":[project_1_page, project_2_page]
    }
)

st.logo("assets/Ubon_Ratchathani_Univ_Emblem.svg.png",)
st.sidebar.text('Welcome to our Project ❤')
pg.run()

