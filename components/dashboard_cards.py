import streamlit as st
def metrics(items):
    cols=st.columns(len(items))
    for col,(label,value) in zip(cols,items): col.metric(label,value)
