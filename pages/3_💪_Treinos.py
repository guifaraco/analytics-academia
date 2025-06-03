import streamlit as st
from utils.auth import check_authentication, logout
from utils.trainings_utils import treinos_academia

check_authentication()

st.title("Treinos da Academia")
if st.sidebar.button("🚪 Sair", use_container_width=True):
    logout() 

treinos_academia()