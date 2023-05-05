# Protocolos / Data Model

# Printable - __str__
# Addible - __add__ | __radd__
class Cor: # Base Class
    icon = "branco"

    # def __repr__(self): # metodo repr (representacao do objeto)
    #     return f"'<Cor object at memory position {id(self)}'"
    
    def __str__(self):
        return self.icon
    
    def __add__(self, other):
        mixtable = [
            ((Amarelo, Vermelho), Laranja),
            ((Azul, Amarelo), Verde),
            ((Vermelho, Azul), Roxo)
        ]
        for mix, result in mixtable:
            if isinstance(self, mix) and isinstance(other, mix):
                return result()

class Amarelo(Cor):
    icon = "amarelo"

class Azul(Cor):
    icon = "azul"

class Vermelho(Cor):
    icon = "vermelho"

class Laranja(Cor):
    icon = "laranja"

class Verde(Cor):
    icon = "verde"

class Roxo(Cor):
    icon = "roxo"

print("Cores primárias")
print(Amarelo(), Azul(), Vermelho())

print("\nCores secundárias")
print("Amarelo + Vermelho =", Amarelo() + Vermelho())
print("Azul + Amarelo =", Azul() + Amarelo())
print("Vermelho + Azul =", Vermelho() + Azul(), "\n")


# Collection (iterable + container + sized)
    # Iterable - __iter__
    # Container - __contains__ -> bool
    # Sized - __len__
# Subscriptable - __getitem__
class Paleta:
    def __init__(self, *cores):
        self._cores = cores

    def __iter__(self):
        return iter([cor for cor in self._cores])
    
    def __contains__(self, item):
        #print([cor.icon for cor in self._cores])
        return item in [cor.icon for cor in self._cores]
    
    def __len__(self):
        return len(self._cores)
    
    def __getitem__(self, item):
        if isinstance(item, (int, slice)): #e.g 0, 2:4
            return self._cores[item]
        if isinstance(item, str):
            for cor in self._cores:
                if cor.__class__.__name__.lower() == item.lower():
                    return cor


rgb = Paleta(Vermelho(), Verde(), Azul())

print("Paleta de cores")
for cor in rgb: # __iter__
    print(cor)
print("\n", "azul" in rgb) # __contains
print("Quantidade de cores:", len(rgb)) # __len__

print(rgb[1]) # __getitem__
print(rgb["azul"]) # __getitem__
