class Animal:
    type = "Animal"

    def __init__(self):
        self.age = 1

    @classmethod
    def lol(cls):
        print("Class method")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Gâu gâu")


dog = Dog()
dog.bark()
print(dog.age)
print(dog.type)
dog.lol()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(isinstance(dog, object))  # object is

print(issubclass(Dog, Animal))
print(issubclass(Dog, object))
