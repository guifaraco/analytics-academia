import streamlit as st
from utils.auth import check_authentication, logout
from utils.payments_utils import show_payment_statistics

check_authentication()
st.set_page_config(page_title="Pagamentos", layout="wide")
st.title("Pagamentos da Academia")
show_payment_statistics()
if st.sidebar.button("🚪 Sair", use_container_width=True):
    logout() 