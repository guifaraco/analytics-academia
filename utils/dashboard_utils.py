import pandas as pd
import streamlit as st
from utils.database import execute_query, get_connection
import matplotlib.pyplot as plt
import plotly.express as px

#gráfico de pessoas por tipo de plano
connection = get_connection()
cur = connection.cursor()

def contagens():
    query = """
    SELECT COUNT(*) as "Contagem Clientes" FROM academia.clientes
"""
    cont = execute_query(query)
    query = """
    SELECT COUNT(nome) as "Contagem", sexo FROM academia.clientes c
    GROUP BY sexo
"""
    hm = pd.read_sql_query(query, connection)
    return [cont[0][0], hm]

def ganhos():
    query = """
    SELECT SUM(valor_pago) as "Receita Bruta" FROM academia.pagamento_clientes
"""
    soma = execute_query(query)
    return soma[0][0]

def instrutores():
    query = """
    SELECT i.nome, i.especialidade FROM academia.instrutores i
"""
    instrutores = pd.read_sql_query(query, connection)
    st.dataframe(instrutores, width=500, hide_index=True)
    return instrutores


#clientes_academia -> nome,idade,sexo,email,telefone,plano_id
#planos -> nome,preco_mensal,duracao_meses
def clientes_planos():
    query = """
    SELECT 
        COUNT(c.nome) AS "Quantidade de Clientes", 
        p.nome AS "Plano" 
    FROM 
        academia.clientes c
    JOIN 
        academia.planos p ON p.id = c.plano_id
    GROUP BY 
        p.nome
    """
    contagem = pd.read_sql_query(query, connection)
    
    fig = px.pie(contagem, 
             names='Plano',
             color_discrete_sequence=px.colors.sequential.RdBu,
             hole=0.3,
             title="Contagem de pessoas por plano")  # Donut style

    # Ajustes de layout do gráfico
    fig.update_traces(textposition='inside', 
                    textinfo='percent+label',
                    hovertemplate="<b>%{label}</b><br>Clientes: %{value}<br>%{percent}",
                    marker=dict(line=dict(color='#000000', width=1)))

    fig.update_layout(
        height=500,
        width=1000,
        showlegend=False,
        margin=dict(t=50, b=50, l=50, r=50),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )

   
    st.plotly_chart(fig)