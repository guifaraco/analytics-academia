from utils.auth import login_page, logout
import streamlit as st

login_page()

if not st.session_state.get('authentication_status'):
    st.sidebar.empty()