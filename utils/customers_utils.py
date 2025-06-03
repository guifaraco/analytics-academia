
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
    st.dataframe(qtd_clientes, use_container_width=True)
    
def customers_page():
    st.subheader("Filtros")
    c1, c2, c3, c4 = st.columns([1,4,4,1], vertical_alignment="bottom")
    filters = []

    min_idade_db = execute_query("SELECT MIN(idade) FROM academia.clientes")[0][0]
    max_idade_db = execute_query("SELECT MAX(idade) FROM academia.clientes")[0][0]

    # Botão de Reset simples
    if c4.button("Resetar filtros", ):
        st.session_state.sexo = None
        st.session_state.idade = (min_idade_db, max_idade_db)
        st.session_state.plano = None

    # SEXO
    sexo = c1.radio("Sexo", ("M", "F"), horizontal=True, index=None, key="sexo")

    # IDADE
    min_idade, max_idade = c2.slider(
        "Idade",
        min_idade_db,
        max_idade_db,
        (min_idade_db, max_idade_db),
        key="idade"
    )

    # PLANOS
    planos = execute_query("SELECT nome FROM academia.planos")
    planos = [plano[0] for plano in planos]
    plano = c3.selectbox(
        "Plano", 
        planos, 
        key="plano",
        index=None
    )
    if min_idade and max_idade:
        filters.append(f"c.idade >= '{min_idade}'")
        filters.append(f"c.idade <= '{max_idade}'")
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
    st.dataframe(df, use_container_width=True)
    st.divider()

