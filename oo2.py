# Componentes 
#   Classe `class` - MaterialEscritorio, Eletronico, gadget, Fruta
#   Objetos - Instancias criadas a partir da classe - caneta, relogio, banana
#   Atributos - Valores definidos nas classes e nos objetos/instancias
#   Metodo - Funcao definida no escopo da classe

# Definição da classe
class Person:  # pascalCase, UpperCamelCase 
    """Represents a Person"""

    # Atributos da classe
    company_name = "Dunder Mifflin"  
    work_address = "Stanton Street, Pensilvania"
    balance = 0

    # Métodos (funcao dentro de uma classe)
    def add_points(person, value): #snacke_case
        print(person.__dict__)
        if person.role == "manager":
            value *= 2
        person.balance += value

jim = Person()  # Instanciação de um objeto a partir da classe
jim.name = "Jim Halpert"
jim.role = "Salesman"
jim.add_points(100)  # Chamada de método associado

print(jim.name)
print(jim.company_name)
print(jim.role)
print(jim.balance)  # Acesso a atributo
