import streamlit as st
from utils.auth import logout
from utils.customers_utils import show_customers_by_instructor, customers_page

st.title("Clientes da Academia")
st.divider()
customers_page()


st.header("Clientes por Instrutor")
clientes_por_instrutores = show_customers_by_instructor() 