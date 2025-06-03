import streamlit as st
from utils.auth import check_authentication, logout
from utils.dashboard_utils import contagens, ganhos, instrutores, clientes_planos

check_authentication()


st.set_page_config(page_title="Dashboard", page_icon="🏠", layout="wide")


if st.session_state.get('authentication_status'):
    if st.sidebar.button("🚪 Sair", use_container_width=True):
        logout() 
        
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

# Parte inferior (tabela ocupando largura total)
st.markdown("### Instrutores e Especialidade")
instrutores()

clientes_planos()
