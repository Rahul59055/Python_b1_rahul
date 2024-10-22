from animal import Animal

class Cat(Animal):#inheriting animal
    Species = "Cat species"
    def meu(self):
        return f"{self.name} says meu!"