import streamlit as st
from utils.auth import check_authentication, logout

check_authentication()

st.set_page_config(page_title="Dashboard", page_icon="🏠", layout="wide")
st.title("Dashboard da Academia")

if st.session_state.get('authentication_status'):
    if st.sidebar.button("🚪 Sair", use_container_width=True):
        logout() 
