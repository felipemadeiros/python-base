#!/usr/bin/env python3
"""
Interpolacao

Iniciar um servidor SMTP local
# python -m smtpd -c DebuggingServer -n localhost:8025
"""

__version__ = "0.1.1"
__author__ = "Felipe Madeiros"
__license__ = "unlicense"

import os
import sys
import smtplib
from email.mime.text import MIMEText

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

with smtplib.SMTP(host="localhost", port=8025) as server:
    for line in open(filepath):
        name, email = line.split(",")
        text = (
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

        from_ = "felipemadeiros@gmail.com"
        to = ", ".join([email])
        message = MIMEText(text)
        message["Subject"] = "Compre mais"
        message["From"] = from_
        message["To"] = to

        #print(message)
        server.sendmail(from_, to, message.as_string())
        