import streamlit as st
def student_form():
    with st.form("student_form"):
        admission=st.text_input("Admission number"); name=st.text_input("Student name")
        class_name=st.selectbox("Class",[str(i) for i in range(1,13)])
        section=st.selectbox("Section",["A","B","C","D"]); roll=st.text_input("Roll number")
        guardian=st.text_input("Guardian"); phone=st.text_input("Phone"); email=st.text_input("Email")
        submit=st.form_submit_button("Save student")
    return submit,{"admission":admission,"name":name,"class_name":class_name,"section":section,
                    "roll":roll,"guardian":guardian,"phone":phone,"email":email}
