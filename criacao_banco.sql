
CREATE TABLE tb_servidores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    cpf TEXT,
    matricula TEXT UNIQUE,
    orgao TEXT,
    cargo TEXT
);

CREATE TABLE tb_folha_pagamento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    matricula TEXT,
    competencia TEXT,
    vencimentos REAL,
    descontos REAL,
    liquido REAL,
    FOREIGN KEY(matricula) REFERENCES tb_servidores(matricula)
);
