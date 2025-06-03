import streamlit as st
from utils.auth import check_authentication, logout
from utils.registrations_utils import cadastro_clientes, cadastro_pagamentos, cadastro_treinos, cadastro_exercio_treino

check_authentication()

st.title("Cadastros")

# cadastro_clientes()
# cadastro_pagamentos()
# cadastro_treinos()
cadastro_exercio_treino()

if st.sidebar.button("🚪 Sair", use_container_width=True):
    logout() 