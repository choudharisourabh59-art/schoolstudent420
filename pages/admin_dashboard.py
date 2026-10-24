import streamlit as st,pandas as pd,plotly.express as px
from database.connection import connect
def render(user):
    st.title("Admin Dashboard")
    with connect() as con:
        n=con.execute("SELECT COUNT(*) FROM students WHERE status='Active'").fetchone()[0]
        t=con.execute("SELECT COUNT(*) FROM teachers").fetchone()[0]
        attendance=con.execute("SELECT COUNT(*) FROM attendance WHERE day=date('now')").fetchone()[0]
        exams=con.execute("SELECT COUNT(*) FROM exams").fetchone()[0]
        byclass=pd.read_sql_query("SELECT class_name,COUNT(*) count FROM students GROUP BY class_name",con)
    a,b,c,d=st.columns(4); a.metric("Active students",n); b.metric("Teachers",t); c.metric("Attendance entries today",attendance); d.metric("Exams",exams)
    if not byclass.empty: st.plotly_chart(px.bar(byclass,x="class_name",y="count",title="Students by class"),use_container_width=True)
