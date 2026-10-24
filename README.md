# School Information System

A modular Streamlit school ERP starter with student/teacher records, attendance,
exams/results, promotion history, student portfolio, uploads, reports and backup.
This is an original implementation, not a source-code copy of eduerp3.web.app.

## Setup (macOS/Linux)
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run app.py
```
Windows activation: `.venv\\Scripts\\activate`

Demo login: `admin` / `ChangeMe123!`
Change the demo password before using real student data. Test locally with sample data first.
SQLite database and uploaded files are stored in `storage/`.
