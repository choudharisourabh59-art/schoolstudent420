from pathlib import Path
from datetime import datetime
import secrets
from config.settings import UPLOAD_DIR,ALLOWED_EXTENSIONS,MAX_UPLOAD_MB
from database.connection import connect
def save_document(student_id,uploaded_file):
    name=Path(uploaded_file.name).name; ext=Path(name).suffix.lower().lstrip(".")
    if ext not in ALLOWED_EXTENSIONS: raise ValueError("File type not allowed.")
    data=uploaded_file.getvalue()
    if len(data)>MAX_UPLOAD_MB*1024*1024: raise ValueError(f"Maximum upload size is {MAX_UPLOAD_MB} MB.")
    stored=secrets.token_hex(16)+"."+ext
    (UPLOAD_DIR/stored).write_bytes(data)
    with connect() as con:
        con.execute("INSERT INTO documents(student_id,original_name,stored_name,uploaded_at) VALUES(?,?,?,?)",
                    (student_id,name,stored,datetime.now().isoformat(timespec="seconds")))
    return stored
