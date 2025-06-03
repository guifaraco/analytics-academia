import streamlit as st
from utils.dashboard_utils import contagens, ganhos, instrutores, clientes_planos, planos

st.title("Dashboard")
cont, hm = contagens()

col1, col2, col3, col4 = st.columns([2,1,2,2])
with col1:
    st.markdown(f"### Contagem de Clientes")
    st.markdown(f"#### {cont} clientes")
    st.markdown(f'Homens: {hm['Contagem'][0]}  -  Mulheres: {hm['Contagem'][1]}')
with col2:
    pass
with col3:
    st.markdown(f"### Renda Bruta")
    st.markdown(f" #### R${ganhos():,.2f}")
with col4:
    # Parte inferior (tabela ocupando largura total)
    st.markdown("### Instrutores e Especialidade")
    instrutores()

col5, col7 = st.columns([3,3])
with col5:
    st.markdown("### Gráfico Pizza de Clientes/Plano")
    clientes_planos()
with col7:
    st.markdown("### Listagem de planos")
    planos()
