#!/usr/bin/env python3

"""Exibe relatorio de criancas por atividades

Imprimir a lista de criancas agrupadas por sala que frequenta
cada uma das atividades.
"""

__version__ = "0.0.1"

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

# Listar alunos em cada atividade por sala
atividades = [
    ("Ingles", aula_ingles), 
    ("Musica", aula_musica),
    ("Danca", aula_danca)
]

for nome_atividade, atividade in atividades:
    print(f"Alunos da atividade {nome_atividade}\n")
    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)

    print("Sala 1", atividade_sala1)
    print("Sala 2", atividade_sala2)
    print("-" * 20)
    print()
