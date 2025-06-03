import streamlit as st
from utils.payments_utils import show_payment_statistics

st.title("Pagamentos da Academia")
show_payment_statistics()
