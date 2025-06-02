import streamlit as st
from utils.auth import check_authentication, logout
from utils.database import create_tables, feed_tables

check_authentication()

st.set_page_config(page_title="Dashboard", page_icon="🏠")
st.title("Dashboard da Academia")
if st.sidebar.button("🚪 Sair", use_container_width=True):
    logout() 