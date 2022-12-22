""" 
É importante tomar bastante cuidado com valores mutáveis, pois como já vimos,
dentro de uma função, o efeito colateral será a alteração do valor global.
"""

#Este é um erro muito comum
def adiciona_a_lista(valor, lista=[]):
    lista.append(valor)
    return lista

adiciona_a_lista(4)
adiciona_a_lista(5)
print(adiciona_a_lista(6))
# [4, 5, 6]

def adiciona_a_lista(valor, lista=None):
    if lista is None:
        lista = []
    lista.append(valor)
    return lista

adiciona_a_lista(4)
adiciona_a_lista(5)
print(adiciona_a_lista(6))
# [6]
