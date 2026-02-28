"""
Fixtures e configurações compartilhadas para testes.
"""

import pytest
import sqlite3
import tempfile
from pathlib import Path


@pytest.fixture
def temp_db():
    """Cria banco de dados temporário para testes."""
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as tmp:
        db_path = tmp.name
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Criar tabelas básicas
    cursor.execute("""
        CREATE TABLE servidores (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            cargo TEXT,
            departamento TEXT,
            salario REAL,
            ativo INTEGER DEFAULT 1
        )
    """)
    
    cursor.execute("""
        CREATE TABLE folha_pagamento (
            id INTEGER PRIMARY KEY,
            servidor_id INTEGER,
            mes INTEGER,
            ano INTEGER,
            valor_liquido REAL,
            FOREIGN KEY (servidor_id) REFERENCES servidores(id)
        )
    """)
    
    conn.commit()
    yield conn
    
    conn.close()
    Path(db_path).unlink(missing_ok=True)


@pytest.fixture
def sample_data(temp_db):
    """Insere dados de exemplo no banco."""
    cursor = temp_db.cursor()
    
    # Inserir servidores
    servidores = [
        ("João Silva", "Assistente", "TI", 3000.00, 1),
        ("Maria Santos", "Analista", "RH", 4500.00, 1),
        ("Pedro Costa", "Assistente", "Fazenda", 3000.00, 0),
    ]
    
    cursor.executemany("""
        INSERT INTO servidores (nome, cargo, departamento, salario, ativo)
        VALUES (?, ?, ?, ?, ?)
    """, servidores)
    
    temp_db.commit()
    return cursor


@pytest.fixture
def mock_env(monkeypatch):
    """Configura variáveis de ambiente para testes."""
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test-key")
    monkeypatch.setenv("GROQ_API_KEY", "gsk-test-key")
    monkeypatch.setenv("DEBUG", "true")
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")


@pytest.fixture
def app_config():
    """Fornece configuração de aplicação para testes."""
    from config.config import (
        GROQ_MODEL, OPENAI_MODEL, DEFAULT_TEMPERATURE, 
        DEFAULT_MAX_TOKENS, MAX_AGENT_ITERATIONS
    )
    return {
        "groq_model": GROQ_MODEL,
        "openai_model": OPENAI_MODEL,
        "temperature": DEFAULT_TEMPERATURE,
        "max_tokens": DEFAULT_MAX_TOKENS,
        "max_iterations": MAX_AGENT_ITERATIONS,
    }
