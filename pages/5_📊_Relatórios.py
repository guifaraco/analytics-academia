import streamlit as st
from utils.auth import check_authentication, logout

check_authentication()

st.title("Relatórios da Academia")
if st.sidebar.button("🚪 Sair", use_container_width=True):
    logout() 