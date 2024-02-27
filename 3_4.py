class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name

class Zoo:
    def __init__(self):
        self.animals = []
    
    def add_animal(self, animal):
        self.animals.append(animal)
    
    def remove_animal(self, animal):
        self.animals = [a for a in self.animals if a != animal]

zoo = Zoo()
zoo.add_animal(Animal("Лев", "Кузя"))
zoo.add_animal(Animal("Слон", "Володимир"))

print("Тварини у зоопарку:", [(animal.species, animal.name) for animal in zoo.animals])

zoo.remove_animal(zoo.animals[0])

print("Тварини у зоопарку після видалення:", [(animal.species, animal.name) for animal in zoo.animals])
