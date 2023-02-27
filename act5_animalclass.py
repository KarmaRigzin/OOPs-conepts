#Activity V: Animal Class. Inheritance

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        print(f"{self.name} makes a {sound} sound.")

class Dog(Animal):
    
    def walk(self, values):
        print(f"{self.name} can {values}.")

dog = Dog("Fido", "Golden Retriever")

dog.make_sound("bark")
dog.walk("Walk")
