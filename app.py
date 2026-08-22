import streamlit as st
import pandas as pd
st.set_page_config(page_title="نور",page_icon="✨")
st.title("مساعد نور ✨")
st.caption("النسخة الذكية مع الجداول")

if "messages" not in st.session_state:
    st.session_state.messages=[]

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

p=st.chat_input("اكتبي: ابغى جدول")
if p:
    with st.chat_message("user"):
        st.write(p)
    with st.chat_message("assistant"):
        if "جدول" in p:
            st.write("تفضلي جدولك ✨")
            df=pd.DataFrame({
                "اليوم":["السبت","الأحد","الاثنين","الثلاثاء"],
                "المادة":["رياضيات","فيزياء","انجليزي","مراجعة"],
                "الوقت":["4-6 م","4-6 م","5-7 م","مفتوح"]
            })
            st.table(df)
        else:
            st.write(f"هلا! سؤالك: {p}")
