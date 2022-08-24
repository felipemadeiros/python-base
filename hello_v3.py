#!/usr/bin/env python3
"""Hello World Multi Linguas

Depedendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variavel LANG configurada. Ex:
 
    export LANG=pt_BR

Execucao:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.3"
__author__ = "Felipe Madeiros"
__license__ = "Unlicense"

import os
import sys

arguments = {
    "lang": None,
    "count": None
}

for arg in sys.argv[1:]:
    #TODO: Tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip() # remover o caracter '-' do comeco e espacos em branco do comeco e fim.
    value = value.strip()

    if key not in arguments:
        print(f"Invalid option `{key}`")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    #TODO: Usar repeticao
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language: ")

current_language = current_language[:5]

msg = {
    "en_US": "Hello World!",
    "pt_BR": "Ola Mundo!",
    "it_IT": "Ciao Mondo!",
    "es_SP": "Hola Mundo!",
    "fr_FR": "Bonjour Monde"
}

print(msg[current_language])