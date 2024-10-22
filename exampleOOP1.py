class Animal:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_age(self):
        return f"{self.name} is {self.age} years old."
    
    def __str__(self):
        return f"{self.name} is {self.__age} years old"
    
    class Dog(Animal):
        species = "Golden retriver"
        def bark(self):
            return f"{self.name} says woof!"
        
    class Cat(Animal):
        species = "Cat species"
        
        def meu(self):
            return f"{self.name} says meu!"
        
dog1 = Dog("d1",3)
cat1 = Cat("c1",4)       

print(dog1)
print(cat1)
        
        
