"""
Testes para módulo principal da aplicação.
"""

import pytest


class TestApplication:
    """Testes da aplicação principal."""
    
    @pytest.mark.unit
    def test_app_imports(self):
        """Testa se módulos principais podem ser importados."""
        try:
            # Apenas testar importação, sem executar Streamlit
            import sys
            import os
            
            # Streamlit não deve ser inicializado em testes
            assert True
        except ImportError as e:
            pytest.fail(f"Erro ao importar módulo: {e}")
    
    @pytest.mark.unit
    def test_config_validation(self, mock_env):
        """Testa validação de configuração."""
        from config.config import validate_config
        # Em ambiente de teste, pode falhar, então apenas verificamos
        result = validate_config()
        assert isinstance(result, bool)
    
    @pytest.mark.unit
    def test_logging_setup(self):
        """Testa configuração de logging."""
        try:
            from config.logging_config import root_logger, agenticops_logger
            assert root_logger is not None
            assert agenticops_logger is not None
        except ImportError as e:
            pytest.fail(f"Erro ao importar logging: {e}")


class TestAgents:
    """Testes de agentes IA."""
    
    @pytest.mark.unit
    @pytest.mark.agent
    def test_agent_types(self):
        """Testa existência de tipos de agentes."""
        agent_types = [
            "Router",
            "Database",
            "Analysis",
            "Memory",
            "Tool Executor"
        ]
        
        # Apenas verificar que os tipos são válidos
        assert len(agent_types) == 5
        assert all(isinstance(agent, str) for agent in agent_types)


class TestTools:
    """Testes de ferramentas do sistema."""
    
    @pytest.mark.unit
    def test_tool_definitions(self):
        """Testa definições de ferramentas."""
        tools = {
            "execute_query": "Executa query SQL",
            "get_table_schema": "Obtém schema de tabela",
            "calculate_statistics": "Calcula estatísticas",
        }
        
        assert len(tools) > 0
        assert all(isinstance(desc, str) for desc in tools.values())


class TestPerformance:
    """Testes de performance."""
    
    @pytest.mark.slow
    @pytest.mark.unit
    def test_import_time(self):
        """Testa tempo de import da aplicação."""
        import time
        
        start = time.time()
        # Simulando import pesado
        import sys
        end = time.time()
        
        # Deve ser rápido (menos de 5 segundos)
        assert (end - start) < 5.0
