# Projeto 7 - Gerenciamento de Memória e Contexto - Sistema de Multi-Agentes de IA com LangGraph Para Automação do CRM e Consulta a Banco de Dados
# Módulo de Criação do Banco de Dados

# Imports
import os
import sqlite3
import pandas as pd
from datetime import datetime, timedelta

# Define o nome do arquivo de banco de dados SQLite
DB_FILE = "folha_pagamento.db"
SQL_FILE = "criacao_banco.sql"

# Declara a função responsável por criar e conectar ao banco de dados SQLite
def cria_database():

    # Verifica se o arquivo SQL existe no diretório atual
    if not os.path.exists(SQL_FILE):
        print(f"Erro: O arquivo de script SQL '{SQL_FILE}' não foi encontrado.")
        return

    # Remove o banco de dados existente para garantir uma recriação limpa
    if os.path.exists(DB_FILE):
        try:
            os.remove(DB_FILE)
            print(f"Banco de dados antigo '{DB_FILE}' removido com sucesso.")
        except PermissionError:
            print(f"Erro: Permissão negada ao tentar remover '{DB_FILE}'. Feche qualquer programa que esteja usando o banco de dados.")
            return

    # Inicializa a variável de conexão como None
    conn = None

    # Início do bloco de tratamento de exceções para operações de banco de dados
    try:

        # Conecta-se ao arquivo de banco de dados SQLite ou cria se não existir
        conn = sqlite3.connect(DB_FILE)
        
        # Cria um cursor para executar comandos SQL
        cursor = conn.cursor()

        # Exibe mensagem de conexão bem-sucedida
        print(f"Conectado ao banco de dados: {DB_FILE}")

        # Lê o conteúdo do arquivo SQL
        # encoding='utf-8' é importante para caracteres especiais
        with open(SQL_FILE, 'r', encoding='utf-8') as f:
            sql_script = f.read()
            
        print("Executando o script SQL...")
        
        # O método executescript permite rodar múltiplos comandos SQL de uma vez
        cursor.executescript(sql_script)
        
        conn.commit()
        print(f"Sucesso! O banco de dados '{DB_FILE}' foi criado e populado com os dados de '{SQL_FILE}'.")

        # Aplica as alterações no banco de dados
        conn.commit()

        # Informa que a estrutura do banco está pronta
        print("Estrutura do banco de dados pronta.")

        # Retorna a conexão e o cursor para uso posterior
        return conn, cursor

    # Captura possíveis erros de SQLite e exibe mensagem de erro
    except sqlite3.Error as e:

        print(f"Erro ao criar/conectar ao banco de dados: {e}")

        # Se a conexão foi aberta, fecha para evitar vazamento de recursos
        if conn:
            conn.close()

        # Retorna None para indicar falha na criação/conexão
        return None, None

# Declara a função que popula as tabelas com dados de exemplo
def popula_tabelas(conn, cursor):

    # Informa início do processo de inserção de dados de exemplo
    print("Populando com dados de exemplo de Folha de Pagamento...")

    # Bloco de tratamento de erros para inserção de dados
    try:
        df = pd.read_csv("folha_pe_200linhas.csv")

        conn = sqlite3.connect("folha_pagamento.db")

        # Popular tabela de servidores
        df_servidores = df[["nome","cpf","matricula","orgao","cargo"]].drop_duplicates()
        df_servidores.to_sql("tb_servidores", conn, if_exists="append", index=False)

        # Popular tabela de folha de pagamento
        df_folha = df[["matricula","competencia","vencimentos","descontos","liquido"]]
        df_folha.to_sql("tb_folha_pagamento", conn, if_exists="append", index=False)

        df_servidores.to_excel("servidores.xlsx", index=False)
        df_servidores.to_csv('servidores.csv', index=False, sep=';')
        df_folha.to_excel("folha.xlsx", index=False)
        df_folha.to_csv('folha.csv', index=False, sep=';')  

        # Aplica as alterações
        conn.commit()
        print(f"Dados de exemplo do arquivo 'folha_pe_200linhas.csv' inseridos com sucesso.")

    except sqlite3.Error as e:
        print(f"Erro ao popular tabelas: {e}")


# Função principal do script, executa criação e população do banco
def main():

    # Verifica se o arquivo de banco já existe
    if os.path.exists(DB_FILE):
        print(f"Banco de dados '{DB_FILE}' já existe.")

    # Chama a função para criar/conectar ao banco de dados e obtém conexão e cursor
    conn, cursor = cria_database()

    # Se a conexão e o cursor foram obtidos com sucesso, popula as tabelas
    if conn and cursor:

        # Executa a função
        popula_tabelas(conn, cursor)

        # Fecha a conexão após a população das tabelas
        conn.close()

        # Mensagem informando que a conexão foi fechada
        print("Conexão com o banco de dados fechada.")

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":

    print("\nIniciando a criação do banco de dados de Folha de Pagamento.\n")

    main()

    print("\nBanco de dados criado com sucesso.\n")