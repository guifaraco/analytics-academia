import os
import psycopg2
import streamlit as st
from psycopg2 import sql
import pandas as pd

def get_connection():
    """Estabelece conexão com o PostgreSQL"""
    try:
        # Configuração para produção (Streamlit Cloud)
        if os.environ.get('POSTGRES_HOST'):
            conn = psycopg2.connect(
                host=os.environ['POSTGRES_HOST'],
                port=os.environ.get('POSTGRES_PORT', '5432'),
                dbname=os.environ['POSTGRES_DB'],
                user=os.environ['POSTGRES_USER'],
                password=os.environ['POSTGRES_PASSWORD']
            )
        # Configuração para desenvolvimento local
        else:
            conn = psycopg2.connect(
                host=st.secrets.postgres.host,
                port=st.secrets.postgres.port,
                dbname=st.secrets.postgres.dbname,
                user=st.secrets.postgres.user,
                password=st.secrets.postgres.password
            )
        return conn
    except Exception as e:
        st.error(f"Erro ao conectar ao banco de dados: {str(e)}")
        return None

def execute_query(query, params=None, return_df=False):
    """Executa uma query no PostgreSQL"""
    conn = get_connection()
    if not conn:
        return None
        
    try:
        with conn.cursor() as cur:
            cur.execute(query, params)
            
            if query.strip().lower().startswith(('select', 'with')):
                if return_df:
                    # Para queries SELECT retornar DataFrame
                    columns = [desc[0] for desc in cur.description]
                    data = cur.fetchall()
                    return pd.DataFrame(data, columns=columns)
                else:
                    return cur.fetchall()
            else:
                conn.commit()
                return cur.rowcount
    except Exception as e:
        st.error(f"Erro na execução da query: {str(e)}")
        conn.rollback()
        return None
    finally:
        conn.close()

def feed_tables():
    sales_reps_df = pd.read_csv('data/clientes_academia.csv')