from pathlib import Path
import shutil
from config.settings import DB_PATH
def backup(destination):
    destination=Path(destination); destination.parent.mkdir(parents=True,exist_ok=True)
    if not DB_PATH.exists(): raise FileNotFoundError("Database not initialized.")
    shutil.copy2(DB_PATH,destination); return destination
