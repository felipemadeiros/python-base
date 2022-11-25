#!/usr/bin/env python3

"""
Faça um programa de terminal que exibe ao usuário uma listas dos quartos
disponiveis para alugar e o preço de cada quarto, esta informação está
disponível em um arquivo de texto separado por virgulas.
`quartos.txt`
# codigo, nome, preço
1,Suite Master,500
2,Quarto Familia,200
3,Quarto Single,100
4,Quarto Simples,50
O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado
e a quantidade de dias e no final exibe o valor estimado a ser pago.
O programa deve salvar esta escolha em outro arquivo contendo as reservas
`reservas.txt`
# cliente, quarto, dias
Bruno,3,12
Se outro usuário tentar reservar o mesmo quarto o programa deve exibir uma
mensagem informando que já está reservado.
"""

import os, sys
import logging

path = os.path.join(os.curdir, 'files')
filepath = os.path.join(path, 'quartos.txt')

rooms = {}
reserves = []

print('Quartos disponiveis para reserva:\n')

try:
    for line in open(filepath):
        if "#" in line:
            continue
        code, name, price = line.strip().split(",")
        rooms[int(code)] = {'name': name, 'price': float(price)}     #TODO: Usar Decimal
        print(f'{code} - {name} por R${float(price):.2f} a diaria.') #TODO: Substituir . por ,
except FileNotFoundError:
    logging.error('Arquino nao existe')
    sys.exit(1)

guest = input('\nInforme seu nome para iniciar a reserva (ou enter para sair): ').strip()

if not guest: #Verifica se usuário deseja continuar
    sys.exit(1)

infos = {
    'quarto': None,
    'dias': None
}

for key in infos.keys():
    try:
        infos[key] = int(input(f'Informe o {key} que deseja reservar: '))
    except ValueError:
        logging.error('Numero invalido, digite apenas numeros')
        sys.exit(1)

filepath = os.path.join(path, 'reservas.txt')
try:
    for line in open(filepath):
        if "#" in line:
            continue
        r_guest, r_room, r_days = line.strip().split(",")
        reserves.append(int(r_room))
except FileNotFoundError:
    logging.error('Arquivo resevas.txt nao existe')

if infos['quarto'] in reserves:
    print('\nEste quarto ja esta reservado.')
    sys.exit(1)
else:
    room = infos['quarto']
    days = infos['dias']
    total = int(rooms[room]['price']) * days

print(f'\nO valor total da reserva é de R${total}')
confirm = input('Digite `sim` para confirmar a reserva ou enter para cancelar: ')

if confirm == 'sim': 
    with open(filepath, "a") as file_:
        file_.write(f'{guest},{room},{days}\n')
        # file_.write(",".join([guest, str(room), str(days)])) # Igual a linha anterior
