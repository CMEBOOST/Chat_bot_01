import streamlit as st
from fn import stream_data
from myinfo import *
from forms.contact import contact_form

@st.dialog('Contace Me')
def show_contact_from():
    contact_form()
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("assets/pic.jpg", width=230, )
with col2:
    st.header('OOP - ChatBOT',divider="gray")
    st.write(
        "นาย สุรเชษฐ์ สีสา ระหัสนักศึกษา 67114540583\n"
        "Email 📩: surachet.se.67@ubu.ac.th"
    )
    if st.button("💨 Contace Me"):
        show_contact_from()

st.write("\n")
info_00 = st.button("Information!")


if info_00:
    st.markdown('**เรียนอาจารย์ อาจารย์ ดร.วิชิต สมบัติ และ อาจารย์ ประจำวิชาทุกท่าน**')
    st.write(stream_data(info_03))
    coll = st.columns(2)
    con1 = st.container(border=True)
    with coll[0]:
        con = st.container(border=True)
        con.write(stream_data(info_02))
    with coll[1]:
        con1 = st.container(border=True)
        con1.write(stream_data(info_04))

