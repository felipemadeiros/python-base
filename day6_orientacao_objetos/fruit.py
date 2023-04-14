class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color


apple = Fruit(name="Apple", color="red")
banana = Fruit("Banana", color="yellow")

print(apple.name, apple.color)
print(banana.name, banana.color)
