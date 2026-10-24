import streamlit as st
from services.auth_service import logout
def navigation(user):
    with st.sidebar:
        st.title("🎓 School ERP"); st.caption(f"{user['username']} · {user['role']}")
        if user["role"] in ("student","parent"): options=["My Portfolio","Documents"]
        elif user["role"]=="teacher": options=["Dashboard","Students","Attendance","Examinations","Results","Documents","Reports"]
        else: options=["Dashboard","Students","Teachers","Attendance","Examinations","Results","My Portfolio","Documents","Reports","Settings"]
        page=st.radio("Navigation",options)
        if st.button("Log out"): logout()
        return page
