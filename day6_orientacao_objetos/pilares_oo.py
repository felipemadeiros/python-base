# Abstracao - Capacidade de abstrair implementacoes
# classe abstrata - super classe
class Person:
    kingdom = "animalia"

class Fruit:
    kingdom = "vegetalia"

    def __init__(self, color) -> None:
        self.color = color

class Animal:
    kingdom = "animalia"


# Heranca - Capacidade de herdar de outras classes
# classe material, derivadas de uma classe (sub classe)
class Apple(Fruit):
    image = "\N{red apple}"

minha_maca = Apple(color=['red'])
print(minha_maca.color)
print(minha_maca.kingdom)
print(minha_maca.image)


# Polimorfismo (protocolo) - Capacide de uma implementacao se comportar de
#   maneira similar, indepedente da forma do objeto
class Dog:
    def make_sound(self):
        return "woof woof"
    
class Cat:
    def make_sound(self):
        return "meow meow"

class Car:
    def make_sound(self):
        return "vrum vrum"

def print_sound(obj): # funcao polimorfica
    if not hasattr(obj, "make_sound"):
        raise TypeError(f"{obj} is not Soundable")    
    print(obj.make_sound())

rex = Dog()
print_sound(rex)

lili = Cat()
print_sound(lili)

ferrari = Car()
print_sound(ferrari)

# print_sound(42)

# Encapsulamento
## Por convencao de nomes (_var | __var)
class Conta:
    _tipo_de_conta = "corrente" # protegido
    __id_interno = 456789 # privado

    def __init__(self, cliente) -> None:
        self.cliente = cliente
        self._saldo = 0 # protegido
        
        if self._tipo_de_conta == "corrente":
            self._saldo = 1
    
    def consultar(self):
        if self._saldo < 0:
            print("AVISO: Voce esta devendo")
        return self._saldo

conta = Conta(cliente="Felipe")
conta._tipo_de_conta = "poupanca"
print(conta.consultar())
print(dir(conta))
#print(conta.__id_interno)



