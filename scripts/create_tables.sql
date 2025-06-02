SET search_path TO academia;

CREATE TABLE IF NOT EXISTS exercicios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE,
    grupo_muscular VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS planos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE,
    preco_mensal DECIMAL(10, 2) NOT NULL,
    duracao_meses INTEGER NOT NULL CHECK (duracao_meses > 0)
);

CREATE TABLE IF NOT EXISTS instrutores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE,
    especialidade VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE,
    idade INTEGER NOT NULL CHECK (idade > 0),
    sexo CHAR(1) CHECK (sexo IN ('M', 'F')),
    email VARCHAR(100) NOT NULL UNIQUE,
    telefone VARCHAR(20),
    plano_id INTEGER NOT NULL,
    FOREIGN KEY (plano_id) REFERENCES planos(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS treinos (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER NOT NULL,
    instrutor_id INTEGER NOT NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    plano_id INTEGER NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE CASCADE,
    FOREIGN KEY (instrutor_id) REFERENCES instrutores(id) ON DELETE CASCADE,
    FOREIGN KEY (plano_id) REFERENCES planos(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS treinos_exercicios (
    treino_id INTEGER NOT NULL,
    exercicio_id INTEGER NOT NULL,
    series INTEGER NOT NULL CHECK (series > 0),
    repeticoes INTEGER NOT NULL CHECK (repeticoes > 0),
    PRIMARY KEY (treino_id, exercicio_id),
    FOREIGN KEY (treino_id) REFERENCES treinos(id) ON DELETE CASCADE,
    FOREIGN KEY (exercicio_id) REFERENCES exercicios(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS pagamento_clientes (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER NOT NULL,
    plano_id INTEGER NOT NULL,
    valor_pago DECIMAL(10,2) NOT NULL CHECK(valor_pago > 0),
    data_pagamento DATE NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE CASCADE,
    FOREIGN KEY (plano_id) REFERENCES planos(id) ON DELETE CASCADE
);