import streamlit as st
from utils.auth import check_authentication, logout
from utils.database import execute_query
from utils.customers_utils import show_customers_by_instructor, customers_page

check_authentication()

st.set_page_config(page_title="Clientes", layout="wide")
st.title("Clientes da Academia")
customers_page()

st.header("Clientes por Instrutor")
clientes_por_instrutores = show_customers_by_instructor() 

if st.session_state.get('authentication_status'):
    if st.sidebar.button("🚪 Sair", use_container_width=True):
        logout() 