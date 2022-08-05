#!/usr/bin/env python3

"""Cadastro de produto"""
__version__ = "0.0.1"

from pprint import pprint

produto = {
    "nome": "caneta",
    "cores": ["azul","branco"],
    "preco": 3.23,
    "dimensao": {
        "altura": 12.1,
        "largura": 0.8,
    },
    "em_estoque": True,
    "codigo": 4567,
    "code_bar": None,
}

cliente = {
    "nome": "Felipe",
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3
}

total_compra = compra["quantidade"] * compra["produto"]["preco"]

print(
    f"O cliente {compra['cliente']['nome']} comprou {compra['quantidade']} unidades"
    f" de {compra['produto']['nome']} e pagou o total de {total_compra}"
)