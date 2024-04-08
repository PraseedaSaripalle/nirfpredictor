import streamlit as st

def display_motivtion():
    st.header("**Problem Statement:** AI Assistant for Bench Marking and Comparative Analysis for NIRF Ranking ")
    st.write("")
    # Status elements
    st.header("Status Elements")
    st.progress(50)
    with st.spinner("Waiting..."):
        st.write("Loading...")
        
    st.balloons()
    st.error("This is an error message")
    st.warning("This is a warning message")
    st.info("This is an info message")
    st.success("This is a success message")
    try:
        raise Exception("This is an exception")
    except Exception as e:
        st.exception(e)    