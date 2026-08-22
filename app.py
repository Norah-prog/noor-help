import streamlit as st

st.set_page_config(page_title="نور", page_icon="✨")

st.title("أهلاً بك في مساعد نور ✨")
st.write("أنا هنا لأساعدك")

سؤال = st.text_input("اكتبي سؤالك:")

if سؤال:
    st.success("سؤالك: " + سؤال)
