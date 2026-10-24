import streamlit as st,plotly.express as px
def bar(data,x,y,title):
    if not data.empty: st.plotly_chart(px.bar(data,x=x,y=y,title=title),use_container_width=True)
