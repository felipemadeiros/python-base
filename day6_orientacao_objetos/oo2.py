# Componentes 
#   Classe `class` - MaterialEscritorio, Eletronico, gadget, Fruta
#   Objetos - Instancias criadas a partir da classe - caneta, relogio, banana
#   Atributos - Valores definidos nas classes e nos objetos/instancias
#   Metodo - Funcao definida no escopo da classe

# Definição da classe
class Person:  # pascalCase, UpperCamelCase 
    """Represents a Person"""

    # Atributos da classe
    # atributo de classe imutável, todo objeto terá esse atributo inicialmente
    company_name = "Dunder Mifflin"  
    work_address = "Stanton Street, Pensilvania"
    balance = 0
    # atributo de classe mutável, novos objetos irá herdar os valores definido por outro objeto anteriormente.
    # usar atributo mutável somente se realmente for sua intenção.
    #prefered_colors = []

    def __init__(self, name, role="Indefined", prefered_colors=None):
        self.name = name
        self.role = role
        self.prefered_colors = prefered_colors or []

    # Métodos (funcao dentro de uma classe)
    # Injecao de dependencia - 1 arg do metodo = a propria instancia/objeto
    def add_points(self, value): #snacke_case
        if self.role == "manager":
            value *= 2
        self.balance += value

jim = Person("Jim Halpert", role="Salesman", prefered_colors=["Blue"])  # Instanciação de um objeto a partir da classe
jim.add_points(500)  # Chamada de método associado
jim.work_address = "Home"
print(jim.name, jim.balance, jim.prefered_colors, jim.work_address, jim.role)

pam = Person("Pam Besly", role="Manager", prefered_colors=["Purple", "Yellow"])  # Instanciação de um objeto a partir da classe
pam.add_points(100)  # Chamada de método associado
print(pam.name, pam.balance, pam.prefered_colors, pam.work_address, pam.role)
