import streamlit as st,pandas as pd
from database.connection import connect
def render(user):
    st.title("Examinations")
    if user["role"] not in ("admin","teacher"): st.warning("Access limited to teachers/admins."); return
    with st.form("exam"):
        title=st.text_input("Exam title"); cls=st.selectbox("Class",[str(i) for i in range(1,13)])
        subject=st.text_input("Subject"); maximum=st.number_input("Maximum marks",min_value=1.0,value=100.0)
        day=st.date_input("Exam date"); submit=st.form_submit_button("Create exam")
    if submit:
        if not title.strip() or not subject.strip(): st.error("Title and subject required.")
        else:
            with connect() as con: con.execute("INSERT INTO exams(title,class_name,subject,max_marks,exam_day) VALUES(?,?,?,?,?)",(title,cls,subject,maximum,day.isoformat()))
            st.success("Exam created.")
    with connect() as con: df=pd.read_sql_query("SELECT * FROM exams ORDER BY exam_day DESC",con)
    st.dataframe(df,use_container_width=True,hide_index=True)
