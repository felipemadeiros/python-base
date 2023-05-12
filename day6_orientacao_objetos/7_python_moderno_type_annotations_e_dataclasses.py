""" Carrinho de compras
Sempre que houver necessidade de trabalhar com precisão de 
numeros (e.g dinheiro, peso de algo e etc), utilizar o decimal ao inves de float
"""
from decimal import Decimal


produto = "Caneta"
# valor = 4.5 # float
valor = Decimal(4.5) # decimal
quantidade = 5

def calcula_total(valor: Decimal, quantidade: int) -> Decimal:
    return valor * quantidade # __mul__ de Decimal

total = calcula_total(valor, quantidade)
print("Tipo:", type(total))
print(f"O total é R${total:.2f}")


########################################
from dataclasses import dataclass

@dataclass
class Pessoa:
    # def __init__(self, pk: str, name: str, points: int):
    #     self.pk = pk
    #     self.name = name
    #     self.points = points
    pk: str
    name: str
    points: int

def funcao(dados: Pessoa):
    ...

dados = Pessoa(pk="joe@doe.com", name="Joe", points=10)
funcao(dados)

print(dados.name)
