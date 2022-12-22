"""
Os argumentos de uma função podem ter um valor por defeito, em inglês default 
que é o valor que será assumido caso nenhum valor seja passado.
"""

def imprime_nome(nome, sobrenome="Sabugosa"):
    print(nome, sobrenome)

imprime_nome("Felipe")
# Felipe Sabugosa

imprime_nome("Felipe", "Madeiros")
# Felipe Madeiros