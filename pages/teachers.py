import streamlit as st,pandas as pd
from database.connection import connect
def render(user):
    st.title("Teachers")
    if user["role"]!="admin": st.warning("Admin access only."); return
    with st.form("teacher"):
        emp=st.text_input("Employee number"); name=st.text_input("Name"); subject=st.text_input("Subject")
        phone=st.text_input("Phone"); email=st.text_input("Email"); assigned=st.text_input("Assigned class")
        submit=st.form_submit_button("Add teacher")
    if submit:
        if not emp.strip() or not name.strip(): st.error("Employee number and name required.")
        else:
            with connect() as con: con.execute("INSERT INTO teachers(employee_no,name,subject,phone,email,assigned_class) VALUES(?,?,?,?,?,?)",(emp,name,subject,phone,email,assigned))
            st.success("Teacher saved.")
    with connect() as con: df=pd.read_sql_query("SELECT * FROM teachers",con)
    st.dataframe(df,use_container_width=True,hide_index=True)
