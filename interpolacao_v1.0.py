#!/usr/bin/env python3
"""
Interpolacao
"""

__version__ = "0.1.0"
__author__ = "Felipe Madeiros"
__license__ = "unlicense"

import os
import sys

# email_template = """"
# Ola, %(nome)s

# Tem interessse em comprar %(produto)s?
# Este produto é ótimo para %(texto)s

# Clique em %(link)s

# Apenas %(quantidade)d disponiveis!

# Preço promocional %(preco).2f
# """

arguments = sys.argv[1:]
if not arguments:
    print("Informe o nome do arquivo de emails")
    sys.exit(1)

path = os.path.join(os.curdir, "files")
filename = arguments[0]
filepath = os.path.join(path, filename)
templatename = arguments[1]
templatepath = os.path.join(path, templatename)

for line in open(filepath):
    name, email = line.split(",")

    # TODO: Substituir por envio de email
    print(f"Enviando email para: {email}")
    print(
        open(templatepath).read()
        % {
            "nome": name,
            "produto": "caneta",
            "texto": "escrever muito bem",
            "link": "https://canetaslegais.com",
            "quantidade": 1,
            "preco": 50.5
        }
    )
    print("-" * 50)
    