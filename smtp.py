#!/usr/bin/env python3
"""
Exemplo de envio de email

Iniciar um servidor SMTP local
# python -m smtpd -c DebuggingServer -n localhost:8025
"""

import smtplib

SERVER = "localhost"
PORT = 8025

FROM = "felipemadeiros@gmail.com"
TO = ["user1@server.com", "user2@server.com"]
SUBJECT = "Meu email via Python"
TEXT = """\
Este é o meu email enviado pelo python
<b> Olá mundo </b>
"""

message = f"""\
From: {FROM}
To: {", ".join(TO)}
Subject: {SUBJECT}

{TEXT}
"""

with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM, TO, message.encode("utf-8"))