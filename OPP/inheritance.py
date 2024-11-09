class Animal:

    def __init__(self, name, color):
        self.nameAnimal = name
        self.colorAnimal = color
    
    def makeSound(self):
        return "Generic sound"
    
class Dog(Animal):
    
    def __init__(self, dog_color, age, dog_name = "dog"):
        super().__init__(dog_name, dog_color)
        self.dog_age = age
    
    def makeSound(self):
        return "Guauuuu"
    
animal1 = Animal("Camel", "Brown")
print(animal1.makeSound())

animal2 = Dog("white", 5)
print(animal2.makeSound())
print(animal2.nameAnimal)