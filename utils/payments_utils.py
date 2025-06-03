import pandas as pd
import streamlit as st
from utils.database import get_connection, execute_query

def get_df():
    query = "SELECT * FROM academia.pagamento_clientes;"
    df = execute_query(query, return_df=True)
    return df

def get_payment_count(df):
    payment_count = len(df)
    return payment_count

def get_payment_total_value(df):
    payment_total_value = df["valor_pago"].sum()
    return payment_total_value

def get_df_last_payment_per_client(df):
    df_last_payment_per_client = df.assign(yr=df['data_pagamento'].astype('datetime64[ns]').dt.year).groupby(['cliente_id','yr']).max().reset_index().drop(columns=['yr', 'id'])
    return df_last_payment_per_client

def show_payment_statistics():
    df = get_df()
    payment_count = get_payment_count(df) 
    payment_total_value = get_payment_total_value(df)
    df_last_payment_per_client = get_df_last_payment_per_client(df)

    col1, col2 = st.columns(2)
    col1.write("## Tabela de Pagamentos")
    col1.dataframe(df, hide_index=True, use_container_width=True)
    col2.write("## Pagamento mais recente por cliente")
    col2.dataframe(df_last_payment_per_client, hide_index=True, use_container_width=True)
    st.divider()
    st.write(f"## Total de pagamentos: {payment_count}")
    st.write(f"## Valor total de pagamentos: R${payment_total_value}")