import streamlit as st
from utils.auth import logout
from utils.registrations_utils import cadastro_clientes, cadastro_pagamentos, cadastro_treinos, cadastro_exercio_treino

st.title("Cadastros")

tab1, tab2, tab3, tab4 = st.tabs(["Clientes", "Pagamentos", "Treinos", "Exercicios"])
with tab1:
    cadastro_clientes()
with tab2:
    cadastro_pagamentos()
with tab3:
    cadastro_treinos()
with tab4:
    cadastro_exercio_treino()