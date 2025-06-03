import streamlit as st
import time
import os

def check_authentication():
    """Verifica se o usuário está autenticado"""
    if not st.session_state.get('authentication_status'):
        st.switch_page("pages/0_🔒_Login.py")

def login_page():
    st.set_page_config(page_title="Login", layout="centered")
    
    admin_user = os.getenv('ADMIN_USER', st.secrets.get('admin.user', 'admin'))
    admin_pass = os.getenv('ADMIN_PASSWORD', st.secrets.get('admin.password', 'admin123'))
    
    with st.container():
        st.title("Sistema de Academia")
        st.subheader("Acesso Administrativo")
        
        username = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")
        
        if st.button("Login"):
            if username == admin_user and password == admin_pass:
                st.session_state.authentication_status = True
                st.session_state.username = username
                st.success("Login válido! Redirecionando...")
                time.sleep(3) 
                st.switch_page("pages/1_🏠_Dashboard.py")
                st.rerun()
            else:
                st.error("Credenciais inválidas")

def logout():
    st.session_state.authenticated = False
    st.toast("Desconectando...")
    time.sleep(2)
    st.switch_page("pages/0_🔒_Login.py")
    st.rerun()