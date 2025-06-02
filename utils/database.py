import os
import psycopg2
import streamlit as st
from psycopg2 import sql
import pandas as pd
from sqlalchemy import create_engine

def get_connection():
    try:
        if os.environ.get('POSTGRES_HOST'):
            conn = psycopg2.connect(
                host=os.environ['POSTGRES_HOST'],
                port=os.environ.get('POSTGRES_PORT', '5432'),
                dbname=os.environ['POSTGRES_DB'],
                user=os.environ['POSTGRES_USER'],
                password=os.environ['POSTGRES_PASSWORD']
            )
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
    conn = get_connection()
    if not conn:
        return None
        
    try:
        with conn.cursor() as cur:
            cur.execute(query, params)
            
            if query.strip().lower().startswith(('select', 'with')):
                if return_df:
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

def create_tables():
    sql_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'scripts', 'create_tables.sql')
    with open(sql_path, 'r') as f:
        content = f.read()
        execute_query(content.strip())

def feed_tables():
    engine = create_engine(
        f'postgresql+psycopg2://{st.secrets.postgres.user}:{st.secrets.postgres.password}@{st.secrets.postgres.host}:{st.secrets.postgres.port}/{st.secrets.postgres.dbname}'
        )

    exercicios_count = execute_query("SELECT COUNT(*) FROM academia.exercicios")
    if exercicios_count[0][0] == 0:
        exercicios_df = pd.read_csv('data/exercicios.csv')
        exercicios_df.to_sql("exercicios", engine, if_exists='append', schema="academia", index=False)

    planos_count = execute_query("SELECT COUNT(*) FROM academia.planos")
    if planos_count[0][0] == 0:
        planos_df = pd.read_csv('data/planos.csv')
        planos_df.to_sql("planos", engine, if_exists='append', schema="academia", index=False)

    instrutores_count = execute_query("SELECT COUNT(*) FROM academia.instrutores")
    if instrutores_count[0][0] == 0:
        instrutores_df = pd.read_csv('data/instrutores.csv')
        instrutores_df.to_sql("instrutores", engine, if_exists='append', schema="academia", index=False)

    clientes_count = execute_query("SELECT COUNT(*) FROM academia.clientes")
    if clientes_count[0][0] == 0:
        clientes_df = pd.read_csv('data/clientes_academia.csv')
        clientes_df.to_sql("clientes", engine, if_exists='append', schema="academia", index=False)

    treinos_count = execute_query("SELECT COUNT(*) FROM academia.treinos")
    if treinos_count[0][0] == 0:
        treinos_df = pd.read_csv('data/treinos.csv')
        treinos_df.to_sql("treinos", engine, if_exists='append', schema="academia", index=False)
        
    treino_exercicios_count = execute_query("SELECT COUNT(*) FROM academia.treino_exercicios")
    if treino_exercicios_count[0][0] == 0:
        treino_exercicios_df = pd.read_csv('data/treino_exercicios.csv')
        treino_exercicios_df.to_sql("treino_exercicios", engine, if_exists='append', schema="academia", index=False)
        

    pagamento_clientes_count = execute_query("SELECT COUNT(*) FROM academia.pagamento_clientes")
    if pagamento_clientes_count[0][0] == 0:
        pagamento_clientes_df = pd.read_csv('data/pagamento_clientes.csv')
        pagamento_clientes_df.to_sql("pagamento_clientes", engine, if_exists='append', schema="academia", index=False)