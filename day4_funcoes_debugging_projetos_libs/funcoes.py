#!/usr/bin/env python3
"""Exemplos de funcoes
f(x) = 5 * (x / 2)
"""

def f(x):
    result = 5 * (x / 2)
    return result

valor = f(10)
print(valor)

##########################

#Funcoes sem return são chamadas de procedimentos/procedure
def print_in_upper(text):
    print(text.upper())
    # implicit returno None

print_in_upper("felipe")

##########################

from math import sqrt

def heron(a, b, c): #Formula matematica de heron para calcular area de um triangulo
    perimeter = a + b + c
    s = perimeter / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c)) # sqrt() = raiz quadrada
    # area = 0.5 ** (s * (s - a) * (s - b) * (s - c)) 
    return area

triangulos = [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17)
]

for t in triangulos:
    area = heron(*t)
    # area = heron(t[0], t[1], t[2])
    print(f"A area do triangulo é {area}")
