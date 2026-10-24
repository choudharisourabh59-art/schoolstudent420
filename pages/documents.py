import streamlit as st,pandas as pd
from database.connection import connect
from services.upload_service import save_document
from config.settings import UPLOAD_DIR
def render(user):
    st.title("Documents")
    with connect() as con: roster=pd.read_sql_query("SELECT id,name FROM students",con)
    if roster.empty: st.info("Add a student first."); return
    sid=st.selectbox("Student",roster.id,format_func=lambda x:roster.loc[roster.id==x,"name"].iloc[0])
    f=st.file_uploader("Upload PDF/image/DOCX/XLSX (8 MB)")
    if f and st.button("Save upload"):
        try: save_document(sid,f); st.success("Saved.")
        except Exception as e: st.error(str(e))
    with connect() as con: docs=pd.read_sql_query("SELECT id,original_name,uploaded_at FROM documents WHERE student_id=?",(con),params=(sid,))
    st.dataframe(docs,use_container_width=True,hide_index=True)
    if not docs.empty:
        did=st.selectbox("Download document",docs.id,format_func=lambda x:docs.loc[docs.id==x,"original_name"].iloc[0])
        with connect() as con: item=con.execute("SELECT * FROM documents WHERE id=?",(int(did),)).fetchone()
        path=UPLOAD_DIR/item["stored_name"]
        if path.exists(): st.download_button("Download",path.read_bytes(),item["original_name"])
