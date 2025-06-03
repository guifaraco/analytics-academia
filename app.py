import streamlit as st
from utils.auth import logout
from utils.database import create_tables, feed_tables

def main():
    st.set_page_config(layout="wide")
    create_tables()
    feed_tables()

    login_page = st.Page("frontend/login.py", title="Login", icon="🔒")
    dashboard_page = st.Page("frontend/dashboard.py", title="Dashboard", icon="🏠", default=True)
    clientes_page = st.Page("frontend/clientes.py", title="Clientes", icon="👥", url_path="/clientes") 
    treinos_page = st.Page("frontend/treinos.py", title="Treinos", icon="💪", url_path="/treinos") 
    pagamentos_page = st.Page("frontend/pagamentos.py", title="Pagamentos", icon="💰", url_path="/pagamentos") 
    cadastros_page = st.Page("frontend/cadastros.py", title="Cadastros", icon="⚙️", url_path="/cadastros")

    if 'authentication_status' not in st.session_state:
        st.session_state.authentication_status = False
        pg = st.navigation([login_page])
        pg.run()
    elif st.session_state.get('authentication_status'):
        pg = st.navigation([
            dashboard_page,
            clientes_page,
            treinos_page,
            pagamentos_page,
            cadastros_page
        ])
        if st.sidebar.button("🚪 Sair", use_container_width=True):
            logout() 
        pg.run()
    else:
        pg = st.navigation([login_page])
        pg.run()

if __name__ == "__main__":
    main()