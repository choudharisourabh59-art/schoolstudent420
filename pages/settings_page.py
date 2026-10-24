import streamlit as st
from services.backup_service import backup
def render(user):
    st.title("Settings")
    if user["role"]!="admin": st.warning("Admin access only."); return
    dest=st.text_input("Backup path","storage/school-backup.db")
    if st.button("Create backup"):
        try: st.success(f"Backup created: {backup(dest)}")
        except Exception as e: st.error(str(e))
