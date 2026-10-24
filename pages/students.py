import streamlit as st,pandas as pd
from database.connection import connect
from components.forms import student_form
from services.student_service import add_student
def render(user):
    st.title("Students")
    if user["role"]=="admin":
        submit,data=student_form()
        if submit:
            try:
                add_student(data["admission"],data["name"],data["class_name"],data["section"],data["roll"],data["guardian"],data["phone"],data["email"])
                st.success("Student created."); st.rerun()
            except Exception as e: st.error(str(e))
    search=st.text_input("Search students")
    with connect() as con: df=pd.read_sql_query("SELECT admission_no,name,class_name,section,roll_no,guardian,phone,status FROM students",con)
    if search: df=df[df.astype(str).apply(lambda c:c.str.contains(search,case=False,na=False)).any(axis=1)]
    st.dataframe(df,use_container_width=True,hide_index=True)
    st.download_button("Export students CSV",df.to_csv(index=False).encode(),"students.csv","text/csv")
