from utils.auth import login_page, logout
import streamlit as st

login_page()
if st.sidebar.button("🚪 Sair", use_container_width=True):
    logout() 