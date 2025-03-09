import streamlit as st
from myinfo import *
from fn import stream_data
st.title("This is sumery of work")

info_00 = st.button("Information!")


if info_00:
    st.write(stream_data(info_03))
    coll = st.columns(2)
    con1 = st.container(border=True)
    with coll[0]:
        con = st.container(border=True)
        con.write(stream_data(info_02))
    with coll[1]:
        con1 = st.container(border=True)
        con1.write(stream_data(info_04))




st.write(stream_data(summer))