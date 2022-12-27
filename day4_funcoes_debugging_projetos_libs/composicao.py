names = ["Bruno", "Joao", "Bernardo", "Cintia", "Marcia", "Juca"]

# estilo procedural
print("Estilo procedural")
def starts_with_b(text):
    """Retorna true se o texto inicial com a letra b"""
    return text[0].lower() == "b"

filtro = filter(starts_with_b, names)
lista = list(filtro)

for name in lista:
    print(name)


# estilo funcional
print(" ")
print("Estilo funcional")
print(*list(filter(lambda text: text[0].lower() == "b", names)))
