#!/usr/bin/env python3

"""Exibe relatorio de criancas por atividades

Imprimir a lista de criancas agrupadas por sala que frequenta
cada uma das atividades.
"""

__version__ = "0.0.1"

# Dados
salas = {
    "1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]
}

aulas = {
    "ingles": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "musica": ["Erik", "Carlos", "Maria"],
    "danca": ["Gustavo", "Sofia", "Joana", "Antonio"]
}

for key in aulas.keys():
    alunos = {}
    print(f"Alunos da aula de {key}\n")

    for i in salas.keys():
        alunos[i] = set(salas[i]) & set(aulas[key])
        print(f"Sala {i}", alunos[i])

    print("-" * 20)
    print()
