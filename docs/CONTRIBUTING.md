# Guia de Contribuição - FACIN_IA_D_P_N_1

## 🤝 Contribuindo para FACIN_IA_D_P_N_1

Obrigado por se interessar em contribuir! Este guia descreve nossos padrões e processos.

---

## 📋 Antes de Começar

- Faça um Fork do repositório
- Clone seu fork: `git clone https://github.com/seu-usuario/FACIN_IA_D_P_N_1.git`
- Crie uma branch: `git checkout -b feature/sua-feature`

---

## 🔧 Setup de Desenvolvimento

```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Instalar dependências
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Instalar pre-commit hooks
pre-commit install
```

---

## ✅ Padrões de Código

### Formatação

```bash
# Black
black . --line-length=100

# isort
isort . --profile black
```

### Verificação

```bash
# Flake8
flake8 .

# mypy
mypy . --ignore-missing-imports

# pylint
pylint **/*.py
```

### Testes

```bash
# Executar testes
pytest -v

# Com cobertura
pytest --cov=. --cov-report=html
```

---

## 📝 Commits

### Mensagens de Commit

```
tipo(escopo): descrição breve

Descrição mais detalhada se necessário.

Fixes #123
```

### Tipos
- `feat`: Nova feature
- `fix`: Correção de bug
- `docs`: Documentação
- `style`: Formatação
- `refactor`: Refatoração
- `test`: Testes
- `chore`: Manutenção

### Exemplo
```
feat(agents): adiciona novo memory agent

- Implementa armazenamento de memória persistente
- Adiciona embeddings semânticos
- Integra com LangGraph

Fixes #456
```

---

## 🧪 Testes

### Localização
Testes devem estar em `tests/` com padrão `test_*.py`

### Template

```python
import pytest
from app import function_to_test

class TestFunctionToTest:
    def test_success_case(self):
        result = function_to_test("input")
        assert result == "expected"
    
    def test_error_case(self):
        with pytest.raises(ValueError):
            function_to_test("invalid")
```

### Cobertura
Mínimo 70% obrigatório na CI/CD

---

## 📚 Documentação

### Docstrings

```python
def execute_query(query: str) -> str:
    """Executa query SQL no banco de dados.
    
    Args:
        query: Comando SQL válido
    
    Returns:
        Resultado da query em JSON
    
    Raises:
        DatabaseError: Se query falhar
    
    Example:
        >>> result = execute_query("SELECT * FROM servidores")
    """
```

### Atualizar Documentação

- `docs/README.md`: Overview do projeto
- `docs/API.md`: Referência de APIs
- `docs/ARCHITECTURE.md`: Arquitetura
- `errors/ERRORS_LOG.md`: Erros encontrados

---

## 🔄 Pull Request

### Checklist

- [ ] Tests passam localmente
- [ ] Código formatado (Black)
- [ ] Imports organizados (isort)
- [ ] Sem linting issues (Flake8)
- [ ] Type hints adicionados (mypy)
- [ ] Documentação atualizada
- [ ] ERRORS_LOG.md atualizado (se aplicável)

### Descrição PR

```markdown
## Descrição
Breve descrição das mudanças

## Tipo de Mudança
- [ ] Bug fix
- [ ] Nova feature
- [ ] Breaking change
- [ ] Documentação

## Como Testar
Passos para reproduzir/testar

## Screenshots (se aplicável)

## Checklist
- [x] Código formatado
- [x] Testes passam
- [x] Documentação atualizada
```

---

## 🐛 Reportando Bugs

### Título Descritivo
`"Database Agent falha com queries complexas"` ao invés de `"Erro"`

### Informações Necessárias
```
- Versão Python
- Versão do FACIN_IA_D_P_N_1
- Stack trace completo
- Passos para reproduzir
- Comportamento esperado vs atual
```

### Template

```markdown
**Descrição do Bug**
[Descrição clara do problema]

**Passos para Reproduzir**
1. [Passo 1]
2. [Passo 2]

**Comportamento Esperado**
[O que deveria acontecer]

**Comportamento Atual**
[O que realmente aconteceu]

**Environment**
- Python: 3.12
- OS: Windows/Linux/macOS
- FACIN_IA_D_P_N_1 Version: 1.0.0
```

---

## ✨ Sugestões de Feature

### Título Descritivo
`"Adicionar suporte a PostgreSQL"` ao invés de `"Melhorar banco de dados"`

### Informação Necessária
- Caso de uso
- Benefício esperado
- Possibilidade de implementação

---

## 📖 Convenções

### Python Style
Seguir [PEP 8](https://www.python.org/dev/peps/pep-0008/)

### Nomenclatura
- Funções/métodos: `snake_case`
- Classes: `PascalCase`
- Constantes: `UPPER_CASE`
- Variáveis privadas: `_private_var`

### Imports
```python
# Ordem: stdlib, third-party, local
import os
import sys
from typing import List

from langchain import ...
from streamlit import ...

from app import execute_query
```

---

## 🚀 Processo de Merge

1. Submeta PR com descrição clara
2. CI/CD valida automaticamente
3. Review code (mínimo 1 aprovação)
4. Merge automático quando aprovado
5. GitHub Actions faz deploy

---

## 📞 Suporte

- **Issues**: [GitHub Issues](https://github.com/gutpassos/FACIN_IA/issues)
- **Discussões**: [GitHub Discussions](https://github.com/gutpassos/FACIN_IA/discussions)
- **Email**: gut.passos@gmail.com

---

## 📄 Licença

Ao contribuir, você concorda que suas mudanças serão licenciadas sob a mesma licença MIT do projeto.

---

**Versão**: 1.0.0  
**Data**: 27/02/2026
