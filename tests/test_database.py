"""
Testes para módulo de banco de dados.
"""

import pytest
import sqlite3


class TestDatabase:
    """Testes de banco de dados."""
    
    @pytest.mark.unit
    @pytest.mark.db
    def test_database_creation(self, temp_db):
        """Testa criação do banco de dados."""
        cursor = temp_db.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in cursor.fetchall()]
        
        assert "servidores" in tables
        assert "folha_pagamento" in tables
    
    @pytest.mark.unit
    @pytest.mark.db
    def test_insert_servidor(self, temp_db):
        """Testa inserção de servidor."""
        cursor = temp_db.cursor()
        
        cursor.execute("""
            INSERT INTO servidores (nome, cargo, departamento, salario)
            VALUES (?, ?, ?, ?)
        """, ("João Silva", "Assistente", "TI", 3000.00))
        
        temp_db.commit()
        
        cursor.execute("SELECT * FROM servidores WHERE nome = ?", ("João Silva",))
        result = cursor.fetchone()
        
        assert result is not None
        assert result[1] == "João Silva"
        assert result[2] == "Assistente"
    
    @pytest.mark.unit
    @pytest.mark.db
    def test_select_query(self, sample_data):
        """Testa seleção de dados."""
        sample_data.execute("SELECT COUNT(*) FROM servidores")
        count = sample_data.fetchone()[0]
        
        assert count == 3
    
    @pytest.mark.unit
    @pytest.mark.db
    def test_select_active_servidores(self, sample_data):
        """Testa seleção de servidores ativos."""
        sample_data.execute("SELECT COUNT(*) FROM servidores WHERE ativo = 1")
        count = sample_data.fetchone()[0]
        
        assert count == 2
    
    @pytest.mark.unit
    @pytest.mark.db
    def test_update_servidor(self, sample_data, temp_db):
        """Testa atualização de servidor."""
        sample_data.execute("""
            UPDATE servidores SET salario = ? WHERE nome = ?
        """, (3500.00, "João Silva"))
        
        temp_db.commit()
        
        sample_data.execute("SELECT salario FROM servidores WHERE nome = ?", ("João Silva",))
        salario = sample_data.fetchone()[0]
        
        assert salario == 3500.00
    
    @pytest.mark.unit
    @pytest.mark.db
    def test_delete_servidor(self, sample_data, temp_db):
        """Testa deleção de servidor."""
        sample_data.execute("DELETE FROM servidores WHERE nome = ?", ("João Silva",))
        temp_db.commit()
        
        sample_data.execute("SELECT COUNT(*) FROM servidores")
        count = sample_data.fetchone()[0]
        
        assert count == 2


class TestDataIntegrity:
    """Testes de integridade de dados."""
    
    @pytest.mark.integration
    @pytest.mark.db
    def test_foreign_key_constraint(self, temp_db):
        """Testa restrição de chave estrangeira."""
        cursor = temp_db.cursor()
        
        # Habilitar foreign keys
        cursor.execute("PRAGMA foreign_keys = ON")
        
        # Tentar inserir folha_pagamento com servidor_id inválido
        with pytest.raises(sqlite3.IntegrityError):
            cursor.execute("""
                INSERT INTO folha_pagamento (servidor_id, mes, ano, valor_liquido)
                VALUES (?, ?, ?, ?)
            """, (999, 1, 2024, 3000.00))
            temp_db.commit()
