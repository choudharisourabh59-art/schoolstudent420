import streamlit as st,pandas as pd
from datetime import date
from database.connection import connect
from services.attendance_service import save_attendance
def render(user):
    st.title("Attendance")
    with connect() as con: roster=pd.read_sql_query("SELECT id,name,class_name FROM students WHERE status='Active'",con)
    if roster.empty: st.info("Add students first."); return
    cls=st.selectbox("Class",sorted(roster.class_name.unique())); day=st.date_input("Date",date.today()).isoformat()
    roster=roster[roster.class_name==cls]
    with st.form("attendance"):
        values={int(s.id):st.selectbox(s.name,["Present","Absent","Late"],key=f"att{s.id}{day}") for _,s in roster.iterrows()}
        submit=st.form_submit_button("Save attendance")
    if submit:
        for sid,status in values.items(): save_attendance(sid,day,status)
        st.success("Attendance saved.")
    with connect() as con: hist=pd.read_sql_query("SELECT day,status,COUNT(*) count FROM attendance GROUP BY day,status ORDER BY day",con)
    st.dataframe(hist,use_container_width=True,hide_index=True)
