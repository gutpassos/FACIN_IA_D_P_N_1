"""
Configuração centralizada do projeto FACIN_IA_D_P_N_1
"""

import os
from typing import Optional
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# ==========================================
# Configurações de API
# ==========================================

OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY: Optional[str] = os.getenv("GROQ_API_KEY")
AGENTICOPS_API_KEY: Optional[str] = os.getenv("AGENTICOPS_API_KEY")

# ==========================================
# Configurações de Banco de Dados
# ==========================================

DATABASE_PATH: str = os.getenv("DATABASE_PATH", "folha_pagamento.db")
DATABASE_TIMEOUT: int = 30
DATABASE_MAX_RETRIES: int = 3

# ==========================================
# Configurações de Aplicação
# ==========================================

DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
PYTHONPATH: str = os.getenv("PYTHONPATH", ".")

# ==========================================
# Configurações de Streamlit
# ==========================================

STREAMLIT_PORT: int = int(os.getenv("STREAMLIT_SERVER_PORT", "8501"))
STREAMLIT_HEADLESS: bool = os.getenv("STREAMLIT_SERVER_HEADLESS", "false").lower() == "true"

# ==========================================
# Configurações de LLM
# ==========================================

GROQ_MODEL: str = "mixtral-8x7b-32768"
OPENAI_MODEL: str = "gpt-4"
DEFAULT_TEMPERATURE: float = 0.7
DEFAULT_MAX_TOKENS: int = 2048

# ==========================================
# Configurações de Agentes
# ==========================================

MAX_AGENT_ITERATIONS: int = 10
AGENT_TIMEOUT_SECONDS: int = 60
ENABLE_MEMORY_AGENT: bool = True
ENABLE_ANALYSIS_AGENT: bool = True

# ==========================================
# Configurações de AgenticOps
# ==========================================

AGENTICOPS_ENABLED: bool = AGENTICOPS_API_KEY is not None
AGENTICOPS_PROJECT_NAME: str = "FACIN_IA_D_P_N_1"
AGENTICOPS_ENVIRONMENT: str = "development" if DEBUG else "production"
AGENTICOPS_LOG_DIR: str = "logs"

# ==========================================
# Configurações de Logging
# ==========================================

LOG_DIR: str = "logs"
ERROR_DIR: str = "errors"
ENABLE_FILE_LOGGING: bool = True
ENABLE_CONSOLE_LOGGING: bool = True
LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# ==========================================
# Validações
# ==========================================

def validate_config() -> bool:
    """Valida se todas as configurações obrigatórias estão presentes."""
    
    errors = []
    
    if not OPENAI_API_KEY:
        errors.append("OPENAI_API_KEY não configurada")
    
    if not GROQ_API_KEY:
        errors.append("GROQ_API_KEY não configurada")
    
    if errors:
        print("❌ Erros de configuração:")
        for error in errors:
            print(f"  - {error}")
        return False
    
    print("✅ Configurações validadas com sucesso")
    return True


if __name__ == "__main__":
    validate_config()
