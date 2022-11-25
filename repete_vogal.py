#!/usr/bin/env python3

"""
Faça um programa que pede ao usuário que digite uma ou mais plavras e imprime
cada uma das palavras com suas vogais duplicadas.

e.g
python3 repete_vogal.py
Digite uma palavra (ou enter para sair): Python
Pythoon
"""

while True:
    word = input("Digite uma palavra (ou enter para sair): ").strip()
    if not word: #condicao de parada
        break

    final_word = ""

    for letter in word:
        #TODO: remover acentuacao usando funcao
        if letter.lower() in "aeiou":
            final_word += letter * 2
        else:
            final_word += letter
        
        # Este IF tem o mesmo efeito que o IF acima (IF ternario)
        # final_word += letter * 2 if letter.lower() in "aeiou" else letter
    
    print(final_word)
