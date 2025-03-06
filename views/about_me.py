import streamlit as st
from fn import stream_data
@st.dialog('Contace Me')
def show_contact_from():
    st.text_input("Frist Name")

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("assets/pic.jpg", width=230, )
with col2:
    st.header('OOP - ChatBOT')
    st.write(
        "นาย สุรเชษฐ์ สีสา ระหัสนักศึกษา 67114540583"
    )
    if st.button("💨 Contace Me"):
        show_contact_from()

st.write("\n")
info_01 = st.button("Information!")

info__ = """
เรียนอาจารย์ อาจารย์ ดร.วิชิต สมบัติ และ อาจารย์ ประจำวิชาทุกท่าน\n
:material/settings: ใช้ AI Moel : DeepSeek-R1 เพราะเป็นตัวที่ดีตอบคำถามได้อย่างครบถ้วน และไม่กินพื้นที่ทรัพยากร")
"""

if info_01:
    st.write(stream_data(info__))

