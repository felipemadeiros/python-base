#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10."""

__version__ = "0.0.1"
__author__ = "Felipe Madeiros"

numeros = list(range(1, 11))

# Iterable (percorriveis)
for n1 in numeros:
    print("\n{:-^18}".format(f"Tabuada do {n1}"))
    for n2 in numeros:
        resultado = n1 * n2
        operacao = f"{n1} x {n2} = {resultado}"
        print("{:^18}".format(operacao))
    print("#" * 18)