#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10."""

__version__ = "0.0.1"
__author__ = "Felipe Madeiros"

#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11))

# Iterable (percorriveis)
for numero in numeros:
    print("Tabuada do:", numero)
    for n in numeros:
        print(numero * n)
    print("-" * 12)