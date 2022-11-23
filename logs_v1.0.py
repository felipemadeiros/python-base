#!/usr/bin/env python3

import os
import logging

# BOILERPLATE
# TODO: criar funçao de logs
# TODO: usar lib (loguru)
log_level =  os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("logs.py", log_level)
# level
ch = logging.StreamHandler() # Console/Terminal/stderr
ch.setLevel(log_level)
# formatacao
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)

"""
logging.debug("Mensagem para o Dev, QA, SysAdmin")
logging.info("Mensagem geral para os usuarios")
logging.warning("Aviso que nao caua error")
logging.error("Erro que afeta uma unica execucao")
logging.critical("Erro geral que pode afetar todos os usuarios")

print("---")

log.debug("Mensagem para o Dev, QA, SysAdmin")
log.info("Mensagem geral para os usuarios")
log.warning("Aviso que nao caua error")
log.error("Erro que afeta uma unica execucao")
log.critical("Erro geral que pode afetar todos os usuarios")

print("---")
"""

try:
    1 / 0
except ZeroDivisionError as error:
    log.error("Deu erro %s", str(error))