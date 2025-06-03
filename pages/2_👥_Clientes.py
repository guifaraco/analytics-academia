import streamlit as st
from utils.auth import check_authentication, logout
from utils.database import execute_query

check_authentication()

st.title("Clientes da Academia")
st.subheader("Filtros")
c1, c2, c3 = st.columns([3,4,2], vertical_alignment=)
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
    key="plano"
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
st.dataframe(df)

if st.sidebar.button("🚪 Sair", use_container_width=True):
    logout() 