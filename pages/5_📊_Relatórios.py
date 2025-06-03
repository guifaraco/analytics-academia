import streamlit as st
from utils.auth import check_authentication, logout

check_authentication()
st.set_page_config(page_title="Relatórios", layout="wide")
st.title("Relatórios da Academia")
if st.sidebar.button("🚪 Sair", use_container_width=True):
    logout() 