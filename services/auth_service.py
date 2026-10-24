import hashlib,secrets,streamlit as st
from database.connection import connect
def hash_password(password,salt=None):
    salt=salt or secrets.token_bytes(16)
    return salt.hex()+":"+hashlib.pbkdf2_hmac("sha256",password.encode(),salt,260000).hex()
def verify_password(password,stored):
    try:
        salt,digest=stored.split(":")
        actual=hash_password(password,bytes.fromhex(salt)).split(":")[1]
        return secrets.compare_digest(actual,digest)
    except (ValueError,TypeError): return False
def login_form():
    st.title("🎓 School Information System")
    with st.form("login"):
        username=st.text_input("Username"); password=st.text_input("Password",type="password")
        submit=st.form_submit_button("Sign in")
    if submit:
        with connect() as con: row=con.execute("SELECT * FROM users WHERE username=?",(username.strip(),)).fetchone()
        if row and verify_password(password,row["password_hash"]):
            st.session_state.user={"id":row["id"],"username":row["username"],"role":row["role"],"linked_id":row["linked_id"]}
            st.rerun()
        st.error("Invalid username or password.")
    st.caption("Demo: admin / ChangeMe123! — change before real use.")
def logout():
    st.session_state.pop("user",None); st.rerun()
