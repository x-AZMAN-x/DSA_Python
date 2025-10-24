'''
Inheritance Lets A New Class(The Child) Use Features From An Existing Class(The Parent)
'''

class Animal:
    """
    Base Class That All Animal Will Inherit From
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"{self.name} Is Created")

    def eat(self):
        print(f"{self.name} Is Eating His Treat!")

    def sleep (self):
        print(f"{self.name} Is Sleeping...")

class Dog(Animal):
    """
    Dog Inherits From Animals - Gets All Animal Methods
    """

    def __init__(self, name, age, breed):
        super().__init__(name, age)   #Calling The Parent Constructor

        self.breed = breed

        #Overriding: Dog Has Its Own Version Of 'sound'
    def sound(self):
        print(f"{self.name} Barks!")

    def fetch_ball(self):
        print(f"{self.name} Is Fetching The Ball!")

class Cat(Animal):
    """
    Cat Inherits From Animals
    """

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def sound(self):
        print(f"{self.name} Meows!")

    def climb(self):
        print(f"{self.name} Is Climbing The Tree!")


print("\n Creating Objects: ")

dog = Dog("Max", 2, "German Sheperd")
cat = Cat("Tom", 3, "Orange")

print("\n Using Inherited Methods: ")

dog.eat()
cat.sleep()

print("\n Overriding Methods:")

dog.sound()
cat.sound()

print("\n Child-Specific Methods:")

dog.fetch_ball()
cat.climb()
