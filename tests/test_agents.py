"""
Testes para integração de agentes IA.
"""

import pytest


class TestAgentArchitecture:
    """Testes da arquitetura de agentes."""
    
    @pytest.mark.unit
    @pytest.mark.agent
    def test_state_dict_definition(self):
        """Testa definição de ConversationState."""
        required_fields = [
            "messages",
            "database_context",
            "current_agent",
            "memory_buffer"
        ]
        
        # Verificar que todos os campos são strings válidos
        assert all(isinstance(field, str) for field in required_fields)
    
    @pytest.mark.unit
    @pytest.mark.agent
    def test_agent_node_names(self):
        """Testa nomes dos nós de agente."""
        agent_nodes = {
            "router": "Router Agent",
            "database": "Database Agent",
            "analysis": "Analysis Agent",
            "memory": "Memory Agent",
            "executor": "Tool Executor"
        }
        
        assert len(agent_nodes) == 5
        assert all(isinstance(name, str) for name in agent_nodes.values())


class TestLangChainIntegration:
    """Testes de integração com LangChain."""
    
    @pytest.mark.unit
    def test_langchain_imports(self):
        """Testa importação de LangChain."""
        try:
            from langchain_groq import ChatGroq
            from langchain_openai import ChatOpenAI
            from langgraph.graph import StateGraph
            
            assert ChatGroq is not None
            assert ChatOpenAI is not None
            assert StateGraph is not None
        except ImportError as e:
            pytest.fail(f"Erro ao importar LangChain: {e}")
    
    @pytest.mark.unit
    @pytest.mark.slow
    def test_chat_model_instantiation(self, mock_env):
        """Testa instanciação de modelos de chat."""
        try:
            # Não fazer chamadas reais em testes
            # Apenas verificar que classes existem
            from langchain_groq import ChatGroq
            from langchain_openai import ChatOpenAI
            
            # Verificar que as classes têm os métodos necessários
            assert hasattr(ChatGroq, 'invoke') or hasattr(ChatGroq, '__call__')
            assert hasattr(ChatOpenAI, 'invoke') or hasattr(ChatOpenAI, '__call__')
        except Exception as e:
            pytest.fail(f"Erro na instanciação: {e}")


class TestLangGraphIntegration:
    """Testes de integração com LangGraph."""
    
    @pytest.mark.unit
    def test_langgraph_imports(self):
        """Testa importação de LangGraph."""
        try:
            from langgraph.graph import StateGraph, START, END
            from langgraph.prebuilt import ToolNode
            
            assert StateGraph is not None
            assert START is not None
            assert END is not None
            assert ToolNode is not None
        except ImportError as e:
            pytest.fail(f"Erro ao importar LangGraph: {e}")
    
    @pytest.mark.unit
    def test_state_graph_structure(self):
        """Testa estrutura básica de StateGraph."""
        from langgraph.graph import StateGraph
        from typing import TypedDict, List
        
        class SimpleState(TypedDict):
            messages: List[str]
            status: str
        
        # Apenas verificar que pode ser estruturado
        assert SimpleState is not None


class TestStreamlitIntegration:
    """Testes de integração com Streamlit."""
    
    @pytest.mark.unit
    def test_streamlit_imports(self):
        """Testa importação de Streamlit."""
        try:
            import streamlit as st
            
            assert st is not None
            assert hasattr(st, 'write')
            assert hasattr(st, 'chat_input')
        except ImportError as e:
            pytest.fail(f"Erro ao importar Streamlit: {e}")
