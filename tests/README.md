# Testes do FACIN_IA

Pasta contendo testes unitários e de integração do projeto.

## Estrutura

```
tests/
├── __init__.py
├── conftest.py                 # Fixtures do pytest
├── test_app.py                # Testes da aplicação principal
├── test_database.py           # Testes de banco de dados
├── test_agents.py             # Testes de agentes IA
└── test_config.py             # Testes de configuração
```

## Executar Testes

### Todos os testes
```bash
pytest -v
```

### Apenas testes unitários
```bash
pytest -v -m unit
```

### Apenas testes de integração
```bash
pytest -v -m integration
```

### Com cobertura
```bash
pytest --cov=. --cov-report=html
```

### Testes específicos
```bash
pytest tests/test_app.py::test_function_name -v
```

## Marcadores Disponíveis

- `@pytest.mark.unit` - Testes rápidos unitários
- `@pytest.mark.integration` - Testes de integração
- `@pytest.mark.slow` - Testes mais lentos
- `@pytest.mark.db` - Testes que acessam BD
- `@pytest.mark.agent` - Testes de agentes IA
- `@pytest.mark.asyncio` - Testes assincronos

## Exemplo de Teste

```python
import pytest
from app import execute_database_query

@pytest.mark.unit
def test_database_query():
    """Testa execução de query no banco."""
    result = execute_database_query("SELECT COUNT(*) FROM servidores")
    assert isinstance(result, str)
    assert len(result) > 0

@pytest.mark.db
@pytest.mark.integration
def test_database_connection(db_connection):
    """Testa conexão com banco de dados."""
    assert db_connection is not None
    cursor = db_connection.cursor()
    cursor.execute("SELECT 1")
    assert cursor.fetchone() == (1,)
```

## Coverage

Cobertura mínima obrigatória: **70%**

Gerar relatório HTML:
```bash
pytest --cov=. --cov-report=html
open htmlcov/index.html
```

---

**Versão**: 1.0.0  
**Data**: 27/02/2026
