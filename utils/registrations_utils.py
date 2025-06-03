import streamlit as st
from utils.database import execute_query

'''
Formulário para cadastro de clientes ok , pagamentos ok , treinos ok e exercícios nos
treinos.
'''

def sel_cliente_id(cliente):
    query = "SELECT id FROM academia.clientes WHERE nome = %s"
    cliente_id = execute_query(query, params=(cliente,))
    return cliente_id[0]

def sel_plano_id(plano):
    query = "SELECT id FROM academia.planos WHERE nome = %s"
    plano_id = execute_query(query, params=(str(plano),))
    return plano_id[0]
    
def sel_instrutor_id(instrutor):
    query = "SELECT id FROM academia.instrutores WHERE nome = %s"
    instrutor_id = execute_query(query, params=(instrutor,))
    return instrutor_id[0]

def sel_exercicio_id(exercicio):
    query = "SELECT id FROM academia.exercicios WHERE nome = %s"
    exercicio_id = execute_query(query, params=(exercicio,))
    return exercicio_id[0]

def sel_treino_id(treino):
    query = "SELECT id FROM academia.treinos WHERE data_inicio = %s"
    treino_id = execute_query(query, params=(treino,))
    return treino_id[0]

def select_box_planos():
    query = "SELECT nome FROM academia.planos"
    planos = execute_query(query=query, params=None, return_df=True)
    plano = st.selectbox("Selecione o plano do cliente: ", planos['nome'].values.flatten().tolist())
    return sel_plano_id(plano)

def select_box_cliente():
    query = "SELECT nome FROM academia.clientes"
    clientes_df = execute_query(query, return_df=True)
    cliente = st.selectbox("Selecione o cliente: ", clientes_df['nome'].values.flatten().tolist())
    return sel_cliente_id(cliente)

def select_box_instrutor():
    query = "SELECT nome FROM academia.instrutores"
    instrutores_df = execute_query(query, return_df=True)
    instrutor = st.selectbox("Selecione o instrutor: ", instrutores_df['nome'].values.flatten().tolist())
    return sel_instrutor_id(instrutor)

def select_box_exercicio():
    query = "SELECT nome FROM academia.exercicios"
    exercicio_df = execute_query(query, return_df=True)
    exercicio = st.selectbox("Selecione o exercício: ", exercicio_df['nome'].values.flatten().tolist())
    return sel_exercicio_id(exercicio)

def select_box_treino():
    query = "SELECT data_inicio FROM academia.treinos"
    treino_df = execute_query(query, return_df=True)
    treino = st.selectbox("Selecio em qual treino você deseja inserir o exercicio:", 
                          treino_df['data_inicio'].values.flatten().tolist())
    return sel_treino_id(treino)

def cadastro_clientes():

    with st.form('cadastro_cliente', clear_on_submit=True):
        nome = st.text_input('Insira o nome do cliente:')
        idade = st.text_input('Insira a idade do cliente:')
        sexo = st.radio(
            "Selecione o seu gênero:",
            ["M", "F"],
            captions=[
                "Masculino",
                "Feminino"
            ],
            horizontal=True
        )
        email = st.text_input("Insira o e-mail do cliente: ")
        telefone = st.text_input("Insira o telefone do cliente: ")
        plano_id = select_box_planos()
        submit = st.form_submit_button()

        if submit and nome and idade and sexo and email and telefone:
            query = "INSERT INTO academia.clientes (nome, idade, sexo, email, telefone, plano_id) VALUES (%s,%s,%s,%s,%s,%s)"
            execute_query(query, params=(nome,idade,sexo,email,telefone,plano_id[0]))

            st.success('Cliente cadastrado com sucesso!!!')
        else:
            st.warning('Erro inesperado.')

def cadastro_pagamentos():
    with st.form('cadastro_pagamento', clear_on_submit=True):
        cliente_id = select_box_cliente()
        plano_id = select_box_planos()
        valor_pago = st.text_input("Digite o valor pago:")
        data_pagamento = st.date_input("Data do pagamento: ")  
        submit = st.form_submit_button()

        if submit and cliente_id and valor_pago and plano_id and data_pagamento:
            query = "INSERT INTO academia.pagamento_clientes (cliente_id, plano_id, valor_pago, data_pagamento) VALUES (%s,%s,%s,%s)"
            execute_query(query, params=(cliente_id, plano_id, valor_pago, data_pagamento))
            st.success('Pagamento cadastrado com sucesso!!!')
        else:
            st.warning('Erro inesperado.')

def cadastro_treinos():
    # cliente_id, instrutor_id, data_inicio, data_fim, plano_id
    with st.form('cadastro_pagamento', clear_on_submit=True):
        cliente_id = select_box_cliente()
        instrutor_id = select_box_instrutor()
        data_inicio = st.date_input("Data do início do treino:")
        data_fim = st.date_input("Data do final do treino: ")
        plano_id = select_box_planos()
        submit = st.form_submit_button()

        if submit and cliente_id and instrutor_id and data_inicio and data_fim and plano_id:
            query = "INSERT INTO academia.treinos (cliente_id, instrutor_id, data_inicio, data_fim, plano_id) VALUES (%s,%s,%s,%s,%s)"
            execute_query(query, params=(cliente_id, instrutor_id, data_inicio, data_fim, plano_id))
            st.success('Treino cadastrado com sucesso!!!')
        else:
            st.warning('Erro inesperado.')

def cadastro_exercio_treino():
    # treino_id, exercicio_id, series, repeticoes
    with st.form('cadastro_ex_treino', clear_on_submit=True):
        treino_id = select_box_treino()
        exercicio_id = select_box_exercicio()
        series = st.text_input("Digite a quantidade de séries: ")
        repeticoes = st.text_input("Digite a quantidade de repetições: ")
        submit = st.form_submit_button()

        if submit and treino_id and exercicio_id and series and repeticoes:
            query = "INSERT INTO academia.treino_exercicios (treino_id, exercicio_id, series, repeticoes) VALUES (%s,%s,%s,%s)"
            execute_query(query, params=(treino_id, exercicio_id, series, repeticoes))
            st.success('Exercicio cadastrado com sucesso!!!')
        else:
            st.warning('Erro inesperado.')
