"""
Uma função pode ter um comportamento polimórfico ao utilizar argumentos 
coringas (em inglês: star arguments) definidos usando *args para argumentos
posicionais e **kwargs para argumentos nomeados.
"""

def funcao(*args, **kwargs):
    print(args, kwargs)

funcao(1, 2, 3, nome="Felipe", sobrenome="Madeiros")
# (1, 2, 3) {'nome': 'Felipe', 'sobrenome': 'Madeiros'}

funcao(1, nome="Felipe")
# (1) {'nome': 'Felipe'}

funcao(1)
# (1,) {}

funcao(sobrenome="Madeiros")
# () {'sobrenome': 'Rocha'}