# Lista de palavras https://www.ime.usp.br/\~pf/dicios/br-utf8.txt
import unicodedata
import os
import random
from rich.prompt import Prompt # input
from rich.console import Console

DIR = os.path.abspath(os.path.dirname(__file__))
MENSAGEM = (
    "Boas Vindas "
    "ao "
    "Pylavras!"
)

INSTRUCAO = "Adivinhe a palavra de 5 letras.\n"


def tira_acento(s):
    return unicodedata.normalize(
        "NFD", s
    ).encode(
        'ascii', "ignore"
    ).decode(
        "utf-8"
    )

def filtrar_palavras():
    """Filta palavra com 5 letras da lista original de palavras"""
    original = open("br-utf8.txt").readlines()

    with open("palavras.txt", "w") as palavras:
        palavras.write(
            "\n".join(
                tira_acento(p.strip().upper()) for p in original if len(p.strip()) == 5
            )
        )


def posicao_correta(letra):
    return f"[white on green]{letra}[/]"

def letra_correta(letra):
    return f"[white on yellow]{letra}[/]"

def letra_errada(letra):
    return f"[white on black]{letra}[/]"

def computa_tentativa(tentativa):
    acertos = []
    for i, letra in enumerate(tentativa):
        if tentativa[i] == palavra_correta[i]:
            acertos += posicao_correta(letra)
        elif letra in palavra_correta:
            acertos += letra_correta(letra)
        else:
            acertos += letra_errada(letra)
    return "".join(acertos)


filtrar_palavras()
palavra_correta = random.choice(
    open(os.path.join(DIR, "palavras.txt")).readlines()
).strip().upper()


tentativas = 6
rodadas = 0

console = Console()
console.print(MENSAGEM)
console.print(INSTRUCAO)

acertados = []
while rodadas < tentativas:
    tentativa = Prompt.ask("Digite [red]5[/] letras").strip().upper()

    if len(tentativa) != 5:
        console.print("ERRO: Digite apenas [red]5[/] letras.")
        continue
    rodadas += 1

    #calcula
    acertos = computa_tentativa(tentativa)
    acertados.append(acertos)

    for acerto in acertados:
        console.print(acerto)
    
    if tentativa == palavra_correta:
        break

console.print(f"Pylavras: {rodadas}/{tentativas}")
console.print(f"Palavra certa: {palavra_correta}")
