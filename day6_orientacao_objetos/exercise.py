"""
Este programa pergunta ao usuário quais items ele deseja comprar
e calcula o valor total da compra.

1. Clique em Run e execute o programa para ver como ele funciona.
2. Para cada um dos comentários marcados abaixo efetue as alterações
   usando orientação a objetos.
"""
from decimal import Decimal

class Product:
    """Products"""
    def __init__(self, name, price):
        self.name = name
        self.price = price

produtos = {
    "1": Product("Maça", price=Decimal(4.5)), # para valores monetários devemos usar Decimal ao invés de float
    "2": Product("Melancia", price=Decimal(6.3))
}

###############################################################################
# 1.
# `produtos` acima é um objeto do tipo `dict` que contém produtos que
# também estão no formato `dict`.
# Desafio: Crie uma classe `Produto` para armazenar `nome` e `valor`
# Faça com que o dicionário `Produtos` armazene instancias de `Produto`
# No lugar de sub dicionários.
###############################################################################

print("Olá cliente, boas vindas à quitanda!")
print("Estes são os produtos disponíveis:")
for codigo, produto in produtos.items():
    print(f"{codigo} -> {produto.name} - R$ {produto.price:.2f}")

###############################################################################
# 2.
# Altere as linhas acima para imprimir as informações usando o objeto Produto
###############################################################################

class Purchase:
    """Compras"""
    def __init__(self, client, items=None) -> None:
        self.client = client
        self.items = items or []

    def calcula_total(self, items):
        """Calcula o total da compra"""
        total = 0
        for cod_produto, quantidade in items:
            produto = produtos[cod_produto]
            total += produto.price * quantidade
        return Decimal(total)

# compra = {"cliente": input("Qual o seu nome?"), "items": []}
purchase = Purchase(input("Qual o seu nome?"))

###############################################################################
# 3.
# Crie uma classe `Compra` que contenha os atributos `cliente` e `items` e
# utilize uma instância desta classe para substituir o dicionário `compra`
# e transforme a função `calcula_total` em um método ou propriedade da classe
###############################################################################

while True:
    cod_produto = input("Código do produto: [enter para sair]").strip()
    if not cod_produto:
        break
    if cod_produto not in produtos:
        print("Codigo inválido tente novamente.")
        continue
    quantidade = int(input("Quantas Unidades?:").strip())
    purchase.items.append([cod_produto, quantidade])

print(f"Olá, {purchase.client}")
print(f"No seu carrinho de compras tem {len(purchase.items)} item.")
print(f"O total da compra é {purchase.calcula_total(purchase.items):.2f}")

###############################################################################
# 4.
# Certifique-se de que o programa continua funcionando após as alterações.
###############################################################################
