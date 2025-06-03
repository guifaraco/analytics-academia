import streamlit as st
from database import execute_query

'''
Formulário para cadastro de clientes, pagamentos, treinos e exercícios nos
treinos.
'''
def cadastro_clientes():
    # nome, idade, sexo, email, telefone, plano_id

    with st.form('cadas_cliente', clear_on_submit=True):
        nome = st.text_input('Insira o nome do cliente:')
        idade = st.text_input('Insira a idade do cliente:')
        sexo = st.radio(
            "Selecione o seu gênero:",
            ["M", "F"],
            captions=[
                "Masculino",
                "Feminino"
            ]
        )
        email = st.text_input("Insira o e-mail do cliente: ")
        telefone = st.text_input("Insira o telefone do cliente: ")
        
        query = "SELECT nome FROM planos"
        planos = execute_query(query=query, params=None)
        st.write(planos)

