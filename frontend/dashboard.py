import streamlit as st
from utils.dashboard_utils import contagens, ganhos, instrutores, clientes_planos, planos
from utils.payments_utils import plot_evolucao_renda

st.title("Dashboard")

st.divider()

cont, hm = contagens()

col1, col2 = st.columns([2,2])
with col1:
    st.markdown(f"### Contagem de Clientes")
    st.markdown(f"#### {cont} clientes")
    st.markdown(f'Homens: {hm['Contagem'][0]}  -  Mulheres: {hm['Contagem'][1]}')
with col2:
    st.markdown(f"### Renda Bruta")
    st.markdown(f" #### R${ganhos():,.2f}")
st.divider()
col3, col4 = st.columns([2,2])
with col3:
    st.markdown("### Instrutores e Especialidade")
    instrutores()
with col4:
    st.markdown("### Listagem de planos")
    planos()

st.divider()

col5, col6 = st.columns([4,4])
with col5:
    st.markdown("### Gráfico Pizza de Clientes/Plano")
    clientes_planos()
with col6:
    st.markdown("### Gráfico Data x Pagamentos")
    plot_evolucao_renda()