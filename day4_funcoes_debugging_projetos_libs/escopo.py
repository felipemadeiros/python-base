"""
Agora que já falamos sobre a anatomia de uma função, vamos falar sobre o 
escopo de uma função.
Um escopo é similar a um namespace, um espaço do código onde os nomes são 
definidos. O isolamento de escopo é importante para que não haja conflito de 
nomes entre os identificadores.
Por exemplo, se tivermos duas funções e dentro do bloco de código de ambas 
funções atribuirmos uma variável nome, o Python cria dentro de cada função um 
escopo chamado local e define esse valor apenas ali dentro.
"""

nome = 'valor'

def nome_da_funcao1():
    nome = 'outro valor'
    nome = nome.upper()
    return nome

def nome_da_funcao2():
    nome = 'outro valor'
    nome = nome.title()
    return nome

print(nome_da_funcao1())
# VALOR

print(nome_da_funcao2())
# Outro Valor

print(nome)
# valor