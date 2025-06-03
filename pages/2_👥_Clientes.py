import streamlit as st
from utils.auth import check_authentication, logout
from utils.customers_utils import customers_page

check_authentication()

st.title("Clientes da Academia")
customers_page()

if st.sidebar.button("🚪 Sair", use_container_width=True):
    logout() 