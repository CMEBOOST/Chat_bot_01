import streamlit as st
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
if info_01:
    st.markdown('เรียนอาจารย์ อาจารย์ ดร.วิชิต สมบัติ และ อาจารย์ ประจำวิชาทุกท่าน')
    st.markdown(":material/settings: ใช้ AI Moel : DeepSeek-R1 เพราะเป็นตัวที่ดีตอบคำถามได้อย่างครบถ้วน และไม่กินพื้นที่ทรัพยากร")
    col = st.columns(3)
    with col[1]:
        st.markdown('Function การทำงาน')