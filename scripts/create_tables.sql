SET search_path TO academia;

CREATE TABLE IF NOT EXISTS exercicios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE,
    grupo_muscular VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS planos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE,
    preco DECIMAL(10, 2) NOT NULL,
    duracao_meses INTEGER NOT NULL CHECK (duracao_meses > 0)
);

CREATE TABLE IF NOT EXISTS instrutores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE,
    especialidade VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS treinos_exercicios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE,
    descricao TEXT,
    repeticoes INTEGER NOT NULL CHECK (repeticoes > 0),
    series INTEGER NOT NULL CHECK (series > 0),
    exercicio_id INTEGER NOT NULL,
    FOREIGN KEY (exercicio_id) REFERENCES exercicios(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS treinos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE,
    descricao TEXT,
    data DATE NOT NULL,
    duracao INTEGER NOT NULL CHECK (duracao > 0),
    instrutor_id INTEGER NOT NULL,
    FOREIGN KEY (instrutor_id) REFERENCES instrutores(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS clientes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefone VARCHAR(15),
    sexo CHAR(1) CHECK (sexo IN ('M', 'F')),
    plano_id INTEGER NOT NULL,
    FOREIGN KEY (plano_id) REFERENCES planos(id) ON DELETE CASCADE,
    treino_id INTEGER REFERENCES treinos(id) ON DELETE CASCADE
);