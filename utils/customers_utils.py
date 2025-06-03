
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import os
import streamlit as st
from utils.database import execute_query

#Mostrar quantos clientes cada instrutor atende.
def show_customers_by_instructor():
    """Mostra a quantidade de clientes por instrutor"""
    query = """
    SELECT 
    tr.instrutor_id as "Instrutor",
    ins.nome as "Nome",
    COUNT(*) AS Clientes
    FROM academia.treinos tr
    JOIN academia.instrutores ins ON tr.instrutor_id = ins.id
    GROUP BY tr.instrutor_id, ins.nome
    ORDER BY Clientes DESC;
    """
    
    qtd_clientes = execute_query(query, return_df=True)
    st.dataframe(qtd_clientes)
    
def customers_page():
    st.subheader("Filtros")
    c1, c2, c3 = st.columns([1,9,1], vertical_alignment="bottom")
    filters = []

    # Botão de Reset simples
    c3.write("")
    if c3.button("Resetar filtros", ):
        st.session_state.sexo = None
        st.session_state.plano = None

    # SEXO
    sexo = c1.radio("Sexo", ("M", "F"), horizontal=True, index=None, key="sexo")

    # PLANOS
    planos = execute_query("SELECT nome FROM academia.planos")
    planos = [plano[0] for plano in planos]
    plano = c2.selectbox(
        "Plano", 
        planos, 
        key="plano",
        index=None
    )

    if sexo:
        filters.append(f"c.sexo = '{sexo}'")
    if plano:
        filters.append(f"p.nome = '{plano}'")

    query = '''SELECT c.nome, c.idade, c.sexo, c.email, c.telefone, p.nome AS plano
        FROM academia.clientes AS c
        JOIN academia.planos AS p ON c.plano_id = p.id '''

    if len(filters) > 0:
        query += ("WHERE "+" AND ".join(filters))

    df = execute_query(query,return_df=True)
    st.dataframe(df, width=9000)

