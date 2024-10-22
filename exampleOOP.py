class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    # Constructor (initializer)
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age
        self.__age = age     # private properties
    # Instance method
    def bark(self):
        return f"{self.name} says woof!"
    
    # Another instance method
    def get_age(self):
        return f"{self.name} is {self.age} years old."
    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.species}" # custom representation for object when it is printed.
    
    # Creating instances (objects) of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)
   
print(dog1.bark())         # Buddy says woof!
print(dog2.get_age())      # Charlie is 5 years old.
print(dog1.species)        # Canis familiaris
print(dog1.age)
#print(dog1.__age)     # private properties
print(dog1) # 