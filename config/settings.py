import os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DB_PATH=Path(os.getenv("ERP_DB_PATH",ROOT/"storage"/"school.db"))
UPLOAD_DIR=ROOT/"storage"/"uploads"
UPLOAD_DIR.mkdir(parents=True,exist_ok=True)
APP_TITLE="School Information System"
MAX_UPLOAD_MB=8
ALLOWED_EXTENSIONS={"pdf","png","jpg","jpeg","docx","xlsx"}
