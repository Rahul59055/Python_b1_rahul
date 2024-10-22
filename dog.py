from animal import Animal
class Dog(Animal):#inheriting animal
    species = "Golden retriver"
    def bark(self):
        return f"{self.name} says Woof!"