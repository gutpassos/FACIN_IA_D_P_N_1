# Configuração de Logging para FACIN_IA

import logging
import logging.handlers
import os
from pathlib import Path
from datetime import datetime

# Criar diretórios de logs se não existirem
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

ERROR_LOG_DIR = Path("errors")
ERROR_LOG_DIR.mkdir(exist_ok=True)

# Formatador
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Logger raiz
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)

# Handler para arquivo de erro
error_handler = logging.handlers.RotatingFileHandler(
    filename=LOG_DIR / f"error_{datetime.now().strftime('%Y%m%d')}.log",
    maxBytes=10_000_000,  # 10MB
    backupCount=5,
    encoding='utf-8'
)
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)
root_logger.addHandler(error_handler)

# Handler para arquivo geral
info_handler = logging.handlers.RotatingFileHandler(
    filename=LOG_DIR / f"app_{datetime.now().strftime('%Y%m%d')}.log",
    maxBytes=10_000_000,  # 10MB
    backupCount=5,
    encoding='utf-8'
)
info_handler.setLevel(logging.INFO)
info_handler.setFormatter(formatter)
root_logger.addHandler(info_handler)

# Handler para console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
root_logger.addHandler(console_handler)

# Logger específico para AgenticOps
agenticops_logger = logging.getLogger('agenticops')
agenticops_logger.setLevel(logging.DEBUG)
agenticops_handler = logging.FileHandler(
    LOG_DIR / 'agenticops.log',
    encoding='utf-8'
)
agenticops_handler.setFormatter(formatter)
agenticops_logger.addHandler(agenticops_handler)

# Logger específico para Database
database_logger = logging.getLogger('database')
database_logger.setLevel(logging.DEBUG)
db_handler = logging.FileHandler(
    LOG_DIR / 'database.log',
    encoding='utf-8'
)
db_handler.setFormatter(formatter)
database_logger.addHandler(db_handler)

# Logger específico para Agents
agents_logger = logging.getLogger('agents')
agents_logger.setLevel(logging.DEBUG)
agents_handler = logging.FileHandler(
    LOG_DIR / 'agents.log',
    encoding='utf-8'
)
agents_handler.setFormatter(formatter)
agents_logger.addHandler(agents_handler)
