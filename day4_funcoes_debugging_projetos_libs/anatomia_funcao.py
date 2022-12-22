"""
Este modulo serve apenas de anotação

definicao ou atribuicao
assinatura + type hints
documentacao / docstrings
codigo
valor de retorno

- parametros
    posicional - passados em ordem
    nomeado - a ordem nao importa
    mista

"""

#Modelo antigo de documentacao de funcoes
def nome_da_funcao(a, b, c):
    #Exemplo
    """[Summary]
    :param [ParamName]: [ParamDescription], defaults to [DefaultParamVal]
    :type [ParamName]: [ParamType](, optional)
    ...
    :raises [ErrorType]: [ErrorDescription]
    ...
    :return: [ReturnDescription]
    :rtype: [ReturnType]
    """

    """Esta funcao faz algo com a, b e c
    
    Use esta funcao quando quiser a + b + c

    :param a: Numero inteiro
    :param b: Numero inteiro
    :param c: Numero inteiro
    """

#Modelo mais recente de documentacao de funcoes
def nome_da_funcao2(a: int, b: int, c: int) -> int:
    #Exemplo
    """Esta funcao faz algo com a, b e c
    
    Use esta funcao quando quiser a + b + c

    >>> nome_da_funcao(1, 2, 3)
    6
    """
    result = a + b + c
    return result

#passagem de argumentos posicionais
valor = nome_da_funcao2(1, 2, 3)

#passagem de argumentos nomeados
valor = nome_da_funcao2(b=1, c=2, a=3)

#passagem de argumentos mista
valor = nome_da_funcao2(1, c=2, b=3)

print(valor)

#####################

def nome_da_funcao3(a, b, c):
    """Explica o que ela faz"""
    return a * 2, b * 2, c * 2

valor3 = nome_da_funcao3(1, 2, 3)
print(valor3)

valor3_1, valor3_2, valor3_3 = nome_da_funcao3(1, 2, 3)
print(valor3_1, valor3_2, valor3_3)

valor3_1, *resto = nome_da_funcao3(1, 2, 3)
print(valor3_1)
print(resto)

#####################################

def soma(n1, n2):
    """Faz a soma de 2 numeros"""
    return n1 + n2

print(soma(10, 20))


args = (10, 20) #tuple
#result = soma(args[0], args[1])
result = soma(*args) #posicional
print(result)

args2 = {"n2": 90, "n1": 100} #dict
#result2 = soma(n1=args2["n1"], n2=args2["n2"])
result2 = soma(**args2)
print(result2)
