import streamlit as st
from utils.auth import check_authentication, logout
from utils.database import create_tables, feed_tables

def main():
    st.set_page_config(page_title="Sistema Academia", layout="wide")
    create_tables()
    # feed_tables()

    if 'authentication_status' not in st.session_state:
        st.session_state.authentication_status = False
        check_authentication() 
    else:
        check_authentication() 

if __name__ == "__main__":
    main()