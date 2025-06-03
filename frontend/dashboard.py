import streamlit as st
from utils.auth import logout
from utils.dashboard_utils import contagens, ganhos, instrutores, clientes_planos

st.title("Dashboard")
cont, hm = contagens()

col1, col2, col3 = st.columns([2,1,2])
with col1:
    st.markdown(f"### Contagem de Clientes")
    st.markdown(f"#### {cont} clientes")
    st.markdown(f'Homens: {hm['Contagem'][0]}  -  Mulheres: {hm['Contagem'][1]}')
with col2:
    pass
with col3:
    st.markdown(f"### Renda Bruta")
    st.markdown(f" #### R${ganhos():,.2f}")

st.markdown("### Instrutores e Especialidade")
instrutores()

clientes_planos()
