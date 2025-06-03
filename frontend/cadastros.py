import streamlit as st
from utils.auth import logout
from utils.registrations_utils import cadastro_clientes, cadastro_pagamentos, cadastro_treinos, cadastro_exercio_treino

st.title("Cadastros")

clientes, pagamentos, treinos, exercicio = st.columns(4)
if clientes.button("Cadastrar novo cliente", use_container_width=True):
    cadastro_clientes()
if pagamentos.button("Cadastrar novo pagamento", use_container_width=True):    
    cadastro_pagamentos()
if treinos.button("Cadastrar novo treino", use_container_width=True):
    cadastro_treinos()
if exercicio.button("Cadastrar novo exercicio ao treino", use_container_width=True):
    cadastro_exercio_treino()