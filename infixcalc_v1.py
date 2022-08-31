#!/usr/bin/env python3
"""Calculadora infix.

Funcionamento:

[operacao] [n1] [n2]

Operacoes:
sum -> +
sub -> -
mul -> 8
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py
operacao: sum
n1: 5
n2: 4

Os resultados serao salvos em infixcalc.log
"""

__version__ = "0.1.0"
__author__ = "Felipe Madeiros"
__license__ = "unlicense"

import os
import sys
from datetime import datetime

arguments = sys.argv[1:]

if not arguments:
    arguments.append(input("Operacao: "))
    arguments.append(input("N1: "))
    arguments.append(input("N2: "))
elif len(arguments) != 3:
    print("Numero de argumentos invalidos")
    print("ex: `sum 5 10`")
    sys.exit(1)

operation, *nums = arguments

valid_operations = ("sum", "sub", "mul", "div")
if operation not in valid_operations:
    print("Operacao invalida")
    print(valid_operations)
    sys.exit(1)

validated_nums =[]
for num in nums:
    if not num.replace(".", "").isdigit():
        print(f"Numero `{num}` invalido")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

if arguments[0] == "sum":
    result = validated_nums[0] + validated_nums[1]

if arguments[0] == "sub":
    result = validated_nums[0] - validated_nums[1]

if arguments[0] == "mul":
    result = validated_nums[0] * validated_nums[1]

if arguments[0] == "div":
    result = validated_nums[0] / validated_nums[1]

os.makedirs("logs", exist_ok=True)
path = os.path.join(os.path.abspath(os.curdir), "logs")
filepath = os.path.join(path, "ifixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv('USER', 'anonymous')

with open(filepath, "a") as file_:
    file_.write(f"{timestamp} - {user} - {arguments[0]}, {validated_nums[0]}, {validated_nums[1]} = {result}\n")

print(f"O resultado é {result}")