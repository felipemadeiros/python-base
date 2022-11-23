#!/usr/bin/env python3

######################################################
# Loop for iteration

# range function ocupa mesmo memoria que uma lista declarada
original = range(1, 4) #original = [1, 2, 3]
dobrada = []

print(original)
for n in original:
    dobrada.append(n * 2)

print(dobrada)

# List Comprehension, faz a mesma coisa que o codigo acima
original = range(1, 4)
dobrada = [n * 2 for n in original]
print(dobrada)
#####################################################

#####################################################
# Dict Comprehension
dados = {
    line.split(":")[0]: line.split(":")[1].strip()
    for line in open("files/post.txt")
    if ":" in line
}
print(dados)

# Esse código faz a mesma coisa que o dict comprehension
dados = {}
for line in open("files/post.txt"):
    if ":" in line:
        key, valor = line.split(":")
        dados[key] = valor.strip()
print(dados)
#########################################################

########################################################
# Loop while
n = 0 
while n < 11:
    if n % 2 != 0:
        n += 1
        continue # retorna para o começo do while
    print(n)
    n += 1