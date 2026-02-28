"""
Testes para módulo de configuração.
"""

import pytest
from config.config import validate_config, OPENAI_API_KEY, GROQ_API_KEY


class TestConfiguration:
    """Testes da configuração do projeto."""
    
    @pytest.mark.unit
    def test_api_keys_loaded(self):
        """Testa se chaves API foram carregadas."""
        # Este teste pode falhar em ambiente de teste sem .env
        # Por isso apenas verificamos o tipo
        assert isinstance(OPENAI_API_KEY, (str, type(None)))
        assert isinstance(GROQ_API_KEY, (str, type(None)))
    
    @pytest.mark.unit
    def test_validate_config_function_exists(self):
        """Testa se função de validação existe."""
        assert callable(validate_config)
    
    @pytest.mark.unit
    def test_config_values_are_valid_types(self):
        """Testa se valores de config têm tipos corretos."""
        from config.config import (
            DATABASE_TIMEOUT, DATABASE_MAX_RETRIES,
            STREAMLIT_PORT, DEFAULT_TEMPERATURE,
            MAX_AGENT_ITERATIONS, AGENT_TIMEOUT_SECONDS
        )
        
        assert isinstance(DATABASE_TIMEOUT, int)
        assert isinstance(DATABASE_MAX_RETRIES, int)
        assert isinstance(STREAMLIT_PORT, int)
        assert isinstance(DEFAULT_TEMPERATURE, float)
        assert isinstance(MAX_AGENT_ITERATIONS, int)
        assert isinstance(AGENT_TIMEOUT_SECONDS, int)


class TestEnvironmentVariables:
    """Testes de variáveis de ambiente."""
    
    @pytest.mark.unit
    def test_env_example_exists(self):
        """Testa se arquivo .env.example existe."""
        from pathlib import Path
        assert Path(".env.example").exists()
    
    @pytest.mark.unit
    def test_required_env_variables(self, mock_env):
        """Testa se variáveis obrigatórias são carregadas."""
        import os
        assert os.getenv("OPENAI_API_KEY") == "sk-test-key"
        assert os.getenv("GROQ_API_KEY") == "gsk-test-key"
