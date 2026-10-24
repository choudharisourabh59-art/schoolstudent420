import streamlit as st,pandas as pd
from database.connection import connect
def render(user):
    st.title("Reports")
    with connect() as con:
        s=pd.read_sql_query("SELECT class_name,COUNT(*) count FROM students GROUP BY class_name",con)
        a=pd.read_sql_query("SELECT day,status,COUNT(*) count FROM attendance GROUP BY day,status ORDER BY day",con)
        g=pd.read_sql_query("""SELECT e.title,e.subject,AVG(r.marks*100.0/e.max_marks) average_percent
        FROM results r JOIN exams e ON e.id=r.exam_id GROUP BY e.id""",con)
    st.subheader("Students by class"); st.dataframe(s,use_container_width=True,hide_index=True)
    st.subheader("Attendance"); st.dataframe(a,use_container_width=True,hide_index=True)
    st.subheader("Exam averages"); st.dataframe(g,use_container_width=True,hide_index=True)
    st.download_button("Download class report",s.to_csv(index=False).encode(),"class_report.csv","text/csv")
