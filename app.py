import streamlit as st
from config.settings import APP_TITLE
from database.connection import init_db
from services.auth_service import login_form
from components.sidebar import navigation
from pages import admin_dashboard, students, teachers, attendance, examinations, results, portfolio, documents, reports, settings_page

st.set_page_config(page_title=APP_TITLE, page_icon="🎓", layout="wide")
init_db()
if "user" not in st.session_state:
    login_form()
    st.stop()
user = st.session_state.user
page = navigation(user)
routes = {
    "Dashboard": admin_dashboard.render, "Students": students.render,
    "Teachers": teachers.render, "Attendance": attendance.render,
    "Examinations": examinations.render, "Results": results.render,
    "My Portfolio": portfolio.render, "Documents": documents.render,
    "Reports": reports.render, "Settings": settings_page.render
}
routes[page](user)
