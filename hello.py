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
__version__ = "0.1.2"
__author__ = "Felipe Madeiros"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

# msg = "Hello World!"

# # Ordem complexidade O(n)
# if current_language == "pt_BR":
#     msg = "Ola Mundo!"
# elif current_language == "it_IT":
#     msg = "Ciao Mondo!"
# elif current_language == "es_SP":
#     msg = "Hola Mundo!"
# elif current_language == "fr_FR":
#     msg = "Bonjour Monde!"

# print(msg)   # test-ignore

####################
# dicts (Hash Table) - O(1) - constante
msg = {
    "en_US": "Hello World!",
    "pt_BR": "Ola Mundo!",
    "it_IT": "Ciao Mondo!",
    "es_SP": "Hola Mundo!",
    "fr_FR": "Bonjour Monde"
}

print(msg[current_language])   # test-ignore