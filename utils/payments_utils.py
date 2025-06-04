import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.database import execute_query

def get_df():
    query = """
SELECT academia.clientes.nome as "Nome do Cliente", academia.planos.nome as "plano", academia.pagamento_clientes.valor_pago as "Valor", academia.pagamento_clientes.data_pagamento as "Data de Pagamento" FROM academia.pagamento_clientes
JOIN academia.clientes ON academia.pagamento_clientes.cliente_id = clientes.id
JOIN academia.planos ON academia.pagamento_clientes.plano_id = planos.id;
"""
    df = execute_query(query, return_df=True)
    return df

def get_payment_count(df):
    payment_count = len(df)
    return payment_count

def get_payment_total_value(df):
    payment_total_value = df["Valor"].sum()
    return payment_total_value

def get_df_last_payment_per_client(df):
    df_last_payment_per_client = df.assign(yr=df['Data de Pagamento'].astype('datetime64[ns]').dt.year).groupby(['Nome do Cliente','yr']).max().reset_index().drop(columns=['yr'])
    return df_last_payment_per_client

def show_payment_statistics():
    df = get_df()
    payment_count = get_payment_count(df) 
    payment_total_value = get_payment_total_value(df)
    df_last_payment_per_client = get_df_last_payment_per_client(df)
    st.divider()
    col1, col2 = st.columns(2)
    col1.write("## Tabela de Pagamentos")
    col1.dataframe(df, hide_index=True, use_container_width=True)
    col2.write("## Pagamento mais recente por cliente")
    col2.dataframe(df_last_payment_per_client, hide_index=True, use_container_width=True)
    st.divider()
    col3, col4 = st.columns(2)
    col3.write(f"## Total de pagamentos: :green[{payment_count}]")
    col4.write(f"## Valor total de pagamentos: :green[R$ {payment_total_value}]")

def plot_evolucao_renda():
    df = get_df()

    if df.empty:
        st.warning("Nenhum dado encontrado para exibir o gráfico.")
        return

    # Converter coluna de data
    df["Data de Pagamento"] = pd.to_datetime(df["Data de Pagamento"])

    # Agrupar por data e somar os valores
    df_agrupado = df.groupby("Data de Pagamento")["Valor"].sum().reset_index()
    df_agrupado = df_agrupado.sort_values("Data de Pagamento")

    # Criar o gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df_agrupado["Data de Pagamento"], df_agrupado["Valor"], marker='o')
    ax.set_title("Evolução da Renda por Data de Pagamento")
    ax.set_xlabel("Data de Pagamento")
    ax.set_ylabel("Valor Recebido (R$)")
    ax.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Exibir no Streamlit
    st.pyplot(fig)