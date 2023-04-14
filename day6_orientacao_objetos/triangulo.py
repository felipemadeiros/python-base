# Esse mesmo exercicio foi realizado na aula sobre funções
# day4_funcoes_debugging_projetos_libs/funcoes.py

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        perimeter = self.a + self.b + self.c
        s = perimeter / 2
        area = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
        return area


triangle = Triangle(5, 12, 13)
print(triangle.area())

triangulos = [
    Triangle(3, 4, 5),
    Triangle(5, 12, 13),
    Triangle(8, 15, 17),
    Triangle(12, 35, 37),
    Triangle(3, 4, 5),
    Triangle(5, 12, 13),
    Triangle(8, 15, 17),
    Triangle(12, 35, 37),
]
for t in triangulos:
    print("A area do triangulo é: ", t.area())
