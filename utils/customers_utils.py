import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import os
import streamlit as st
from utils.database import execute_query

#Mostrar quantos clientes cada instrutor atende.

def show_customers_by_instructor():
    """Mostra a quantidade de clientes por instrutor"""
    query = """
    SELECT 
    tr.instrutor_id as "Instrutor",
    ins.nome as "Nome",
    COUNT(*) AS Clientes
    FROM academia.treinos tr
    JOIN academia.instrutores ins ON tr.instrutor_id = ins.id
    GROUP BY tr.instrutor_id, ins.nome
    ORDER BY Clientes DESC;
    """
    
    qtd_clientes = execute_query(query, return_df=True)
    st.dataframe(qtd_clientes)
    
