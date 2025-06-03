import pandas as pd
import streamlit as st
from utils.database import get_connection

#Tabela treinos -> cliente_id,instrutor_id,data_inicio,data_fim,plano_id
#Tabela exercicios -> nome,grupo_muscular
#Tabela treino_exercicios -> treino_id,exercicio_id,series,repeticoes
connection = get_connection()
cur = connection.cursor()

def treinos_academia():
    grupos_musculares = pd.read_sql_query("""
    SELECT DISTINCT grupo_muscular FROM academia.exercicios
""", connection)
    escolha = st.multiselect("Selecione o grupo muscular para ver os exercícios relacionados",grupos_musculares['grupo_muscular'], placeholder="Escolha uma ou mais opções")

    if escolha:
        placeholders = ','.join(['%s'] * len(escolha))
        
        query = f"""
        SELECT DISTINCT 
            e.nome as "Nome", 
            e.grupo_muscular as "Grupo Muscular", 
            te.series as "Quantidade Séries", 
            te.repeticoes as "Repetições" 
        FROM academia.exercicios e
        JOIN academia.treino_exercicios te ON te.exercicio_id = e.id
        WHERE e.grupo_muscular IN ({placeholders})
        ORDER BY e.grupo_muscular, e.nome
        """

        exercicios = pd.read_sql_query(query, connection, params=escolha)
        styled_df = exercicios.style \
        .set_properties(**{"background-color": "#f8f9fa", "color": "black"}) \
        .set_table_styles([
            {"selector": "th", "props": [("background-color", "#343a40"), ("color", "white")]}
        ])
        return st.dataframe(styled_df, width= 700, hide_index=True)
    else:
        return 'Nenhum grupo muscular selecionado'
