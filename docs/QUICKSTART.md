# Guia de Início Rápido - FACIN_IA_D_P_N_1

## ⚡ 5 Minutos para Começar

### 1. Clone/Fork o Repositório

```bash
# Clone (ou seu fork)
git clone https://github.com/gutpassos/FACIN_IA.git
cd FACIN_IA
```

### 2. Configure o Ambiente

```bash
# Criar ambiente virtual (recomendado)
python -m venv .venv

# Ativar
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### 3. Configure Variáveis de Ambiente

**Opção 1: Arquivo .env (Recomendado para produção)**

```bash
# Copiar arquivo de exemplo
cp .env.example .env

# Editar com suas chaves
# GROQ_API_KEY=gsk_seu_groq_key_aqui
# OPENAI_API_KEY=sk-seu_openai_key_aqui
```

**Opção 2: Interface Streamlit (Desenvolvimento)**

As chaves podem ser inseridas diretamente na sidebar do Streamlit ao iniciar a aplicação.

⚠️ **Ambas as chaves são obrigatórias** (Groq e OpenAI)

### 4. Criar Banco de Dados

```bash
# Executar script de inicialização
python cria_db.py
```

### 5. Iniciar Aplicação

```bash
# Executar Streamlit
streamlit run app.py
```

✅ Aplicação rodando em `http://localhost:8501`

---

## 🤖 Como Usar

### Exemplos de Consultas

Faça perguntas em português natural:

```
❓ "Quantos servidores estão ativos?"
❓ "Qual é a remuneração do Servidor 2?"
❓ "Quantos servidores ocupam o cargo de Assistente?"
❓ "Quantos servidores são da Secretaria da Saúde?"
❓ "Na Fazenda, quantos servidores ocupam o cargo de Assistente?"
❓ "Quantos servidores tiveram aumento?"
❓ "@groq Mostre todos os órgãos no banco de dados"
❓ "@openai Qual a folha total em 202401?"
```

O sistema usa **LangGraph** para:
- ✅ Alternar automaticamente entre Groq (Llama3) e OpenAI (GPT)
- ✅ Permitir seleção explícita com @groq ou @openai  
- ✅ Executar ferramentas (query_folha_database) quando necessário
- ✅ Consultar banco SQLite com validação de segurança
- ✅ Fornecer resposta formatada em português

O sistema usa LangGraph para:
- ✅ Rotear sua pergunta ao agente apropriado
- ✅ Consultar banco de dados
- ✅ Analisar dados
- ✅ Fornecer resposta em português

---

## 📁 Arquivos Importantes

| Arquivo | Descrição |
|---------|-----------|
| `app.py` | Aplicação principal (Streamlit) |
| `cria_db.py` | Setup do banco de dados |
| `requirements.txt` | Dependências Python |
| `.env` | Variáveis de ambiente (local) |
| `spec.json` | Especificação do projeto |
| `docs/` | Documentação completa |
| `errors/` | Erros encontrados e soluções |

---

## 🔐 Variáveis de Ambiente

```bash
# APIs (obrigatórias para LLMs)
OPENAI_API_KEY=sk-...
GROQ_API_KEY=gsk-...

# Opcional (monitoramento)
AGENTICOPS_API_KEY=...

# Banco de dados
DATABASE_PATH=folha_pagamento.db

# Desenvolvimento
DEBUG=true
PYTHONPATH=.
```

---

## 🧪 Verificações Rápidas

### Testar Conexão com Banco

```python
python -c "
import sqlite3
conn = sqlite3.connect('folha_pagamento.db')
cursor = conn.cursor()
cursor.execute('SELECT COUNT(*) FROM servidores')
print(f'Total de servidores: {cursor.fetchone()[0]}')
conn.close()
"
```

### Validar Formatação

```bash
black . --check --line-length=100
```

### Executar Testes

```bash
pytest -v
```

---

## 🐛 Troubleshooting

### ModuleNotFoundError: No module named 'streamlit'

```bash
# Reinstalar dependências
pip install --upgrade -r requirements.txt
```

### OPENAI_API_KEY not found

```bash
# Verificar .env
cat .env

# Adicionar chave
echo "OPENAI_API_KEY=sk-..." >> .env
```

### Erro ao carregar banco de dados

```bash
# Recriar banco
rm folha_pagamento.db
python cria_db.py
```

### Porta 8501 já em uso

```bash
# Usar porta diferente
streamlit run app.py --server.port=8502
```

---

## 📚 Próximos Passos

1. **Ler documentação**
   - [README.md](README.md) - Overview
   - [ARCHITECTURE.md](ARCHITECTURE.md) - Como funciona
   - [API.md](API.md) - Referência técnica

2. **Explorar código**
   - Entender estrutura em `app.py`
   - Ver agentes em LangGraph
   - Examinar ferramentas

3. **Desenvolver**
   - Criar seu próprio agente
   - Adicionar ferramentas
   - Melhorar respostas

4. **Contribuir**
   - Ver [CONTRIBUTING.md](CONTRIBUTING.md)
   - Submeter PR
   - Reportar bugs

---

## 🚀 Dicas Pro

### VSCode + GitHub Copilot

```json
{
    "github.copilot.enable": {"python": true},
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe"
}
```

### Debugging

```python
# No app.py
import streamlit as st

# Visualizar estado
st.write(state)
st.json(messages)
```

### Performance

```python
# Use @st.cache_data para caching
@st.cache_data(ttl=3600)
def expensive_query():
    return execute_database_query(...)
```

---

## 📞 Precisa de Ajuda?

1. Verifique [errors/ERRORS_LOG.md](../errors/ERRORS_LOG.md)
2. Abra uma [Issue no GitHub](https://github.com/gutpassos/FACIN_IA/issues)
3. Email: gut.passos@gmail.com

---

## ✅ Checklist de Setup

- [ ] Python 3.10+ instalado
- [ ] Repositório clonado
- [ ] Ambiente virtual criado
- [ ] Dependências instaladas
- [ ] .env configurado
- [ ] Banco de dados criado
- [ ] Aplicação rodando em localhost:8501
- [ ] Teste uma consulta básica

---

**Pronto para começar a desenvolver?** 🚀

---

**Versão**: 1.0.0  
**Data**: 27/02/2026
