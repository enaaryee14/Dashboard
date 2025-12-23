import streamlit as st

st.set_page_config(page_title="Login", page_icon="🔐")

st.title("Performance Mannagement system")

st.write("Your productivity measurement solution")

import streamlit as st

st.set_page_config(page_title="Welcome | NIC Dashboard")

st.title("Welcome to the NIC Task Management Dashboard")
st.write("This dashboard helps the Commissioner monitor and manage departmental tasks efficiently.")

if st.button("Proceed to Login"):
    st.switch_page("pages/1_welcome.py")
