import streamlit as st
from utils.auth import check_authentication, logout
from utils.database import execute_query
from utils.customers_utils import show_customers_by_instructor

check_authentication()

st.title("Clientes da Academia")
if st.sidebar.button("🚪 Sair", use_container_width=True):
    logout()

st.header("Clientes por Instrutor")
clientes_por_instrutores = show_customers_by_instructor() 